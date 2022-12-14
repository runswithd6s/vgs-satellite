from unittest.mock import ANY, Mock

import pytest
from freezegun import freeze_time
from pylarky.model.http_message import HttpMessage

from satellite.audit_logs.records import OperationLogRecord
from satellite.ctx import ProxyContext
from satellite.operations.operations import (
    CustomScriptOperation,
    Operation,
    OperationStatus,
)
from satellite.proxy import ProxyMode
from satellite.routes import Phase
from ..factories import load_flow


class MockOperation(Operation):
    operation_name = 'test-operation'

    @property
    def code(self):
        return 'some code'


class LegitMockOperation(Operation):
    operation_name = 'legit-test-operation'

    @property
    def code(self):
        return '''
load('@stdlib/json', 'json')
decoded_payload=json.decode(request.data)
decoded_payload["brand-new-field"]="brand-new-value"
request.data=json.encode(decoded_payload)
request.add_header("brand-new-header", "brand-spanking-new-header-value")
request
        '''


@freeze_time('2020-11-18')
@pytest.mark.parametrize('phase', [Phase.REQUEST])
def test_evaluate_ok_nomock(phase, monkeypatch, snapshot):
    monkeypatch.setattr(
        'satellite.operations.operations.get_proxy_context',
        Mock(
            return_value=ProxyContext(
                mode=ProxyMode.FORWARD,
                port=9099,
            )
        ),
    )

    mock_emit = Mock()
    monkeypatch.setattr(
        'satellite.operations.pipeline.audit_logs.emit',
        mock_emit,
    )

    flow = load_flow('http_raw')
    operation = LegitMockOperation(route_id='route-id', filter_id='filter-id')
    operation.evaluate(flow, phase)

    snapshot.assert_match(flow.request.get_state(), name='request')
    mock_emit.assert_called_once_with(
        OperationLogRecord(
            flow_id=flow.id,
            proxy_mode=ProxyMode.FORWARD,
            route_id='route-id',
            filter_id='filter-id',
            phase=phase,
            operation_name='legit-test-operation',
            execution_time_ms=ANY,
            execution_time_ns=ANY,
            status=OperationStatus.OK,
            error_message=None,
        )
    )


@freeze_time('2020-11-18')
@pytest.mark.parametrize('phase', [Phase.REQUEST, Phase.RESPONSE])
def test_evaluate_ok(phase, monkeypatch, snapshot):
    monkeypatch.setattr(
        'satellite.operations.operations.get_proxy_context',
        Mock(
            return_value=ProxyContext(
                mode=ProxyMode.FORWARD,
                port=9099,
            )
        ),
    )

    mock_evaluate = Mock(
        wraps=lambda code, msg: HttpMessage(
            url=msg.url,
            headers=msg.headers,
            data=msg.data.replace('bar', 'bar_processed'),
        )
    )
    monkeypatch.setattr(
        'satellite.operations.operations.evaluate',
        mock_evaluate,
    )
    mock_emit = Mock()
    monkeypatch.setattr(
        'satellite.operations.pipeline.audit_logs.emit',
        mock_emit,
    )

    flow = load_flow('http_raw')
    operation = MockOperation(route_id='route-id', filter_id='filter-id')
    operation.evaluate(flow, phase)

    snapshot.assert_match(flow.request.get_state(), name='request')
    snapshot.assert_match(flow.response.get_state(), name='response')
    mock_emit.assert_called_once_with(
        OperationLogRecord(
            flow_id=flow.id,
            proxy_mode=ProxyMode.FORWARD,
            route_id='route-id',
            filter_id='filter-id',
            phase=phase,
            operation_name='test-operation',
            execution_time_ms=ANY,
            execution_time_ns=ANY,
            status=OperationStatus.OK,
            error_message=None,
        )
    )


@freeze_time('2020-11-18')
def test_evaluate_error(monkeypatch):
    monkeypatch.setattr(
        'satellite.operations.operations.get_proxy_context',
        Mock(
            return_value=ProxyContext(
                mode=ProxyMode.FORWARD,
                port=9099,
            )
        ),
    )
    monkeypatch.setattr(
        'satellite.operations.operations.evaluate',
        Mock(side_effect=Exception('test error')),
    )
    mock_emit = Mock()
    monkeypatch.setattr(
        'satellite.operations.pipeline.audit_logs.emit',
        mock_emit,
    )

    flow = load_flow('http_raw')
    operation = MockOperation(route_id='route-id', filter_id='filter-id')
    operation.evaluate(flow, Phase.REQUEST)

    mock_emit.assert_called_once_with(
        OperationLogRecord(
            flow_id=flow.id,
            proxy_mode=ProxyMode.FORWARD,
            route_id='route-id',
            filter_id='filter-id',
            phase=Phase.REQUEST,
            operation_name='test-operation',
            execution_time_ms=ANY,
            execution_time_ns=ANY,
            status=OperationStatus.ERROR,
            error_message='test error',
        )
    )


def test_custom_script_operation():
    operation = CustomScriptOperation(
        route_id='route-id', filter_id='filter-id', script='custom script'
    )
    assert operation.code == 'custom script'
