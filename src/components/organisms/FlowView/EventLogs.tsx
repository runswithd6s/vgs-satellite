import React from 'react';
import cn from 'classnames';
import history from 'src/redux/utils/history';
import { Button, Icon, Table } from 'src/components/antd';
import { unixToFormat } from 'src/redux/utils/utils';
import { IEventLog } from 'src/redux/interfaces/eventLogs';
import { IRoute } from 'src/redux/interfaces/routes';

interface IEventLogsProps {
  traceId: string;
  isLoading: boolean;
  eventLogs: IEventLog[];
  routes: IRoute[];
}

const eventLogsMap = {
  method: 'Method',
  uri: 'Uri',
  bytes: 'Bytes',
  label: 'Label',
  upstream: 'Upstream',
  status_code: 'Status code',
  route_id: 'Route ID',
  filter_id: 'Filter ID',
  matched: 'Matched',
  action_type: 'Action Type',
  alias_generator: 'Alias Generator',
  record_type: 'Record Type',
  operation_name: 'Operation Name',
  phase: 'Phase',
  status: 'Status',
  error_message: 'Error Message',
  execution_time_ms: 'Ecxecution time (ms)',
};

const EventLogs: React.FC<IEventLogsProps> = (props) => {
  const { traceId, isLoading, eventLogs, routes } = props;

  const customExpandIcon = (tableProps: any) => (tableProps.expandable ? (
    <Icon
      type="caret-right"
      onClick={(e) => tableProps.onExpand(tableProps.record, e)}
      className={cn('mr-2 icon-rotate d-inline-flex', { 'icon-rotate-90': tableProps.expanded })}
    />
  ) : <span />);

  return (
    <div className="mt-3 pt-0 eventlogs-table">
      <Table
        key={`eventLogs-${traceId}`}
        loading={isLoading}
        columns={[
          {
            title: () => <span className="small-capsy">Events</span>,
            align: 'left',
            dataIndex: 'name',
            render: (record) => (
              <span className="_600 text-text-dark" data-role="event-name">{record}</span>
            ),
          },
          {
            title: () => <span className="small-capsy">Date and time</span>,
            align: 'right',
            dataIndex: 'timestamp',
            render: (record) => unixToFormat(record, 'YYYY-MM-DDTHH:mm:ss.SSS'),
          },
        ]}
        dataSource={eventLogs}
        striped={false}
        type="dark"
        pagination={false}
        rowKey={(record) => `${record.type}-${record.timestamp}`}
        rowBorderRounded={false}
        rowBorderNone={false}
        scroll={{ y: 300 }}
        expandIcon={customExpandIcon}
        expandIconAsCell={false}
        expandRowByClick={true}
        expandedRowRender={record => (
          <div data-role="event-details">
            {Object.keys(eventLogsMap).map((key) => {
              if (record.hasOwnProperty(key)) {
                return (
                  <p className="mb-0 ml-4 pl-1 py-2 small-capsy" key={key} data-role={key}>
                    <span className="text-text-light pr-2" data-role="name">
                      {eventLogsMap[key]}
                    </span>
                    <span data-role="value">
                      {key === 'route_id' && routes.find(route => route.id === record[key]) ? (
                        <Button
                          type="link"
                          size="small"
                          className="p-0 small-capsy"
                          onClick={() => history.push(`/routes/${record[key]}/edit`)}
                        >
                          {record[key]}
                        </Button>
                      ) : (
                        record[key]?.toString() || '[Empty]'
                      )}
                    </span>
                  </p>
                )
              } else return;
            })}
          </div>
        )}
      />
    </div>
  );
};

export default EventLogs;
