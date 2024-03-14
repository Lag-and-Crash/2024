import pyshark


def parse_packets( file_path: str, ip: str ):
    capture = pyshark.FileCapture( file_path, display_filter=f'ip.addr == {ip} && http' )
    packet_details = []

    for packet in capture:
        try:
            if 'HTTP' in packet:
                http_layer = packet.http
                packet_info = { "ip": ip, "details": {} }

                if hasattr( http_layer, 'request_method' ):
                    packet_info[ "details" ][ "request_method" ] = http_layer.request_method

                if hasattr( http_layer, 'user-agent' ):
                    packet_info[ "details" ][ "user-agent" ] = http_layer.user_agent

                if hasattr( http_layer, 'response_code' ):
                    if hasattr( http_layer, 'response_phrase' ):
                        packet_info[ "details" ][ "server" ] = http_layer.server

                packet_details.append( packet_info )

        except Exception as e:
            print( str( e ) )

    capture.close()

    unique = {}
    for packet in packet_details:
        ip = packet[ "ip" ]
        details = packet[ "details" ]

        if ip not in unique:
            unique[ ip ] = { "user-agents": set(), "request_methods": set(), "servers": set() }

        if "user-agent" in details:
            unique[ ip ][ "user-agents" ].add( details[ "user-agent" ] )

        if "request_method" in details:
            unique[ ip ][ "request_methods" ].add( details[ "request_method" ] )

        if "server" in details:
            unique[ ip ][ "servers" ].add( details[ "server" ] )

    return unique


def get_unique_http_ips( file_path: str ):
    capture = pyshark.FileCapture( file_path, display_filter='http' )

    unique_ips = set()

    for packet in capture:
        try:
            if 'IP' in packet:
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                unique_ips.add( src_ip )
                unique_ips.add( dst_ip )
        except AttributeError:
            pass

    capture.close()
    return list( unique_ips )


if __name__ == "__main__":
    file_path = '../dist/capture.pcapng'
    # unique_ips = get_unique_http_ips( file_path )
    # print( f"Found {len(unique_ips)} unique IPs that made HTTP requests" )
    # print( unique_ips )

    unique_ips = [ '151.101.65.140', '151.101.193.140', '151.101.1.140', '151.101.129.140', '34.125.177.32' ]

    for ip in unique_ips:
        packets = parse_packets( file_path, ip )
        print( f"IP: {ip}" )
        print( f"User-agents: {packets[ ip ][ 'user-agents' ]}" )
        print( f"Request methods: {packets[ ip ][ 'request_methods' ]}" )
        print( f"Servers: {packets[ ip ][ 'servers' ]}" )
        print( "" )