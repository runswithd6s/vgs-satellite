# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_transform_body[Phase.REQUEST] 1'] = {
    'client_conn': {
        'address': (
            '::1',
            64256,
            0,
            0
        ),
        'alpn_offers': None,
        'alpn_proto_negotiated': b'h2',
        'certificate_list': [
        ],
        'cipher_list': None,
        'cipher_name': 'ECDHE-RSA-AES128-GCM-SHA256',
        'error': None,
        'id': '226dc802-2672-4846-9b54-ad104fef8e7e',
        'mitmcert': b'-----BEGIN CERTIFICATE-----\nMIIDBjCCAe6gAwIBAgIGDo6B8x4YMA0GCSqGSIb3DQEBCwUAMCgxEjAQBgNVBAMM\nCW1pdG1wcm94eTESMBAGA1UECgwJbWl0bXByb3h5MB4XDTIwMDkxNzEzNDAzM1oX\nDTIxMDkxOTEzNDAzM1owFjEUMBIGA1UEAwwLaHR0cGJpbi5vcmcwggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDfGDkMRihqvXAKqT3XQPH4MQJwMYXvAeBH\nHGJj6PSTQbbqBLEitWVx0BRY4GcBhl92a1idJJBANZ9OadbJ7WEE80r3HmHFfjx3\nVLGCsj0GtAAEEMJy+xrogATKR7fcJYVd4X93gxksNpPyzZs+yGrEZWKEBf3pzXee\ngpPwxW1eFmXD0MgUFVUsfoioD22Wb2hRdoW5/vQogQPKjTskezbyfSRbS6l6Npc5\nGiNtzXpNW6eYXH3VEJw8XxLVY/QQUe2M5kRY/jw7L+b8BJAXKhgF2eDLvTWzGzUL\nwsoNNEe+sIj+Pfhh7/VKqWaesQA4k4WxDdG2KZiwH05JKkdLZf13AgMBAAGjSDBG\nMCUGA1UdEQQeMByCDSouaHR0cGJpbi5vcmeCC2h0dHBiaW4ub3JnMB0GA1UdJQQW\nMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0BAQsFAAOCAQEAg0sXiWXE\nlCMgMNKD85SaItwAk282VlHyPpmtkZzJa7/sCrTjV1tIldJToCK5qfgR7XNsO2V2\n771U4jcTdFs1lwv6IqQ0s+M7+DX/ixv1vM+2G93HGqo2TxQDi+FH3RxxqSYQhGBx\n0QExpMp1unG5533USprfmpZbXIoAZ6/J9jRxykNHrt4LGDV8ndpPZQqVm1a2vl/u\nQ7Fnl9AakXJ9FOXB01NBQNYpkpCh9ZwYmJF1zy+CRdPWDtE+N94ycUdXkpDpwXD6\nuVvhhF+71p5K+SxYl2XtszahZa9gBxNS+fbJ5LuUb1YKte7CSBdYxSr+L87+bvF2\nEfKh2WT5Sai8QA==\n-----END CERTIFICATE-----\n',
        'sni': 'httpbin.org',
        'sockname': (
            '',
            0
        ),
        'state': 0,
        'timestamp_end': None,
        'timestamp_start': 1600522833.4427578,
        'timestamp_tls_setup': 1600522833.9239712,
        'tls': None,
        'tls_established': True,
        'tls_extensions': [
            (
                0,
                b'\x00\x0e\x00\x00\x0bhttpbin.org'
            ),
            (
                11,
                b'\x01\x00'
            ),
            (
                10,
                b'\x00\x06\x00\x1d\x00\x17\x00\x18'
            ),
            (
                13,
                b'\x00\x1a\x06\x01\x06\x03\xef\xef\x05\x01\x05\x03\x04\x01\x04\x03\xee\xee\xed\xed\x03\x01\x03\x03\x02\x01\x02\x03'
            ),
            (
                16,
                b'\x00\x0c\x02h2\x08http/1.1'
            )
        ],
        'tls_version': 'TLSv1.2'
    },
    'error': None,
    'id': '805b2a13-c921-48f4-85c4-dbceaea21fb4',
    'intercepted': False,
    'is_replay': None,
    'marked': False,
    'metadata': {
    },
    'mode': 'regular',
    'request': {
        'authority': b'httpbin.org',
        'content': b'{"foo": "bar_redacted"}',
        'headers': (
            (
                b'user-agent',
                b'curl/7.64.1'
            ),
            (
                b'accept',
                b'*/*'
            ),
            (
                b'content-type',
                b'application/json'
            ),
            (
                b'content-length',
                b'23'
            ),
            (
                b'vgs-client',
                b'vgs-collect'
            )
        ),
        'host': 'httpbin.org',
        'http_version': b'HTTP/2.0',
        'method': b'POST',
        'path': b'/post',
        'port': 443,
        'scheme': b'https',
        'timestamp_end': 1600522833.936801,
        'timestamp_start': 1600522833.932597,
        'trailers': None
    },
    'response': {
        'content': b'{\n  "args": {}, \n  "data": "{\\"foo\\": \\"bar\\"}", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Content-Length": "14", \n    "Content-Type": "application/json", \n    "Host": "httpbin.org", \n    "User-Agent": "curl/7.64.1", \n    "X-Amzn-Trace-Id": "Root=1-5f660a52-406ee7a82be72f6c58b5ba7c"\n  }, \n  "json": {\n    "foo": "bar"\n  }, \n  "origin": "185.205.44.203", \n  "url": "https://httpbin.org/post"\n}\n',
        'headers': (
            (
                b'date',
                b'Sat, 19 Sep 2020 13:40:34 GMT'
            ),
            (
                b'content-type',
                b'application/json'
            ),
            (
                b'content-length',
                b'426'
            ),
            (
                b'server',
                b'gunicorn/19.9.0'
            ),
            (
                b'access-control-allow-origin',
                b'*'
            ),
            (
                b'access-control-allow-credentials',
                b'true'
            )
        ),
        'http_version': b'HTTP/2.0',
        'reason': b'',
        'status_code': 200,
        'timestamp_end': 1600522834.1649642,
        'timestamp_start': 1600522834.159654,
        'trailers': None
    },
    'server_conn': {
        'address': (
            'httpbin.org',
            443
        ),
        'alpn_offers': None,
        'alpn_proto_negotiated': b'h2',
        'certificate_list': [
        ],
        'cipher_list': None,
        'cipher_name': None,
        'error': None,
        'id': '2cfaddb6-49d2-42c9-a427-a97a02e49584',
        'ip_address': (
            '35.172.162.144',
            443
        ),
        'sni': 'httpbin.org',
        'source_address': (
            '192.168.88.227',
            64257
        ),
        'state': 0,
        'timestamp_end': None,
        'timestamp_start': 1600522833.459318,
        'timestamp_tcp_setup': 1600522833.594885,
        'timestamp_tls_setup': 1600522833.86449,
        'tls': None,
        'tls_established': True,
        'tls_version': 'TLSv1.2',
        'via': None,
        'via2': None
    },
    'type': 'http',
    'version': 10
}

snapshots['test_transform_body[Phase.RESPONSE] 1'] = {
    'client_conn': {
        'address': (
            '::1',
            64256,
            0,
            0
        ),
        'alpn_offers': None,
        'alpn_proto_negotiated': b'h2',
        'certificate_list': [
        ],
        'cipher_list': None,
        'cipher_name': 'ECDHE-RSA-AES128-GCM-SHA256',
        'error': None,
        'id': '226dc802-2672-4846-9b54-ad104fef8e7e',
        'mitmcert': b'-----BEGIN CERTIFICATE-----\nMIIDBjCCAe6gAwIBAgIGDo6B8x4YMA0GCSqGSIb3DQEBCwUAMCgxEjAQBgNVBAMM\nCW1pdG1wcm94eTESMBAGA1UECgwJbWl0bXByb3h5MB4XDTIwMDkxNzEzNDAzM1oX\nDTIxMDkxOTEzNDAzM1owFjEUMBIGA1UEAwwLaHR0cGJpbi5vcmcwggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDfGDkMRihqvXAKqT3XQPH4MQJwMYXvAeBH\nHGJj6PSTQbbqBLEitWVx0BRY4GcBhl92a1idJJBANZ9OadbJ7WEE80r3HmHFfjx3\nVLGCsj0GtAAEEMJy+xrogATKR7fcJYVd4X93gxksNpPyzZs+yGrEZWKEBf3pzXee\ngpPwxW1eFmXD0MgUFVUsfoioD22Wb2hRdoW5/vQogQPKjTskezbyfSRbS6l6Npc5\nGiNtzXpNW6eYXH3VEJw8XxLVY/QQUe2M5kRY/jw7L+b8BJAXKhgF2eDLvTWzGzUL\nwsoNNEe+sIj+Pfhh7/VKqWaesQA4k4WxDdG2KZiwH05JKkdLZf13AgMBAAGjSDBG\nMCUGA1UdEQQeMByCDSouaHR0cGJpbi5vcmeCC2h0dHBiaW4ub3JnMB0GA1UdJQQW\nMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0BAQsFAAOCAQEAg0sXiWXE\nlCMgMNKD85SaItwAk282VlHyPpmtkZzJa7/sCrTjV1tIldJToCK5qfgR7XNsO2V2\n771U4jcTdFs1lwv6IqQ0s+M7+DX/ixv1vM+2G93HGqo2TxQDi+FH3RxxqSYQhGBx\n0QExpMp1unG5533USprfmpZbXIoAZ6/J9jRxykNHrt4LGDV8ndpPZQqVm1a2vl/u\nQ7Fnl9AakXJ9FOXB01NBQNYpkpCh9ZwYmJF1zy+CRdPWDtE+N94ycUdXkpDpwXD6\nuVvhhF+71p5K+SxYl2XtszahZa9gBxNS+fbJ5LuUb1YKte7CSBdYxSr+L87+bvF2\nEfKh2WT5Sai8QA==\n-----END CERTIFICATE-----\n',
        'sni': 'httpbin.org',
        'sockname': (
            '',
            0
        ),
        'state': 0,
        'timestamp_end': None,
        'timestamp_start': 1600522833.4427578,
        'timestamp_tls_setup': 1600522833.9239712,
        'tls': None,
        'tls_established': True,
        'tls_extensions': [
            (
                0,
                b'\x00\x0e\x00\x00\x0bhttpbin.org'
            ),
            (
                11,
                b'\x01\x00'
            ),
            (
                10,
                b'\x00\x06\x00\x1d\x00\x17\x00\x18'
            ),
            (
                13,
                b'\x00\x1a\x06\x01\x06\x03\xef\xef\x05\x01\x05\x03\x04\x01\x04\x03\xee\xee\xed\xed\x03\x01\x03\x03\x02\x01\x02\x03'
            ),
            (
                16,
                b'\x00\x0c\x02h2\x08http/1.1'
            )
        ],
        'tls_version': 'TLSv1.2'
    },
    'error': None,
    'id': '805b2a13-c921-48f4-85c4-dbceaea21fb4',
    'intercepted': False,
    'is_replay': None,
    'marked': False,
    'metadata': {
    },
    'mode': 'regular',
    'request': {
        'authority': b'httpbin.org',
        'content': b'{"foo": "bar"}',
        'headers': (
            (
                b'user-agent',
                b'curl/7.64.1'
            ),
            (
                b'accept',
                b'*/*'
            ),
            (
                b'content-type',
                b'application/json'
            ),
            (
                b'content-length',
                b'14'
            ),
            (
                b'vgs-client',
                b'vgs-collect'
            )
        ),
        'host': 'httpbin.org',
        'http_version': b'HTTP/2.0',
        'method': b'POST',
        'path': b'/post',
        'port': 443,
        'scheme': b'https',
        'timestamp_end': 1600522833.936801,
        'timestamp_start': 1600522833.932597,
        'trailers': None
    },
    'response': {
        'content': b'{"args": {}, "data": "{\\"foo\\": \\"bar\\"}", "files": {}, "form": {}, "headers": {"Accept": "*/*", "Content-Length": "14", "Content-Type": "application/json", "Host": "httpbin.org", "User-Agent": "curl/7.64.1", "X-Amzn-Trace-Id": "Root=1-5f660a52-406ee7a82be72f6c58b5ba7c"}, "json": {"foo": "bar"}, "origin": "185.205.44.203", "url": "https://httpbin.org/post"}',
        'headers': (
            (
                b'date',
                b'Sat, 19 Sep 2020 13:40:34 GMT'
            ),
            (
                b'content-type',
                b'application/json'
            ),
            (
                b'content-length',
                b'359'
            ),
            (
                b'server',
                b'gunicorn/19.9.0'
            ),
            (
                b'access-control-allow-origin',
                b'*'
            ),
            (
                b'access-control-allow-credentials',
                b'true'
            )
        ),
        'http_version': b'HTTP/2.0',
        'reason': b'',
        'status_code': 200,
        'timestamp_end': 1600522834.1649642,
        'timestamp_start': 1600522834.159654,
        'trailers': None
    },
    'server_conn': {
        'address': (
            'httpbin.org',
            443
        ),
        'alpn_offers': None,
        'alpn_proto_negotiated': b'h2',
        'certificate_list': [
        ],
        'cipher_list': None,
        'cipher_name': None,
        'error': None,
        'id': '2cfaddb6-49d2-42c9-a427-a97a02e49584',
        'ip_address': (
            '35.172.162.144',
            443
        ),
        'sni': 'httpbin.org',
        'source_address': (
            '192.168.88.227',
            64257
        ),
        'state': 0,
        'timestamp_end': None,
        'timestamp_start': 1600522833.459318,
        'timestamp_tcp_setup': 1600522833.594885,
        'timestamp_tls_setup': 1600522833.86449,
        'tls': None,
        'tls_established': True,
        'tls_version': 'TLSv1.2',
        'via': None,
        'via2': None
    },
    'type': 'http',
    'version': 10
}
