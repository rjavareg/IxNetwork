params = {
    "windowsApiServerIp": "192.168.70.3",
    "windowsServerIpPort": 11009,
    "linuxApiServerIp": "192.168.70.3",
    "linuxServerIpPort": 443,
    "forceTakePortOwnership": True,
    "releasePortsWhenDone": False,
    "enableDebugTracing": True,
    "deleteSessionAfterTest": False,
    "licenseServerIp": "192.168.70.3",
    "licenseModel": "subscription",
    "licenseTier": "tier3",    
    "ixChassisIp": "192.168.70.11",
    "portList": [["192.168.70.11", "1", "1"],
                 ["192.168.70.11", "2", "1"]
             ],
    
    "topology": [
        {
            "name": "Topology-1",
            "ports": [["192.168.70.11", "1", "1"]],
            "deviceGroup": [
                {
                    "name": "DG-1",		
                    "multiplier": 1,
                    "ethernet": [
                        {
                            "name": "Ethernet-1",
                            "macAddress": {"start": "00:01:01:00:00:01",
                                           "direction": "increment",
                                           "step": "00:00:00:00:00:01",
                                           "portStep": "disabled"},
                            "vlanId": {"start": 101, "direction": "increment", "step": 0},
                            "ipv4": [
                                {
                                    "name": "ipv4-2",
                                    "address": {"start": "1.1.1.1",
                                                "direction": "increment",
                                                "step": "0.0.0.1",
                                                "portStep": "disabled"},
                                    "gateway": {"start": "1.1.1.2",
                                                "direction": "increment",
                                                "step": "0.0.0.1",
                                                "portStep": "disabled"},
                                    "prefix": 24,
                                    "bgp": [
                                        {
                                            "name": "BGP-1",
                                            "dutIp": {"start": "1.1.1.2",
                                                      "direction": "increment",
                                                      "step": "0.0.0.0"},
                                            "type": "internal",
                                            "localAs2Bytes": 101
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "networkGroup": [
                        {
                            "name": "bgpRouteRange1",
                            "multiplier": 100,
                            "prefix": 32,
                            "routeRange": {"start": "100.0.0.1",
                                           "direction": "increment",
                                           "step": "0.0.0.1"}
                        }
                    ]
                }
            ]
        },	
        {
            "name": "Topology-2",
            "ports": [["192.168.70.11", "2", "1"]],
            "deviceGroup": [
                {
                    "name": "DG-2",		
                    "multiplier": 1,
                    "ethernet": [
                        {
                            "name": "Ethernet-2",
                            "macAddress": {"start": "00:01:01:00:00:02",
                                           "direction": "increment",
                                           "step": "00:00:00:00:00:01",
                                           "portStep": "disabled"},
                            "vlanId": {"start": 101, "direction": "increment", "step": 0},
                            "ipv4": [
                                {
                                    "name": "ipv4-2",
                                    "address": {"start": "1.1.1.2",
                                                "direction": "increment",
                                                "step": "0.0.0.1",
                                                "portStep": "disabled"},
                                    "gateway": {"start": "1.1.1.1",
                                                "direction": "increment",
                                                "step": "0.0.0.1",
                                                "portStep": "disabled"},
                                    "prefix": 24,
                                    "bgp": [
                                        {
                                            "name": "BGP-1",
                                            "dutIp": {"start": "1.1.1.1",
                                                      "direction": "increment",
                                                      "step": "0.0.0.0"},
                                            "type": "internal",
                                            "localAs2Bytes": 101
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    "networkGroup": [
                        {
                            "name": "bgpRouteRange2",
                            "multiplier": 100,
                            "prefix": 32,
                            "routeRange": {"start": "200.0.0.1",
                                           "direction": "increment",
                                           "step": "0.0.0.1"}
                        }
                    ]
                }	
            ]
        }
    ],
    
    "trafficItems":  [
        {
            "name": "Port1 to Port2",
            "trafficType": "ipv4",
            "bidirectional": True,
            "trackBy": ["flowGroup0", "vlanVlanId0"],
            "endpoints": [{"name": "FlowGroup-1",
                           "sources": ["/topology/1"],
                           "destinations": ["/topology/2"]
                       }
            ],
            "configElements": [
                {
                    "transmissionType": "fixedPacketCount",
                    "frameCount": 2000000,
                    "frameRate": 100,
                    "frameRateType": "percentLineRate",
                    "frameSize": 64
                }
            ]
        }
    ]
}


