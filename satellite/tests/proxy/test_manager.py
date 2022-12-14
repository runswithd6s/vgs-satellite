import time
from dataclasses import dataclass
from unittest.mock import Mock

from satellite.audit_logs.records import AuditLogRecord
from satellite.proxy import ProxyMode, commands, events
from satellite.proxy.manager import ProxyManager


@dataclass
class AuditLogTestRecord(AuditLogRecord):
    name: str = 'Test record'


def test_start_stop(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [(Mock(), Mock()), (Mock(), Mock())]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )

    manager = ProxyManager(9099, 9098, Mock())

    manager.start()
    try:
        for process in proxy_processes:
            process.start.assert_called_once()
    finally:
        manager.stop()

    for cmd_channel, _ in connections:
        cmd_channel.send.assert_called_once_with(commands.StopCommand())


def test_get_flows(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(recv=Mock(return_value=[{'timestamp_start': 2}])), Mock()),
        (Mock(recv=Mock(return_value=[{'timestamp_start': 1}])), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.load_flow_from_state',
        lambda state: Mock(**state),
    )

    manager = ProxyManager(9099, 9098, Mock())
    flows = manager.get_flows()
    assert len(flows) == 2
    assert flows[0].timestamp_start == 1
    assert flows[1].timestamp_start == 2
    for cmd_channel, _ in connections:
        cmd_channel.send.assert_called_once_with(commands.GetFlowsCommand())


def test_get_flow(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    flow_state = {'mode': ProxyMode.FORWARD.value, 'timestamp_start': 1}
    connections = [
        (Mock(recv=Mock(return_value=flow_state)), Mock()),
        (Mock(), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.load_flow_from_state',
        lambda state: Mock(**state),
    )

    flow_id = '23f11ab7-e071-4997-97f3-ace07bb9e56d'
    manager = ProxyManager(9099, 9098, Mock())
    manager._flows[flow_id] = ProxyMode.FORWARD

    flow = manager.get_flow(flow_id)
    assert flow.timestamp_start == 1
    assert flow.mode == ProxyMode.FORWARD.value
    connections[0][0].send.assert_called_once_with(
        commands.GetFlowCommand(flow_id),
    )


def test_remove_flow(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(), Mock()),
        (Mock(), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )

    flow_id = '23f11ab7-e071-4997-97f3-ace07bb9e56d'
    manager = ProxyManager(9099, 9098, Mock())
    manager._flows[flow_id] = ProxyMode.FORWARD

    manager.remove_flow(flow_id)

    connections[0][0].send.assert_called_once_with(
        commands.RemoveFlowCommand(flow_id),
    )


def test_duplicate_flow(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(), Mock()),
        (Mock(), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )

    flow_id = '23f11ab7-e071-4997-97f3-ace07bb9e56d'
    manager = ProxyManager(9099, 9098, Mock())
    manager._flows[flow_id] = ProxyMode.FORWARD

    manager.duplicate_flow(flow_id)

    connections[0][0].send.assert_called_once_with(
        commands.DuplicateFlowCommand(flow_id),
    )


def test_replay_flow(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(), Mock()),
        (Mock(), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )

    flow_id = '23f11ab7-e071-4997-97f3-ace07bb9e56d'
    manager = ProxyManager(9099, 9098, Mock())
    manager._flows[flow_id] = ProxyMode.FORWARD

    manager.replay_flow(flow_id)

    connections[0][0].send.assert_called_once_with(
        commands.ReplayFlowCommand(flow_id),
    )


def test_update_flow(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(), Mock()),
        (Mock(), Mock()),
    ]
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        Mock(side_effect=proxy_processes),
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )

    flow_id = '23f11ab7-e071-4997-97f3-ace07bb9e56d'
    flow_data = {'flow': 'data'}
    manager = ProxyManager(9099, 9098, Mock())
    manager._flows[flow_id] = ProxyMode.FORWARD

    manager.update_flow(flow_id, flow_data)

    connections[0][0].send.assert_called_once_with(
        commands.UpdateFlowCommand(flow_id, flow_data),
    )


def test_audit_logs(monkeypatch):
    proxy_processes = [
        Mock(mode=ProxyMode.FORWARD),
        Mock(mode=ProxyMode.REVERSE),
    ]
    connections = [
        (Mock(), Mock()),
        (Mock(), Mock()),
    ]
    make_proxy_process = Mock(side_effect=proxy_processes)
    monkeypatch.setattr(
        'satellite.proxy.manager.ProxyProcess',
        make_proxy_process,
    )
    monkeypatch.setattr(
        'satellite.proxy.manager.Pipe',
        Mock(side_effect=connections),
    )
    manager = ProxyManager(9099, 9098, Mock())
    manager.start()

    try:
        event_queue = make_proxy_process.call_args.kwargs['event_queue']
        record = AuditLogTestRecord(
            flow_id='flow-id',
            proxy_mode=ProxyMode.FORWARD,
        )
        event_queue.put(
            events.AuditLogEvent(
                proxy_mode=ProxyMode.FORWARD,
                record=record,
            )
        )
        time.sleep(0.1)
        assert manager.get_audit_logs('flow-id') == [record]
    finally:
        manager.stop()
