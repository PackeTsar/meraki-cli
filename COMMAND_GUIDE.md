###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Command Guide

Below is a list of commands supported by the Meraki-CLI tool.

This documentation is built automatically by parsing the [Meraki Dashboard API Python SDK](https://github.com/meraki/dashboard-api-python) and may not be 100% up to date since that library changes regularly.


## Version

This command guide is based on version **v1.32.1** of the [Meraki Dashboard API Python SDK](https://github.com/meraki/dashboard-api-python). If you want to see the version of the SDK you have installed, issue the command `meraki -v`.


# TABLE OF CONTENTS
- [Administered](#administered)
    - [Administered Get Administered Identities Me](#administered-get-administered-identities-me)
- [Appliance](#appliance)
    - [Appliance Create Device Appliance Vmx Authentication Token](#appliance-create-device-appliance-vmx-authentication-token)
    - [Appliance Create Network Appliance Prefixes Delegated Static](#appliance-create-network-appliance-prefixes-delegated-static)
    - [Appliance Create Network Appliance Static Route](#appliance-create-network-appliance-static-route)
    - [Appliance Create Network Appliance Traffic Shaping Custom Performance Class](#appliance-create-network-appliance-traffic-shaping-custom-performance-class)
    - [Appliance Create Network Appliance Vlan](#appliance-create-network-appliance-vlan)
    - [Appliance Delete Network Appliance Prefixes Delegated Static](#appliance-delete-network-appliance-prefixes-delegated-static)
    - [Appliance Delete Network Appliance Static Route](#appliance-delete-network-appliance-static-route)
    - [Appliance Delete Network Appliance Traffic Shaping Custom Performance Class](#appliance-delete-network-appliance-traffic-shaping-custom-performance-class)
    - [Appliance Delete Network Appliance Vlan](#appliance-delete-network-appliance-vlan)
    - [Appliance Get Device Appliance Dhcp Subnets](#appliance-get-device-appliance-dhcp-subnets)
    - [Appliance Get Device Appliance Performance](#appliance-get-device-appliance-performance)
    - [Appliance Get Device Appliance Prefixes Delegated](#appliance-get-device-appliance-prefixes-delegated)
    - [Appliance Get Device Appliance Prefixes Delegated Vlan Assignments](#appliance-get-device-appliance-prefixes-delegated-vlan-assignments)
    - [Appliance Get Device Appliance Uplinks Settings](#appliance-get-device-appliance-uplinks-settings)
    - [Appliance Get Network Appliance Client Security Events](#appliance-get-network-appliance-client-security-events)
    - [Appliance Get Network Appliance Connectivity Monitoring Destinations](#appliance-get-network-appliance-connectivity-monitoring-destinations)
    - [Appliance Get Network Appliance Content Filtering](#appliance-get-network-appliance-content-filtering)
    - [Appliance Get Network Appliance Content Filtering Categories](#appliance-get-network-appliance-content-filtering-categories)
    - [Appliance Get Network Appliance Firewall Cellular Firewall Rules](#appliance-get-network-appliance-firewall-cellular-firewall-rules)
    - [Appliance Get Network Appliance Firewall Firewalled Service](#appliance-get-network-appliance-firewall-firewalled-service)
    - [Appliance Get Network Appliance Firewall Firewalled Services](#appliance-get-network-appliance-firewall-firewalled-services)
    - [Appliance Get Network Appliance Firewall Inbound Cellular Firewall Rules](#appliance-get-network-appliance-firewall-inbound-cellular-firewall-rules)
    - [Appliance Get Network Appliance Firewall Inbound Firewall Rules](#appliance-get-network-appliance-firewall-inbound-firewall-rules)
    - [Appliance Get Network Appliance Firewall L3 Firewall Rules](#appliance-get-network-appliance-firewall-l3-firewall-rules)
    - [Appliance Get Network Appliance Firewall L7 Firewall Rules](#appliance-get-network-appliance-firewall-l7-firewall-rules)
    - [Appliance Get Network Appliance Firewall L7 Firewall Rules Application Categories](#appliance-get-network-appliance-firewall-l7-firewall-rules-application-categories)
    - [Appliance Get Network Appliance Firewall One To Many Nat Rules](#appliance-get-network-appliance-firewall-one-to-many-nat-rules)
    - [Appliance Get Network Appliance Firewall One To One Nat Rules](#appliance-get-network-appliance-firewall-one-to-one-nat-rules)
    - [Appliance Get Network Appliance Firewall Port Forwarding Rules](#appliance-get-network-appliance-firewall-port-forwarding-rules)
    - [Appliance Get Network Appliance Firewall Settings](#appliance-get-network-appliance-firewall-settings)
    - [Appliance Get Network Appliance Port](#appliance-get-network-appliance-port)
    - [Appliance Get Network Appliance Ports](#appliance-get-network-appliance-ports)
    - [Appliance Get Network Appliance Prefixes Delegated Static](#appliance-get-network-appliance-prefixes-delegated-static)
    - [Appliance Get Network Appliance Prefixes Delegated Statics](#appliance-get-network-appliance-prefixes-delegated-statics)
    - [Appliance Get Network Appliance Security Events](#appliance-get-network-appliance-security-events)
    - [Appliance Get Network Appliance Security Intrusion](#appliance-get-network-appliance-security-intrusion)
    - [Appliance Get Network Appliance Security Malware](#appliance-get-network-appliance-security-malware)
    - [Appliance Get Network Appliance Settings](#appliance-get-network-appliance-settings)
    - [Appliance Get Network Appliance Single Lan](#appliance-get-network-appliance-single-lan)
    - [Appliance Get Network Appliance Ssid](#appliance-get-network-appliance-ssid)
    - [Appliance Get Network Appliance Ssids](#appliance-get-network-appliance-ssids)
    - [Appliance Get Network Appliance Static Route](#appliance-get-network-appliance-static-route)
    - [Appliance Get Network Appliance Static Routes](#appliance-get-network-appliance-static-routes)
    - [Appliance Get Network Appliance Traffic Shaping](#appliance-get-network-appliance-traffic-shaping)
    - [Appliance Get Network Appliance Traffic Shaping Custom Performance Class](#appliance-get-network-appliance-traffic-shaping-custom-performance-class)
    - [Appliance Get Network Appliance Traffic Shaping Custom Performance Classes](#appliance-get-network-appliance-traffic-shaping-custom-performance-classes)
    - [Appliance Get Network Appliance Traffic Shaping Rules](#appliance-get-network-appliance-traffic-shaping-rules)
    - [Appliance Get Network Appliance Traffic Shaping Uplink Bandwidth](#appliance-get-network-appliance-traffic-shaping-uplink-bandwidth)
    - [Appliance Get Network Appliance Traffic Shaping Uplink Selection](#appliance-get-network-appliance-traffic-shaping-uplink-selection)
    - [Appliance Get Network Appliance Uplinks Usage History](#appliance-get-network-appliance-uplinks-usage-history)
    - [Appliance Get Network Appliance Vlan](#appliance-get-network-appliance-vlan)
    - [Appliance Get Network Appliance Vlans](#appliance-get-network-appliance-vlans)
    - [Appliance Get Network Appliance Vlans Settings](#appliance-get-network-appliance-vlans-settings)
    - [Appliance Get Network Appliance Vpn Bgp](#appliance-get-network-appliance-vpn-bgp)
    - [Appliance Get Network Appliance Vpn Site To Site Vpn](#appliance-get-network-appliance-vpn-site-to-site-vpn)
    - [Appliance Get Network Appliance Warm Spare](#appliance-get-network-appliance-warm-spare)
    - [Appliance Get Organization Appliance Security Events](#appliance-get-organization-appliance-security-events)
    - [Appliance Get Organization Appliance Security Intrusion](#appliance-get-organization-appliance-security-intrusion)
    - [Appliance Get Organization Appliance Uplink Statuses](#appliance-get-organization-appliance-uplink-statuses)
    - [Appliance Get Organization Appliance Vpn Stats](#appliance-get-organization-appliance-vpn-stats)
    - [Appliance Get Organization Appliance Vpn Statuses](#appliance-get-organization-appliance-vpn-statuses)
    - [Appliance Get Organization Appliance Vpn Third Party V P N Peers](#appliance-get-organization-appliance-vpn-third-party-v-p-n-peers)
    - [Appliance Get Organization Appliance Vpn Vpn Firewall Rules](#appliance-get-organization-appliance-vpn-vpn-firewall-rules)
    - [Appliance Swap Network Appliance Warm Spare](#appliance-swap-network-appliance-warm-spare)
    - [Appliance Update Device Appliance Uplinks Settings](#appliance-update-device-appliance-uplinks-settings)
    - [Appliance Update Network Appliance Connectivity Monitoring Destinations](#appliance-update-network-appliance-connectivity-monitoring-destinations)
    - [Appliance Update Network Appliance Content Filtering](#appliance-update-network-appliance-content-filtering)
    - [Appliance Update Network Appliance Firewall Cellular Firewall Rules](#appliance-update-network-appliance-firewall-cellular-firewall-rules)
    - [Appliance Update Network Appliance Firewall Firewalled Service](#appliance-update-network-appliance-firewall-firewalled-service)
    - [Appliance Update Network Appliance Firewall Inbound Cellular Firewall Rules](#appliance-update-network-appliance-firewall-inbound-cellular-firewall-rules)
    - [Appliance Update Network Appliance Firewall Inbound Firewall Rules](#appliance-update-network-appliance-firewall-inbound-firewall-rules)
    - [Appliance Update Network Appliance Firewall L3 Firewall Rules](#appliance-update-network-appliance-firewall-l3-firewall-rules)
    - [Appliance Update Network Appliance Firewall L7 Firewall Rules](#appliance-update-network-appliance-firewall-l7-firewall-rules)
    - [Appliance Update Network Appliance Firewall One To Many Nat Rules](#appliance-update-network-appliance-firewall-one-to-many-nat-rules)
    - [Appliance Update Network Appliance Firewall One To One Nat Rules](#appliance-update-network-appliance-firewall-one-to-one-nat-rules)
    - [Appliance Update Network Appliance Firewall Port Forwarding Rules](#appliance-update-network-appliance-firewall-port-forwarding-rules)
    - [Appliance Update Network Appliance Firewall Settings](#appliance-update-network-appliance-firewall-settings)
    - [Appliance Update Network Appliance Port](#appliance-update-network-appliance-port)
    - [Appliance Update Network Appliance Prefixes Delegated Static](#appliance-update-network-appliance-prefixes-delegated-static)
    - [Appliance Update Network Appliance Security Intrusion](#appliance-update-network-appliance-security-intrusion)
    - [Appliance Update Network Appliance Security Malware](#appliance-update-network-appliance-security-malware)
    - [Appliance Update Network Appliance Settings](#appliance-update-network-appliance-settings)
    - [Appliance Update Network Appliance Single Lan](#appliance-update-network-appliance-single-lan)
    - [Appliance Update Network Appliance Ssid](#appliance-update-network-appliance-ssid)
    - [Appliance Update Network Appliance Static Route](#appliance-update-network-appliance-static-route)
    - [Appliance Update Network Appliance Traffic Shaping](#appliance-update-network-appliance-traffic-shaping)
    - [Appliance Update Network Appliance Traffic Shaping Custom Performance Class](#appliance-update-network-appliance-traffic-shaping-custom-performance-class)
    - [Appliance Update Network Appliance Traffic Shaping Rules](#appliance-update-network-appliance-traffic-shaping-rules)
    - [Appliance Update Network Appliance Traffic Shaping Uplink Bandwidth](#appliance-update-network-appliance-traffic-shaping-uplink-bandwidth)
    - [Appliance Update Network Appliance Traffic Shaping Uplink Selection](#appliance-update-network-appliance-traffic-shaping-uplink-selection)
    - [Appliance Update Network Appliance Vlan](#appliance-update-network-appliance-vlan)
    - [Appliance Update Network Appliance Vlans Settings](#appliance-update-network-appliance-vlans-settings)
    - [Appliance Update Network Appliance Vpn Bgp](#appliance-update-network-appliance-vpn-bgp)
    - [Appliance Update Network Appliance Vpn Site To Site Vpn](#appliance-update-network-appliance-vpn-site-to-site-vpn)
    - [Appliance Update Network Appliance Warm Spare](#appliance-update-network-appliance-warm-spare)
    - [Appliance Update Organization Appliance Security Intrusion](#appliance-update-organization-appliance-security-intrusion)
    - [Appliance Update Organization Appliance Vpn Third Party V P N Peers](#appliance-update-organization-appliance-vpn-third-party-v-p-n-peers)
    - [Appliance Update Organization Appliance Vpn Vpn Firewall Rules](#appliance-update-organization-appliance-vpn-vpn-firewall-rules)
- [Batch](#batch)
    - [Batch Appliance](#batch-appliance)
        - [Batch Appliance Create Device Appliance Vmx Authentication Token](#batch-appliance-create-device-appliance-vmx-authentication-token)
        - [Batch Appliance Create Network Appliance Prefixes Delegated Static](#batch-appliance-create-network-appliance-prefixes-delegated-static)
        - [Batch Appliance Create Network Appliance Traffic Shaping Custom Performance Class](#batch-appliance-create-network-appliance-traffic-shaping-custom-performance-class)
        - [Batch Appliance Create Network Appliance Vlan](#batch-appliance-create-network-appliance-vlan)
        - [Batch Appliance Delete Network Appliance Prefixes Delegated Static](#batch-appliance-delete-network-appliance-prefixes-delegated-static)
        - [Batch Appliance Delete Network Appliance Traffic Shaping Custom Performance Class](#batch-appliance-delete-network-appliance-traffic-shaping-custom-performance-class)
        - [Batch Appliance Delete Network Appliance Vlan](#batch-appliance-delete-network-appliance-vlan)
        - [Batch Appliance Swap Network Appliance Warm Spare](#batch-appliance-swap-network-appliance-warm-spare)
        - [Batch Appliance Update Device Appliance Uplinks Settings](#batch-appliance-update-device-appliance-uplinks-settings)
        - [Batch Appliance Update Network Appliance Connectivity Monitoring Destinations](#batch-appliance-update-network-appliance-connectivity-monitoring-destinations)
        - [Batch Appliance Update Network Appliance Firewall L7 Firewall Rules](#batch-appliance-update-network-appliance-firewall-l7-firewall-rules)
        - [Batch Appliance Update Network Appliance Port](#batch-appliance-update-network-appliance-port)
        - [Batch Appliance Update Network Appliance Prefixes Delegated Static](#batch-appliance-update-network-appliance-prefixes-delegated-static)
        - [Batch Appliance Update Network Appliance Settings](#batch-appliance-update-network-appliance-settings)
        - [Batch Appliance Update Network Appliance Single Lan](#batch-appliance-update-network-appliance-single-lan)
        - [Batch Appliance Update Network Appliance Ssid](#batch-appliance-update-network-appliance-ssid)
        - [Batch Appliance Update Network Appliance Traffic Shaping Custom Performance Class](#batch-appliance-update-network-appliance-traffic-shaping-custom-performance-class)
        - [Batch Appliance Update Network Appliance Traffic Shaping Rules](#batch-appliance-update-network-appliance-traffic-shaping-rules)
        - [Batch Appliance Update Network Appliance Traffic Shaping Uplink Bandwidth](#batch-appliance-update-network-appliance-traffic-shaping-uplink-bandwidth)
        - [Batch Appliance Update Network Appliance Traffic Shaping Uplink Selection](#batch-appliance-update-network-appliance-traffic-shaping-uplink-selection)
        - [Batch Appliance Update Network Appliance Vlan](#batch-appliance-update-network-appliance-vlan)
        - [Batch Appliance Update Network Appliance Vlans Settings](#batch-appliance-update-network-appliance-vlans-settings)
        - [Batch Appliance Update Network Appliance Vpn Bgp](#batch-appliance-update-network-appliance-vpn-bgp)
        - [Batch Appliance Update Network Appliance Vpn Site To Site Vpn](#batch-appliance-update-network-appliance-vpn-site-to-site-vpn)
        - [Batch Appliance Update Network Appliance Warm Spare](#batch-appliance-update-network-appliance-warm-spare)
        - [Batch Appliance Update Organization Appliance Vpn Third Party V P N Peers](#batch-appliance-update-organization-appliance-vpn-third-party-v-p-n-peers)
    - [Batch Camera](#batch-camera)
        - [Batch Camera Update Device Camera Custom Analytics](#batch-camera-update-device-camera-custom-analytics)
        - [Batch Camera Update Device Camera Quality And Retention](#batch-camera-update-device-camera-quality-and-retention)
        - [Batch Camera Update Device Camera Sense](#batch-camera-update-device-camera-sense)
        - [Batch Camera Update Device Camera Video Settings](#batch-camera-update-device-camera-video-settings)
        - [Batch Camera Update Device Camera Wireless Profiles](#batch-camera-update-device-camera-wireless-profiles)
    - [Batch Cellular Gateway](#batch-cellular-gateway)
        - [Batch Cellular Gateway Update Device Cellular Gateway Lan](#batch-cellular-gateway-update-device-cellular-gateway-lan)
        - [Batch Cellular Gateway Update Device Cellular Gateway Port Forwarding Rules](#batch-cellular-gateway-update-device-cellular-gateway-port-forwarding-rules)
        - [Batch Cellular Gateway Update Network Cellular Gateway Connectivity Monitoring Destinations](#batch-cellular-gateway-update-network-cellular-gateway-connectivity-monitoring-destinations)
        - [Batch Cellular Gateway Update Network Cellular Gateway Dhcp](#batch-cellular-gateway-update-network-cellular-gateway-dhcp)
        - [Batch Cellular Gateway Update Network Cellular Gateway Subnet Pool](#batch-cellular-gateway-update-network-cellular-gateway-subnet-pool)
        - [Batch Cellular Gateway Update Network Cellular Gateway Uplink](#batch-cellular-gateway-update-network-cellular-gateway-uplink)
    - [Batch Devices](#batch-devices)
        - [Batch Devices Update Device](#batch-devices-update-device)
        - [Batch Devices Update Device Management Interface](#batch-devices-update-device-management-interface)
    - [Batch Insight](#batch-insight)
        - [Batch Insight Create Organization Insight Monitored Media Server](#batch-insight-create-organization-insight-monitored-media-server)
        - [Batch Insight Delete Organization Insight Monitored Media Server](#batch-insight-delete-organization-insight-monitored-media-server)
        - [Batch Insight Update Organization Insight Monitored Media Server](#batch-insight-update-organization-insight-monitored-media-server)
    - [Batch Networks](#batch-networks)
        - [Batch Networks Bind Network](#batch-networks-bind-network)
        - [Batch Networks Claim Network Devices](#batch-networks-claim-network-devices)
        - [Batch Networks Create Network Firmware Upgrades Rollback](#batch-networks-create-network-firmware-upgrades-rollback)
        - [Batch Networks Create Network Firmware Upgrades Staged Group](#batch-networks-create-network-firmware-upgrades-staged-group)
        - [Batch Networks Create Network Group Policy](#batch-networks-create-network-group-policy)
        - [Batch Networks Create Network Meraki Auth User](#batch-networks-create-network-meraki-auth-user)
        - [Batch Networks Create Network Mqtt Broker](#batch-networks-create-network-mqtt-broker)
        - [Batch Networks Create Network Webhooks Payload Template](#batch-networks-create-network-webhooks-payload-template)
        - [Batch Networks Delete Network](#batch-networks-delete-network)
        - [Batch Networks Delete Network Firmware Upgrades Staged Group](#batch-networks-delete-network-firmware-upgrades-staged-group)
        - [Batch Networks Delete Network Floor Plan](#batch-networks-delete-network-floor-plan)
        - [Batch Networks Delete Network Group Policy](#batch-networks-delete-network-group-policy)
        - [Batch Networks Delete Network Meraki Auth User](#batch-networks-delete-network-meraki-auth-user)
        - [Batch Networks Delete Network Mqtt Broker](#batch-networks-delete-network-mqtt-broker)
        - [Batch Networks Delete Network Webhooks Payload Template](#batch-networks-delete-network-webhooks-payload-template)
        - [Batch Networks Provision Network Clients](#batch-networks-provision-network-clients)
        - [Batch Networks Remove Network Devices](#batch-networks-remove-network-devices)
        - [Batch Networks Split Network](#batch-networks-split-network)
        - [Batch Networks Unbind Network](#batch-networks-unbind-network)
        - [Batch Networks Update Network](#batch-networks-update-network)
        - [Batch Networks Update Network Firmware Upgrades](#batch-networks-update-network-firmware-upgrades)
        - [Batch Networks Update Network Floor Plan](#batch-networks-update-network-floor-plan)
        - [Batch Networks Update Network Group Policy](#batch-networks-update-network-group-policy)
        - [Batch Networks Update Network Meraki Auth User](#batch-networks-update-network-meraki-auth-user)
        - [Batch Networks Update Network Mqtt Broker](#batch-networks-update-network-mqtt-broker)
        - [Batch Networks Update Network Settings](#batch-networks-update-network-settings)
        - [Batch Networks Update Network Webhooks Payload Template](#batch-networks-update-network-webhooks-payload-template)
        - [Batch Networks Vmx Network Devices Claim](#batch-networks-vmx-network-devices-claim)
    - [Batch Organizations](#batch-organizations)
        - [Batch Organizations Assign Organization Licenses Seats](#batch-organizations-assign-organization-licenses-seats)
        - [Batch Organizations Combine Organization Networks](#batch-organizations-combine-organization-networks)
        - [Batch Organizations Create Organization Adaptive Policy Acl](#batch-organizations-create-organization-adaptive-policy-acl)
        - [Batch Organizations Create Organization Adaptive Policy Group](#batch-organizations-create-organization-adaptive-policy-group)
        - [Batch Organizations Create Organization Adaptive Policy Policy](#batch-organizations-create-organization-adaptive-policy-policy)
        - [Batch Organizations Create Organization Alerts Profile](#batch-organizations-create-organization-alerts-profile)
        - [Batch Organizations Create Organization Branding Policy](#batch-organizations-create-organization-branding-policy)
        - [Batch Organizations Create Organization Config Template](#batch-organizations-create-organization-config-template)
        - [Batch Organizations Create Organization Network](#batch-organizations-create-organization-network)
        - [Batch Organizations Create Organization Policy Object](#batch-organizations-create-organization-policy-object)
        - [Batch Organizations Create Organization Policy Objects Group](#batch-organizations-create-organization-policy-objects-group)
        - [Batch Organizations Create Organization Saml Idp](#batch-organizations-create-organization-saml-idp)
        - [Batch Organizations Delete Organization Adaptive Policy Acl](#batch-organizations-delete-organization-adaptive-policy-acl)
        - [Batch Organizations Delete Organization Adaptive Policy Group](#batch-organizations-delete-organization-adaptive-policy-group)
        - [Batch Organizations Delete Organization Adaptive Policy Policy](#batch-organizations-delete-organization-adaptive-policy-policy)
        - [Batch Organizations Delete Organization Alerts Profile](#batch-organizations-delete-organization-alerts-profile)
        - [Batch Organizations Delete Organization Branding Policy](#batch-organizations-delete-organization-branding-policy)
        - [Batch Organizations Delete Organization Policy Object](#batch-organizations-delete-organization-policy-object)
        - [Batch Organizations Delete Organization Policy Objects Group](#batch-organizations-delete-organization-policy-objects-group)
        - [Batch Organizations Delete Organization Saml Idp](#batch-organizations-delete-organization-saml-idp)
        - [Batch Organizations Delete Organization User](#batch-organizations-delete-organization-user)
        - [Batch Organizations Move Organization Licenses](#batch-organizations-move-organization-licenses)
        - [Batch Organizations Move Organization Licenses Seats](#batch-organizations-move-organization-licenses-seats)
        - [Batch Organizations Renew Organization Licenses Seats](#batch-organizations-renew-organization-licenses-seats)
        - [Batch Organizations Update Organization Adaptive Policy Acl](#batch-organizations-update-organization-adaptive-policy-acl)
        - [Batch Organizations Update Organization Adaptive Policy Group](#batch-organizations-update-organization-adaptive-policy-group)
        - [Batch Organizations Update Organization Adaptive Policy Policy](#batch-organizations-update-organization-adaptive-policy-policy)
        - [Batch Organizations Update Organization Adaptive Policy Settings](#batch-organizations-update-organization-adaptive-policy-settings)
        - [Batch Organizations Update Organization Alerts Profile](#batch-organizations-update-organization-alerts-profile)
        - [Batch Organizations Update Organization Branding Policies Priorities](#batch-organizations-update-organization-branding-policies-priorities)
        - [Batch Organizations Update Organization Branding Policy](#batch-organizations-update-organization-branding-policy)
        - [Batch Organizations Update Organization Config Template](#batch-organizations-update-organization-config-template)
        - [Batch Organizations Update Organization Early Access Features Opt In](#batch-organizations-update-organization-early-access-features-opt-in)
        - [Batch Organizations Update Organization License](#batch-organizations-update-organization-license)
        - [Batch Organizations Update Organization Login Security](#batch-organizations-update-organization-login-security)
        - [Batch Organizations Update Organization Policy Object](#batch-organizations-update-organization-policy-object)
        - [Batch Organizations Update Organization Policy Objects Group](#batch-organizations-update-organization-policy-objects-group)
        - [Batch Organizations Update Organization Saml Idp](#batch-organizations-update-organization-saml-idp)
    - [Batch Sensor](#batch-sensor)
        - [Batch Sensor Create Network Sensor Alerts Profile](#batch-sensor-create-network-sensor-alerts-profile)
        - [Batch Sensor Delete Network Sensor Alerts Profile](#batch-sensor-delete-network-sensor-alerts-profile)
        - [Batch Sensor Update Device Sensor Relationships](#batch-sensor-update-device-sensor-relationships)
        - [Batch Sensor Update Network Sensor Alerts Profile](#batch-sensor-update-network-sensor-alerts-profile)
    - [Batch Sm](#batch-sm)
        - [Batch Sm Delete Network Sm User Access Device](#batch-sm-delete-network-sm-user-access-device)
    - [Batch Switch](#batch-switch)
        - [Batch Switch Clone Organization Switch Devices](#batch-switch-clone-organization-switch-devices)
        - [Batch Switch Create Device Switch Routing Interface](#batch-switch-create-device-switch-routing-interface)
        - [Batch Switch Create Device Switch Routing Static Route](#batch-switch-create-device-switch-routing-static-route)
        - [Batch Switch Create Network Switch Access Policy](#batch-switch-create-network-switch-access-policy)
        - [Batch Switch Create Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#batch-switch-create-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
        - [Batch Switch Create Network Switch Link Aggregation](#batch-switch-create-network-switch-link-aggregation)
        - [Batch Switch Create Network Switch Qos Rule](#batch-switch-create-network-switch-qos-rule)
        - [Batch Switch Create Network Switch Routing Multicast Rendezvous Point](#batch-switch-create-network-switch-routing-multicast-rendezvous-point)
        - [Batch Switch Create Network Switch Stack Routing Interface](#batch-switch-create-network-switch-stack-routing-interface)
        - [Batch Switch Create Network Switch Stack Routing Static Route](#batch-switch-create-network-switch-stack-routing-static-route)
        - [Batch Switch Cycle Device Switch Ports](#batch-switch-cycle-device-switch-ports)
        - [Batch Switch Delete Device Switch Routing Interface](#batch-switch-delete-device-switch-routing-interface)
        - [Batch Switch Delete Device Switch Routing Static Route](#batch-switch-delete-device-switch-routing-static-route)
        - [Batch Switch Delete Network Switch Access Policy](#batch-switch-delete-network-switch-access-policy)
        - [Batch Switch Delete Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#batch-switch-delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
        - [Batch Switch Delete Network Switch Link Aggregation](#batch-switch-delete-network-switch-link-aggregation)
        - [Batch Switch Delete Network Switch Qos Rule](#batch-switch-delete-network-switch-qos-rule)
        - [Batch Switch Delete Network Switch Routing Multicast Rendezvous Point](#batch-switch-delete-network-switch-routing-multicast-rendezvous-point)
        - [Batch Switch Delete Network Switch Stack Routing Interface](#batch-switch-delete-network-switch-stack-routing-interface)
        - [Batch Switch Delete Network Switch Stack Routing Static Route](#batch-switch-delete-network-switch-stack-routing-static-route)
        - [Batch Switch Update Device Switch Port](#batch-switch-update-device-switch-port)
        - [Batch Switch Update Device Switch Routing Interface](#batch-switch-update-device-switch-routing-interface)
        - [Batch Switch Update Device Switch Routing Interface Dhcp](#batch-switch-update-device-switch-routing-interface-dhcp)
        - [Batch Switch Update Device Switch Routing Static Route](#batch-switch-update-device-switch-routing-static-route)
        - [Batch Switch Update Device Switch Warm Spare](#batch-switch-update-device-switch-warm-spare)
        - [Batch Switch Update Network Switch Access Policy](#batch-switch-update-network-switch-access-policy)
        - [Batch Switch Update Network Switch Alternate Management Interface](#batch-switch-update-network-switch-alternate-management-interface)
        - [Batch Switch Update Network Switch Dhcp Server Policy](#batch-switch-update-network-switch-dhcp-server-policy)
        - [Batch Switch Update Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#batch-switch-update-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
        - [Batch Switch Update Network Switch Dscp To Cos Mappings](#batch-switch-update-network-switch-dscp-to-cos-mappings)
        - [Batch Switch Update Network Switch Link Aggregation](#batch-switch-update-network-switch-link-aggregation)
        - [Batch Switch Update Network Switch Mtu](#batch-switch-update-network-switch-mtu)
        - [Batch Switch Update Network Switch Port Schedule](#batch-switch-update-network-switch-port-schedule)
        - [Batch Switch Update Network Switch Qos Rule](#batch-switch-update-network-switch-qos-rule)
        - [Batch Switch Update Network Switch Qos Rules Order](#batch-switch-update-network-switch-qos-rules-order)
        - [Batch Switch Update Network Switch Routing Multicast](#batch-switch-update-network-switch-routing-multicast)
        - [Batch Switch Update Network Switch Routing Multicast Rendezvous Point](#batch-switch-update-network-switch-routing-multicast-rendezvous-point)
        - [Batch Switch Update Network Switch Routing Ospf](#batch-switch-update-network-switch-routing-ospf)
        - [Batch Switch Update Network Switch Settings](#batch-switch-update-network-switch-settings)
        - [Batch Switch Update Network Switch Stack Routing Interface](#batch-switch-update-network-switch-stack-routing-interface)
        - [Batch Switch Update Network Switch Stack Routing Interface Dhcp](#batch-switch-update-network-switch-stack-routing-interface-dhcp)
        - [Batch Switch Update Network Switch Stack Routing Static Route](#batch-switch-update-network-switch-stack-routing-static-route)
        - [Batch Switch Update Network Switch Storm Control](#batch-switch-update-network-switch-storm-control)
        - [Batch Switch Update Network Switch Stp](#batch-switch-update-network-switch-stp)
        - [Batch Switch Update Organization Config Template Switch Profile Port](#batch-switch-update-organization-config-template-switch-profile-port)
    - [Batch Wireless](#batch-wireless)
        - [Batch Wireless Create Network Wireless Rf Profile](#batch-wireless-create-network-wireless-rf-profile)
        - [Batch Wireless Create Network Wireless Ssid Identity Psk](#batch-wireless-create-network-wireless-ssid-identity-psk)
        - [Batch Wireless Delete Network Wireless Rf Profile](#batch-wireless-delete-network-wireless-rf-profile)
        - [Batch Wireless Delete Network Wireless Ssid Identity Psk](#batch-wireless-delete-network-wireless-ssid-identity-psk)
        - [Batch Wireless Update Device Wireless Bluetooth Settings](#batch-wireless-update-device-wireless-bluetooth-settings)
        - [Batch Wireless Update Device Wireless Radio Settings](#batch-wireless-update-device-wireless-radio-settings)
        - [Batch Wireless Update Network Wireless Alternate Management Interface](#batch-wireless-update-network-wireless-alternate-management-interface)
        - [Batch Wireless Update Network Wireless Billing](#batch-wireless-update-network-wireless-billing)
        - [Batch Wireless Update Network Wireless Rf Profile](#batch-wireless-update-network-wireless-rf-profile)
        - [Batch Wireless Update Network Wireless Settings](#batch-wireless-update-network-wireless-settings)
        - [Batch Wireless Update Network Wireless Ssid](#batch-wireless-update-network-wireless-ssid)
        - [Batch Wireless Update Network Wireless Ssid Bonjour Forwarding](#batch-wireless-update-network-wireless-ssid-bonjour-forwarding)
        - [Batch Wireless Update Network Wireless Ssid Device Type Group Policies](#batch-wireless-update-network-wireless-ssid-device-type-group-policies)
        - [Batch Wireless Update Network Wireless Ssid Eap Override](#batch-wireless-update-network-wireless-ssid-eap-override)
        - [Batch Wireless Update Network Wireless Ssid Firewall L3 Firewall Rules](#batch-wireless-update-network-wireless-ssid-firewall-l3-firewall-rules)
        - [Batch Wireless Update Network Wireless Ssid Firewall L7 Firewall Rules](#batch-wireless-update-network-wireless-ssid-firewall-l7-firewall-rules)
        - [Batch Wireless Update Network Wireless Ssid Hotspot20](#batch-wireless-update-network-wireless-ssid-hotspot20)
        - [Batch Wireless Update Network Wireless Ssid Identity Psk](#batch-wireless-update-network-wireless-ssid-identity-psk)
        - [Batch Wireless Update Network Wireless Ssid Schedules](#batch-wireless-update-network-wireless-ssid-schedules)
        - [Batch Wireless Update Network Wireless Ssid Splash Settings](#batch-wireless-update-network-wireless-ssid-splash-settings)
        - [Batch Wireless Update Network Wireless Ssid Traffic Shaping Rules](#batch-wireless-update-network-wireless-ssid-traffic-shaping-rules)
        - [Batch Wireless Update Network Wireless Ssid Vpn](#batch-wireless-update-network-wireless-ssid-vpn)
- [Camera](#camera)
    - [Camera Create Network Camera Quality Retention Profile](#camera-create-network-camera-quality-retention-profile)
    - [Camera Create Network Camera Wireless Profile](#camera-create-network-camera-wireless-profile)
    - [Camera Create Organization Camera Custom Analytics Artifact](#camera-create-organization-camera-custom-analytics-artifact)
    - [Camera Delete Network Camera Quality Retention Profile](#camera-delete-network-camera-quality-retention-profile)
    - [Camera Delete Network Camera Wireless Profile](#camera-delete-network-camera-wireless-profile)
    - [Camera Delete Organization Camera Custom Analytics Artifact](#camera-delete-organization-camera-custom-analytics-artifact)
    - [Camera Generate Device Camera Snapshot](#camera-generate-device-camera-snapshot)
    - [Camera Get Device Camera Analytics Live](#camera-get-device-camera-analytics-live)
    - [Camera Get Device Camera Analytics Overview](#camera-get-device-camera-analytics-overview)
    - [Camera Get Device Camera Analytics Recent](#camera-get-device-camera-analytics-recent)
    - [Camera Get Device Camera Analytics Zone History](#camera-get-device-camera-analytics-zone-history)
    - [Camera Get Device Camera Analytics Zones](#camera-get-device-camera-analytics-zones)
    - [Camera Get Device Camera Custom Analytics](#camera-get-device-camera-custom-analytics)
    - [Camera Get Device Camera Quality And Retention](#camera-get-device-camera-quality-and-retention)
    - [Camera Get Device Camera Sense](#camera-get-device-camera-sense)
    - [Camera Get Device Camera Sense Object Detection Models](#camera-get-device-camera-sense-object-detection-models)
    - [Camera Get Device Camera Video Link](#camera-get-device-camera-video-link)
    - [Camera Get Device Camera Video Settings](#camera-get-device-camera-video-settings)
    - [Camera Get Device Camera Wireless Profiles](#camera-get-device-camera-wireless-profiles)
    - [Camera Get Network Camera Quality Retention Profile](#camera-get-network-camera-quality-retention-profile)
    - [Camera Get Network Camera Quality Retention Profiles](#camera-get-network-camera-quality-retention-profiles)
    - [Camera Get Network Camera Schedules](#camera-get-network-camera-schedules)
    - [Camera Get Network Camera Wireless Profile](#camera-get-network-camera-wireless-profile)
    - [Camera Get Network Camera Wireless Profiles](#camera-get-network-camera-wireless-profiles)
    - [Camera Get Organization Camera Custom Analytics Artifact](#camera-get-organization-camera-custom-analytics-artifact)
    - [Camera Get Organization Camera Custom Analytics Artifacts](#camera-get-organization-camera-custom-analytics-artifacts)
    - [Camera Get Organization Camera Onboarding Statuses](#camera-get-organization-camera-onboarding-statuses)
    - [Camera Update Device Camera Custom Analytics](#camera-update-device-camera-custom-analytics)
    - [Camera Update Device Camera Quality And Retention](#camera-update-device-camera-quality-and-retention)
    - [Camera Update Device Camera Sense](#camera-update-device-camera-sense)
    - [Camera Update Device Camera Video Settings](#camera-update-device-camera-video-settings)
    - [Camera Update Device Camera Wireless Profiles](#camera-update-device-camera-wireless-profiles)
    - [Camera Update Network Camera Quality Retention Profile](#camera-update-network-camera-quality-retention-profile)
    - [Camera Update Network Camera Wireless Profile](#camera-update-network-camera-wireless-profile)
    - [Camera Update Organization Camera Onboarding Statuses](#camera-update-organization-camera-onboarding-statuses)
- [Cellular Gateway](#cellular-gateway)
    - [Cellular Gateway Get Device Cellular Gateway Lan](#cellular-gateway-get-device-cellular-gateway-lan)
    - [Cellular Gateway Get Device Cellular Gateway Port Forwarding Rules](#cellular-gateway-get-device-cellular-gateway-port-forwarding-rules)
    - [Cellular Gateway Get Network Cellular Gateway Connectivity Monitoring Destinations](#cellular-gateway-get-network-cellular-gateway-connectivity-monitoring-destinations)
    - [Cellular Gateway Get Network Cellular Gateway Dhcp](#cellular-gateway-get-network-cellular-gateway-dhcp)
    - [Cellular Gateway Get Network Cellular Gateway Subnet Pool](#cellular-gateway-get-network-cellular-gateway-subnet-pool)
    - [Cellular Gateway Get Network Cellular Gateway Uplink](#cellular-gateway-get-network-cellular-gateway-uplink)
    - [Cellular Gateway Get Organization Cellular Gateway Uplink Statuses](#cellular-gateway-get-organization-cellular-gateway-uplink-statuses)
    - [Cellular Gateway Update Device Cellular Gateway Lan](#cellular-gateway-update-device-cellular-gateway-lan)
    - [Cellular Gateway Update Device Cellular Gateway Port Forwarding Rules](#cellular-gateway-update-device-cellular-gateway-port-forwarding-rules)
    - [Cellular Gateway Update Network Cellular Gateway Connectivity Monitoring Destinations](#cellular-gateway-update-network-cellular-gateway-connectivity-monitoring-destinations)
    - [Cellular Gateway Update Network Cellular Gateway Dhcp](#cellular-gateway-update-network-cellular-gateway-dhcp)
    - [Cellular Gateway Update Network Cellular Gateway Subnet Pool](#cellular-gateway-update-network-cellular-gateway-subnet-pool)
    - [Cellular Gateway Update Network Cellular Gateway Uplink](#cellular-gateway-update-network-cellular-gateway-uplink)
- [Devices](#devices)
    - [Devices Blink Device Leds](#devices-blink-device-leds)
    - [Devices Create Device Live Tools Ping](#devices-create-device-live-tools-ping)
    - [Devices Create Device Live Tools Ping Device](#devices-create-device-live-tools-ping-device)
    - [Devices Get Device](#devices-get-device)
    - [Devices Get Device Cellular Sims](#devices-get-device-cellular-sims)
    - [Devices Get Device Clients](#devices-get-device-clients)
    - [Devices Get Device Live Tools Ping](#devices-get-device-live-tools-ping)
    - [Devices Get Device Live Tools Ping Device](#devices-get-device-live-tools-ping-device)
    - [Devices Get Device Lldp Cdp](#devices-get-device-lldp-cdp)
    - [Devices Get Device Loss And Latency History](#devices-get-device-loss-and-latency-history)
    - [Devices Get Device Management Interface](#devices-get-device-management-interface)
    - [Devices Reboot Device](#devices-reboot-device)
    - [Devices Update Device](#devices-update-device)
    - [Devices Update Device Cellular Sims](#devices-update-device-cellular-sims)
    - [Devices Update Device Management Interface](#devices-update-device-management-interface)
- [Insight](#insight)
    - [Insight Create Organization Insight Monitored Media Server](#insight-create-organization-insight-monitored-media-server)
    - [Insight Delete Organization Insight Monitored Media Server](#insight-delete-organization-insight-monitored-media-server)
    - [Insight Get Network Insight Application Health By Time](#insight-get-network-insight-application-health-by-time)
    - [Insight Get Organization Insight Applications](#insight-get-organization-insight-applications)
    - [Insight Get Organization Insight Monitored Media Server](#insight-get-organization-insight-monitored-media-server)
    - [Insight Get Organization Insight Monitored Media Servers](#insight-get-organization-insight-monitored-media-servers)
    - [Insight Update Organization Insight Monitored Media Server](#insight-update-organization-insight-monitored-media-server)
- [Licensing](#licensing)
    - [Licensing Get Organization Licensing Coterm Licenses](#licensing-get-organization-licensing-coterm-licenses)
    - [Licensing Move Organization Licensing Coterm Licenses](#licensing-move-organization-licensing-coterm-licenses)
- [Networks](#networks)
    - [Networks Bind Network](#networks-bind-network)
    - [Networks Claim Network Devices](#networks-claim-network-devices)
    - [Networks Create Network Firmware Upgrades Rollback](#networks-create-network-firmware-upgrades-rollback)
    - [Networks Create Network Firmware Upgrades Staged Event](#networks-create-network-firmware-upgrades-staged-event)
    - [Networks Create Network Firmware Upgrades Staged Group](#networks-create-network-firmware-upgrades-staged-group)
    - [Networks Create Network Floor Plan](#networks-create-network-floor-plan)
    - [Networks Create Network Group Policy](#networks-create-network-group-policy)
    - [Networks Create Network Meraki Auth User](#networks-create-network-meraki-auth-user)
    - [Networks Create Network Mqtt Broker](#networks-create-network-mqtt-broker)
    - [Networks Create Network Pii Request](#networks-create-network-pii-request)
    - [Networks Create Network Webhooks Http Server](#networks-create-network-webhooks-http-server)
    - [Networks Create Network Webhooks Payload Template](#networks-create-network-webhooks-payload-template)
    - [Networks Create Network Webhooks Webhook Test](#networks-create-network-webhooks-webhook-test)
    - [Networks Defer Network Firmware Upgrades Staged Events](#networks-defer-network-firmware-upgrades-staged-events)
    - [Networks Delete Network](#networks-delete-network)
    - [Networks Delete Network Firmware Upgrades Staged Group](#networks-delete-network-firmware-upgrades-staged-group)
    - [Networks Delete Network Floor Plan](#networks-delete-network-floor-plan)
    - [Networks Delete Network Group Policy](#networks-delete-network-group-policy)
    - [Networks Delete Network Meraki Auth User](#networks-delete-network-meraki-auth-user)
    - [Networks Delete Network Mqtt Broker](#networks-delete-network-mqtt-broker)
    - [Networks Delete Network Pii Request](#networks-delete-network-pii-request)
    - [Networks Delete Network Webhooks Http Server](#networks-delete-network-webhooks-http-server)
    - [Networks Delete Network Webhooks Payload Template](#networks-delete-network-webhooks-payload-template)
    - [Networks Get Network](#networks-get-network)
    - [Networks Get Network Alerts History](#networks-get-network-alerts-history)
    - [Networks Get Network Alerts Settings](#networks-get-network-alerts-settings)
    - [Networks Get Network Bluetooth Client](#networks-get-network-bluetooth-client)
    - [Networks Get Network Bluetooth Clients](#networks-get-network-bluetooth-clients)
    - [Networks Get Network Client](#networks-get-network-client)
    - [Networks Get Network Client Policy](#networks-get-network-client-policy)
    - [Networks Get Network Client Splash Authorization Status](#networks-get-network-client-splash-authorization-status)
    - [Networks Get Network Client Traffic History](#networks-get-network-client-traffic-history)
    - [Networks Get Network Client Usage History](#networks-get-network-client-usage-history)
    - [Networks Get Network Clients](#networks-get-network-clients)
    - [Networks Get Network Clients Application Usage](#networks-get-network-clients-application-usage)
    - [Networks Get Network Clients Bandwidth Usage History](#networks-get-network-clients-bandwidth-usage-history)
    - [Networks Get Network Clients Overview](#networks-get-network-clients-overview)
    - [Networks Get Network Clients Usage Histories](#networks-get-network-clients-usage-histories)
    - [Networks Get Network Devices](#networks-get-network-devices)
    - [Networks Get Network Events](#networks-get-network-events)
    - [Networks Get Network Events Event Types](#networks-get-network-events-event-types)
    - [Networks Get Network Firmware Upgrades](#networks-get-network-firmware-upgrades)
    - [Networks Get Network Firmware Upgrades Staged Events](#networks-get-network-firmware-upgrades-staged-events)
    - [Networks Get Network Firmware Upgrades Staged Group](#networks-get-network-firmware-upgrades-staged-group)
    - [Networks Get Network Firmware Upgrades Staged Groups](#networks-get-network-firmware-upgrades-staged-groups)
    - [Networks Get Network Firmware Upgrades Staged Stages](#networks-get-network-firmware-upgrades-staged-stages)
    - [Networks Get Network Floor Plan](#networks-get-network-floor-plan)
    - [Networks Get Network Floor Plans](#networks-get-network-floor-plans)
    - [Networks Get Network Group Policies](#networks-get-network-group-policies)
    - [Networks Get Network Group Policy](#networks-get-network-group-policy)
    - [Networks Get Network Health Alerts](#networks-get-network-health-alerts)
    - [Networks Get Network Meraki Auth User](#networks-get-network-meraki-auth-user)
    - [Networks Get Network Meraki Auth Users](#networks-get-network-meraki-auth-users)
    - [Networks Get Network Mqtt Broker](#networks-get-network-mqtt-broker)
    - [Networks Get Network Mqtt Brokers](#networks-get-network-mqtt-brokers)
    - [Networks Get Network Netflow](#networks-get-network-netflow)
    - [Networks Get Network Network Health Channel Utilization](#networks-get-network-network-health-channel-utilization)
    - [Networks Get Network Pii Pii Keys](#networks-get-network-pii-pii-keys)
    - [Networks Get Network Pii Request](#networks-get-network-pii-request)
    - [Networks Get Network Pii Requests](#networks-get-network-pii-requests)
    - [Networks Get Network Pii Sm Devices For Key](#networks-get-network-pii-sm-devices-for-key)
    - [Networks Get Network Pii Sm Owners For Key](#networks-get-network-pii-sm-owners-for-key)
    - [Networks Get Network Policies By Client](#networks-get-network-policies-by-client)
    - [Networks Get Network Settings](#networks-get-network-settings)
    - [Networks Get Network Snmp](#networks-get-network-snmp)
    - [Networks Get Network Splash Login Attempts](#networks-get-network-splash-login-attempts)
    - [Networks Get Network Syslog Servers](#networks-get-network-syslog-servers)
    - [Networks Get Network Topology Link Layer](#networks-get-network-topology-link-layer)
    - [Networks Get Network Traffic](#networks-get-network-traffic)
    - [Networks Get Network Traffic Analysis](#networks-get-network-traffic-analysis)
    - [Networks Get Network Traffic Shaping Application Categories](#networks-get-network-traffic-shaping-application-categories)
    - [Networks Get Network Traffic Shaping Dscp Tagging Options](#networks-get-network-traffic-shaping-dscp-tagging-options)
    - [Networks Get Network Webhooks Http Server](#networks-get-network-webhooks-http-server)
    - [Networks Get Network Webhooks Http Servers](#networks-get-network-webhooks-http-servers)
    - [Networks Get Network Webhooks Payload Template](#networks-get-network-webhooks-payload-template)
    - [Networks Get Network Webhooks Payload Templates](#networks-get-network-webhooks-payload-templates)
    - [Networks Get Network Webhooks Webhook Test](#networks-get-network-webhooks-webhook-test)
    - [Networks Provision Network Clients](#networks-provision-network-clients)
    - [Networks Remove Network Devices](#networks-remove-network-devices)
    - [Networks Rollbacks Network Firmware Upgrades Staged Events](#networks-rollbacks-network-firmware-upgrades-staged-events)
    - [Networks Split Network](#networks-split-network)
    - [Networks Unbind Network](#networks-unbind-network)
    - [Networks Update Network](#networks-update-network)
    - [Networks Update Network Alerts Settings](#networks-update-network-alerts-settings)
    - [Networks Update Network Client Policy](#networks-update-network-client-policy)
    - [Networks Update Network Client Splash Authorization Status](#networks-update-network-client-splash-authorization-status)
    - [Networks Update Network Firmware Upgrades](#networks-update-network-firmware-upgrades)
    - [Networks Update Network Firmware Upgrades Staged Events](#networks-update-network-firmware-upgrades-staged-events)
    - [Networks Update Network Firmware Upgrades Staged Group](#networks-update-network-firmware-upgrades-staged-group)
    - [Networks Update Network Firmware Upgrades Staged Stages](#networks-update-network-firmware-upgrades-staged-stages)
    - [Networks Update Network Floor Plan](#networks-update-network-floor-plan)
    - [Networks Update Network Group Policy](#networks-update-network-group-policy)
    - [Networks Update Network Meraki Auth User](#networks-update-network-meraki-auth-user)
    - [Networks Update Network Mqtt Broker](#networks-update-network-mqtt-broker)
    - [Networks Update Network Netflow](#networks-update-network-netflow)
    - [Networks Update Network Settings](#networks-update-network-settings)
    - [Networks Update Network Snmp](#networks-update-network-snmp)
    - [Networks Update Network Syslog Servers](#networks-update-network-syslog-servers)
    - [Networks Update Network Traffic Analysis](#networks-update-network-traffic-analysis)
    - [Networks Update Network Webhooks Http Server](#networks-update-network-webhooks-http-server)
    - [Networks Update Network Webhooks Payload Template](#networks-update-network-webhooks-payload-template)
    - [Networks Vmx Network Devices Claim](#networks-vmx-network-devices-claim)
- [Organizations](#organizations)
    - [Organizations Assign Organization Licenses Seats](#organizations-assign-organization-licenses-seats)
    - [Organizations Claim Into Organization](#organizations-claim-into-organization)
    - [Organizations Claim Into Organization Inventory](#organizations-claim-into-organization-inventory)
    - [Organizations Clone Organization](#organizations-clone-organization)
    - [Organizations Combine Organization Networks](#organizations-combine-organization-networks)
    - [Organizations Create Organization](#organizations-create-organization)
    - [Organizations Create Organization Action Batch](#organizations-create-organization-action-batch)
    - [Organizations Create Organization Adaptive Policy Acl](#organizations-create-organization-adaptive-policy-acl)
    - [Organizations Create Organization Adaptive Policy Group](#organizations-create-organization-adaptive-policy-group)
    - [Organizations Create Organization Adaptive Policy Policy](#organizations-create-organization-adaptive-policy-policy)
    - [Organizations Create Organization Admin](#organizations-create-organization-admin)
    - [Organizations Create Organization Alerts Profile](#organizations-create-organization-alerts-profile)
    - [Organizations Create Organization Branding Policy](#organizations-create-organization-branding-policy)
    - [Organizations Create Organization Config Template](#organizations-create-organization-config-template)
    - [Organizations Create Organization Early Access Features Opt In](#organizations-create-organization-early-access-features-opt-in)
    - [Organizations Create Organization Inventory Onboarding Cloud Monitoring Export Event](#organizations-create-organization-inventory-onboarding-cloud-monitoring-export-event)
    - [Organizations Create Organization Inventory Onboarding Cloud Monitoring Import](#organizations-create-organization-inventory-onboarding-cloud-monitoring-import)
    - [Organizations Create Organization Inventory Onboarding Cloud Monitoring Prepare](#organizations-create-organization-inventory-onboarding-cloud-monitoring-prepare)
    - [Organizations Create Organization Network](#organizations-create-organization-network)
    - [Organizations Create Organization Policy Object](#organizations-create-organization-policy-object)
    - [Organizations Create Organization Policy Objects Group](#organizations-create-organization-policy-objects-group)
    - [Organizations Create Organization Saml Idp](#organizations-create-organization-saml-idp)
    - [Organizations Create Organization Saml Role](#organizations-create-organization-saml-role)
    - [Organizations Delete Organization](#organizations-delete-organization)
    - [Organizations Delete Organization Action Batch](#organizations-delete-organization-action-batch)
    - [Organizations Delete Organization Adaptive Policy Acl](#organizations-delete-organization-adaptive-policy-acl)
    - [Organizations Delete Organization Adaptive Policy Group](#organizations-delete-organization-adaptive-policy-group)
    - [Organizations Delete Organization Adaptive Policy Policy](#organizations-delete-organization-adaptive-policy-policy)
    - [Organizations Delete Organization Admin](#organizations-delete-organization-admin)
    - [Organizations Delete Organization Alerts Profile](#organizations-delete-organization-alerts-profile)
    - [Organizations Delete Organization Branding Policy](#organizations-delete-organization-branding-policy)
    - [Organizations Delete Organization Config Template](#organizations-delete-organization-config-template)
    - [Organizations Delete Organization Early Access Features Opt In](#organizations-delete-organization-early-access-features-opt-in)
    - [Organizations Delete Organization Policy Object](#organizations-delete-organization-policy-object)
    - [Organizations Delete Organization Policy Objects Group](#organizations-delete-organization-policy-objects-group)
    - [Organizations Delete Organization Saml Idp](#organizations-delete-organization-saml-idp)
    - [Organizations Delete Organization Saml Role](#organizations-delete-organization-saml-role)
    - [Organizations Delete Organization User](#organizations-delete-organization-user)
    - [Organizations Get Organization](#organizations-get-organization)
    - [Organizations Get Organization Action Batch](#organizations-get-organization-action-batch)
    - [Organizations Get Organization Action Batches](#organizations-get-organization-action-batches)
    - [Organizations Get Organization Adaptive Policy Acl](#organizations-get-organization-adaptive-policy-acl)
    - [Organizations Get Organization Adaptive Policy Acls](#organizations-get-organization-adaptive-policy-acls)
    - [Organizations Get Organization Adaptive Policy Group](#organizations-get-organization-adaptive-policy-group)
    - [Organizations Get Organization Adaptive Policy Groups](#organizations-get-organization-adaptive-policy-groups)
    - [Organizations Get Organization Adaptive Policy Overview](#organizations-get-organization-adaptive-policy-overview)
    - [Organizations Get Organization Adaptive Policy Policies](#organizations-get-organization-adaptive-policy-policies)
    - [Organizations Get Organization Adaptive Policy Policy](#organizations-get-organization-adaptive-policy-policy)
    - [Organizations Get Organization Adaptive Policy Settings](#organizations-get-organization-adaptive-policy-settings)
    - [Organizations Get Organization Admins](#organizations-get-organization-admins)
    - [Organizations Get Organization Alerts Profiles](#organizations-get-organization-alerts-profiles)
    - [Organizations Get Organization Api Requests](#organizations-get-organization-api-requests)
    - [Organizations Get Organization Api Requests Overview](#organizations-get-organization-api-requests-overview)
    - [Organizations Get Organization Api Requests Overview Response Codes By Interval](#organizations-get-organization-api-requests-overview-response-codes-by-interval)
    - [Organizations Get Organization Branding Policies](#organizations-get-organization-branding-policies)
    - [Organizations Get Organization Branding Policies Priorities](#organizations-get-organization-branding-policies-priorities)
    - [Organizations Get Organization Branding Policy](#organizations-get-organization-branding-policy)
    - [Organizations Get Organization Clients Bandwidth Usage History](#organizations-get-organization-clients-bandwidth-usage-history)
    - [Organizations Get Organization Clients Overview](#organizations-get-organization-clients-overview)
    - [Organizations Get Organization Clients Search](#organizations-get-organization-clients-search)
    - [Organizations Get Organization Config Template](#organizations-get-organization-config-template)
    - [Organizations Get Organization Config Templates](#organizations-get-organization-config-templates)
    - [Organizations Get Organization Configuration Changes](#organizations-get-organization-configuration-changes)
    - [Organizations Get Organization Devices](#organizations-get-organization-devices)
    - [Organizations Get Organization Devices Availabilities](#organizations-get-organization-devices-availabilities)
    - [Organizations Get Organization Devices Power Modules Statuses By Device](#organizations-get-organization-devices-power-modules-statuses-by-device)
    - [Organizations Get Organization Devices Statuses](#organizations-get-organization-devices-statuses)
    - [Organizations Get Organization Devices Statuses Overview](#organizations-get-organization-devices-statuses-overview)
    - [Organizations Get Organization Devices Uplinks Addresses By Device](#organizations-get-organization-devices-uplinks-addresses-by-device)
    - [Organizations Get Organization Devices Uplinks Loss And Latency](#organizations-get-organization-devices-uplinks-loss-and-latency)
    - [Organizations Get Organization Early Access Features](#organizations-get-organization-early-access-features)
    - [Organizations Get Organization Early Access Features Opt In](#organizations-get-organization-early-access-features-opt-in)
    - [Organizations Get Organization Early Access Features Opt Ins](#organizations-get-organization-early-access-features-opt-ins)
    - [Organizations Get Organization Firmware Upgrades](#organizations-get-organization-firmware-upgrades)
    - [Organizations Get Organization Firmware Upgrades By Device](#organizations-get-organization-firmware-upgrades-by-device)
    - [Organizations Get Organization Inventory Device](#organizations-get-organization-inventory-device)
    - [Organizations Get Organization Inventory Devices](#organizations-get-organization-inventory-devices)
    - [Organizations Get Organization Inventory Onboarding Cloud Monitoring Imports](#organizations-get-organization-inventory-onboarding-cloud-monitoring-imports)
    - [Organizations Get Organization Inventory Onboarding Cloud Monitoring Networks](#organizations-get-organization-inventory-onboarding-cloud-monitoring-networks)
    - [Organizations Get Organization License](#organizations-get-organization-license)
    - [Organizations Get Organization Licenses](#organizations-get-organization-licenses)
    - [Organizations Get Organization Licenses Overview](#organizations-get-organization-licenses-overview)
    - [Organizations Get Organization Login Security](#organizations-get-organization-login-security)
    - [Organizations Get Organization Networks](#organizations-get-organization-networks)
    - [Organizations Get Organization Openapi Spec](#organizations-get-organization-openapi-spec)
    - [Organizations Get Organization Policy Object](#organizations-get-organization-policy-object)
    - [Organizations Get Organization Policy Objects](#organizations-get-organization-policy-objects)
    - [Organizations Get Organization Policy Objects Group](#organizations-get-organization-policy-objects-group)
    - [Organizations Get Organization Policy Objects Groups](#organizations-get-organization-policy-objects-groups)
    - [Organizations Get Organization Saml](#organizations-get-organization-saml)
    - [Organizations Get Organization Saml Idp](#organizations-get-organization-saml-idp)
    - [Organizations Get Organization Saml Idps](#organizations-get-organization-saml-idps)
    - [Organizations Get Organization Saml Role](#organizations-get-organization-saml-role)
    - [Organizations Get Organization Saml Roles](#organizations-get-organization-saml-roles)
    - [Organizations Get Organization Snmp](#organizations-get-organization-snmp)
    - [Organizations Get Organization Summary Top Appliances By Utilization](#organizations-get-organization-summary-top-appliances-by-utilization)
    - [Organizations Get Organization Summary Top Clients By Usage](#organizations-get-organization-summary-top-clients-by-usage)
    - [Organizations Get Organization Summary Top Clients Manufacturers By Usage](#organizations-get-organization-summary-top-clients-manufacturers-by-usage)
    - [Organizations Get Organization Summary Top Devices By Usage](#organizations-get-organization-summary-top-devices-by-usage)
    - [Organizations Get Organization Summary Top Devices Models By Usage](#organizations-get-organization-summary-top-devices-models-by-usage)
    - [Organizations Get Organization Summary Top Ssids By Usage](#organizations-get-organization-summary-top-ssids-by-usage)
    - [Organizations Get Organization Summary Top Switches By Energy Usage](#organizations-get-organization-summary-top-switches-by-energy-usage)
    - [Organizations Get Organization Uplinks Statuses](#organizations-get-organization-uplinks-statuses)
    - [Organizations Get Organization Webhooks Alert Types](#organizations-get-organization-webhooks-alert-types)
    - [Organizations Get Organization Webhooks Logs](#organizations-get-organization-webhooks-logs)
    - [Organizations Get Organizations](#organizations-get-organizations)
    - [Organizations Move Organization Licenses](#organizations-move-organization-licenses)
    - [Organizations Move Organization Licenses Seats](#organizations-move-organization-licenses-seats)
    - [Organizations Release From Organization Inventory](#organizations-release-from-organization-inventory)
    - [Organizations Renew Organization Licenses Seats](#organizations-renew-organization-licenses-seats)
    - [Organizations Update Organization](#organizations-update-organization)
    - [Organizations Update Organization Action Batch](#organizations-update-organization-action-batch)
    - [Organizations Update Organization Adaptive Policy Acl](#organizations-update-organization-adaptive-policy-acl)
    - [Organizations Update Organization Adaptive Policy Group](#organizations-update-organization-adaptive-policy-group)
    - [Organizations Update Organization Adaptive Policy Policy](#organizations-update-organization-adaptive-policy-policy)
    - [Organizations Update Organization Adaptive Policy Settings](#organizations-update-organization-adaptive-policy-settings)
    - [Organizations Update Organization Admin](#organizations-update-organization-admin)
    - [Organizations Update Organization Alerts Profile](#organizations-update-organization-alerts-profile)
    - [Organizations Update Organization Branding Policies Priorities](#organizations-update-organization-branding-policies-priorities)
    - [Organizations Update Organization Branding Policy](#organizations-update-organization-branding-policy)
    - [Organizations Update Organization Config Template](#organizations-update-organization-config-template)
    - [Organizations Update Organization Early Access Features Opt In](#organizations-update-organization-early-access-features-opt-in)
    - [Organizations Update Organization License](#organizations-update-organization-license)
    - [Organizations Update Organization Login Security](#organizations-update-organization-login-security)
    - [Organizations Update Organization Policy Object](#organizations-update-organization-policy-object)
    - [Organizations Update Organization Policy Objects Group](#organizations-update-organization-policy-objects-group)
    - [Organizations Update Organization Saml](#organizations-update-organization-saml)
    - [Organizations Update Organization Saml Idp](#organizations-update-organization-saml-idp)
    - [Organizations Update Organization Saml Role](#organizations-update-organization-saml-role)
    - [Organizations Update Organization Snmp](#organizations-update-organization-snmp)
- [Sensor](#sensor)
    - [Sensor Create Network Sensor Alerts Profile](#sensor-create-network-sensor-alerts-profile)
    - [Sensor Delete Network Sensor Alerts Profile](#sensor-delete-network-sensor-alerts-profile)
    - [Sensor Get Device Sensor Relationships](#sensor-get-device-sensor-relationships)
    - [Sensor Get Network Sensor Alerts Current Overview By Metric](#sensor-get-network-sensor-alerts-current-overview-by-metric)
    - [Sensor Get Network Sensor Alerts Overview By Metric](#sensor-get-network-sensor-alerts-overview-by-metric)
    - [Sensor Get Network Sensor Alerts Profile](#sensor-get-network-sensor-alerts-profile)
    - [Sensor Get Network Sensor Alerts Profiles](#sensor-get-network-sensor-alerts-profiles)
    - [Sensor Get Network Sensor Relationships](#sensor-get-network-sensor-relationships)
    - [Sensor Get Organization Sensor Readings History](#sensor-get-organization-sensor-readings-history)
    - [Sensor Get Organization Sensor Readings Latest](#sensor-get-organization-sensor-readings-latest)
    - [Sensor Update Device Sensor Relationships](#sensor-update-device-sensor-relationships)
    - [Sensor Update Network Sensor Alerts Profile](#sensor-update-network-sensor-alerts-profile)
- [Sm](#sm)
    - [Sm Checkin Network Sm Devices](#sm-checkin-network-sm-devices)
    - [Sm Create Network Sm Bypass Activation Lock Attempt](#sm-create-network-sm-bypass-activation-lock-attempt)
    - [Sm Create Network Sm Target Group](#sm-create-network-sm-target-group)
    - [Sm Delete Network Sm Target Group](#sm-delete-network-sm-target-group)
    - [Sm Delete Network Sm User Access Device](#sm-delete-network-sm-user-access-device)
    - [Sm Get Network Sm Bypass Activation Lock Attempt](#sm-get-network-sm-bypass-activation-lock-attempt)
    - [Sm Get Network Sm Device Cellular Usage History](#sm-get-network-sm-device-cellular-usage-history)
    - [Sm Get Network Sm Device Certs](#sm-get-network-sm-device-certs)
    - [Sm Get Network Sm Device Connectivity](#sm-get-network-sm-device-connectivity)
    - [Sm Get Network Sm Device Desktop Logs](#sm-get-network-sm-device-desktop-logs)
    - [Sm Get Network Sm Device Device Command Logs](#sm-get-network-sm-device-device-command-logs)
    - [Sm Get Network Sm Device Device Profiles](#sm-get-network-sm-device-device-profiles)
    - [Sm Get Network Sm Device Network Adapters](#sm-get-network-sm-device-network-adapters)
    - [Sm Get Network Sm Device Performance History](#sm-get-network-sm-device-performance-history)
    - [Sm Get Network Sm Device Restrictions](#sm-get-network-sm-device-restrictions)
    - [Sm Get Network Sm Device Security Centers](#sm-get-network-sm-device-security-centers)
    - [Sm Get Network Sm Device Softwares](#sm-get-network-sm-device-softwares)
    - [Sm Get Network Sm Device Wlan Lists](#sm-get-network-sm-device-wlan-lists)
    - [Sm Get Network Sm Devices](#sm-get-network-sm-devices)
    - [Sm Get Network Sm Profiles](#sm-get-network-sm-profiles)
    - [Sm Get Network Sm Target Group](#sm-get-network-sm-target-group)
    - [Sm Get Network Sm Target Groups](#sm-get-network-sm-target-groups)
    - [Sm Get Network Sm Trusted Access Configs](#sm-get-network-sm-trusted-access-configs)
    - [Sm Get Network Sm User Access Devices](#sm-get-network-sm-user-access-devices)
    - [Sm Get Network Sm User Device Profiles](#sm-get-network-sm-user-device-profiles)
    - [Sm Get Network Sm User Softwares](#sm-get-network-sm-user-softwares)
    - [Sm Get Network Sm Users](#sm-get-network-sm-users)
    - [Sm Get Organization Sm Apns Cert](#sm-get-organization-sm-apns-cert)
    - [Sm Get Organization Sm Vpp Account](#sm-get-organization-sm-vpp-account)
    - [Sm Get Organization Sm Vpp Accounts](#sm-get-organization-sm-vpp-accounts)
    - [Sm Lock Network Sm Devices](#sm-lock-network-sm-devices)
    - [Sm Modify Network Sm Devices Tags](#sm-modify-network-sm-devices-tags)
    - [Sm Move Network Sm Devices](#sm-move-network-sm-devices)
    - [Sm Refresh Network Sm Device Details](#sm-refresh-network-sm-device-details)
    - [Sm Unenroll Network Sm Device](#sm-unenroll-network-sm-device)
    - [Sm Update Network Sm Devices Fields](#sm-update-network-sm-devices-fields)
    - [Sm Update Network Sm Target Group](#sm-update-network-sm-target-group)
    - [Sm Wipe Network Sm Devices](#sm-wipe-network-sm-devices)
- [Switch](#switch)
    - [Switch Add Network Switch Stack](#switch-add-network-switch-stack)
    - [Switch Clone Organization Switch Devices](#switch-clone-organization-switch-devices)
    - [Switch Create Device Switch Routing Interface](#switch-create-device-switch-routing-interface)
    - [Switch Create Device Switch Routing Static Route](#switch-create-device-switch-routing-static-route)
    - [Switch Create Network Switch Access Policy](#switch-create-network-switch-access-policy)
    - [Switch Create Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#switch-create-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
    - [Switch Create Network Switch Link Aggregation](#switch-create-network-switch-link-aggregation)
    - [Switch Create Network Switch Port Schedule](#switch-create-network-switch-port-schedule)
    - [Switch Create Network Switch Qos Rule](#switch-create-network-switch-qos-rule)
    - [Switch Create Network Switch Routing Multicast Rendezvous Point](#switch-create-network-switch-routing-multicast-rendezvous-point)
    - [Switch Create Network Switch Stack](#switch-create-network-switch-stack)
    - [Switch Create Network Switch Stack Routing Interface](#switch-create-network-switch-stack-routing-interface)
    - [Switch Create Network Switch Stack Routing Static Route](#switch-create-network-switch-stack-routing-static-route)
    - [Switch Cycle Device Switch Ports](#switch-cycle-device-switch-ports)
    - [Switch Delete Device Switch Routing Interface](#switch-delete-device-switch-routing-interface)
    - [Switch Delete Device Switch Routing Static Route](#switch-delete-device-switch-routing-static-route)
    - [Switch Delete Network Switch Access Policy](#switch-delete-network-switch-access-policy)
    - [Switch Delete Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#switch-delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
    - [Switch Delete Network Switch Link Aggregation](#switch-delete-network-switch-link-aggregation)
    - [Switch Delete Network Switch Port Schedule](#switch-delete-network-switch-port-schedule)
    - [Switch Delete Network Switch Qos Rule](#switch-delete-network-switch-qos-rule)
    - [Switch Delete Network Switch Routing Multicast Rendezvous Point](#switch-delete-network-switch-routing-multicast-rendezvous-point)
    - [Switch Delete Network Switch Stack](#switch-delete-network-switch-stack)
    - [Switch Delete Network Switch Stack Routing Interface](#switch-delete-network-switch-stack-routing-interface)
    - [Switch Delete Network Switch Stack Routing Static Route](#switch-delete-network-switch-stack-routing-static-route)
    - [Switch Get Device Switch Port](#switch-get-device-switch-port)
    - [Switch Get Device Switch Ports](#switch-get-device-switch-ports)
    - [Switch Get Device Switch Ports Statuses](#switch-get-device-switch-ports-statuses)
    - [Switch Get Device Switch Ports Statuses Packets](#switch-get-device-switch-ports-statuses-packets)
    - [Switch Get Device Switch Routing Interface](#switch-get-device-switch-routing-interface)
    - [Switch Get Device Switch Routing Interface Dhcp](#switch-get-device-switch-routing-interface-dhcp)
    - [Switch Get Device Switch Routing Interfaces](#switch-get-device-switch-routing-interfaces)
    - [Switch Get Device Switch Routing Static Route](#switch-get-device-switch-routing-static-route)
    - [Switch Get Device Switch Routing Static Routes](#switch-get-device-switch-routing-static-routes)
    - [Switch Get Device Switch Warm Spare](#switch-get-device-switch-warm-spare)
    - [Switch Get Network Switch Access Control Lists](#switch-get-network-switch-access-control-lists)
    - [Switch Get Network Switch Access Policies](#switch-get-network-switch-access-policies)
    - [Switch Get Network Switch Access Policy](#switch-get-network-switch-access-policy)
    - [Switch Get Network Switch Alternate Management Interface](#switch-get-network-switch-alternate-management-interface)
    - [Switch Get Network Switch Dhcp Server Policy](#switch-get-network-switch-dhcp-server-policy)
    - [Switch Get Network Switch Dhcp Server Policy Arp Inspection Trusted Servers](#switch-get-network-switch-dhcp-server-policy-arp-inspection-trusted-servers)
    - [Switch Get Network Switch Dhcp Server Policy Arp Inspection Warnings By Device](#switch-get-network-switch-dhcp-server-policy-arp-inspection-warnings-by-device)
    - [Switch Get Network Switch Dhcp V4 Servers Seen](#switch-get-network-switch-dhcp-v4-servers-seen)
    - [Switch Get Network Switch Dscp To Cos Mappings](#switch-get-network-switch-dscp-to-cos-mappings)
    - [Switch Get Network Switch Link Aggregations](#switch-get-network-switch-link-aggregations)
    - [Switch Get Network Switch Mtu](#switch-get-network-switch-mtu)
    - [Switch Get Network Switch Port Schedules](#switch-get-network-switch-port-schedules)
    - [Switch Get Network Switch Qos Rule](#switch-get-network-switch-qos-rule)
    - [Switch Get Network Switch Qos Rules](#switch-get-network-switch-qos-rules)
    - [Switch Get Network Switch Qos Rules Order](#switch-get-network-switch-qos-rules-order)
    - [Switch Get Network Switch Routing Multicast](#switch-get-network-switch-routing-multicast)
    - [Switch Get Network Switch Routing Multicast Rendezvous Point](#switch-get-network-switch-routing-multicast-rendezvous-point)
    - [Switch Get Network Switch Routing Multicast Rendezvous Points](#switch-get-network-switch-routing-multicast-rendezvous-points)
    - [Switch Get Network Switch Routing Ospf](#switch-get-network-switch-routing-ospf)
    - [Switch Get Network Switch Settings](#switch-get-network-switch-settings)
    - [Switch Get Network Switch Stack](#switch-get-network-switch-stack)
    - [Switch Get Network Switch Stack Routing Interface](#switch-get-network-switch-stack-routing-interface)
    - [Switch Get Network Switch Stack Routing Interface Dhcp](#switch-get-network-switch-stack-routing-interface-dhcp)
    - [Switch Get Network Switch Stack Routing Interfaces](#switch-get-network-switch-stack-routing-interfaces)
    - [Switch Get Network Switch Stack Routing Static Route](#switch-get-network-switch-stack-routing-static-route)
    - [Switch Get Network Switch Stack Routing Static Routes](#switch-get-network-switch-stack-routing-static-routes)
    - [Switch Get Network Switch Stacks](#switch-get-network-switch-stacks)
    - [Switch Get Network Switch Storm Control](#switch-get-network-switch-storm-control)
    - [Switch Get Network Switch Stp](#switch-get-network-switch-stp)
    - [Switch Get Organization Config Template Switch Profile Port](#switch-get-organization-config-template-switch-profile-port)
    - [Switch Get Organization Config Template Switch Profile Ports](#switch-get-organization-config-template-switch-profile-ports)
    - [Switch Get Organization Config Template Switch Profiles](#switch-get-organization-config-template-switch-profiles)
    - [Switch Get Organization Switch Ports By Switch](#switch-get-organization-switch-ports-by-switch)
    - [Switch Remove Network Switch Stack](#switch-remove-network-switch-stack)
    - [Switch Update Device Switch Port](#switch-update-device-switch-port)
    - [Switch Update Device Switch Routing Interface](#switch-update-device-switch-routing-interface)
    - [Switch Update Device Switch Routing Interface Dhcp](#switch-update-device-switch-routing-interface-dhcp)
    - [Switch Update Device Switch Routing Static Route](#switch-update-device-switch-routing-static-route)
    - [Switch Update Device Switch Warm Spare](#switch-update-device-switch-warm-spare)
    - [Switch Update Network Switch Access Control Lists](#switch-update-network-switch-access-control-lists)
    - [Switch Update Network Switch Access Policy](#switch-update-network-switch-access-policy)
    - [Switch Update Network Switch Alternate Management Interface](#switch-update-network-switch-alternate-management-interface)
    - [Switch Update Network Switch Dhcp Server Policy](#switch-update-network-switch-dhcp-server-policy)
    - [Switch Update Network Switch Dhcp Server Policy Arp Inspection Trusted Server](#switch-update-network-switch-dhcp-server-policy-arp-inspection-trusted-server)
    - [Switch Update Network Switch Dscp To Cos Mappings](#switch-update-network-switch-dscp-to-cos-mappings)
    - [Switch Update Network Switch Link Aggregation](#switch-update-network-switch-link-aggregation)
    - [Switch Update Network Switch Mtu](#switch-update-network-switch-mtu)
    - [Switch Update Network Switch Port Schedule](#switch-update-network-switch-port-schedule)
    - [Switch Update Network Switch Qos Rule](#switch-update-network-switch-qos-rule)
    - [Switch Update Network Switch Qos Rules Order](#switch-update-network-switch-qos-rules-order)
    - [Switch Update Network Switch Routing Multicast](#switch-update-network-switch-routing-multicast)
    - [Switch Update Network Switch Routing Multicast Rendezvous Point](#switch-update-network-switch-routing-multicast-rendezvous-point)
    - [Switch Update Network Switch Routing Ospf](#switch-update-network-switch-routing-ospf)
    - [Switch Update Network Switch Settings](#switch-update-network-switch-settings)
    - [Switch Update Network Switch Stack Routing Interface](#switch-update-network-switch-stack-routing-interface)
    - [Switch Update Network Switch Stack Routing Interface Dhcp](#switch-update-network-switch-stack-routing-interface-dhcp)
    - [Switch Update Network Switch Stack Routing Static Route](#switch-update-network-switch-stack-routing-static-route)
    - [Switch Update Network Switch Storm Control](#switch-update-network-switch-storm-control)
    - [Switch Update Network Switch Stp](#switch-update-network-switch-stp)
    - [Switch Update Organization Config Template Switch Profile Port](#switch-update-organization-config-template-switch-profile-port)
- [Wireless](#wireless)
    - [Wireless Create Network Wireless Rf Profile](#wireless-create-network-wireless-rf-profile)
    - [Wireless Create Network Wireless Ssid Identity Psk](#wireless-create-network-wireless-ssid-identity-psk)
    - [Wireless Delete Network Wireless Rf Profile](#wireless-delete-network-wireless-rf-profile)
    - [Wireless Delete Network Wireless Ssid Identity Psk](#wireless-delete-network-wireless-ssid-identity-psk)
    - [Wireless Get Device Wireless Bluetooth Settings](#wireless-get-device-wireless-bluetooth-settings)
    - [Wireless Get Device Wireless Connection Stats](#wireless-get-device-wireless-connection-stats)
    - [Wireless Get Device Wireless Latency Stats](#wireless-get-device-wireless-latency-stats)
    - [Wireless Get Device Wireless Radio Settings](#wireless-get-device-wireless-radio-settings)
    - [Wireless Get Device Wireless Status](#wireless-get-device-wireless-status)
    - [Wireless Get Network Wireless Air Marshal](#wireless-get-network-wireless-air-marshal)
    - [Wireless Get Network Wireless Alternate Management Interface](#wireless-get-network-wireless-alternate-management-interface)
    - [Wireless Get Network Wireless Billing](#wireless-get-network-wireless-billing)
    - [Wireless Get Network Wireless Bluetooth Settings](#wireless-get-network-wireless-bluetooth-settings)
    - [Wireless Get Network Wireless Channel Utilization History](#wireless-get-network-wireless-channel-utilization-history)
    - [Wireless Get Network Wireless Client Connection Stats](#wireless-get-network-wireless-client-connection-stats)
    - [Wireless Get Network Wireless Client Connectivity Events](#wireless-get-network-wireless-client-connectivity-events)
    - [Wireless Get Network Wireless Client Count History](#wireless-get-network-wireless-client-count-history)
    - [Wireless Get Network Wireless Client Latency History](#wireless-get-network-wireless-client-latency-history)
    - [Wireless Get Network Wireless Client Latency Stats](#wireless-get-network-wireless-client-latency-stats)
    - [Wireless Get Network Wireless Clients Connection Stats](#wireless-get-network-wireless-clients-connection-stats)
    - [Wireless Get Network Wireless Clients Latency Stats](#wireless-get-network-wireless-clients-latency-stats)
    - [Wireless Get Network Wireless Connection Stats](#wireless-get-network-wireless-connection-stats)
    - [Wireless Get Network Wireless Data Rate History](#wireless-get-network-wireless-data-rate-history)
    - [Wireless Get Network Wireless Devices Connection Stats](#wireless-get-network-wireless-devices-connection-stats)
    - [Wireless Get Network Wireless Devices Latency Stats](#wireless-get-network-wireless-devices-latency-stats)
    - [Wireless Get Network Wireless Failed Connections](#wireless-get-network-wireless-failed-connections)
    - [Wireless Get Network Wireless Latency History](#wireless-get-network-wireless-latency-history)
    - [Wireless Get Network Wireless Latency Stats](#wireless-get-network-wireless-latency-stats)
    - [Wireless Get Network Wireless Mesh Statuses](#wireless-get-network-wireless-mesh-statuses)
    - [Wireless Get Network Wireless Rf Profile](#wireless-get-network-wireless-rf-profile)
    - [Wireless Get Network Wireless Rf Profiles](#wireless-get-network-wireless-rf-profiles)
    - [Wireless Get Network Wireless Settings](#wireless-get-network-wireless-settings)
    - [Wireless Get Network Wireless Signal Quality History](#wireless-get-network-wireless-signal-quality-history)
    - [Wireless Get Network Wireless Ssid](#wireless-get-network-wireless-ssid)
    - [Wireless Get Network Wireless Ssid Bonjour Forwarding](#wireless-get-network-wireless-ssid-bonjour-forwarding)
    - [Wireless Get Network Wireless Ssid Device Type Group Policies](#wireless-get-network-wireless-ssid-device-type-group-policies)
    - [Wireless Get Network Wireless Ssid Eap Override](#wireless-get-network-wireless-ssid-eap-override)
    - [Wireless Get Network Wireless Ssid Firewall L3 Firewall Rules](#wireless-get-network-wireless-ssid-firewall-l3-firewall-rules)
    - [Wireless Get Network Wireless Ssid Firewall L7 Firewall Rules](#wireless-get-network-wireless-ssid-firewall-l7-firewall-rules)
    - [Wireless Get Network Wireless Ssid Hotspot20](#wireless-get-network-wireless-ssid-hotspot20)
    - [Wireless Get Network Wireless Ssid Identity Psk](#wireless-get-network-wireless-ssid-identity-psk)
    - [Wireless Get Network Wireless Ssid Identity Psks](#wireless-get-network-wireless-ssid-identity-psks)
    - [Wireless Get Network Wireless Ssid Schedules](#wireless-get-network-wireless-ssid-schedules)
    - [Wireless Get Network Wireless Ssid Splash Settings](#wireless-get-network-wireless-ssid-splash-settings)
    - [Wireless Get Network Wireless Ssid Traffic Shaping Rules](#wireless-get-network-wireless-ssid-traffic-shaping-rules)
    - [Wireless Get Network Wireless Ssid Vpn](#wireless-get-network-wireless-ssid-vpn)
    - [Wireless Get Network Wireless Ssids](#wireless-get-network-wireless-ssids)
    - [Wireless Get Network Wireless Usage History](#wireless-get-network-wireless-usage-history)
    - [Wireless Get Organization Wireless Devices Ethernet Statuses](#wireless-get-organization-wireless-devices-ethernet-statuses)
    - [Wireless Update Device Wireless Bluetooth Settings](#wireless-update-device-wireless-bluetooth-settings)
    - [Wireless Update Device Wireless Radio Settings](#wireless-update-device-wireless-radio-settings)
    - [Wireless Update Network Wireless Alternate Management Interface](#wireless-update-network-wireless-alternate-management-interface)
    - [Wireless Update Network Wireless Billing](#wireless-update-network-wireless-billing)
    - [Wireless Update Network Wireless Bluetooth Settings](#wireless-update-network-wireless-bluetooth-settings)
    - [Wireless Update Network Wireless Rf Profile](#wireless-update-network-wireless-rf-profile)
    - [Wireless Update Network Wireless Settings](#wireless-update-network-wireless-settings)
    - [Wireless Update Network Wireless Ssid](#wireless-update-network-wireless-ssid)
    - [Wireless Update Network Wireless Ssid Bonjour Forwarding](#wireless-update-network-wireless-ssid-bonjour-forwarding)
    - [Wireless Update Network Wireless Ssid Device Type Group Policies](#wireless-update-network-wireless-ssid-device-type-group-policies)
    - [Wireless Update Network Wireless Ssid Eap Override](#wireless-update-network-wireless-ssid-eap-override)
    - [Wireless Update Network Wireless Ssid Firewall L3 Firewall Rules](#wireless-update-network-wireless-ssid-firewall-l3-firewall-rules)
    - [Wireless Update Network Wireless Ssid Firewall L7 Firewall Rules](#wireless-update-network-wireless-ssid-firewall-l7-firewall-rules)
    - [Wireless Update Network Wireless Ssid Hotspot20](#wireless-update-network-wireless-ssid-hotspot20)
    - [Wireless Update Network Wireless Ssid Identity Psk](#wireless-update-network-wireless-ssid-identity-psk)
    - [Wireless Update Network Wireless Ssid Schedules](#wireless-update-network-wireless-ssid-schedules)
    - [Wireless Update Network Wireless Ssid Splash Settings](#wireless-update-network-wireless-ssid-splash-settings)
    - [Wireless Update Network Wireless Ssid Traffic Shaping Rules](#wireless-update-network-wireless-ssid-traffic-shaping-rules)
    - [Wireless Update Network Wireless Ssid Vpn](#wireless-update-network-wireless-ssid-vpn)



# Administered


----------------------------------------
## Administered Get Administered Identities Me


**Returns the identity of the current user.**

https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me

##### Arguments


##### Example:
```
meraki administered getAdministeredIdentitiesMe
````

##### Method Code:
```python
def getAdministeredIdentitiesMe():
    # Code
````

# Appliance


----------------------------------------
## Appliance Create Device Appliance Vmx Authentication Token


**Generate a new vMX authentication token**

https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance createDeviceApplianceVmxAuthenticationToken --serial 'STRING'
````

##### Method Code:
```python
def createDeviceApplianceVmxAuthenticationToken(serial:str):
    # Code
````



----------------------------------------
## Appliance Create Network Appliance Prefixes Delegated Static


**Add a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--prefix` (string): A static IPv6 prefix
- `--origin` (object): The origin of the prefix
- `--description` (string): A name or description for the prefix


##### Example:
```
meraki appliance createNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --prefix 'STRING' --origin JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance createNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --prefix 'STRING' --origin JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkAppliancePrefixesDelegatedStatic(networkId:str, prefix:str, origin:dict, **kwargs):
    # Code
````



----------------------------------------
## Appliance Create Network Appliance Static Route


**Add a static route for an MX or teleworker network**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new static route
- `--subnet` (string): The subnet of the static route
- `--gatewayIp` (string): The gateway IP (next hop) of the static route
- `--gatewayVlanId` (string): The gateway IP (next hop) VLAN ID of the static route


##### Example:
```
meraki appliance createNetworkApplianceStaticRoute --networkId 'STRING' --name 'STRING' --subnet 'STRING' --gatewayIp 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance createNetworkApplianceStaticRoute --networkId 'STRING' --name 'STRING' --subnet 'STRING' --gatewayIp 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkApplianceStaticRoute(networkId:str, name:str, subnet:str, gatewayIp:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Create Network Appliance Traffic Shaping Custom Performance Class


**Add a custom performance class for an MX network**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the custom performance class
- `--maxLatency` (integer): Maximum latency in milliseconds
- `--maxJitter` (integer): Maximum jitter in milliseconds
- `--maxLossPercentage` (integer): Maximum percentage of packet loss


##### Example:
```
meraki appliance createNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance createNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Create Network Appliance Vlan


**Add a VLAN**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
- `--name` (string): The name of the new VLAN
- `--subnet` (string): The subnet of the VLAN
- `--applianceIp` (string): The local IP of the appliance on the VLAN
- `--groupPolicyId` (string): The id of the desired group policy to apply to the VLAN
- `--templateVlanType` (string): Type of subnetting of the VLAN. Applicable only for template network.
- `--cidr` (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
- `--mask` (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki appliance createNetworkApplianceVlan --networkId 'STRING' --id 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance createNetworkApplianceVlan --networkId 'STRING' --id 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkApplianceVlan(networkId:str, id:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Delete Network Appliance Prefixes Delegated Static


**Delete a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--staticDelegatedPrefixId` (string): (required)


##### Example:
```
meraki appliance deleteNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING'
````

##### Method Code:
```python
def deleteNetworkAppliancePrefixesDelegatedStatic(networkId:str, staticDelegatedPrefixId:str):
    # Code
````



----------------------------------------
## Appliance Delete Network Appliance Static Route


**Delete a static route from an MX or teleworker network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route

##### Arguments
- `--networkId` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki appliance deleteNetworkApplianceStaticRoute --networkId 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def deleteNetworkApplianceStaticRoute(networkId:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Appliance Delete Network Appliance Traffic Shaping Custom Performance Class


**Delete a custom performance class from an MX network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--customPerformanceClassId` (string): (required)


##### Example:
```
meraki appliance deleteNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING'
````

##### Method Code:
```python
def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, customPerformanceClassId:str):
    # Code
````



----------------------------------------
## Appliance Delete Network Appliance Vlan


**Delete a VLAN from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--vlanId` (string): (required)


##### Example:
```
meraki appliance deleteNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING'
````

##### Method Code:
```python
def deleteNetworkApplianceVlan(networkId:str, vlanId:str):
    # Code
````



----------------------------------------
## Appliance Get Device Appliance Dhcp Subnets


**Return the DHCP subnet information for an appliance**

https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance getDeviceApplianceDhcpSubnets --serial 'STRING'
````

##### Method Code:
```python
def getDeviceApplianceDhcpSubnets(serial:str):
    # Code
````



----------------------------------------
## Appliance Get Device Appliance Performance


**Return the performance score for a single MX**

https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance getDeviceAppliancePerformance --serial 'STRING'
````

##### Method Code:
```python
def getDeviceAppliancePerformance(serial:str):
    # Code
````



----------------------------------------
## Appliance Get Device Appliance Prefixes Delegated


**Return current delegated IPv6 prefixes on an appliance.**

https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance getDeviceAppliancePrefixesDelegated --serial 'STRING'
````

##### Method Code:
```python
def getDeviceAppliancePrefixesDelegated(serial:str):
    # Code
````



----------------------------------------
## Appliance Get Device Appliance Prefixes Delegated Vlan Assignments


**Return prefixes assigned to all IPv6 enabled VLANs on an appliance.**

https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated-vlan-assignments

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance getDeviceAppliancePrefixesDelegatedVlanAssignments --serial 'STRING'
````

##### Method Code:
```python
def getDeviceAppliancePrefixesDelegatedVlanAssignments(serial:str):
    # Code
````



----------------------------------------
## Appliance Get Device Appliance Uplinks Settings


**Return the uplink settings for an MX appliance**

https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-uplinks-settings

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki appliance getDeviceApplianceUplinksSettings --serial 'STRING'
````

##### Method Code:
```python
def getDeviceApplianceUplinksSettings(serial:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Client Security Events


**List the security events for a client**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--sortOrder` (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.


##### Example:
```
meraki appliance getNetworkApplianceClientSecurityEvents --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getNetworkApplianceClientSecurityEvents --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkApplianceClientSecurityEvents(networkId:str, clientId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Connectivity Monitoring Destinations


**Return the connectivity testing destinations for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceConnectivityMonitoringDestinations --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceConnectivityMonitoringDestinations(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Content Filtering


**Return the content filtering settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceContentFiltering --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceContentFiltering(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Content Filtering Categories


**List all available content filtering categories for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceContentFilteringCategories --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceContentFilteringCategories(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Cellular Firewall Rules


**Return the cellular firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallCellularFirewallRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallCellularFirewallRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Firewalled Service


**Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service

##### Arguments
- `--networkId` (string): (required)
- `--service` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallFirewalledService --networkId 'STRING' --service 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallFirewalledService(networkId:str, service:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Firewalled Services


**List the appliance services and their accessibility rules**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallFirewalledServices --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallFirewalledServices(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Inbound Cellular Firewall Rules


**Return the inbound cellular firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-cellular-firewall-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallInboundCellularFirewallRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallInboundCellularFirewallRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Inbound Firewall Rules


**Return the inbound firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallInboundFirewallRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallInboundFirewallRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall L3 Firewall Rules


**Return the L3 firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallL3FirewallRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallL3FirewallRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall L7 Firewall Rules


**List the MX L7 firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallL7FirewallRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallL7FirewallRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall L7 Firewall Rules Application Categories


**Return the L7 firewall application categories and their associated applications for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallL7FirewallRulesApplicationCategories --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall One To Many Nat Rules


**Return the 1:Many NAT mapping rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallOneToManyNatRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallOneToManyNatRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall One To One Nat Rules


**Return the 1:1 NAT mapping rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallOneToOneNatRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallOneToOneNatRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Port Forwarding Rules


**Return the port forwarding rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallPortForwardingRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallPortForwardingRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Firewall Settings


**Return the firewall settings for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceFirewallSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceFirewallSettings(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Port


**Return per-port VLAN settings for a single MX port.**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port

##### Arguments
- `--networkId` (string): (required)
- `--portId` (string): (required)


##### Example:
```
meraki appliance getNetworkAppliancePort --networkId 'STRING' --portId 'STRING'
````

##### Method Code:
```python
def getNetworkAppliancePort(networkId:str, portId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Ports


**List per-port VLAN settings for all ports of a MX.**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkAppliancePorts --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkAppliancePorts(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Prefixes Delegated Static


**Return a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--staticDelegatedPrefixId` (string): (required)


##### Example:
```
meraki appliance getNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING'
````

##### Method Code:
```python
def getNetworkAppliancePrefixesDelegatedStatic(networkId:str, staticDelegatedPrefixId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Prefixes Delegated Statics


**List static delegated prefixes for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-statics

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkAppliancePrefixesDelegatedStatics --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkAppliancePrefixesDelegatedStatics(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Security Events


**List the security events for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--sortOrder` (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.


##### Example:
```
meraki appliance getNetworkApplianceSecurityEvents --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getNetworkApplianceSecurityEvents --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkApplianceSecurityEvents(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Security Intrusion


**Returns all supported intrusion settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSecurityIntrusion --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSecurityIntrusion(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Security Malware


**Returns all supported malware settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSecurityMalware --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSecurityMalware(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Settings


**Return the appliance settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSettings(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Single Lan


**Return single LAN configuration**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSingleLan --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSingleLan(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Ssid


**Return a single MX SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSsid --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSsid(networkId:str, number:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Ssids


**List the MX SSIDs in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssids

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceSsids --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceSsids(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Static Route


**Return a static route for an MX or teleworker network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route

##### Arguments
- `--networkId` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceStaticRoute --networkId 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceStaticRoute(networkId:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Static Routes


**List the static routes for an MX or teleworker network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceStaticRoutes --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceStaticRoutes(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping


**Display the traffic shaping settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShaping --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShaping(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping Custom Performance Class


**Return a custom performance class for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--customPerformanceClassId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, customPerformanceClassId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping Custom Performance Classes


**List all custom performance classes for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShapingCustomPerformanceClasses --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShapingCustomPerformanceClasses(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping Rules


**Display the traffic shaping settings rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShapingRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShapingRules(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping Uplink Bandwidth


**Returns the uplink bandwidth limits for your MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShapingUplinkBandwidth --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShapingUplinkBandwidth(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Traffic Shaping Uplink Selection


**Show uplink selection settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceTrafficShapingUplinkSelection --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceTrafficShapingUplinkSelection(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Uplinks Usage History


**Get the sent and received bytes for each uplink of a network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.


##### Example:
```
meraki appliance getNetworkApplianceUplinksUsageHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getNetworkApplianceUplinksUsageHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkApplianceUplinksUsageHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Vlan


**Return a VLAN**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--vlanId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceVlan(networkId:str, vlanId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Vlans


**List the VLANs for an MX network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceVlans --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceVlans(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Vlans Settings


**Returns the enabled status of VLANs for the network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceVlansSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceVlansSettings(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Vpn Bgp


**Return a Hub BGP Configuration**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-bgp

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceVpnBgp --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceVpnBgp(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Vpn Site To Site Vpn


**Return the site-to-site VPN settings of a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceVpnSiteToSiteVpn --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceVpnSiteToSiteVpn(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Network Appliance Warm Spare


**Return MX warm spare settings**

https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance getNetworkApplianceWarmSpare --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkApplianceWarmSpare(networkId:str):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Security Events


**List the security events for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--sortOrder` (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.


##### Example:
```
meraki appliance getOrganizationApplianceSecurityEvents --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getOrganizationApplianceSecurityEvents --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApplianceSecurityEvents(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Security Intrusion


**Returns all supported intrusion settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki appliance getOrganizationApplianceSecurityIntrusion --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationApplianceSecurityIntrusion(organizationId:str):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Uplink Statuses


**List the uplink status of every Meraki MX and Z series appliances in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- `--serials` (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- `--iccids` (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.


##### Example:
```
meraki appliance getOrganizationApplianceUplinkStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getOrganizationApplianceUplinkStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApplianceUplinkStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Vpn Stats


**Show VPN history stat for networks in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-stats

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki appliance getOrganizationApplianceVpnStats --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getOrganizationApplianceVpnStats --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApplianceVpnStats(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Vpn Statuses


**Show VPN status for networks in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456


##### Example:
```
meraki appliance getOrganizationApplianceVpnStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance getOrganizationApplianceVpnStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApplianceVpnStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Vpn Third Party V P N Peers


**Return the third party VPN peers for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-third-party-v-p-n-peers

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki appliance getOrganizationApplianceVpnThirdPartyVPNPeers --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationApplianceVpnThirdPartyVPNPeers(organizationId:str):
    # Code
````



----------------------------------------
## Appliance Get Organization Appliance Vpn Vpn Firewall Rules


**Return the firewall rules for an organization's site-to-site VPN**

https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki appliance getOrganizationApplianceVpnVpnFirewallRules --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationApplianceVpnVpnFirewallRules(organizationId:str):
    # Code
````



----------------------------------------
## Appliance Swap Network Appliance Warm Spare


**Swap MX primary and warm spare appliances**

https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki appliance swapNetworkApplianceWarmSpare --networkId 'STRING'
````

##### Method Code:
```python
def swapNetworkApplianceWarmSpare(networkId:str):
    # Code
````



----------------------------------------
## Appliance Update Device Appliance Uplinks Settings


**Update the uplink settings for an MX appliance**

https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

##### Arguments
- `--serial` (string): (required)
- `--interfaces` (object): Interface settings.


##### Example:
```
meraki appliance updateDeviceApplianceUplinksSettings --serial 'STRING' --interfaces JSON_STRING
````

##### Method Code:
```python
def updateDeviceApplianceUplinksSettings(serial:str, interfaces:dict):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Connectivity Monitoring Destinations


**Update the connectivity testing destinations for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)
- `--destinations` (array): The list of connectivity monitoring destinations


##### Example:
```
meraki appliance updateNetworkApplianceConnectivityMonitoringDestinations --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceConnectivityMonitoringDestinations --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceConnectivityMonitoringDestinations(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Content Filtering


**Update the content filtering settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-content-filtering

##### Arguments
- `--networkId` (string): (required)
- `--allowedUrlPatterns` (array): A list of URL patterns that are allowed
- `--blockedUrlPatterns` (array): A list of URL patterns that are blocked
- `--blockedUrlCategories` (array): A list of URL categories to block
- `--urlCategoryListSize` (string): URL category list size which is either 'topSites' or 'fullList'


##### Example:
```
meraki appliance updateNetworkApplianceContentFiltering --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceContentFiltering --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceContentFiltering(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Cellular Firewall Rules


**Update the cellular firewall rules of an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the firewall rules (not including the default rule)


##### Example:
```
meraki appliance updateNetworkApplianceFirewallCellularFirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallCellularFirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallCellularFirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Firewalled Service


**Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-firewalled-service

##### Arguments
- `--networkId` (string): (required)
- `--service` (string): (required)
- `--access` (string): A string indicating the rule for which IPs are allowed to use the specified service. Acceptable values are "blocked" (no remote IPs can access the service), "restricted" (only allowed IPs can access the service), and "unrestriced" (any remote IP can access the service). This field is required
- `--allowedIps` (array): An array of allowed IPs that can access the service. This field is required if "access" is set to "restricted". Otherwise this field is ignored


##### Example:
```
meraki appliance updateNetworkApplianceFirewallFirewalledService --networkId 'STRING' --service 'STRING' --access 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallFirewalledService --networkId 'STRING' --service 'STRING' --access 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallFirewalledService(networkId:str, service:str, access:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Inbound Cellular Firewall Rules


**Update the inbound cellular firewall rules of an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-cellular-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the firewall rules (not including the default rule)


##### Example:
```
meraki appliance updateNetworkApplianceFirewallInboundCellularFirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallInboundCellularFirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallInboundCellularFirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Inbound Firewall Rules


**Update the inbound firewall rules of an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the firewall rules (not including the default rule)
- `--syslogDefaultRule` (boolean): Log the special default rule (boolean value - `--enable` only if you've configured a syslog server) (optional)


##### Example:
```
meraki appliance updateNetworkApplianceFirewallInboundFirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallInboundFirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallInboundFirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall L3 Firewall Rules


**Update the L3 firewall rules of an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the firewall rules (not including the default rule)
- `--syslogDefaultRule` (boolean): Log the special default rule (boolean value - `--enable` only if you've configured a syslog server) (optional)


##### Example:
```
meraki appliance updateNetworkApplianceFirewallL3FirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallL3FirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallL3FirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall L7 Firewall Rules


**Update the MX L7 firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the MX L7 firewall rules


##### Example:
```
meraki appliance updateNetworkApplianceFirewallL7FirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallL7FirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallL7FirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall One To Many Nat Rules


**Set the 1:Many NAT mapping rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-many-nat-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An array of 1:Many nat rules


##### Example:
```
meraki appliance updateNetworkApplianceFirewallOneToManyNatRules --networkId 'STRING' --rules ITEM
````

##### Method Code:
```python
def updateNetworkApplianceFirewallOneToManyNatRules(networkId:str, rules:list):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall One To One Nat Rules


**Set the 1:1 NAT mapping rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-one-nat-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An array of 1:1 nat rules


##### Example:
```
meraki appliance updateNetworkApplianceFirewallOneToOneNatRules --networkId 'STRING' --rules ITEM
````

##### Method Code:
```python
def updateNetworkApplianceFirewallOneToOneNatRules(networkId:str, rules:list):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Port Forwarding Rules


**Update the port forwarding rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-port-forwarding-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An array of port forwarding params


##### Example:
```
meraki appliance updateNetworkApplianceFirewallPortForwardingRules --networkId 'STRING' --rules ITEM
````

##### Method Code:
```python
def updateNetworkApplianceFirewallPortForwardingRules(networkId:str, rules:list):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Firewall Settings


**Update the firewall settings for this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-settings

##### Arguments
- `--networkId` (string): (required)
- `--spoofingProtection` (object): Spoofing protection settings


##### Example:
```
meraki appliance updateNetworkApplianceFirewallSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceFirewallSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Port


**Update the per-port VLAN settings for a single MX port.**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

##### Arguments
- `--networkId` (string): (required)
- `--portId` (string): (required)
- `--enabled` (boolean): The status of the port
- `--dropUntaggedTraffic` (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
- `--type` (string): The type of the port: 'access' or 'trunk'.
- `--vlan` (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
- `--allowedVlans` (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
- `--accessPolicy` (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.


##### Example:
```
meraki appliance updateNetworkAppliancePort --networkId 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkAppliancePort --networkId 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkAppliancePort(networkId:str, portId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Prefixes Delegated Static


**Update a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--staticDelegatedPrefixId` (string): (required)
- `--prefix` (string): A static IPv6 prefix
- `--origin` (object): The origin of the prefix
- `--description` (string): A name or description for the prefix


##### Example:
```
meraki appliance updateNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkAppliancePrefixesDelegatedStatic(networkId:str, staticDelegatedPrefixId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Security Intrusion


**Set the supported intrusion settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-intrusion

##### Arguments
- `--networkId` (string): (required)
- `--mode` (string): Set mode to 'disabled'/'detection'/'prevention' (optional - `--omitting` will leave current config unchanged)
- `--idsRulesets` (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - `--omitting` will leave current config unchanged). Default value is 'balanced' if none currently saved
- `--protectedNetworks` (object): Set the included/excluded networks from the intrusion engine (optional - `--omitting` will leave current config unchanged). This is available only in 'passthrough' mode


##### Example:
```
meraki appliance updateNetworkApplianceSecurityIntrusion --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceSecurityIntrusion --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSecurityIntrusion(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Security Malware


**Set the supported malware settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-malware

##### Arguments
- `--networkId` (string): (required)
- `--mode` (string): Set mode to 'enabled' to enable malware prevention, otherwise 'disabled'
- `--allowedUrls` (array): The urls that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing
- `--allowedFiles` (array): The sha256 digests of files that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing


##### Example:
```
meraki appliance updateNetworkApplianceSecurityMalware --networkId 'STRING' --mode 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceSecurityMalware --networkId 'STRING' --mode 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSecurityMalware(networkId:str, mode:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Settings


**Update the appliance settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

##### Arguments
- `--networkId` (string): (required)
- `--clientTrackingMethod` (string): Client tracking method of a network
- `--deploymentMode` (string): Deployment mode of a network
- `--dynamicDns` (object): Dynamic DNS settings for a network


##### Example:
```
meraki appliance updateNetworkApplianceSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Single Lan


**Update single LAN configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

##### Arguments
- `--networkId` (string): (required)
- `--subnet` (string): The subnet of the single LAN configuration
- `--applianceIp` (string): The appliance IP address of the single LAN
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this LAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki appliance updateNetworkApplianceSingleLan --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceSingleLan --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSingleLan(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Ssid


**Update the attributes of an MX SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the SSID.
- `--enabled` (boolean): Whether or not the SSID is enabled.
- `--defaultVlanId` (integer): The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode.
- `--authMode` (string): The association control method for the SSID ('open', 'psk', '8021x-meraki' or '8021x-radius').
- `--psk` (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'.
- `--radiusServers` (array): The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is '8021x-radius'.
- `--encryptionMode` (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'.
- `--wpaEncryptionMode` (string): The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only'). This param is only valid if (1) the authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is '8021x-meraki' OR (3) the authMode is '8021x-radius'
- `--visible` (boolean): Boolean indicating whether the MX should advertise or hide this SSID.
- `--dhcpEnforcedDeauthentication` (object): DHCP Enforced Deauthentication enables the disassociation of wireless clients in addition to Mandatory DHCP. This param is only valid on firmware versions >= MX 17.0 where the associated LAN has Mandatory DHCP Enabled 


##### Example:
```
meraki appliance updateNetworkApplianceSsid --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceSsid --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSsid(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Static Route


**Update a static route for an MX or teleworker network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route

##### Arguments
- `--networkId` (string): (required)
- `--staticRouteId` (string): (required)
- `--name` (string): The name of the static route
- `--subnet` (string): The subnet of the static route
- `--gatewayIp` (string): The gateway IP (next hop) of the static route
- `--gatewayVlanId` (string): The gateway IP (next hop) VLAN ID of the static route
- `--enabled` (boolean): The enabled state of the static route
- `--fixedIpAssignments` (object): The DHCP fixed IP assignments on the static route. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
- `--reservedIpRanges` (array): The DHCP reserved IP ranges on the static route


##### Example:
```
meraki appliance updateNetworkApplianceStaticRoute --networkId 'STRING' --staticRouteId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceStaticRoute --networkId 'STRING' --staticRouteId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceStaticRoute(networkId:str, staticRouteId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Traffic Shaping


**Update the traffic shaping settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping

##### Arguments
- `--networkId` (string): (required)
- `--globalBandwidthLimits` (object): Global per-client bandwidth limit


##### Example:
```
meraki appliance updateNetworkApplianceTrafficShaping --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceTrafficShaping --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShaping(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Traffic Shaping Custom Performance Class


**Update a custom performance class for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--customPerformanceClassId` (string): (required)
- `--name` (string): Name of the custom performance class
- `--maxLatency` (integer): Maximum latency in milliseconds
- `--maxJitter` (integer): Maximum jitter in milliseconds
- `--maxLossPercentage` (integer): Maximum percentage of packet loss


##### Example:
```
meraki appliance updateNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, customPerformanceClassId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Traffic Shaping Rules


**Update the traffic shaping settings rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)
- `--defaultRulesEnabled` (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- `--rules` (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.



##### Example:
```
meraki appliance updateNetworkApplianceTrafficShapingRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceTrafficShapingRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Traffic Shaping Uplink Bandwidth


**Updates the uplink bandwidth settings for your MX network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

##### Arguments
- `--networkId` (string): (required)
- `--bandwidthLimits` (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)


##### Example:
```
meraki appliance updateNetworkApplianceTrafficShapingUplinkBandwidth --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceTrafficShapingUplinkBandwidth --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingUplinkBandwidth(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Traffic Shaping Uplink Selection


**Update uplink selection settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

##### Arguments
- `--networkId` (string): (required)
- `--activeActiveAutoVpnEnabled` (boolean): Toggle for enabling or disabling active-active AutoVPN
- `--defaultUplink` (string): The default uplink. Must be one of: 'wan1' or 'wan2'
- `--loadBalancingEnabled` (boolean): Toggle for enabling or disabling load balancing
- `--failoverAndFailback` (object): WAN failover and failback behavior
- `--wanTrafficUplinkPreferences` (array): Array of uplink preference rules for WAN traffic
- `--vpnTrafficUplinkPreferences` (array): Array of uplink preference rules for VPN traffic


##### Example:
```
meraki appliance updateNetworkApplianceTrafficShapingUplinkSelection --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceTrafficShapingUplinkSelection --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingUplinkSelection(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Vlan


**Update a VLAN**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--vlanId` (string): (required)
- `--name` (string): The name of the VLAN
- `--subnet` (string): The subnet of the VLAN
- `--applianceIp` (string): The local IP of the appliance on the VLAN
- `--groupPolicyId` (string): The id of the desired group policy to apply to the VLAN
- `--vpnNatSubnet` (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
- `--dhcpHandling` (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
- `--dhcpRelayServerIps` (array): The IPs of the DHCP servers that DHCP requests should be relayed to
- `--dhcpLeaseTime` (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
- `--dhcpBootOptionsEnabled` (boolean): Use DHCP boot options specified in other properties
- `--dhcpBootNextServer` (string): DHCP boot option to direct boot clients to the server to load the boot file from
- `--dhcpBootFilename` (string): DHCP boot option for boot filename
- `--fixedIpAssignments` (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
- `--reservedIpRanges` (array): The DHCP reserved IP ranges on the VLAN
- `--dnsNameservers` (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
- `--dhcpOptions` (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
- `--templateVlanType` (string): Type of subnetting of the VLAN. Applicable only for template network.
- `--cidr` (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
- `--mask` (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki appliance updateNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVlan(networkId:str, vlanId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Vlans Settings


**Enable/Disable VLANs for the given network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

##### Arguments
- `--networkId` (string): (required)
- `--vlansEnabled` (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network


##### Example:
```
meraki appliance updateNetworkApplianceVlansSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceVlansSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVlansSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Vpn Bgp


**Update a Hub BGP Configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.
- `--asNumber` (integer): An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512.
- `--ibgpHoldTimer` (integer): The IBGP holdtimer in seconds. The IBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240.
- `--neighbors` (array): List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated.


##### Example:
```
meraki appliance updateNetworkApplianceVpnBgp --networkId 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceVpnBgp --networkId 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVpnBgp(networkId:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Vpn Site To Site Vpn


**Update the site-to-site VPN settings of a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

##### Arguments
- `--networkId` (string): (required)
- `--mode` (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
- `--hubs` (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
- `--subnets` (array): The list of subnets and their VPN presence.


##### Example:
```
meraki appliance updateNetworkApplianceVpnSiteToSiteVpn --networkId 'STRING' --mode 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceVpnSiteToSiteVpn --networkId 'STRING' --mode 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVpnSiteToSiteVpn(networkId:str, mode:str, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Network Appliance Warm Spare


**Update MX warm spare settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Enable warm spare
- `--spareSerial` (string): Serial number of the warm spare appliance
- `--uplinkMode` (string): Uplink mode, either virtual or public
- `--virtualIp1` (string): The WAN 1 shared IP
- `--virtualIp2` (string): The WAN 2 shared IP


##### Example:
```
meraki appliance updateNetworkApplianceWarmSpare --networkId 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateNetworkApplianceWarmSpare --networkId 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceWarmSpare(networkId:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Appliance Update Organization Appliance Security Intrusion


**Sets supported intrusion settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion

##### Arguments
- `--organizationId` (string): (required)
- `--allowedRules` (array): Sets a list of specific SNORT signatures to allow


##### Example:
```
meraki appliance updateOrganizationApplianceSecurityIntrusion --organizationId 'STRING' --allowedRules ITEM
````

##### Method Code:
```python
def updateOrganizationApplianceSecurityIntrusion(organizationId:str, allowedRules:list):
    # Code
````



----------------------------------------
## Appliance Update Organization Appliance Vpn Third Party V P N Peers


**Update the third party VPN peers for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

##### Arguments
- `--organizationId` (string): (required)
- `--peers` (array): The list of VPN peers


##### Example:
```
meraki appliance updateOrganizationApplianceVpnThirdPartyVPNPeers --organizationId 'STRING' --peers ITEM
````

##### Method Code:
```python
def updateOrganizationApplianceVpnThirdPartyVPNPeers(organizationId:str, peers:list):
    # Code
````



----------------------------------------
## Appliance Update Organization Appliance Vpn Vpn Firewall Rules


**Update the firewall rules of an organization's site-to-site VPN**

https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules

##### Arguments
- `--organizationId` (string): (required)
- `--rules` (array): An ordered array of the firewall rules (not including the default rule)
- `--syslogDefaultRule` (boolean): Log the special default rule (boolean value - `--enable` only if you've configured a syslog server) (optional)


##### Example:
```
meraki appliance updateOrganizationApplianceVpnVpnFirewallRules --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki appliance updateOrganizationApplianceVpnVpnFirewallRules --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationApplianceVpnVpnFirewallRules(organizationId:str, **kwargs):
    # Code
````

# Batch
# Batch Appliance


----------------------------------------
## Batch Appliance Create Device Appliance Vmx Authentication Token


**Generate a new vMX authentication token**

https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki batch appliance createDeviceApplianceVmxAuthenticationToken --serial 'STRING'
````

##### Method Code:
```python
def createDeviceApplianceVmxAuthenticationToken(serial:str):
    # Code
````



----------------------------------------
## Batch Appliance Create Network Appliance Prefixes Delegated Static


**Add a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--prefix` (string): A static IPv6 prefix
- `--origin` (object): The origin of the prefix
- `--description` (string): A name or description for the prefix


##### Example:
```
meraki batch appliance createNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --prefix 'STRING' --origin JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance createNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --prefix 'STRING' --origin JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkAppliancePrefixesDelegatedStatic(networkId:str, prefix:str, origin:dict, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Create Network Appliance Traffic Shaping Custom Performance Class


**Add a custom performance class for an MX network**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the custom performance class
- `--maxLatency` (integer): Maximum latency in milliseconds
- `--maxJitter` (integer): Maximum jitter in milliseconds
- `--maxLossPercentage` (integer): Maximum percentage of packet loss


##### Example:
```
meraki batch appliance createNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance createNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Create Network Appliance Vlan


**Add a VLAN**

https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
- `--name` (string): The name of the new VLAN
- `--subnet` (string): The subnet of the VLAN
- `--applianceIp` (string): The local IP of the appliance on the VLAN
- `--groupPolicyId` (string): The id of the desired group policy to apply to the VLAN
- `--templateVlanType` (string): Type of subnetting of the VLAN. Applicable only for template network.
- `--cidr` (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
- `--mask` (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki batch appliance createNetworkApplianceVlan --networkId 'STRING' --id 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance createNetworkApplianceVlan --networkId 'STRING' --id 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkApplianceVlan(networkId:str, id:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Delete Network Appliance Prefixes Delegated Static


**Delete a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--staticDelegatedPrefixId` (string): (required)


##### Example:
```
meraki batch appliance deleteNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING'
````

##### Method Code:
```python
def deleteNetworkAppliancePrefixesDelegatedStatic(networkId:str, staticDelegatedPrefixId:str):
    # Code
````



----------------------------------------
## Batch Appliance Delete Network Appliance Traffic Shaping Custom Performance Class


**Delete a custom performance class from an MX network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--customPerformanceClassId` (string): (required)


##### Example:
```
meraki batch appliance deleteNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING'
````

##### Method Code:
```python
def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, customPerformanceClassId:str):
    # Code
````



----------------------------------------
## Batch Appliance Delete Network Appliance Vlan


**Delete a VLAN from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--vlanId` (string): (required)


##### Example:
```
meraki batch appliance deleteNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING'
````

##### Method Code:
```python
def deleteNetworkApplianceVlan(networkId:str, vlanId:str):
    # Code
````



----------------------------------------
## Batch Appliance Swap Network Appliance Warm Spare


**Swap MX primary and warm spare appliances**

https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki batch appliance swapNetworkApplianceWarmSpare --networkId 'STRING'
````

##### Method Code:
```python
def swapNetworkApplianceWarmSpare(networkId:str):
    # Code
````



----------------------------------------
## Batch Appliance Update Device Appliance Uplinks Settings


**Update the uplink settings for an MX appliance**

https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

##### Arguments
- `--serial` (string): (required)
- `--interfaces` (object): Interface settings.


##### Example:
```
meraki batch appliance updateDeviceApplianceUplinksSettings --serial 'STRING' --interfaces JSON_STRING
````

##### Method Code:
```python
def updateDeviceApplianceUplinksSettings(serial:str, interfaces:dict):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Connectivity Monitoring Destinations


**Update the connectivity testing destinations for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)
- `--destinations` (array): The list of connectivity monitoring destinations


##### Example:
```
meraki batch appliance updateNetworkApplianceConnectivityMonitoringDestinations --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceConnectivityMonitoringDestinations --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceConnectivityMonitoringDestinations(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Firewall L7 Firewall Rules


**Update the MX L7 firewall rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the MX L7 firewall rules


##### Example:
```
meraki batch appliance updateNetworkApplianceFirewallL7FirewallRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceFirewallL7FirewallRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceFirewallL7FirewallRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Port


**Update the per-port VLAN settings for a single MX port.**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

##### Arguments
- `--networkId` (string): (required)
- `--portId` (string): (required)
- `--enabled` (boolean): The status of the port
- `--dropUntaggedTraffic` (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
- `--type` (string): The type of the port: 'access' or 'trunk'.
- `--vlan` (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
- `--allowedVlans` (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
- `--accessPolicy` (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.


##### Example:
```
meraki batch appliance updateNetworkAppliancePort --networkId 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkAppliancePort --networkId 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkAppliancePort(networkId:str, portId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Prefixes Delegated Static


**Update a static delegated prefix from a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

##### Arguments
- `--networkId` (string): (required)
- `--staticDelegatedPrefixId` (string): (required)
- `--prefix` (string): A static IPv6 prefix
- `--origin` (object): The origin of the prefix
- `--description` (string): A name or description for the prefix


##### Example:
```
meraki batch appliance updateNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkAppliancePrefixesDelegatedStatic --networkId 'STRING' --staticDelegatedPrefixId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkAppliancePrefixesDelegatedStatic(networkId:str, staticDelegatedPrefixId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Settings


**Update the appliance settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

##### Arguments
- `--networkId` (string): (required)
- `--clientTrackingMethod` (string): Client tracking method of a network
- `--deploymentMode` (string): Deployment mode of a network
- `--dynamicDns` (object): Dynamic DNS settings for a network


##### Example:
```
meraki batch appliance updateNetworkApplianceSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Single Lan


**Update single LAN configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

##### Arguments
- `--networkId` (string): (required)
- `--subnet` (string): The subnet of the single LAN configuration
- `--applianceIp` (string): The appliance IP address of the single LAN
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this LAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki batch appliance updateNetworkApplianceSingleLan --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceSingleLan --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSingleLan(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Ssid


**Update the attributes of an MX SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the SSID.
- `--enabled` (boolean): Whether or not the SSID is enabled.
- `--defaultVlanId` (integer): The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode.
- `--authMode` (string): The association control method for the SSID ('open', 'psk', '8021x-meraki' or '8021x-radius').
- `--psk` (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'.
- `--radiusServers` (array): The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is '8021x-radius'.
- `--encryptionMode` (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'.
- `--wpaEncryptionMode` (string): The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only'). This param is only valid if (1) the authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is '8021x-meraki' OR (3) the authMode is '8021x-radius'
- `--visible` (boolean): Boolean indicating whether the MX should advertise or hide this SSID.
- `--dhcpEnforcedDeauthentication` (object): DHCP Enforced Deauthentication enables the disassociation of wireless clients in addition to Mandatory DHCP. This param is only valid on firmware versions >= MX 17.0 where the associated LAN has Mandatory DHCP Enabled 


##### Example:
```
meraki batch appliance updateNetworkApplianceSsid --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceSsid --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceSsid(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Traffic Shaping Custom Performance Class


**Update a custom performance class for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

##### Arguments
- `--networkId` (string): (required)
- `--customPerformanceClassId` (string): (required)
- `--name` (string): Name of the custom performance class
- `--maxLatency` (integer): Maximum latency in milliseconds
- `--maxJitter` (integer): Maximum jitter in milliseconds
- `--maxLossPercentage` (integer): Maximum percentage of packet loss


##### Example:
```
meraki batch appliance updateNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceTrafficShapingCustomPerformanceClass --networkId 'STRING' --customPerformanceClassId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingCustomPerformanceClass(networkId:str, customPerformanceClassId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Traffic Shaping Rules


**Update the traffic shaping settings rules for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)
- `--defaultRulesEnabled` (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- `--rules` (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.



##### Example:
```
meraki batch appliance updateNetworkApplianceTrafficShapingRules --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceTrafficShapingRules --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingRules(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Traffic Shaping Uplink Bandwidth


**Updates the uplink bandwidth settings for your MX network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

##### Arguments
- `--networkId` (string): (required)
- `--bandwidthLimits` (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)


##### Example:
```
meraki batch appliance updateNetworkApplianceTrafficShapingUplinkBandwidth --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceTrafficShapingUplinkBandwidth --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingUplinkBandwidth(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Traffic Shaping Uplink Selection


**Update uplink selection settings for an MX network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

##### Arguments
- `--networkId` (string): (required)
- `--activeActiveAutoVpnEnabled` (boolean): Toggle for enabling or disabling active-active AutoVPN
- `--defaultUplink` (string): The default uplink. Must be one of: 'wan1' or 'wan2'
- `--loadBalancingEnabled` (boolean): Toggle for enabling or disabling load balancing
- `--failoverAndFailback` (object): WAN failover and failback behavior
- `--wanTrafficUplinkPreferences` (array): Array of uplink preference rules for WAN traffic
- `--vpnTrafficUplinkPreferences` (array): Array of uplink preference rules for VPN traffic


##### Example:
```
meraki batch appliance updateNetworkApplianceTrafficShapingUplinkSelection --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceTrafficShapingUplinkSelection --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceTrafficShapingUplinkSelection(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Vlan


**Update a VLAN**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

##### Arguments
- `--networkId` (string): (required)
- `--vlanId` (string): (required)
- `--name` (string): The name of the VLAN
- `--subnet` (string): The subnet of the VLAN
- `--applianceIp` (string): The local IP of the appliance on the VLAN
- `--groupPolicyId` (string): The id of the desired group policy to apply to the VLAN
- `--vpnNatSubnet` (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
- `--dhcpHandling` (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
- `--dhcpRelayServerIps` (array): The IPs of the DHCP servers that DHCP requests should be relayed to
- `--dhcpLeaseTime` (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
- `--dhcpBootOptionsEnabled` (boolean): Use DHCP boot options specified in other properties
- `--dhcpBootNextServer` (string): DHCP boot option to direct boot clients to the server to load the boot file from
- `--dhcpBootFilename` (string): DHCP boot option for boot filename
- `--fixedIpAssignments` (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
- `--reservedIpRanges` (array): The DHCP reserved IP ranges on the VLAN
- `--dnsNameservers` (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
- `--dhcpOptions` (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
- `--templateVlanType` (string): Type of subnetting of the VLAN. Applicable only for template network.
- `--cidr` (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
- `--mask` (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
- `--ipv6` (object): IPv6 configuration on the VLAN
- `--mandatoryDhcp` (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above


##### Example:
```
meraki batch appliance updateNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceVlan --networkId 'STRING' --vlanId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVlan(networkId:str, vlanId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Vlans Settings


**Enable/Disable VLANs for the given network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

##### Arguments
- `--networkId` (string): (required)
- `--vlansEnabled` (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network


##### Example:
```
meraki batch appliance updateNetworkApplianceVlansSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceVlansSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVlansSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Vpn Bgp


**Update a Hub BGP Configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.
- `--asNumber` (integer): An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512.
- `--ibgpHoldTimer` (integer): The IBGP holdtimer in seconds. The IBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240.
- `--neighbors` (array): List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated.


##### Example:
```
meraki batch appliance updateNetworkApplianceVpnBgp --networkId 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceVpnBgp --networkId 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVpnBgp(networkId:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Vpn Site To Site Vpn


**Update the site-to-site VPN settings of a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

##### Arguments
- `--networkId` (string): (required)
- `--mode` (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
- `--hubs` (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
- `--subnets` (array): The list of subnets and their VPN presence.


##### Example:
```
meraki batch appliance updateNetworkApplianceVpnSiteToSiteVpn --networkId 'STRING' --mode 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceVpnSiteToSiteVpn --networkId 'STRING' --mode 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceVpnSiteToSiteVpn(networkId:str, mode:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Network Appliance Warm Spare


**Update MX warm spare settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Enable warm spare
- `--spareSerial` (string): Serial number of the warm spare appliance
- `--uplinkMode` (string): Uplink mode, either virtual or public
- `--virtualIp1` (string): The WAN 1 shared IP
- `--virtualIp2` (string): The WAN 2 shared IP


##### Example:
```
meraki batch appliance updateNetworkApplianceWarmSpare --networkId 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch appliance updateNetworkApplianceWarmSpare --networkId 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkApplianceWarmSpare(networkId:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Batch Appliance Update Organization Appliance Vpn Third Party V P N Peers


**Update the third party VPN peers for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

##### Arguments
- `--organizationId` (string): (required)
- `--peers` (array): The list of VPN peers


##### Example:
```
meraki batch appliance updateOrganizationApplianceVpnThirdPartyVPNPeers --organizationId 'STRING' --peers ITEM
````

##### Method Code:
```python
def updateOrganizationApplianceVpnThirdPartyVPNPeers(organizationId:str, peers:list):
    # Code
````

# Batch Camera


----------------------------------------
## Batch Camera Update Device Camera Custom Analytics


**Update custom analytics settings for a camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-custom-analytics

##### Arguments
- `--serial` (string): (required)
- `--enabled` (boolean): Enable custom analytics
- `--artifactId` (string): The ID of the custom analytics artifact
- `--parameters` (array): Parameters for the custom analytics workload


##### Example:
```
meraki batch camera updateDeviceCameraCustomAnalytics --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch camera updateDeviceCameraCustomAnalytics --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraCustomAnalytics(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Camera Update Device Camera Quality And Retention


**Update quality and retention settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

##### Arguments
- `--serial` (string): (required)
- `--profileId` (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
- `--motionBasedRetentionEnabled` (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
- `--audioRecordingEnabled` (boolean): Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
- `--restrictedBandwidthModeEnabled` (boolean): Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
- `--quality` (string): Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
- `--resolution` (string): Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2058x2058', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
- `--motionDetectorVersion` (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.


##### Example:
```
meraki batch camera updateDeviceCameraQualityAndRetention --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch camera updateDeviceCameraQualityAndRetention --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraQualityAndRetention(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Camera Update Device Camera Sense


**Update sense settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

##### Arguments
- `--serial` (string): (required)
- `--senseEnabled` (boolean): Boolean indicating if sense(license) is enabled(true) or disabled(false) on the camera
- `--mqttBrokerId` (string): The ID of the MQTT broker to be enabled on the camera. A value of null will disable MQTT on the camera
- `--audioDetection` (object): The details of the audio detection config.
- `--detectionModelId` (string): The ID of the object detection model


##### Example:
```
meraki batch camera updateDeviceCameraSense --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch camera updateDeviceCameraSense --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraSense(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Camera Update Device Camera Video Settings


**Update video settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

##### Arguments
- `--serial` (string): (required)
- `--externalRtspEnabled` (boolean): Boolean indicating if external rtsp stream is exposed


##### Example:
```
meraki batch camera updateDeviceCameraVideoSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch camera updateDeviceCameraVideoSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraVideoSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Camera Update Device Camera Wireless Profiles


**Assign wireless profiles to the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-wireless-profiles

##### Arguments
- `--serial` (string): (required)
- `--ids` (object): The ids of the wireless profile to assign to the given camera


##### Example:
```
meraki batch camera updateDeviceCameraWirelessProfiles --serial 'STRING' --ids JSON_STRING
````

##### Method Code:
```python
def updateDeviceCameraWirelessProfiles(serial:str, ids:dict):
    # Code
````

# Batch Cellular Gateway


----------------------------------------
## Batch Cellular Gateway Update Device Cellular Gateway Lan


**Update the LAN Settings for a single MG.**

https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

##### Arguments
- `--serial` (string): (required)
- `--reservedIpRanges` (array): list of all reserved IP ranges for a single MG
- `--fixedIpAssignments` (array): list of all fixed IP assignments for a single MG


##### Example:
```
meraki batch cellularGateway updateDeviceCellularGatewayLan --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateDeviceCellularGatewayLan --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCellularGatewayLan(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Cellular Gateway Update Device Cellular Gateway Port Forwarding Rules


**Updates the port forwarding rules for a single MG.**

https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

##### Arguments
- `--serial` (string): (required)
- `--rules` (array): An array of port forwarding params


##### Example:
```
meraki batch cellularGateway updateDeviceCellularGatewayPortForwardingRules --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateDeviceCellularGatewayPortForwardingRules --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCellularGatewayPortForwardingRules(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Cellular Gateway Update Network Cellular Gateway Connectivity Monitoring Destinations


**Update the connectivity testing destinations for an MG network**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)
- `--destinations` (array): The list of connectivity monitoring destinations


##### Example:
```
meraki batch cellularGateway updateNetworkCellularGatewayConnectivityMonitoringDestinations --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateNetworkCellularGatewayConnectivityMonitoringDestinations --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayConnectivityMonitoringDestinations(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Cellular Gateway Update Network Cellular Gateway Dhcp


**Update common DHCP settings of MGs**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

##### Arguments
- `--networkId` (string): (required)
- `--dhcpLeaseTime` (string): DHCP Lease time for all MG of the network. Possible values are '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
- `--dnsNameservers` (string): DNS name servers mode for all MG of the network. Possible values are: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
- `--dnsCustomNameservers` (array): list of fixed IPs representing the the DNS Name servers when the mode is 'custom'


##### Example:
```
meraki batch cellularGateway updateNetworkCellularGatewayDhcp --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateNetworkCellularGatewayDhcp --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayDhcp(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Cellular Gateway Update Network Cellular Gateway Subnet Pool


**Update the subnet pool and mask configuration for MGs in the network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

##### Arguments
- `--networkId` (string): (required)
- `--mask` (integer): Mask used for the subnet of all MGs in  this network.
- `--cidr` (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.


##### Example:
```
meraki batch cellularGateway updateNetworkCellularGatewaySubnetPool --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateNetworkCellularGatewaySubnetPool --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewaySubnetPool(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Cellular Gateway Update Network Cellular Gateway Uplink


**Updates the uplink settings for your MG network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

##### Arguments
- `--networkId` (string): (required)
- `--bandwidthLimits` (object): The bandwidth settings for the 'cellular' uplink


##### Example:
```
meraki batch cellularGateway updateNetworkCellularGatewayUplink --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch cellularGateway updateNetworkCellularGatewayUplink --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayUplink(networkId:str, **kwargs):
    # Code
````

# Batch Devices


----------------------------------------
## Batch Devices Update Device


**Update the attributes of a device**

https://developer.cisco.com/meraki/api-v1/#!update-device

##### Arguments
- `--serial` (string): (required)
- `--name` (string): The name of a device
- `--tags` (array): The list of tags of a device
- `--lat` (number): The latitude of a device
- `--lng` (number): The longitude of a device
- `--address` (string): The address of a device
- `--notes` (string): The notes for the device. String. Limited to 255 characters.
- `--moveMapMarker` (boolean): Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
- `--switchProfileId` (string): The ID of a switch profile to bind to the device (for available switch profiles, see the 'Switch Profiles' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch profile, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
- `--floorPlanId` (string): The floor plan to associate to this device. null disassociates the device from the floorplan.


##### Example:
```
meraki batch devices updateDevice --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch devices updateDevice --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDevice(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Devices Update Device Management Interface


**Update the management interface settings for a device**

https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface

##### Arguments
- `--serial` (string): (required)
- `--wan1` (object): WAN 1 settings
- `--wan2` (object): WAN 2 settings (only for MX devices)


##### Example:
```
meraki batch devices updateDeviceManagementInterface --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch devices updateDeviceManagementInterface --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceManagementInterface(serial:str, **kwargs):
    # Code
````

# Batch Insight


----------------------------------------
## Batch Insight Create Organization Insight Monitored Media Server


**Add a media server to be monitored for this organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the VoIP provider
- `--address` (string): The IP address (IPv4 only) or hostname of the media server to monitor
- `--bestEffortMonitoringEnabled` (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.


##### Example:
```
meraki batch insight createOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --name 'STRING' --address 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch insight createOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --name 'STRING' --address 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationInsightMonitoredMediaServer(organizationId:str, name:str, address:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Insight Delete Organization Insight Monitored Media Server


**Delete a monitored media server from this organization**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--monitoredMediaServerId` (string): (required)


##### Example:
```
meraki batch insight deleteOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationInsightMonitoredMediaServer(organizationId:str, monitoredMediaServerId:str):
    # Code
````



----------------------------------------
## Batch Insight Update Organization Insight Monitored Media Server


**Update a monitored media server for this organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--monitoredMediaServerId` (string): (required)
- `--name` (string): The name of the VoIP provider
- `--address` (string): The IP address (IPv4 only) or hostname of the media server to monitor
- `--bestEffortMonitoringEnabled` (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.


##### Example:
```
meraki batch insight updateOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch insight updateOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationInsightMonitoredMediaServer(organizationId:str, monitoredMediaServerId:str, **kwargs):
    # Code
````

# Batch Networks


----------------------------------------
## Batch Networks Bind Network


**Bind a network to a template.**

https://developer.cisco.com/meraki/api-v1/#!bind-network

##### Arguments
- `--networkId` (string): (required)
- `--configTemplateId` (string): The ID of the template to which the network should be bound.
- `--autoBind` (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.


##### Example:
```
meraki batch networks bindNetwork --networkId 'STRING' --configTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks bindNetwork --networkId 'STRING' --configTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def bindNetwork(networkId:str, configTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Claim Network Devices


**Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)**

https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

##### Arguments
- `--networkId` (string): (required)
- `--serials` (array): A list of serials of devices to claim


##### Example:
```
meraki batch networks claimNetworkDevices --networkId 'STRING' --serials ITEM
````

##### Method Code:
```python
def claimNetworkDevices(networkId:str, serials:list):
    # Code
````



----------------------------------------
## Batch Networks Create Network Firmware Upgrades Rollback


**Rollback a Firmware Upgrade For A Network**

https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

##### Arguments
- `--networkId` (string): (required)
- `--reasons` (array): Reasons for the rollback
- `--product` (string): Product type to rollback (if the network is a combined network)
- `--time` (string): Scheduled time for the rollback
- `--toVersion` (object): Version to downgrade to (if the network has firmware flexibility)


##### Example:
```
meraki batch networks createNetworkFirmwareUpgradesRollback --networkId 'STRING' --reasons ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkFirmwareUpgradesRollback --networkId 'STRING' --reasons ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFirmwareUpgradesRollback(networkId:str, reasons:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Create Network Firmware Upgrades Staged Group


**Create a Staged Upgrade Group for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--isDefault` (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
- `--description` (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--assignedDevices` (object): The devices and Switch Stacks assigned to the Group


##### Example:
```
meraki batch networks createNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --name 'STRING' --isDefault --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --name 'STRING' --isDefault --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFirmwareUpgradesStagedGroup(networkId:str, name:str, isDefault:bool, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Create Network Group Policy


**Create a group policy**

https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name for your group policy. Required.
- `--scheduling` (object):     The schedule for the group policy. Schedules are applied to days of the week.

- `--bandwidth` (object):     The bandwidth settings for clients bound to your group policy.

- `--firewallAndTrafficShaping` (object):     The firewall and traffic shaping rules and settings for your policy.

- `--contentFiltering` (object): The content filtering settings for your group policy
- `--splashAuthSettings` (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- `--vlanTagging` (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- `--bonjourForwarding` (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.


##### Example:
```
meraki batch networks createNetworkGroupPolicy --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkGroupPolicy --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkGroupPolicy(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Create Network Meraki Auth User


**Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)**

https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--email` (string): Email address of the user
- `--authorizations` (array): Authorization zones and expiration dates for the user.
- `--name` (string): Name of the user. Only required If the user is not a Dashboard administrator.
- `--password` (string): The password for this user account. Only required If the user is not a Dashboard administrator.
- `--accountType` (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for wired networks. Defaults to '802.1X'.
- `--emailPasswordToUser` (boolean): Whether or not Meraki should email the password to user. Default is false.
- `--isAdmin` (boolean): Whether or not the user is a Dashboard administrator.


##### Example:
```
meraki batch networks createNetworkMerakiAuthUser --networkId 'STRING' --email 'STRING' --authorizations ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkMerakiAuthUser --networkId 'STRING' --email 'STRING' --authorizations ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkMerakiAuthUser(networkId:str, email:str, authorizations:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Create Network Mqtt Broker


**Add an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the MQTT broker.
- `--host` (string): Host name/IP address where the MQTT broker runs.
- `--port` (integer): Host port though which the MQTT broker can be reached.
- `--security` (object): Security settings of the MQTT broker.
- `--authentication` (object): Authentication settings of the MQTT broker


##### Example:
```
meraki batch networks createNetworkMqttBroker --networkId 'STRING' --name 'STRING' --host 'STRING' --port INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkMqttBroker --networkId 'STRING' --name 'STRING' --host 'STRING' --port INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkMqttBroker(networkId:str, name:str, host:str, port:int, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Create Network Webhooks Payload Template


**Create a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new template
- `--body` (string): The liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
- `--headers` (array): The liquid template used with the webhook headers.
- `--bodyFile` (string): A file containing liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
- `--headersFile` (string): A file containing the liquid template used with the webhook headers.


##### Example:
```
meraki batch networks createNetworkWebhooksPayloadTemplate --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks createNetworkWebhooksPayloadTemplate --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWebhooksPayloadTemplate(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Delete Network


**Delete a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki batch networks deleteNetwork --networkId 'STRING'
````

##### Method Code:
```python
def deleteNetwork(networkId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Firmware Upgrades Staged Group


**Delete a Staged Upgrade Group**

https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--groupId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --groupId 'STRING'
````

##### Method Code:
```python
def deleteNetworkFirmwareUpgradesStagedGroup(networkId:str, groupId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Floor Plan


**Destroy a floor plan**

https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--floorPlanId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING'
````

##### Method Code:
```python
def deleteNetworkFloorPlan(networkId:str, floorPlanId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Group Policy


**Delete a group policy**

https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--groupPolicyId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING'
````

##### Method Code:
```python
def deleteNetworkGroupPolicy(networkId:str, groupPolicyId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Meraki Auth User


**Deauthorize a user**

https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--merakiAuthUserId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING'
````

##### Method Code:
```python
def deleteNetworkMerakiAuthUser(networkId:str, merakiAuthUserId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Mqtt Broker


**Delete an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--mqttBrokerId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING'
````

##### Method Code:
```python
def deleteNetworkMqttBroker(networkId:str, mqttBrokerId:str):
    # Code
````



----------------------------------------
## Batch Networks Delete Network Webhooks Payload Template


**Destroy a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--payloadTemplateId` (string): (required)


##### Example:
```
meraki batch networks deleteNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWebhooksPayloadTemplate(networkId:str, payloadTemplateId:str):
    # Code
````



----------------------------------------
## Batch Networks Provision Network Clients


**Provisions a client with a name and policy**

https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

##### Arguments
- `--networkId` (string): (required)
- `--clients` (array): The array of clients to provision
- `--devicePolicy` (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
- `--groupPolicyId` (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
- `--policiesBySecurityAppliance` (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
- `--policiesBySsid` (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy


##### Example:
```
meraki batch networks provisionNetworkClients --networkId 'STRING' --clients ITEM --devicePolicy 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks provisionNetworkClients --networkId 'STRING' --clients ITEM --devicePolicy 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def provisionNetworkClients(networkId:str, clients:list, devicePolicy:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Remove Network Devices


**Remove a single device**

https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

##### Arguments
- `--networkId` (string): (required)
- `--serial` (string): The serial of a device


##### Example:
```
meraki batch networks removeNetworkDevices --networkId 'STRING' --serial 'STRING'
````

##### Method Code:
```python
def removeNetworkDevices(networkId:str, serial:str):
    # Code
````



----------------------------------------
## Batch Networks Split Network


**Split a combined network into individual networks for each type of device**

https://developer.cisco.com/meraki/api-v1/#!split-network

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki batch networks splitNetwork --networkId 'STRING'
````

##### Method Code:
```python
def splitNetwork(networkId:str):
    # Code
````



----------------------------------------
## Batch Networks Unbind Network


**Unbind a network from a template.**

https://developer.cisco.com/meraki/api-v1/#!unbind-network

##### Arguments
- `--networkId` (string): (required)
- `--retainConfigs` (boolean): Optional boolean to retain all the current configs given by the template.


##### Example:
```
meraki batch networks unbindNetwork --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks unbindNetwork --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def unbindNetwork(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network


**Update a network**

https://developer.cisco.com/meraki/api-v1/#!update-network

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the network
- `--timeZone` (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- `--tags` (array): A list of tags to be applied to the network
- `--enrollmentString` (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
- `--notes` (string): Add any notes or additional information about this network here.


##### Example:
```
meraki batch networks updateNetwork --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetwork --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetwork(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Firmware Upgrades


**Update firmware upgrade information for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

##### Arguments
- `--networkId` (string): (required)
- `--upgradeWindow` (object): Upgrade window for devices in network
- `--timezone` (string): The timezone for the network
- `--products` (object): Contains information about the network to update


##### Example:
```
meraki batch networks updateNetworkFirmwareUpgrades --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkFirmwareUpgrades --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFirmwareUpgrades(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Floor Plan


**Update a floor plan's geolocation and other meta data**

https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--floorPlanId` (string): (required)
- `--name` (string): The name of your floor plan.
- `--center` (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
- `--bottomLeftCorner` (object): The longitude and latitude of the bottom left corner of your floor plan.
- `--bottomRightCorner` (object): The longitude and latitude of the bottom right corner of your floor plan.
- `--topLeftCorner` (object): The longitude and latitude of the top left corner of your floor plan.
- `--topRightCorner` (object): The longitude and latitude of the top right corner of your floor plan.
- `--imageContents` (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.


##### Example:
```
meraki batch networks updateNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFloorPlan(networkId:str, floorPlanId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Group Policy


**Update a group policy**

https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--groupPolicyId` (string): (required)
- `--name` (string): The name for your group policy.
- `--scheduling` (object):     The schedule for the group policy. Schedules are applied to days of the week.

- `--bandwidth` (object):     The bandwidth settings for clients bound to your group policy.

- `--firewallAndTrafficShaping` (object):     The firewall and traffic shaping rules and settings for your policy.

- `--contentFiltering` (object): The content filtering settings for your group policy
- `--splashAuthSettings` (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- `--vlanTagging` (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- `--bonjourForwarding` (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.


##### Example:
```
meraki batch networks updateNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkGroupPolicy(networkId:str, groupPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Meraki Auth User


**Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)**

https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--merakiAuthUserId` (string): (required)
- `--name` (string): Name of the user. Only allowed If the user is not Dashboard administrator.
- `--password` (string): The password for this user account. Only allowed If the user is not Dashboard administrator.
- `--emailPasswordToUser` (boolean): Whether or not Meraki should email the password to user. Default is false.
- `--authorizations` (array): Authorization zones and expiration dates for the user.


##### Example:
```
meraki batch networks updateNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkMerakiAuthUser(networkId:str, merakiAuthUserId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Mqtt Broker


**Update an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--mqttBrokerId` (string): (required)
- `--name` (string): Name of the MQTT broker.
- `--host` (string): Host name/IP address where the MQTT broker runs.
- `--port` (integer): Host port though which the MQTT broker can be reached.
- `--security` (object): Security settings of the MQTT broker.
- `--authentication` (object): Authentication settings of the MQTT broker


##### Example:
```
meraki batch networks updateNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkMqttBroker(networkId:str, mqttBrokerId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Settings


**Update the settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-settings

##### Arguments
- `--networkId` (string): (required)
- `--localStatusPageEnabled` (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
- `--remoteStatusPageEnabled` (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
- `--localStatusPage` (object): A hash of Local Status page(s)' authentication options applied to the Network.
- `--securePort` (object): A hash of SecureConnect options applied to the Network.


##### Example:
```
meraki batch networks updateNetworkSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Update Network Webhooks Payload Template


**Update a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--payloadTemplateId` (string): (required)
- `--name` (string): The name of the template
- `--body` (string): The liquid template used for the body of the webhook message.
- `--headers` (array): The liquid template used with the webhook headers.
- `--bodyFile` (string): A file containing liquid template used for the body of the webhook message.
- `--headersFile` (string): A file containing the liquid template used with the webhook headers.


##### Example:
```
meraki batch networks updateNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch networks updateNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWebhooksPayloadTemplate(networkId:str, payloadTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Networks Vmx Network Devices Claim


**Claim a vMX into a network**

https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

##### Arguments
- `--networkId` (string): (required)
- `--size` (string): The size of the vMX you claim. It can be one of: small, medium, large, 100


##### Example:
```
meraki batch networks vmxNetworkDevicesClaim --networkId 'STRING' --size 'STRING'
````

##### Method Code:
```python
def vmxNetworkDevicesClaim(networkId:str, size:str):
    # Code
````

# Batch Organizations


----------------------------------------
## Batch Organizations Assign Organization Licenses Seats


**Assign SM seats to a network**

https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--licenseId` (string): The ID of the SM license to assign seats from
- `--networkId` (string): The ID of the SM network to assign the seats to
- `--seatCount` (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license


##### Example:
```
meraki batch organizations assignOrganizationLicensesSeats --organizationId 'STRING' --licenseId 'STRING' --networkId 'STRING' --seatCount INT
````

##### Method Code:
```python
def assignOrganizationLicensesSeats(organizationId:str, licenseId:str, networkId:str, seatCount:int):
    # Code
````



----------------------------------------
## Batch Organizations Combine Organization Networks


**Combine multiple networks into a single network**

https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the combined network
- `--networkIds` (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
- `--enrollmentString` (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.


##### Example:
```
meraki batch organizations combineOrganizationNetworks --organizationId 'STRING' --name 'STRING' --networkIds ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations combineOrganizationNetworks --organizationId 'STRING' --name 'STRING' --networkIds ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def combineOrganizationNetworks(organizationId:str, name:str, networkIds:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Adaptive Policy Acl


**Creates new adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the adaptive policy ACL
- `--rules` (array): An ordered array of the adaptive policy ACL rules.
- `--ipVersion` (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
- `--description` (string): Description of the adaptive policy ACL


##### Example:
```
meraki batch organizations createOrganizationAdaptivePolicyAcl --organizationId 'STRING' --name 'STRING' --rules ITEM --ipVersion 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationAdaptivePolicyAcl --organizationId 'STRING' --name 'STRING' --rules ITEM --ipVersion 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyAcl(organizationId:str, name:str, rules:list, ipVersion:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Adaptive Policy Group


**Creates a new adaptive policy group**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the group
- `--sgt` (integer): SGT value of the group
- `--description` (string): Description of the group (default: "")
- `--policyObjects` (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: [])


##### Example:
```
meraki batch organizations createOrganizationAdaptivePolicyGroup --organizationId 'STRING' --name 'STRING' --sgt INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationAdaptivePolicyGroup --organizationId 'STRING' --name 'STRING' --sgt INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyGroup(organizationId:str, name:str, sgt:int, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Adaptive Policy Policy


**Add an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--sourceGroup` (object): The source adaptive policy group (requires one unique attribute)
- `--destinationGroup` (object): The destination adaptive policy group (requires one unique attribute)
- `--acls` (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])
- `--lastEntryRule` (string): The rule to apply if there is no matching ACL (default: "default")


##### Example:
```
meraki batch organizations createOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --sourceGroup JSON_STRING --destinationGroup JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --sourceGroup JSON_STRING --destinationGroup JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyPolicy(organizationId:str, sourceGroup:dict, destinationGroup:dict, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Alerts Profile


**Create an organization-wide alert configuration**

https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--type` (string): The alert type
- `--alertCondition` (object): The conditions that determine if the alert triggers
- `--recipients` (object): List of recipients that will recieve the alert.
- `--networkTags` (array): Networks with these tags will be monitored for the alert
- `--description` (string): User supplied description of the alert


##### Example:
```
meraki batch organizations createOrganizationAlertsProfile --organizationId 'STRING' --type 'STRING' --alertCondition JSON_STRING --recipients JSON_STRING --networkTags ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationAlertsProfile --organizationId 'STRING' --type 'STRING' --alertCondition JSON_STRING --recipients JSON_STRING --networkTags ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAlertsProfile(organizationId:str, type:str, alertCondition:dict, recipients:dict, networkTags:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Branding Policy


**Add a new branding policy to an organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the Dashboard branding policy.
- `--enabled` (boolean): Boolean indicating whether this policy is enabled.
- `--adminSettings` (object): Settings for describing which kinds of admins this policy applies to.
- `--helpSettings` (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.
Each property defaults to 'default or inherit' when not provided.
- `--customLogo` (object): Properties describing the custom logo attached to the branding policy.


##### Example:
```
meraki batch organizations createOrganizationBrandingPolicy --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationBrandingPolicy --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationBrandingPolicy(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Config Template


**Create a new configuration template**

https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the configuration template
- `--timeZone` (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
- `--copyFromNetworkId` (string): The ID of the network or config template to copy configuration from


##### Example:
```
meraki batch organizations createOrganizationConfigTemplate --organizationId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationConfigTemplate --organizationId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationConfigTemplate(organizationId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Network


**Create a network**

https://developer.cisco.com/meraki/api-v1/#!create-organization-network

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the new network
- `--productTypes` (array): The product type(s) of the new network. If more than one type is included, the network will be a combined network.
- `--tags` (array): A list of tags to be applied to the network
- `--timeZone` (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- `--copyFromNetworkId` (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
- `--notes` (string): Add any notes or additional information about this network here.


##### Example:
```
meraki batch organizations createOrganizationNetwork --organizationId 'STRING' --name 'STRING' --productTypes ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationNetwork --organizationId 'STRING' --name 'STRING' --productTypes ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationNetwork(organizationId:str, name:str, productTypes:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Policy Object


**Creates a new Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--category` (string): Category of a policy object (one of: adaptivePolicy, network)
- `--type` (string): Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask)
- `--cidr` (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
- `--fqdn` (string): Fully qualified domain name of policy object (e.g. "example.com")
- `--mask` (string): Mask of a policy object (e.g. "255.255.0.0")
- `--ip` (string): IP Address of a policy object (e.g. "1.2.3.4")
- `--groupIds` (array): The IDs of policy object groups the policy object belongs to


##### Example:
```
meraki batch organizations createOrganizationPolicyObject --organizationId 'STRING' --name 'STRING' --category 'STRING' --type 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationPolicyObject --organizationId 'STRING' --name 'STRING' --category 'STRING' --type 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationPolicyObject(organizationId:str, name:str, category:str, type:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Policy Objects Group


**Creates a new Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--category` (string): Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup)
- `--objectIds` (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)


##### Example:
```
meraki batch organizations createOrganizationPolicyObjectsGroup --organizationId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationPolicyObjectsGroup --organizationId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationPolicyObjectsGroup(organizationId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Create Organization Saml Idp


**Create a SAML IdP for your organization.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--x509certSha1Fingerprint` (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- `--sloLogoutUrl` (string): Dashboard will redirect users to this URL when they sign out.


##### Example:
```
meraki batch organizations createOrganizationSamlIdp --organizationId 'STRING' --x509certSha1Fingerprint 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations createOrganizationSamlIdp --organizationId 'STRING' --x509certSha1Fingerprint 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationSamlIdp(organizationId:str, x509certSha1Fingerprint:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Adaptive Policy Acl


**Deletes the specified adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--aclId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyAcl(organizationId:str, aclId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Adaptive Policy Group


**Deletes the specified adaptive policy group and any associated policies and references**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyGroup(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Adaptive Policy Policy


**Delete an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyPolicy(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Alerts Profile


**Removes an organization-wide alert config**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--alertConfigId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAlertsProfile(organizationId:str, alertConfigId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Branding Policy


**Delete a branding policy**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationBrandingPolicy(organizationId:str, brandingPolicyId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Policy Object


**Deletes a Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationPolicyObject(organizationId:str, policyObjectId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Policy Objects Group


**Deletes a Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectGroupId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationPolicyObjectsGroup(organizationId:str, policyObjectGroupId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization Saml Idp


**Remove a SAML IdP in your organization.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--idpId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationSamlIdp(organizationId:str, idpId:str):
    # Code
````



----------------------------------------
## Batch Organizations Delete Organization User


**Delete a user and all of its authentication methods.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-user

##### Arguments
- `--organizationId` (string): (required)
- `--userId` (string): (required)


##### Example:
```
meraki batch organizations deleteOrganizationUser --organizationId 'STRING' --userId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationUser(organizationId:str, userId:str):
    # Code
````



----------------------------------------
## Batch Organizations Move Organization Licenses


**Move licenses to another organization**

https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

##### Arguments
- `--organizationId` (string): (required)
- `--destOrganizationId` (string): The ID of the organization to move the licenses to
- `--licenseIds` (array): A list of IDs of licenses to move to the new organization


##### Example:
```
meraki batch organizations moveOrganizationLicenses --organizationId 'STRING' --destOrganizationId 'STRING' --licenseIds ITEM
````

##### Method Code:
```python
def moveOrganizationLicenses(organizationId:str, destOrganizationId:str, licenseIds:list):
    # Code
````



----------------------------------------
## Batch Organizations Move Organization Licenses Seats


**Move SM seats to another organization**

https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--destOrganizationId` (string): The ID of the organization to move the SM seats to
- `--licenseId` (string): The ID of the SM license to move the seats from
- `--seatCount` (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license


##### Example:
```
meraki batch organizations moveOrganizationLicensesSeats --organizationId 'STRING' --destOrganizationId 'STRING' --licenseId 'STRING' --seatCount INT
````

##### Method Code:
```python
def moveOrganizationLicensesSeats(organizationId:str, destOrganizationId:str, licenseId:str, seatCount:int):
    # Code
````



----------------------------------------
## Batch Organizations Renew Organization Licenses Seats


**Renew SM seats of a license**

https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--licenseIdToRenew` (string): The ID of the SM license to renew. This license must already be assigned to an SM network
- `--unusedLicenseId` (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'


##### Example:
```
meraki batch organizations renewOrganizationLicensesSeats --organizationId 'STRING' --licenseIdToRenew 'STRING' --unusedLicenseId 'STRING'
````

##### Method Code:
```python
def renewOrganizationLicensesSeats(organizationId:str, licenseIdToRenew:str, unusedLicenseId:str):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Adaptive Policy Acl


**Updates an adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--aclId` (string): (required)
- `--name` (string): Name of the adaptive policy ACL
- `--description` (string): Description of the adaptive policy ACL
- `--rules` (array): An ordered array of the adaptive policy ACL rules. An empty array will clear the rules.
- `--ipVersion` (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'


##### Example:
```
meraki batch organizations updateOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyAcl(organizationId:str, aclId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Adaptive Policy Group


**Updates an adaptive policy group**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)
- `--name` (string): Name of the group
- `--sgt` (integer): SGT value of the group
- `--description` (string): Description of the group
- `--policyObjects` (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute)


##### Example:
```
meraki batch organizations updateOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyGroup(organizationId:str, id:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Adaptive Policy Policy


**Update an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)
- `--sourceGroup` (object): The source adaptive policy group (requires one unique attribute)
- `--destinationGroup` (object): The destination adaptive policy group (requires one unique attribute)
- `--acls` (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
- `--lastEntryRule` (string): The rule to apply if there is no matching ACL


##### Example:
```
meraki batch organizations updateOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyPolicy(organizationId:str, id:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Adaptive Policy Settings


**Update global adaptive policy settings**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

##### Arguments
- `--organizationId` (string): (required)
- `--enabledNetworks` (array): List of network IDs with adaptive policy enabled


##### Example:
```
meraki batch organizations updateOrganizationAdaptivePolicySettings --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationAdaptivePolicySettings --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicySettings(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Alerts Profile


**Update an organization-wide alert config**

https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--alertConfigId` (string): (required)
- `--enabled` (boolean): Is the alert config enabled
- `--type` (string): The alert type
- `--alertCondition` (object): The conditions that determine if the alert triggers
- `--recipients` (object): List of recipients that will recieve the alert.
- `--networkTags` (array): Networks with these tags will be monitored for the alert
- `--description` (string): User supplied description of the alert


##### Example:
```
meraki batch organizations updateOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAlertsProfile(organizationId:str, alertConfigId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Branding Policies Priorities


**Update the priority ordering of an organization's branding policies.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyIds` (array):       An ordered list of branding policy IDs that determines the priority order of how to apply the policies



##### Example:
```
meraki batch organizations updateOrganizationBrandingPoliciesPriorities --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationBrandingPoliciesPriorities --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationBrandingPoliciesPriorities(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Branding Policy


**Update a branding policy**

https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyId` (string): (required)
- `--name` (string): Name of the Dashboard branding policy.
- `--enabled` (boolean): Boolean indicating whether this policy is enabled.
- `--adminSettings` (object): Settings for describing which kinds of admins this policy applies to.
- `--helpSettings` (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.

- `--customLogo` (object): Properties describing the custom logo attached to the branding policy.


##### Example:
```
meraki batch organizations updateOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationBrandingPolicy(organizationId:str, brandingPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Config Template


**Update a configuration template**

https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--name` (string): The name of the configuration template
- `--timeZone` (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>


##### Example:
```
meraki batch organizations updateOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationConfigTemplate(organizationId:str, configTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Early Access Features Opt In


**Update an early access feature opt-in for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

##### Arguments
- `--organizationId` (string): (required)
- `--optInId` (string): (required)
- `--limitScopeToNetworks` (array): A list of network IDs to apply the opt-in to


##### Example:
```
meraki batch organizations updateOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationEarlyAccessFeaturesOptIn(organizationId:str, optInId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization License


**Update a license**

https://developer.cisco.com/meraki/api-v1/#!update-organization-license

##### Arguments
- `--organizationId` (string): (required)
- `--licenseId` (string): (required)
- `--deviceSerial` (string): The serial number of the device to assign this license to. Set this to  null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.


##### Example:
```
meraki batch organizations updateOrganizationLicense --organizationId 'STRING' --licenseId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationLicense --organizationId 'STRING' --licenseId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationLicense(organizationId:str, licenseId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Login Security


**Update the login security settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

##### Arguments
- `--organizationId` (string): (required)
- `--enforcePasswordExpiration` (boolean): Boolean indicating whether users are forced to change their password every X number of days.
- `--passwordExpirationDays` (integer): Number of days after which users will be forced to change their password.
- `--enforceDifferentPasswords` (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
- `--numDifferentPasswords` (integer): Number of recent passwords that new password must be distinct from.
- `--enforceStrongPasswords` (boolean): Boolean indicating whether users will be forced to choose strong passwords for their accounts. Strong passwords are at least 8 characters that contain 3 of the following: number, uppercase letter, lowercase letter, and symbol
- `--enforceAccountLockout` (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
- `--accountLockoutAttempts` (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
- `--enforceIdleTimeout` (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
- `--idleTimeoutMinutes` (integer): Number of minutes users can remain idle before being logged out of their accounts.
- `--enforceTwoFactorAuth` (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the authenticator application.
- `--enforceLoginIpRanges` (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
- `--loginIpRanges` (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
- `--apiAuthentication` (object): Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.


##### Example:
```
meraki batch organizations updateOrganizationLoginSecurity --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationLoginSecurity --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationLoginSecurity(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Policy Object


**Updates a Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectId` (string): (required)
- `--name` (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--cidr` (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
- `--fqdn` (string): Fully qualified domain name of policy object (e.g. "example.com")
- `--mask` (string): Mask of a policy object (e.g. "255.255.0.0")
- `--ip` (string): IP Address of a policy object (e.g. "1.2.3.4")
- `--groupIds` (array): The IDs of policy object groups the policy object belongs to


##### Example:
```
meraki batch organizations updateOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationPolicyObject(organizationId:str, policyObjectId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Policy Objects Group


**Updates a Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectGroupId` (string): (required)
- `--name` (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--objectIds` (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)


##### Example:
```
meraki batch organizations updateOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationPolicyObjectsGroup(organizationId:str, policyObjectGroupId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Organizations Update Organization Saml Idp


**Update a SAML IdP in your organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--idpId` (string): (required)
- `--x509certSha1Fingerprint` (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- `--sloLogoutUrl` (string): Dashboard will redirect users to this URL when they sign out.


##### Example:
```
meraki batch organizations updateOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch organizations updateOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationSamlIdp(organizationId:str, idpId:str, **kwargs):
    # Code
````

# Batch Sensor


----------------------------------------
## Batch Sensor Create Network Sensor Alerts Profile


**Creates a sensor alert profile for a network.**

https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the sensor alert profile.
- `--conditions` (array): List of conditions that will cause the profile to send an alert.
- `--schedule` (object): The sensor schedule to use with the alert profile.
- `--recipients` (object): List of recipients that will recieve the alert.
- `--serials` (array): List of device serials assigned to this sensor alert profile.


##### Example:
```
meraki batch sensor createNetworkSensorAlertsProfile --networkId 'STRING' --name 'STRING' --conditions ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch sensor createNetworkSensorAlertsProfile --networkId 'STRING' --name 'STRING' --conditions ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSensorAlertsProfile(networkId:str, name:str, conditions:list, **kwargs):
    # Code
````



----------------------------------------
## Batch Sensor Delete Network Sensor Alerts Profile


**Deletes a sensor alert profile from a network.**

https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki batch sensor deleteNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteNetworkSensorAlertsProfile(networkId:str, id:str):
    # Code
````



----------------------------------------
## Batch Sensor Update Device Sensor Relationships


**Assign one or more sensor roles to a given sensor or camera device.**

https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

##### Arguments
- `--serial` (string): (required)
- `--livestream` (object): A role defined between an MT sensor and an MV camera that adds the camera's livestream to the sensor's details page. Snapshots from the camera will also appear in alert notifications that the sensor triggers.


##### Example:
```
meraki batch sensor updateDeviceSensorRelationships --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch sensor updateDeviceSensorRelationships --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSensorRelationships(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Sensor Update Network Sensor Alerts Profile


**Updates a sensor alert profile for a network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): (required)
- `--name` (string): Name of the sensor alert profile.
- `--schedule` (object): The sensor schedule to use with the alert profile.
- `--conditions` (array): List of conditions that will cause the profile to send an alert.
- `--recipients` (object): List of recipients that will recieve the alert.
- `--serials` (array): List of device serials assigned to this sensor alert profile.


##### Example:
```
meraki batch sensor updateNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch sensor updateNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSensorAlertsProfile(networkId:str, id:str, **kwargs):
    # Code
````

# Batch Sm


----------------------------------------
## Batch Sm Delete Network Sm User Access Device


**Delete a User Access Device**

https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

##### Arguments
- `--networkId` (string): (required)
- `--userAccessDeviceId` (string): (required)


##### Example:
```
meraki batch sm deleteNetworkSmUserAccessDevice --networkId 'STRING' --userAccessDeviceId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSmUserAccessDevice(networkId:str, userAccessDeviceId:str):
    # Code
````

# Batch Switch


----------------------------------------
## Batch Switch Clone Organization Switch Devices


**Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**

https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

##### Arguments
- `--organizationId` (string): (required)
- `--sourceSerial` (string): Serial number of the source switch (must be on a network not bound to a template)
- `--targetSerials` (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)


##### Example:
```
meraki batch switch cloneOrganizationSwitchDevices --organizationId 'STRING' --sourceSerial 'STRING' --targetSerials ITEM
````

##### Method Code:
```python
def cloneOrganizationSwitchDevices(organizationId:str, sourceSerial:str, targetSerials:list):
    # Code
````



----------------------------------------
## Batch Switch Create Device Switch Routing Interface


**Create a layer 3 interface for a switch**

https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ospfV3` (object): The OSPFv3 routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki batch switch createDeviceSwitchRoutingInterface --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createDeviceSwitchRoutingInterface --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceSwitchRoutingInterface(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Device Switch Routing Static Route


**Create a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--name` (string): Name or description for layer 3 static route
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki batch switch createDeviceSwitchRoutingStaticRoute --serial 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createDeviceSwitchRoutingStaticRoute --serial 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceSwitchRoutingStaticRoute(serial:str, subnet:str, nextHopIp:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Access Policy


**Create an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the access policy
- `--radiusServers` (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- `--radiusTestingEnabled` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusCoaSupportEnabled` (boolean): Change of authentication for RADIUS re-authentication and disconnection
- `--radiusAccountingEnabled` (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- `--hostMode` (string): Choose the Host Mode for the access policy.
- `--urlRedirectWalledGardenEnabled` (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- `--radius` (object): Object for RADIUS Settings
- `--guestPortBouncing` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusAccountingServers` (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- `--radiusGroupAttribute` (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
- `--accessPolicyType` (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- `--increaseAccessSpeed` (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- `--guestVlanId` (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- `--dot1x` (object): 802.1x Settings
- `--voiceVlanClients` (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- `--urlRedirectWalledGardenRanges` (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication


##### Example:
```
meraki batch switch createNetworkSwitchAccessPolicy --networkId 'STRING' --name 'STRING' --radiusServers ITEM --radiusTestingEnabled --radiusCoaSupportEnabled --radiusAccountingEnabled --hostMode 'STRING' --urlRedirectWalledGardenEnabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createNetworkSwitchAccessPolicy --networkId 'STRING' --name 'STRING' --radiusServers ITEM --radiusTestingEnabled --radiusCoaSupportEnabled --radiusAccountingEnabled --hostMode 'STRING' --urlRedirectWalledGardenEnabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchAccessPolicy(networkId:str, name:str, radiusServers:list, radiusTestingEnabled:bool, radiusCoaSupportEnabled:bool, radiusAccountingEnabled:bool, hostMode:str, urlRedirectWalledGardenEnabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Add a server to be trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--mac` (string): The mac address of the trusted server being added
- `--vlan` (integer): The VLAN of the trusted server being added. It must be between 1 and 4094
- `--ipv4` (object): The IPv4 attributes of the trusted server being added


##### Example:
```
meraki batch switch createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --mac 'STRING' --vlan INT --ipv4 JSON_STRING
````

##### Method Code:
```python
def createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, mac:str, vlan:int, ipv4:dict):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Link Aggregation


**Create a link aggregation group**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--switchPorts` (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
- `--switchProfilePorts` (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.


##### Example:
```
meraki batch switch createNetworkSwitchLinkAggregation --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createNetworkSwitchLinkAggregation --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchLinkAggregation(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Qos Rule


**Add a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--vlan` (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- `--protocol` (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY"
- `--srcPort` (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--srcPortRange` (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dstPort` (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--dstPortRange` (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dscp` (integer): DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0


##### Example:
```
meraki batch switch createNetworkSwitchQosRule --networkId 'STRING' --vlan INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createNetworkSwitchQosRule --networkId 'STRING' --vlan INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchQosRule(networkId:str, vlan:int, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Routing Multicast Rendezvous Point


**Create a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--interfaceIp` (string): The IP address of the interface where the RP needs to be created.
- `--multicastGroup` (string): 'Any', or the IP address of a multicast group


##### Example:
```
meraki batch switch createNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --interfaceIp 'STRING' --multicastGroup 'STRING'
````

##### Method Code:
```python
def createNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, interfaceIp:str, multicastGroup:str):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Stack Routing Interface


**Create a layer 3 interface for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki batch switch createNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --name 'STRING' --vlanId INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --name 'STRING' --vlanId INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, name:str, vlanId:int, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Create Network Switch Stack Routing Static Route


**Create a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--name` (string): Name or description for layer 3 static route
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki batch switch createNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch createNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, subnet:str, nextHopIp:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Cycle Device Switch Ports


**Cycle a set of switch ports**

https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

##### Arguments
- `--serial` (string): (required)
- `--ports` (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]


##### Example:
```
meraki batch switch cycleDeviceSwitchPorts --serial 'STRING' --ports ITEM
````

##### Method Code:
```python
def cycleDeviceSwitchPorts(serial:str, ports:list):
    # Code
````



----------------------------------------
## Batch Switch Delete Device Switch Routing Interface


**Delete a layer 3 interface from the switch**

https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki batch switch deleteDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def deleteDeviceSwitchRoutingInterface(serial:str, interfaceId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Device Switch Routing Static Route


**Delete a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki batch switch deleteDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def deleteDeviceSwitchRoutingStaticRoute(serial:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Access Policy


**Delete an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--accessPolicyNumber` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchAccessPolicy(networkId:str, accessPolicyNumber:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Remove a server from being trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--trustedServerId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, trustedServerId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Link Aggregation


**Split a link aggregation group into separate ports**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--linkAggregationId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchLinkAggregation(networkId:str, linkAggregationId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Qos Rule


**Delete a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--qosRuleId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchQosRule(networkId:str, qosRuleId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Routing Multicast Rendezvous Point


**Delete a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--rendezvousPointId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --rendezvousPointId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, rendezvousPointId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Stack Routing Interface


**Delete a layer 3 interface from a switch stack**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, interfaceId:str):
    # Code
````



----------------------------------------
## Batch Switch Delete Network Switch Stack Routing Static Route


**Delete a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki batch switch deleteNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Batch Switch Update Device Switch Port


**Update a switch port**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

##### Arguments
- `--serial` (string): (required)
- `--portId` (string): (required)
- `--name` (string): The name of the switch port.
- `--tags` (array): The list of tags of the switch port.
- `--enabled` (boolean): The status of the switch port.
- `--poeEnabled` (boolean): The PoE status of the switch port.
- `--type` (string): The type of the switch port ('trunk' or 'access').
- `--vlan` (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
- `--voiceVlan` (integer): The voice VLAN of the switch port. Only applicable to access ports.
- `--allowedVlans` (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
- `--isolationEnabled` (boolean): The isolation status of the switch port.
- `--rstpEnabled` (boolean): The rapid spanning tree protocol status.
- `--stpGuard` (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
- `--linkNegotiation` (string): The link speed for the switch port.
- `--portScheduleId` (string): The ID of the port schedule. A value of null will clear the port schedule.
- `--udld` (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- `--accessPolicyType` (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
- `--accessPolicyNumber` (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
- `--macAllowList` (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
- `--stickyMacAllowList` (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stickyMacAllowListLimit` (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stormControlEnabled` (boolean): The storm control status of the switch port.
- `--adaptivePolicyGroupId` (string): The adaptive policy group ID that will be used to tag traffic through this switch port. This ID must pre-exist during the configuration, else needs to be created using adaptivePolicy/groups API. Cannot be applied to a port on a switch bound to profile.
- `--peerSgtCapable` (boolean): If true, Peer SGT is enabled for traffic through this switch port. Applicable to trunk port only, not access port. Cannot be applied to a port on a switch bound to profile.
- `--flexibleStackingEnabled` (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
- `--daiTrusted` (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
- `--profile` (object): Profile attributes


##### Example:
```
meraki batch switch updateDeviceSwitchPort --serial 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateDeviceSwitchPort --serial 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchPort(serial:str, portId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Device Switch Routing Interface


**Update a layer 3 interface for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ospfV3` (object): The OSPFv3 routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki batch switch updateDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingInterface(serial:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Device Switch Routing Interface Dhcp


**Update a layer 3 interface DHCP configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)
- `--dhcpMode` (string): The DHCP mode options for the switch interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- `--dhcpRelayServerIps` (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface
- `--dhcpLeaseTime` (string): The DHCP lease time config for the dhcp server running on switch interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- `--dnsNameserversOption` (string): The DHCP name server option for the dhcp server running on the switch interface ('googlePublicDns', 'openDns' or 'custom')
- `--dnsCustomNameservers` (array): The DHCP name server IPs when DHCP name server option is 'custom'
- `--bootOptionsEnabled` (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch interface
- `--bootNextServer` (string): The PXE boot server IP for the DHCP server running on the switch interface
- `--bootFileName` (string): The PXE boot server filename for the DHCP server running on the switch interface
- `--dhcpOptions` (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch interface
- `--reservedIpRanges` (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch interface
- `--fixedIpAssignments` (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch interface


##### Example:
```
meraki batch switch updateDeviceSwitchRoutingInterfaceDhcp --serial 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateDeviceSwitchRoutingInterfaceDhcp --serial 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingInterfaceDhcp(serial:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Device Switch Routing Static Route


**Update a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--staticRouteId` (string): (required)
- `--name` (string): Name or description for layer 3 static route
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki batch switch updateDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingStaticRoute(serial:str, staticRouteId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Device Switch Warm Spare


**Update warm spare configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

##### Arguments
- `--serial` (string): (required)
- `--enabled` (boolean): Enable or disable warm spare for a switch
- `--spareSerial` (string): Serial number of the warm spare switch


##### Example:
```
meraki batch switch updateDeviceSwitchWarmSpare --serial 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateDeviceSwitchWarmSpare --serial 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchWarmSpare(serial:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Access Policy


**Update an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--accessPolicyNumber` (string): (required)
- `--name` (string): Name of the access policy
- `--radiusServers` (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- `--radius` (object): Object for RADIUS Settings
- `--guestPortBouncing` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusTestingEnabled` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusCoaSupportEnabled` (boolean): Change of authentication for RADIUS re-authentication and disconnection
- `--radiusAccountingEnabled` (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- `--radiusAccountingServers` (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- `--radiusGroupAttribute` (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
- `--hostMode` (string): Choose the Host Mode for the access policy.
- `--accessPolicyType` (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- `--increaseAccessSpeed` (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- `--guestVlanId` (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- `--dot1x` (object): 802.1x Settings
- `--voiceVlanClients` (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- `--urlRedirectWalledGardenEnabled` (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- `--urlRedirectWalledGardenRanges` (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication


##### Example:
```
meraki batch switch updateNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchAccessPolicy(networkId:str, accessPolicyNumber:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Alternate Management Interface


**Update the switch alternate management interface for the network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable AMI configuration. If enabled, VLAN and protocols must be set
- `--vlanId` (integer): Alternate management VLAN, must be between 1 and 4094
- `--protocols` (array): Can be one or more of the following values: 'radius', 'snmp' or 'syslog'
- `--switches` (array): Array of switch serial number and IP assignment. If parameter is present, it cannot have empty body. Note: switches parameter is not applicable for template networks, in other words, do not put 'switches' in the body when updating template networks. Also, an empty 'switches' array will remove all previous assignments


##### Example:
```
meraki batch switch updateNetworkSwitchAlternateManagementInterface --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchAlternateManagementInterface --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchAlternateManagementInterface(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Dhcp Server Policy


**Update the DHCP server settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

##### Arguments
- `--networkId` (string): (required)
- `--alerts` (object): Alert settings for DHCP servers
- `--defaultPolicy` (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
- `--allowedServers` (array): List the MAC addresses of DHCP servers to permit on the network when defaultPolicy is set to block. An empty array will clear the entries.
- `--blockedServers` (array): List the MAC addresses of DHCP servers to block on the network when defaultPolicy is set to allow. An empty array will clear the entries.
- `--arpInspection` (object): Dynamic ARP Inspection settings


##### Example:
```
meraki batch switch updateNetworkSwitchDhcpServerPolicy --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchDhcpServerPolicy --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchDhcpServerPolicy(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Update a server that is trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--trustedServerId` (string): (required)
- `--mac` (string): The updated mac address of the trusted server
- `--vlan` (integer): The updated VLAN of the trusted server. It must be between 1 and 4094
- `--ipv4` (object): The updated IPv4 attributes of the trusted server


##### Example:
```
meraki batch switch updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, trustedServerId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Dscp To Cos Mappings


**Update the DSCP to CoS mappings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

##### Arguments
- `--networkId` (string): (required)
- `--mappings` (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.


##### Example:
```
meraki batch switch updateNetworkSwitchDscpToCosMappings --networkId 'STRING' --mappings ITEM
````

##### Method Code:
```python
def updateNetworkSwitchDscpToCosMappings(networkId:str, mappings:list):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Link Aggregation


**Update a link aggregation group**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--linkAggregationId` (string): (required)
- `--switchPorts` (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
- `--switchProfilePorts` (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.


##### Example:
```
meraki batch switch updateNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchLinkAggregation(networkId:str, linkAggregationId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Mtu


**Update the MTU configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

##### Arguments
- `--networkId` (string): (required)
- `--defaultMtuSize` (integer): MTU size for the entire network. Default value is 9578.
- `--overrides` (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.


##### Example:
```
meraki batch switch updateNetworkSwitchMtu --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchMtu --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchMtu(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Port Schedule


**Update a switch port schedule**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

##### Arguments
- `--networkId` (string): (required)
- `--portScheduleId` (string): (required)
- `--name` (string): The name for your port schedule.
- `--portSchedule` (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
When it's empty, default schedule with all days of a week are configured.
Any unspecified day in the schedule is added as a default schedule configuration of the day.



##### Example:
```
meraki batch switch updateNetworkSwitchPortSchedule --networkId 'STRING' --portScheduleId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchPortSchedule --networkId 'STRING' --portScheduleId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchPortSchedule(networkId:str, portScheduleId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Qos Rule


**Update a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--qosRuleId` (string): (required)
- `--vlan` (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- `--protocol` (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY".
- `--srcPort` (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--srcPortRange` (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dstPort` (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--dstPortRange` (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dscp` (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0.


##### Example:
```
meraki batch switch updateNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchQosRule(networkId:str, qosRuleId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Qos Rules Order


**Update the order in which the rules should be processed by the switch**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

##### Arguments
- `--networkId` (string): (required)
- `--ruleIds` (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.


##### Example:
```
meraki batch switch updateNetworkSwitchQosRulesOrder --networkId 'STRING' --ruleIds ITEM
````

##### Method Code:
```python
def updateNetworkSwitchQosRulesOrder(networkId:str, ruleIds:list):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Routing Multicast


**Update multicast settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

##### Arguments
- `--networkId` (string): (required)
- `--defaultSettings` (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
- `--overrides` (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.


##### Example:
```
meraki batch switch updateNetworkSwitchRoutingMulticast --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchRoutingMulticast --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingMulticast(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Routing Multicast Rendezvous Point


**Update a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--rendezvousPointId` (string): (required)
- `--interfaceIp` (string): The IP address of the interface to use
- `--multicastGroup` (string): 'Any', or the IP address of a multicast group


##### Example:
```
meraki batch switch updateNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --rendezvousPointId 'STRING' --interfaceIp 'STRING' --multicastGroup 'STRING'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, rendezvousPointId:str, interfaceIp:str, multicastGroup:str):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Routing Ospf


**Update layer 3 OSPF routing configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
- `--helloTimerInSeconds` (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds.
- `--deadTimerInSeconds` (integer): Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535
- `--areas` (array): OSPF areas
- `--v3` (object): OSPF v3 configuration
- `--md5AuthenticationEnabled` (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
- `--md5AuthenticationKey` (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true


##### Example:
```
meraki batch switch updateNetworkSwitchRoutingOspf --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchRoutingOspf --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingOspf(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Settings


**Update switch network settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

##### Arguments
- `--networkId` (string): (required)
- `--vlan` (integer): Management VLAN
- `--useCombinedPower` (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
- `--powerExceptions` (array): Exceptions on a per switch basis to "useCombinedPower"


##### Example:
```
meraki batch switch updateNetworkSwitchSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Stack Routing Interface


**Update a layer 3 interface for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki batch switch updateNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Stack Routing Interface Dhcp


**Update a layer 3 interface DHCP configuration for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)
- `--dhcpMode` (string): The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- `--dhcpRelayServerIps` (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface
- `--dhcpLeaseTime` (string): The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- `--dnsNameserversOption` (string): The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')
- `--dnsCustomNameservers` (array): The DHCP name server IPs when DHCP name server option is 'custom'
- `--bootOptionsEnabled` (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface
- `--bootNextServer` (string): The PXE boot server IP for the DHCP server running on the switch stack interface
- `--bootFileName` (string): The PXE boot server file name for the DHCP server running on the switch stack interface
- `--dhcpOptions` (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface
- `--reservedIpRanges` (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface
- `--fixedIpAssignments` (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface


##### Example:
```
meraki batch switch updateNetworkSwitchStackRoutingInterfaceDhcp --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchStackRoutingInterfaceDhcp --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingInterfaceDhcp(networkId:str, switchStackId:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Stack Routing Static Route


**Update a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--staticRouteId` (string): (required)
- `--name` (string): Name or description for layer 3 static route
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki batch switch updateNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, staticRouteId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Storm Control


**Update the storm control configuration for a switch network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

##### Arguments
- `--networkId` (string): (required)
- `--broadcastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
- `--multicastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
- `--unknownUnicastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.


##### Example:
```
meraki batch switch updateNetworkSwitchStormControl --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchStormControl --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStormControl(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Network Switch Stp


**Updates STP settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

##### Arguments
- `--networkId` (string): (required)
- `--rstpEnabled` (boolean): The spanning tree protocol status in network
- `--stpBridgePriority` (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.


##### Example:
```
meraki batch switch updateNetworkSwitchStp --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateNetworkSwitchStp --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStp(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Switch Update Organization Config Template Switch Profile Port


**Update a switch profile port**

https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--profileId` (string): (required)
- `--portId` (string): (required)
- `--name` (string): The name of the switch profile port.
- `--tags` (array): The list of tags of the switch profile port.
- `--enabled` (boolean): The status of the switch profile port.
- `--poeEnabled` (boolean): The PoE status of the switch profile port.
- `--type` (string): The type of the switch profile port ('trunk' or 'access').
- `--vlan` (integer): The VLAN of the switch profile port. A null value will clear the value set for trunk ports.
- `--voiceVlan` (integer): The voice VLAN of the switch profile port. Only applicable to access ports.
- `--allowedVlans` (string): The VLANs allowed on the switch profile port. Only applicable to trunk ports.
- `--isolationEnabled` (boolean): The isolation status of the switch profile port.
- `--rstpEnabled` (boolean): The rapid spanning tree protocol status.
- `--stpGuard` (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
- `--linkNegotiation` (string): The link speed for the switch profile port.
- `--portScheduleId` (string): The ID of the port schedule. A value of null will clear the port schedule.
- `--udld` (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- `--accessPolicyType` (string): The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
- `--accessPolicyNumber` (integer): The number of a custom access policy to configure on the switch profile port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
- `--macAllowList` (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
- `--stickyMacAllowList` (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stickyMacAllowListLimit` (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stormControlEnabled` (boolean): The storm control status of the switch profile port.
- `--flexibleStackingEnabled` (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
- `--daiTrusted` (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
- `--profile` (object): Profile attributes


##### Example:
```
meraki batch switch updateOrganizationConfigTemplateSwitchProfilePort --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch switch updateOrganizationConfigTemplateSwitchProfilePort --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationConfigTemplateSwitchProfilePort(organizationId:str, configTemplateId:str, profileId:str, portId:str, **kwargs):
    # Code
````

# Batch Wireless


----------------------------------------
## Batch Wireless Create Network Wireless Rf Profile


**Creates new RF profile for this network**

https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique. This param is required on creation.
- `--bandSelectionType` (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
- `--clientBalancingEnabled` (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
- `--minBitrateType` (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
- `--apBandSettings` (object): Settings that will be enabled if selectionType is set to 'ap'.
- `--twoFourGhzSettings` (object): Settings related to 2.4Ghz band
- `--fiveGhzSettings` (object): Settings related to 5Ghz band
- `--transmission` (object): Settings related to radio transmission.
- `--perSsidSettings` (object): Per-SSID radio settings by number.


##### Example:
```
meraki batch wireless createNetworkWirelessRfProfile --networkId 'STRING' --name 'STRING' --bandSelectionType 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless createNetworkWirelessRfProfile --networkId 'STRING' --name 'STRING' --bandSelectionType 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWirelessRfProfile(networkId:str, name:str, bandSelectionType:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Create Network Wireless Ssid Identity Psk


**Create an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the Identity PSK
- `--groupPolicyId` (string): The group policy to be applied to clients
- `--passphrase` (string): The passphrase for client authentication. If left blank, one will be auto-generated.


##### Example:
```
meraki batch wireless createNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --name 'STRING' --groupPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless createNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --name 'STRING' --groupPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWirelessSsidIdentityPsk(networkId:str, number:str, name:str, groupPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Delete Network Wireless Rf Profile


**Delete a RF Profile**

https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--rfProfileId` (string): (required)


##### Example:
```
meraki batch wireless deleteNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWirelessRfProfile(networkId:str, rfProfileId:str):
    # Code
````



----------------------------------------
## Batch Wireless Delete Network Wireless Ssid Identity Psk


**Delete an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--identityPskId` (string): (required)


##### Example:
```
meraki batch wireless deleteNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWirelessSsidIdentityPsk(networkId:str, number:str, identityPskId:str):
    # Code
````



----------------------------------------
## Batch Wireless Update Device Wireless Bluetooth Settings


**Update the bluetooth settings for a wireless device**

https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

##### Arguments
- `--serial` (string): (required)
- `--uuid` (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- `--major` (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- `--minor` (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.


##### Example:
```
meraki batch wireless updateDeviceWirelessBluetoothSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateDeviceWirelessBluetoothSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceWirelessBluetoothSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Device Wireless Radio Settings


**Update the radio settings of a device**

https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

##### Arguments
- `--serial` (string): (required)
- `--rfProfileId` (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
- `--twoFourGhzSettings` (object): Manual radio settings for 2.4 GHz.
- `--fiveGhzSettings` (object): Manual radio settings for 5 GHz.


##### Example:
```
meraki batch wireless updateDeviceWirelessRadioSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateDeviceWirelessRadioSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceWirelessRadioSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Alternate Management Interface


**Update alternate management interface and device static IP**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable alternate management interface
- `--vlanId` (integer): Alternate management interface VLAN, must be between 1 and 4094
- `--protocols` (array): Can be one or more of the following values: 'radius', 'snmp', 'syslog' or 'ldap'
- `--accessPoints` (array): Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put 'accessPoints' in the body when updating template networks. Also, an empty 'accessPoints' array will remove all previous static IP assignments


##### Example:
```
meraki batch wireless updateNetworkWirelessAlternateManagementInterface --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessAlternateManagementInterface --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessAlternateManagementInterface(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Billing


**Update the billing settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

##### Arguments
- `--networkId` (string): (required)
- `--currency` (string): The currency code of this node group's billing plans
- `--plans` (array): Array of billing plans in the node group. (Can configure a maximum of 5)


##### Example:
```
meraki batch wireless updateNetworkWirelessBilling --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessBilling --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessBilling(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Rf Profile


**Updates specified RF profile for this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--rfProfileId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique.
- `--clientBalancingEnabled` (boolean): Steers client to best available access point. Can be either true or false.
- `--minBitrateType` (string): Minimum bitrate can be set to either 'band' or 'ssid'.
- `--bandSelectionType` (string): Band selection can be set to either 'ssid' or 'ap'.
- `--apBandSettings` (object): Settings that will be enabled if selectionType is set to 'ap'.
- `--twoFourGhzSettings` (object): Settings related to 2.4Ghz band
- `--fiveGhzSettings` (object): Settings related to 5Ghz band
- `--transmission` (object): Settings related to radio transmission.
- `--perSsidSettings` (object): Per-SSID radio settings by number.


##### Example:
```
meraki batch wireless updateNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessRfProfile(networkId:str, rfProfileId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Settings


**Update the wireless settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

##### Arguments
- `--networkId` (string): (required)
- `--meshingEnabled` (boolean): Toggle for enabling or disabling meshing in a network
- `--ipv6BridgeEnabled` (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
- `--locationAnalyticsEnabled` (boolean): Toggle for enabling or disabling location analytics for your network
- `--upgradeStrategy` (string): The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
- `--ledLightsOn` (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)


##### Example:
```
meraki batch wireless updateNetworkWirelessSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid


**Update the attributes of an MR SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the SSID
- `--enabled` (boolean): Whether or not the SSID is enabled
- `--authMode` (string): The association control method for the SSID ('open', 'open-enhanced', 'psk', 'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius', '8021x-google', '8021x-localradius', 'ipsk-with-radius' or 'ipsk-without-radius')
- `--enterpriseAdminAccess` (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
- `--encryptionMode` (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
- `--psk` (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
- `--wpaEncryptionMode` (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security')
- `--dot11w` (object): The current setting for Protected Management Frames (802.11w).
- `--dot11r` (object): The current setting for 802.11r
- `--splashPage` (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain'). This attribute is not supported for template children.
- `--splashGuestSponsorDomains` (array): Array of valid sponsor email domains for sponsored guest splash type.
- `--oauth` (object): The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
- `--localRadius` (object): The current setting for Local Authentication, a built-in RADIUS server on the access point. Only valid if authMode is '8021x-localradius'.
- `--ldap` (object): The current setting for LDAP. Only valid if splashPage is 'Password-protected with LDAP'.
- `--activeDirectory` (object): The current setting for Active Directory. Only valid if splashPage is 'Password-protected with Active Directory'
- `--radiusServers` (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- `--radiusProxyEnabled` (boolean): If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.
- `--radiusTestingEnabled` (boolean): If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity 'meraki_8021x_test' to ensure that the RADIUS servers are reachable.
- `--radiusCalledStationId` (string): The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
- `--radiusAuthenticationNasId` (string): The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$:$VAP_NUM$).
- `--radiusServerTimeout` (integer): The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds).
- `--radiusServerAttemptsLimit` (integer): The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5).
- `--radiusFallbackEnabled` (boolean): Whether or not higher priority RADIUS servers should be retried after 60 seconds.
- `--radiusCoaEnabled` (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
- `--radiusFailoverPolicy` (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
- `--radiusLoadBalancingPolicy` (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
- `--radiusAccountingEnabled` (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- `--radiusAccountingServers` (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
- `--radiusAccountingInterimInterval` (integer): The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server.
- `--radiusAttributeForGroupPolicies` (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
- `--ipAssignmentMode` (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator' or 'VPN')
- `--useVlanTagging` (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--concentratorNetworkId` (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
- `--secondaryConcentratorNetworkId` (string): The secondary concentrator to use when the ipAssignmentMode is 'VPN'. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. ('disabled' represents no secondary concentrator.)
- `--disassociateClientsOnVpnFailover` (boolean): Disassociate clients when 'VPN' concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is 'VPN'.
- `--vlanId` (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
- `--defaultVlanId` (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--apTagsAndVlanIds` (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--walledGardenEnabled` (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
- `--walledGardenRanges` (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
- `--gre` (object): Ethernet over GRE settings
- `--radiusOverride` (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
- `--radiusGuestVlanEnabled` (boolean): Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- `--radiusGuestVlanId` (integer): VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- `--minBitrate` (number): The minimum bitrate in Mbps of this SSID in the default indoor RF profile. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
- `--bandSelection` (string): The client-serving radio frequencies of this SSID in the default indoor RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
- `--perClientBandwidthLimitUp` (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
- `--perClientBandwidthLimitDown` (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
- `--perSsidBandwidthLimitUp` (integer): The total upload bandwidth limit in Kbps. (0 represents no limit.)
- `--perSsidBandwidthLimitDown` (integer): The total download bandwidth limit in Kbps. (0 represents no limit.)
- `--lanIsolationEnabled` (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
- `--visible` (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
- `--availableOnAllAps` (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
- `--availabilityTags` (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
- `--mandatoryDhcpEnabled` (boolean): If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate.
- `--adultContentFilteringEnabled` (boolean): Boolean indicating whether or not adult content will be blocked
- `--dnsRewrite` (object): DNS servers rewrite settings
- `--speedBurst` (object): The SpeedBurst setting for this SSID'


##### Example:
```
meraki batch wireless updateNetworkWirelessSsid --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsid --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsid(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Bonjour Forwarding


**Update the bonjour forwarding setting and rules for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, Bonjour forwarding is enabled on this SSID.
- `--rules` (array): List of bonjour forwarding rules.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidBonjourForwarding --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidBonjourForwarding --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidBonjourForwarding(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Device Type Group Policies


**Update the device type group policies for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, the SSID device type group policies are enabled.
- `--deviceTypePolicies` (array): List of device type policies.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidDeviceTypeGroupPolicies --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidDeviceTypeGroupPolicies --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Eap Override


**Update the EAP overridden parameters for an SSID.**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--timeout` (integer): General EAP timeout in seconds.
- `--identity` (object): EAP settings for identity requests.
- `--maxRetries` (integer): Maximum number of general EAP retries.
- `--eapolKey` (object): EAPOL Key settings.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidEapOverride --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidEapOverride --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidEapOverride(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Firewall L3 Firewall Rules


**Update the L3 firewall rules of an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--rules` (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
- `--allowLanAccess` (boolean): Allow wireless client access to local LAN (boolean value - `--true` allows access and false denies access) (optional)


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidFirewallL3FirewallRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidFirewallL3FirewallRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidFirewallL3FirewallRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Firewall L7 Firewall Rules


**Update the L7 firewall rules of an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--rules` (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidFirewallL7FirewallRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidFirewallL7FirewallRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidFirewallL7FirewallRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Hotspot20


**Update the Hotspot 2.0 settings of an SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): Whether or not Hotspot 2.0 for this SSID is enabled
- `--operator` (object): Operator settings for this SSID
- `--venue` (object): Venue settings for this SSID
- `--networkAccessType` (string): The network type of this SSID ('Private network', 'Private network with guest access', 'Chargeable public network', 'Free public network', 'Personal device network', 'Emergency services only network', 'Test or experimental', 'Wildcard')
- `--domains` (array): An array of domain names
- `--roamConsortOis` (array): An array of roaming consortium OIs (hexadecimal number 3-5 octets in length)
- `--mccMncs` (array): An array of MCC/MNC pairs
- `--naiRealms` (array): An array of NAI realms


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidHotspot20 --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidHotspot20 --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidHotspot20(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Identity Psk


**Update an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--identityPskId` (string): (required)
- `--name` (string): The name of the Identity PSK
- `--passphrase` (string): The passphrase for client authentication
- `--groupPolicyId` (string): The group policy to be applied to clients


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidIdentityPsk(networkId:str, number:str, identityPskId:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Schedules


**Update the outage schedule for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, the SSID outage schedule is enabled.
- `--ranges` (array): List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.
- `--rangesInSeconds` (array): List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidSchedules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidSchedules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidSchedules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Splash Settings


**Modify the splash page settings for the given SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--splashUrl` (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
- `--useSplashUrl` (boolean): [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
- `--splashTimeout` (integer): Splash timeout in minutes. This will determine how often users will see the splash page.
- `--redirectUrl` (string): The custom redirect URL where the users will go after the splash page.
- `--useRedirectUrl` (boolean): The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
- `--welcomeMessage` (string): The welcome message for the users on the splash page.
- `--splashLogo` (object): The logo used in the splash page.
- `--splashImage` (object): The image used in the splash page.
- `--splashPrepaidFront` (object): The prepaid front image used in the splash page.
- `--blockAllTrafficBeforeSignOn` (boolean): How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
- `--controllerDisconnectionBehavior` (string): How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.
- `--allowSimultaneousLogins` (boolean): Whether or not to allow simultaneous logins from different devices.
- `--guestSponsorship` (object): Details associated with guest sponsored splash.
- `--billing` (object): Details associated with billing splash.
- `--sentryEnrollment` (object): Systems Manager sentry enrollment splash settings.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidSplashSettings --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidSplashSettings --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidSplashSettings(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Traffic Shaping Rules


**Update the traffic shaping settings for an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--trafficShapingEnabled` (boolean): Whether traffic shaping rules are applied to clients on your SSID.
- `--defaultRulesEnabled` (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- `--rules` (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.



##### Example:
```
meraki batch wireless updateNetworkWirelessSsidTrafficShapingRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidTrafficShapingRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidTrafficShapingRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Batch Wireless Update Network Wireless Ssid Vpn


**Update the VPN settings for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--concentrator` (object): The VPN concentrator settings for this SSID.
- `--splitTunnel` (object): The VPN split tunnel settings for this SSID.
- `--failover` (object): Secondary VPN concentrator settings. This is only used when two VPN concentrators are configured on the SSID.


##### Example:
```
meraki batch wireless updateNetworkWirelessSsidVpn --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki batch wireless updateNetworkWirelessSsidVpn --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidVpn(networkId:str, number:str, **kwargs):
    # Code
````

# Camera


----------------------------------------
## Camera Create Network Camera Quality Retention Profile


**Creates new quality retention profile for this network.**

https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique. This parameter is required.
- `--motionBasedRetentionEnabled` (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
- `--restrictedBandwidthModeEnabled` (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
- `--audioRecordingEnabled` (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
- `--cloudArchiveEnabled` (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
- `--motionDetectorVersion` (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
- `--scheduleId` (string): Schedule for which this camera will record video, or 'null' to always record.
- `--maxRetentionDays` (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days.
- `--videoSettings` (object): Video quality and resolution settings for all the camera models.


##### Example:
```
meraki camera createNetworkCameraQualityRetentionProfile --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera createNetworkCameraQualityRetentionProfile --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkCameraQualityRetentionProfile(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Create Network Camera Wireless Profile


**Creates a new camera wireless profile for this network.**

https://developer.cisco.com/meraki/api-v1/#!create-network-camera-wireless-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the camera wireless profile. This parameter is required.
- `--ssid` (object): The details of the SSID config.
- `--identity` (object): The identity of the wireless profile. Required for creating wireless profiles in 8021x-radius auth mode.


##### Example:
```
meraki camera createNetworkCameraWirelessProfile --networkId 'STRING' --name 'STRING' --ssid JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera createNetworkCameraWirelessProfile --networkId 'STRING' --name 'STRING' --ssid JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkCameraWirelessProfile(networkId:str, name:str, ssid:dict, **kwargs):
    # Code
````



----------------------------------------
## Camera Create Organization Camera Custom Analytics Artifact


**Create custom analytics artifact**

https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-custom-analytics-artifact

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Unique name of the artifact


##### Example:
```
meraki camera createOrganizationCameraCustomAnalyticsArtifact --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera createOrganizationCameraCustomAnalyticsArtifact --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationCameraCustomAnalyticsArtifact(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Delete Network Camera Quality Retention Profile


**Delete an existing quality retention profile for this network.**

https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile

##### Arguments
- `--networkId` (string): (required)
- `--qualityRetentionProfileId` (string): (required)


##### Example:
```
meraki camera deleteNetworkCameraQualityRetentionProfile --networkId 'STRING' --qualityRetentionProfileId 'STRING'
````

##### Method Code:
```python
def deleteNetworkCameraQualityRetentionProfile(networkId:str, qualityRetentionProfileId:str):
    # Code
````



----------------------------------------
## Camera Delete Network Camera Wireless Profile


**Delete an existing camera wireless profile for this network.**

https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-wireless-profile

##### Arguments
- `--networkId` (string): (required)
- `--wirelessProfileId` (string): (required)


##### Example:
```
meraki camera deleteNetworkCameraWirelessProfile --networkId 'STRING' --wirelessProfileId 'STRING'
````

##### Method Code:
```python
def deleteNetworkCameraWirelessProfile(networkId:str, wirelessProfileId:str):
    # Code
````



----------------------------------------
## Camera Delete Organization Camera Custom Analytics Artifact


**Delete Custom Analytics Artifact**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-camera-custom-analytics-artifact

##### Arguments
- `--organizationId` (string): (required)
- `--artifactId` (string): (required)


##### Example:
```
meraki camera deleteOrganizationCameraCustomAnalyticsArtifact --organizationId 'STRING' --artifactId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationCameraCustomAnalyticsArtifact(organizationId:str, artifactId:str):
    # Code
````



----------------------------------------
## Camera Generate Device Camera Snapshot


**Generate a snapshot of what the camera sees at the specified time and return a link to that image.**

https://developer.cisco.com/meraki/api-v1/#!generate-device-camera-snapshot

##### Arguments
- `--serial` (string): (required)
- `--timestamp` (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
- `--fullframe` (boolean): [optional] If set to "true" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.


##### Example:
```
meraki camera generateDeviceCameraSnapshot --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera generateDeviceCameraSnapshot --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def generateDeviceCameraSnapshot(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Get Device Camera Analytics Live


**Returns live state from camera of analytics zones**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-live

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraAnalyticsLive --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraAnalyticsLive(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Analytics Overview


**Returns an overview of aggregate analytics data for a timespan**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
- `--objectType` (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].


##### Example:
```
meraki camera getDeviceCameraAnalyticsOverview --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera getDeviceCameraAnalyticsOverview --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceCameraAnalyticsOverview(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Get Device Camera Analytics Recent


**Returns most recent record for analytics zones**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-recent

##### Arguments
- `--serial` (string): (required)
- `--objectType` (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].


##### Example:
```
meraki camera getDeviceCameraAnalyticsRecent --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera getDeviceCameraAnalyticsRecent --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceCameraAnalyticsRecent(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Get Device Camera Analytics Zone History


**Return historical records for analytic zones**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zone-history

##### Arguments
- `--serial` (string): (required)
- `--zoneId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
- `--objectType` (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].


##### Example:
```
meraki camera getDeviceCameraAnalyticsZoneHistory --serial 'STRING' --zoneId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera getDeviceCameraAnalyticsZoneHistory --serial 'STRING' --zoneId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceCameraAnalyticsZoneHistory(serial:str, zoneId:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Get Device Camera Analytics Zones


**Returns all configured analytic zones for this camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zones

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraAnalyticsZones --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraAnalyticsZones(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Custom Analytics


**Return custom analytics settings for a camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-custom-analytics

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraCustomAnalytics --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraCustomAnalytics(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Quality And Retention


**Returns quality and retention settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-quality-and-retention

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraQualityAndRetention --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraQualityAndRetention(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Sense


**Returns sense settings for a given camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraSense --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraSense(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Sense Object Detection Models


**Returns the MV Sense object detection model list for the given camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense-object-detection-models

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraSenseObjectDetectionModels --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraSenseObjectDetectionModels(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Video Link


**Returns video link to the specified camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-link

##### Arguments
- `--serial` (string): (required)
- `--timestamp` (string): [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.


##### Example:
```
meraki camera getDeviceCameraVideoLink --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera getDeviceCameraVideoLink --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceCameraVideoLink(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Get Device Camera Video Settings


**Returns video settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-settings

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraVideoSettings --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraVideoSettings(serial:str):
    # Code
````



----------------------------------------
## Camera Get Device Camera Wireless Profiles


**Returns wireless profile assigned to the given camera**

https://developer.cisco.com/meraki/api-v1/#!get-device-camera-wireless-profiles

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki camera getDeviceCameraWirelessProfiles --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCameraWirelessProfiles(serial:str):
    # Code
````



----------------------------------------
## Camera Get Network Camera Quality Retention Profile


**Retrieve a single quality retention profile**

https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile

##### Arguments
- `--networkId` (string): (required)
- `--qualityRetentionProfileId` (string): (required)


##### Example:
```
meraki camera getNetworkCameraQualityRetentionProfile --networkId 'STRING' --qualityRetentionProfileId 'STRING'
````

##### Method Code:
```python
def getNetworkCameraQualityRetentionProfile(networkId:str, qualityRetentionProfileId:str):
    # Code
````



----------------------------------------
## Camera Get Network Camera Quality Retention Profiles


**List the quality retention profiles for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki camera getNetworkCameraQualityRetentionProfiles --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCameraQualityRetentionProfiles(networkId:str):
    # Code
````



----------------------------------------
## Camera Get Network Camera Schedules


**Returns a list of all camera recording schedules.**

https://developer.cisco.com/meraki/api-v1/#!get-network-camera-schedules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki camera getNetworkCameraSchedules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCameraSchedules(networkId:str):
    # Code
````



----------------------------------------
## Camera Get Network Camera Wireless Profile


**Retrieve a single camera wireless profile.**

https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profile

##### Arguments
- `--networkId` (string): (required)
- `--wirelessProfileId` (string): (required)


##### Example:
```
meraki camera getNetworkCameraWirelessProfile --networkId 'STRING' --wirelessProfileId 'STRING'
````

##### Method Code:
```python
def getNetworkCameraWirelessProfile(networkId:str, wirelessProfileId:str):
    # Code
````



----------------------------------------
## Camera Get Network Camera Wireless Profiles


**List the camera wireless profiles for this network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profiles

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki camera getNetworkCameraWirelessProfiles --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCameraWirelessProfiles(networkId:str):
    # Code
````



----------------------------------------
## Camera Get Organization Camera Custom Analytics Artifact


**Get Custom Analytics Artifact**

https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifact

##### Arguments
- `--organizationId` (string): (required)
- `--artifactId` (string): (required)


##### Example:
```
meraki camera getOrganizationCameraCustomAnalyticsArtifact --organizationId 'STRING' --artifactId 'STRING'
````

##### Method Code:
```python
def getOrganizationCameraCustomAnalyticsArtifact(organizationId:str, artifactId:str):
    # Code
````



----------------------------------------
## Camera Get Organization Camera Custom Analytics Artifacts


**List Custom Analytics Artifacts**

https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifacts

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki camera getOrganizationCameraCustomAnalyticsArtifacts --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationCameraCustomAnalyticsArtifacts(organizationId:str):
    # Code
````



----------------------------------------
## Camera Get Organization Camera Onboarding Statuses


**Fetch onboarding status of cameras**

https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-onboarding-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--serials` (array): A list of serial numbers. The returned cameras will be filtered to only include these serials.
- `--networkIds` (array): A list of network IDs. The returned cameras will be filtered to only include these networks.


##### Example:
```
meraki camera getOrganizationCameraOnboardingStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera getOrganizationCameraOnboardingStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationCameraOnboardingStatuses(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Device Camera Custom Analytics


**Update custom analytics settings for a camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-custom-analytics

##### Arguments
- `--serial` (string): (required)
- `--enabled` (boolean): Enable custom analytics
- `--artifactId` (string): The ID of the custom analytics artifact
- `--parameters` (array): Parameters for the custom analytics workload


##### Example:
```
meraki camera updateDeviceCameraCustomAnalytics --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateDeviceCameraCustomAnalytics --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraCustomAnalytics(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Device Camera Quality And Retention


**Update quality and retention settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

##### Arguments
- `--serial` (string): (required)
- `--profileId` (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
- `--motionBasedRetentionEnabled` (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
- `--audioRecordingEnabled` (boolean): Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
- `--restrictedBandwidthModeEnabled` (boolean): Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
- `--quality` (string): Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
- `--resolution` (string): Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2058x2058', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
- `--motionDetectorVersion` (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.


##### Example:
```
meraki camera updateDeviceCameraQualityAndRetention --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateDeviceCameraQualityAndRetention --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraQualityAndRetention(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Device Camera Sense


**Update sense settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

##### Arguments
- `--serial` (string): (required)
- `--senseEnabled` (boolean): Boolean indicating if sense(license) is enabled(true) or disabled(false) on the camera
- `--mqttBrokerId` (string): The ID of the MQTT broker to be enabled on the camera. A value of null will disable MQTT on the camera
- `--audioDetection` (object): The details of the audio detection config.
- `--detectionModelId` (string): The ID of the object detection model


##### Example:
```
meraki camera updateDeviceCameraSense --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateDeviceCameraSense --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraSense(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Device Camera Video Settings


**Update video settings for the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

##### Arguments
- `--serial` (string): (required)
- `--externalRtspEnabled` (boolean): Boolean indicating if external rtsp stream is exposed


##### Example:
```
meraki camera updateDeviceCameraVideoSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateDeviceCameraVideoSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCameraVideoSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Device Camera Wireless Profiles


**Assign wireless profiles to the given camera**

https://developer.cisco.com/meraki/api-v1/#!update-device-camera-wireless-profiles

##### Arguments
- `--serial` (string): (required)
- `--ids` (object): The ids of the wireless profile to assign to the given camera


##### Example:
```
meraki camera updateDeviceCameraWirelessProfiles --serial 'STRING' --ids JSON_STRING
````

##### Method Code:
```python
def updateDeviceCameraWirelessProfiles(serial:str, ids:dict):
    # Code
````



----------------------------------------
## Camera Update Network Camera Quality Retention Profile


**Update an existing quality retention profile for this network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile

##### Arguments
- `--networkId` (string): (required)
- `--qualityRetentionProfileId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique.
- `--motionBasedRetentionEnabled` (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
- `--restrictedBandwidthModeEnabled` (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
- `--audioRecordingEnabled` (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
- `--cloudArchiveEnabled` (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
- `--motionDetectorVersion` (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
- `--scheduleId` (string): Schedule for which this camera will record video, or 'null' to always record.
- `--maxRetentionDays` (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days.
- `--videoSettings` (object): Video quality and resolution settings for all the camera models.


##### Example:
```
meraki camera updateNetworkCameraQualityRetentionProfile --networkId 'STRING' --qualityRetentionProfileId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateNetworkCameraQualityRetentionProfile --networkId 'STRING' --qualityRetentionProfileId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCameraQualityRetentionProfile(networkId:str, qualityRetentionProfileId:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Network Camera Wireless Profile


**Update an existing camera wireless profile in this network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-camera-wireless-profile

##### Arguments
- `--networkId` (string): (required)
- `--wirelessProfileId` (string): (required)
- `--name` (string): The name of the camera wireless profile.
- `--ssid` (object): The details of the SSID config.
- `--identity` (object): The identity of the wireless profile. Required for creating wireless profiles in 8021x-radius auth mode.


##### Example:
```
meraki camera updateNetworkCameraWirelessProfile --networkId 'STRING' --wirelessProfileId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateNetworkCameraWirelessProfile --networkId 'STRING' --wirelessProfileId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCameraWirelessProfile(networkId:str, wirelessProfileId:str, **kwargs):
    # Code
````



----------------------------------------
## Camera Update Organization Camera Onboarding Statuses


**Notify that credential handoff to camera has completed**

https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-onboarding-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--serial` (string): Serial of camera
- `--wirelessCredentialsSent` (boolean): Note whether credentials were sent successfully


##### Example:
```
meraki camera updateOrganizationCameraOnboardingStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki camera updateOrganizationCameraOnboardingStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationCameraOnboardingStatuses(organizationId:str, **kwargs):
    # Code
````

# Cellular Gateway


----------------------------------------
## Cellular Gateway Get Device Cellular Gateway Lan


**Show the LAN Settings of a MG**

https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki cellularGateway getDeviceCellularGatewayLan --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCellularGatewayLan(serial:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Device Cellular Gateway Port Forwarding Rules


**Returns the port forwarding rules for a single MG.**

https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki cellularGateway getDeviceCellularGatewayPortForwardingRules --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCellularGatewayPortForwardingRules(serial:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Network Cellular Gateway Connectivity Monitoring Destinations


**Return the connectivity testing destinations for an MG network**

https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki cellularGateway getNetworkCellularGatewayConnectivityMonitoringDestinations --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCellularGatewayConnectivityMonitoringDestinations(networkId:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Network Cellular Gateway Dhcp


**List common DHCP settings of MGs**

https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki cellularGateway getNetworkCellularGatewayDhcp --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCellularGatewayDhcp(networkId:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Network Cellular Gateway Subnet Pool


**Return the subnet pool and mask configured for MGs in the network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki cellularGateway getNetworkCellularGatewaySubnetPool --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCellularGatewaySubnetPool(networkId:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Network Cellular Gateway Uplink


**Returns the uplink settings for your MG network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki cellularGateway getNetworkCellularGatewayUplink --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkCellularGatewayUplink(networkId:str):
    # Code
````



----------------------------------------
## Cellular Gateway Get Organization Cellular Gateway Uplink Statuses


**List the uplink status of every Meraki MG cellular gateway in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- `--serials` (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- `--iccids` (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.


##### Example:
```
meraki cellularGateway getOrganizationCellularGatewayUplinkStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway getOrganizationCellularGatewayUplinkStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationCellularGatewayUplinkStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Device Cellular Gateway Lan


**Update the LAN Settings for a single MG.**

https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

##### Arguments
- `--serial` (string): (required)
- `--reservedIpRanges` (array): list of all reserved IP ranges for a single MG
- `--fixedIpAssignments` (array): list of all fixed IP assignments for a single MG


##### Example:
```
meraki cellularGateway updateDeviceCellularGatewayLan --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateDeviceCellularGatewayLan --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCellularGatewayLan(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Device Cellular Gateway Port Forwarding Rules


**Updates the port forwarding rules for a single MG.**

https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

##### Arguments
- `--serial` (string): (required)
- `--rules` (array): An array of port forwarding params


##### Example:
```
meraki cellularGateway updateDeviceCellularGatewayPortForwardingRules --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateDeviceCellularGatewayPortForwardingRules --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCellularGatewayPortForwardingRules(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Network Cellular Gateway Connectivity Monitoring Destinations


**Update the connectivity testing destinations for an MG network**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

##### Arguments
- `--networkId` (string): (required)
- `--destinations` (array): The list of connectivity monitoring destinations


##### Example:
```
meraki cellularGateway updateNetworkCellularGatewayConnectivityMonitoringDestinations --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateNetworkCellularGatewayConnectivityMonitoringDestinations --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayConnectivityMonitoringDestinations(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Network Cellular Gateway Dhcp


**Update common DHCP settings of MGs**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

##### Arguments
- `--networkId` (string): (required)
- `--dhcpLeaseTime` (string): DHCP Lease time for all MG of the network. Possible values are '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
- `--dnsNameservers` (string): DNS name servers mode for all MG of the network. Possible values are: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
- `--dnsCustomNameservers` (array): list of fixed IPs representing the the DNS Name servers when the mode is 'custom'


##### Example:
```
meraki cellularGateway updateNetworkCellularGatewayDhcp --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateNetworkCellularGatewayDhcp --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayDhcp(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Network Cellular Gateway Subnet Pool


**Update the subnet pool and mask configuration for MGs in the network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

##### Arguments
- `--networkId` (string): (required)
- `--mask` (integer): Mask used for the subnet of all MGs in  this network.
- `--cidr` (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.


##### Example:
```
meraki cellularGateway updateNetworkCellularGatewaySubnetPool --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateNetworkCellularGatewaySubnetPool --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewaySubnetPool(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Cellular Gateway Update Network Cellular Gateway Uplink


**Updates the uplink settings for your MG network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

##### Arguments
- `--networkId` (string): (required)
- `--bandwidthLimits` (object): The bandwidth settings for the 'cellular' uplink


##### Example:
```
meraki cellularGateway updateNetworkCellularGatewayUplink --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki cellularGateway updateNetworkCellularGatewayUplink --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkCellularGatewayUplink(networkId:str, **kwargs):
    # Code
````

# Devices


----------------------------------------
## Devices Blink Device Leds


**Blink the LEDs on a device**

https://developer.cisco.com/meraki/api-v1/#!blink-device-leds

##### Arguments
- `--serial` (string): (required)
- `--duration` (integer): The duration in seconds. Must be between 5 and 120. Default is 20 seconds
- `--period` (integer): The period in milliseconds. Must be between 100 and 1000. Default is 160 milliseconds
- `--duty` (integer): The duty cycle as the percent active. Must be between 10 and 90. Default is 50.


##### Example:
```
meraki devices blinkDeviceLeds --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices blinkDeviceLeds --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def blinkDeviceLeds(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Create Device Live Tools Ping


**Enqueue a job to ping a target host from the device**

https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping

##### Arguments
- `--serial` (string): (required)
- `--target` (string): FQDN, IPv4 or IPv6 address
- `--count` (integer): Count parameter to pass to ping. [1..5], default 5


##### Example:
```
meraki devices createDeviceLiveToolsPing --serial 'STRING' --target 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices createDeviceLiveToolsPing --serial 'STRING' --target 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceLiveToolsPing(serial:str, target:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Create Device Live Tools Ping Device


**Enqueue a job to check connectivity status to the device**

https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping-device

##### Arguments
- `--serial` (string): (required)
- `--count` (integer): Count parameter to pass to ping. [1..5], default 5


##### Example:
```
meraki devices createDeviceLiveToolsPingDevice --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices createDeviceLiveToolsPingDevice --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceLiveToolsPingDevice(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Get Device


**Return a single device**

https://developer.cisco.com/meraki/api-v1/#!get-device

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki devices getDevice --serial 'STRING'
````

##### Method Code:
```python
def getDevice(serial:str):
    # Code
````



----------------------------------------
## Devices Get Device Cellular Sims


**Return the SIM and APN configurations for a cellular device.**

https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-sims

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki devices getDeviceCellularSims --serial 'STRING'
````

##### Method Code:
```python
def getDeviceCellularSims(serial:str):
    # Code
````



----------------------------------------
## Devices Get Device Clients


**List the clients of a device, up to a maximum of a month ago**

https://developer.cisco.com/meraki/api-v1/#!get-device-clients

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki devices getDeviceClients --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices getDeviceClients --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceClients(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Get Device Live Tools Ping


**Return a ping job**

https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping

##### Arguments
- `--serial` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki devices getDeviceLiveToolsPing --serial 'STRING' --id 'STRING'
````

##### Method Code:
```python
def getDeviceLiveToolsPing(serial:str, id:str):
    # Code
````



----------------------------------------
## Devices Get Device Live Tools Ping Device


**Return a ping device job**

https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping-device

##### Arguments
- `--serial` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki devices getDeviceLiveToolsPingDevice --serial 'STRING' --id 'STRING'
````

##### Method Code:
```python
def getDeviceLiveToolsPingDevice(serial:str, id:str):
    # Code
````



----------------------------------------
## Devices Get Device Lldp Cdp


**List LLDP and CDP information for a device**

https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki devices getDeviceLldpCdp --serial 'STRING'
````

##### Method Code:
```python
def getDeviceLldpCdp(serial:str):
    # Code
````



----------------------------------------
## Devices Get Device Loss And Latency History


**Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.**

https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history

##### Arguments
- `--serial` (string): (required)
- `--ip` (string): The destination IP used to obtain the requested stats. This is required.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
- `--uplink` (string): The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.


##### Example:
```
meraki devices getDeviceLossAndLatencyHistory --serial 'STRING' --ip 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices getDeviceLossAndLatencyHistory --serial 'STRING' --ip 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceLossAndLatencyHistory(serial:str, ip:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Get Device Management Interface


**Return the management interface settings for a device**

https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki devices getDeviceManagementInterface --serial 'STRING'
````

##### Method Code:
```python
def getDeviceManagementInterface(serial:str):
    # Code
````



----------------------------------------
## Devices Reboot Device


**Reboot a device**

https://developer.cisco.com/meraki/api-v1/#!reboot-device

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki devices rebootDevice --serial 'STRING'
````

##### Method Code:
```python
def rebootDevice(serial:str):
    # Code
````



----------------------------------------
## Devices Update Device


**Update the attributes of a device**

https://developer.cisco.com/meraki/api-v1/#!update-device

##### Arguments
- `--serial` (string): (required)
- `--name` (string): The name of a device
- `--tags` (array): The list of tags of a device
- `--lat` (number): The latitude of a device
- `--lng` (number): The longitude of a device
- `--address` (string): The address of a device
- `--notes` (string): The notes for the device. String. Limited to 255 characters.
- `--moveMapMarker` (boolean): Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
- `--switchProfileId` (string): The ID of a switch profile to bind to the device (for available switch profiles, see the 'Switch Profiles' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch profile, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
- `--floorPlanId` (string): The floor plan to associate to this device. null disassociates the device from the floorplan.


##### Example:
```
meraki devices updateDevice --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices updateDevice --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDevice(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Update Device Cellular Sims


**Updates the SIM and APN configurations for a cellular device.**

https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-sims

##### Arguments
- `--serial` (string): (required)
- `--sims` (array): List of SIMs. If a SIM was previously configured and not specified in this request, it will remain unchanged.
- `--simFailover` (object): SIM Failover settings.


##### Example:
```
meraki devices updateDeviceCellularSims --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices updateDeviceCellularSims --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceCellularSims(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Devices Update Device Management Interface


**Update the management interface settings for a device**

https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface

##### Arguments
- `--serial` (string): (required)
- `--wan1` (object): WAN 1 settings
- `--wan2` (object): WAN 2 settings (only for MX devices)


##### Example:
```
meraki devices updateDeviceManagementInterface --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki devices updateDeviceManagementInterface --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceManagementInterface(serial:str, **kwargs):
    # Code
````

# Insight


----------------------------------------
## Insight Create Organization Insight Monitored Media Server


**Add a media server to be monitored for this organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the VoIP provider
- `--address` (string): The IP address (IPv4 only) or hostname of the media server to monitor
- `--bestEffortMonitoringEnabled` (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.


##### Example:
```
meraki insight createOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --name 'STRING' --address 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki insight createOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --name 'STRING' --address 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationInsightMonitoredMediaServer(organizationId:str, name:str, address:str, **kwargs):
    # Code
````



----------------------------------------
## Insight Delete Organization Insight Monitored Media Server


**Delete a monitored media server from this organization**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--monitoredMediaServerId` (string): (required)


##### Example:
```
meraki insight deleteOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationInsightMonitoredMediaServer(organizationId:str, monitoredMediaServerId:str):
    # Code
````



----------------------------------------
## Insight Get Network Insight Application Health By Time


**Get application health by time**

https://developer.cisco.com/meraki/api-v1/#!get-network-insight-application-health-by-time

##### Arguments
- `--networkId` (string): (required)
- `--applicationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.


##### Example:
```
meraki insight getNetworkInsightApplicationHealthByTime --networkId 'STRING' --applicationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki insight getNetworkInsightApplicationHealthByTime --networkId 'STRING' --applicationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkInsightApplicationHealthByTime(networkId:str, applicationId:str, **kwargs):
    # Code
````



----------------------------------------
## Insight Get Organization Insight Applications


**List all Insight tracked applications**

https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-applications

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki insight getOrganizationInsightApplications --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationInsightApplications(organizationId:str):
    # Code
````



----------------------------------------
## Insight Get Organization Insight Monitored Media Server


**Return a monitored media server for this organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--monitoredMediaServerId` (string): (required)


##### Example:
```
meraki insight getOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING'
````

##### Method Code:
```python
def getOrganizationInsightMonitoredMediaServer(organizationId:str, monitoredMediaServerId:str):
    # Code
````



----------------------------------------
## Insight Get Organization Insight Monitored Media Servers


**List the monitored media servers for this organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki insight getOrganizationInsightMonitoredMediaServers --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationInsightMonitoredMediaServers(organizationId:str):
    # Code
````



----------------------------------------
## Insight Update Organization Insight Monitored Media Server


**Update a monitored media server for this organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

##### Arguments
- `--organizationId` (string): (required)
- `--monitoredMediaServerId` (string): (required)
- `--name` (string): The name of the VoIP provider
- `--address` (string): The IP address (IPv4 only) or hostname of the media server to monitor
- `--bestEffortMonitoringEnabled` (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.


##### Example:
```
meraki insight updateOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki insight updateOrganizationInsightMonitoredMediaServer --organizationId 'STRING' --monitoredMediaServerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationInsightMonitoredMediaServer(organizationId:str, monitoredMediaServerId:str, **kwargs):
    # Code
````

# Licensing


----------------------------------------
## Licensing Get Organization Licensing Coterm Licenses


**List the licenses in a coterm organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--invalidated` (boolean): Filter for licenses that are invalidated
- `--expired` (boolean): Filter for licenses that are expired


##### Example:
```
meraki licensing getOrganizationLicensingCotermLicenses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki licensing getOrganizationLicensingCotermLicenses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationLicensingCotermLicenses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Licensing Move Organization Licensing Coterm Licenses


**Moves a license to a different organization (coterm only)**

https://developer.cisco.com/meraki/api-v1/#!move-organization-licensing-coterm-licenses

##### Arguments
- `--organizationId` (string): (required)
- `--destination` (object): Destination data for the license move
- `--licenses` (array): The list of licenses to move


##### Example:
```
meraki licensing moveOrganizationLicensingCotermLicenses --organizationId 'STRING' --destination JSON_STRING --licenses ITEM
````

##### Method Code:
```python
def moveOrganizationLicensingCotermLicenses(organizationId:str, destination:dict, licenses:list):
    # Code
````

# Networks


----------------------------------------
## Networks Bind Network


**Bind a network to a template.**

https://developer.cisco.com/meraki/api-v1/#!bind-network

##### Arguments
- `--networkId` (string): (required)
- `--configTemplateId` (string): The ID of the template to which the network should be bound.
- `--autoBind` (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.


##### Example:
```
meraki networks bindNetwork --networkId 'STRING' --configTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks bindNetwork --networkId 'STRING' --configTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def bindNetwork(networkId:str, configTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Claim Network Devices


**Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)**

https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

##### Arguments
- `--networkId` (string): (required)
- `--serials` (array): A list of serials of devices to claim


##### Example:
```
meraki networks claimNetworkDevices --networkId 'STRING' --serials ITEM
````

##### Method Code:
```python
def claimNetworkDevices(networkId:str, serials:list):
    # Code
````



----------------------------------------
## Networks Create Network Firmware Upgrades Rollback


**Rollback a Firmware Upgrade For A Network**

https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

##### Arguments
- `--networkId` (string): (required)
- `--reasons` (array): Reasons for the rollback
- `--product` (string): Product type to rollback (if the network is a combined network)
- `--time` (string): Scheduled time for the rollback
- `--toVersion` (object): Version to downgrade to (if the network has firmware flexibility)


##### Example:
```
meraki networks createNetworkFirmwareUpgradesRollback --networkId 'STRING' --reasons ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkFirmwareUpgradesRollback --networkId 'STRING' --reasons ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFirmwareUpgradesRollback(networkId:str, reasons:list, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Firmware Upgrades Staged Event


**Create a Staged Upgrade Event for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-event

##### Arguments
- `--networkId` (string): (required)
- `--stages` (array): All firmware upgrade stages in the network with their start time.
- `--products` (object): Contains firmware upgrade version information


##### Example:
```
meraki networks createNetworkFirmwareUpgradesStagedEvent --networkId 'STRING' --stages ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkFirmwareUpgradesStagedEvent --networkId 'STRING' --stages ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFirmwareUpgradesStagedEvent(networkId:str, stages:list, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Firmware Upgrades Staged Group


**Create a Staged Upgrade Group for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--isDefault` (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
- `--description` (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--assignedDevices` (object): The devices and Switch Stacks assigned to the Group


##### Example:
```
meraki networks createNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --name 'STRING' --isDefault --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --name 'STRING' --isDefault --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFirmwareUpgradesStagedGroup(networkId:str, name:str, isDefault:bool, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Floor Plan


**Upload a floor plan**

https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of your floor plan.
- `--imageContents` (string): The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
- `--center` (object): The longitude and latitude of the center of your floor plan. The 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
- `--bottomLeftCorner` (object): The longitude and latitude of the bottom left corner of your floor plan.
- `--bottomRightCorner` (object): The longitude and latitude of the bottom right corner of your floor plan.
- `--topLeftCorner` (object): The longitude and latitude of the top left corner of your floor plan.
- `--topRightCorner` (object): The longitude and latitude of the top right corner of your floor plan.


##### Example:
```
meraki networks createNetworkFloorPlan --networkId 'STRING' --name 'STRING' --imageContents 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkFloorPlan --networkId 'STRING' --name 'STRING' --imageContents 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkFloorPlan(networkId:str, name:str, imageContents:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Group Policy


**Create a group policy**

https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name for your group policy. Required.
- `--scheduling` (object):     The schedule for the group policy. Schedules are applied to days of the week.

- `--bandwidth` (object):     The bandwidth settings for clients bound to your group policy.

- `--firewallAndTrafficShaping` (object):     The firewall and traffic shaping rules and settings for your policy.

- `--contentFiltering` (object): The content filtering settings for your group policy
- `--splashAuthSettings` (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- `--vlanTagging` (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- `--bonjourForwarding` (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.


##### Example:
```
meraki networks createNetworkGroupPolicy --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkGroupPolicy --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkGroupPolicy(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Meraki Auth User


**Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)**

https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--email` (string): Email address of the user
- `--authorizations` (array): Authorization zones and expiration dates for the user.
- `--name` (string): Name of the user. Only required If the user is not a Dashboard administrator.
- `--password` (string): The password for this user account. Only required If the user is not a Dashboard administrator.
- `--accountType` (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for wired networks. Defaults to '802.1X'.
- `--emailPasswordToUser` (boolean): Whether or not Meraki should email the password to user. Default is false.
- `--isAdmin` (boolean): Whether or not the user is a Dashboard administrator.


##### Example:
```
meraki networks createNetworkMerakiAuthUser --networkId 'STRING' --email 'STRING' --authorizations ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkMerakiAuthUser --networkId 'STRING' --email 'STRING' --authorizations ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkMerakiAuthUser(networkId:str, email:str, authorizations:list, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Mqtt Broker


**Add an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the MQTT broker.
- `--host` (string): Host name/IP address where the MQTT broker runs.
- `--port` (integer): Host port though which the MQTT broker can be reached.
- `--security` (object): Security settings of the MQTT broker.
- `--authentication` (object): Authentication settings of the MQTT broker


##### Example:
```
meraki networks createNetworkMqttBroker --networkId 'STRING' --name 'STRING' --host 'STRING' --port INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkMqttBroker --networkId 'STRING' --name 'STRING' --host 'STRING' --port INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkMqttBroker(networkId:str, name:str, host:str, port:int, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Pii Request


**Submit a new delete or restrict processing PII request**

https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

##### Arguments
- `--networkId` (string): (required)
- `--type` (string): One of "delete" or "restrict processing"
- `--datasets` (array): The datasets related to the provided key that should be deleted. Only applies to "delete" requests. The value "all" will be expanded to all datasets applicable to this type. The datasets by applicable to each type are: mac (usage, events, traffic), email (users, loginAttempts), username (users, loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device), smUserId (user)
- `--username` (string): The username of a network log in. Only applies to "delete" requests.
- `--email` (string): The email of a network user account. Only applies to "delete" requests.
- `--mac` (string): The MAC of a network client device. Applies to both "restrict processing" and "delete" requests.
- `--smDeviceId` (string): The sm_device_id of a Systems Manager device. The only way to "restrict processing" or "delete" a Systems Manager device. Must include "device" in the dataset for a "delete" request to destroy the device.
- `--smUserId` (string): The sm_user_id of a Systems Manager user. The only way to "restrict processing" or "delete" a Systems Manager user. Must include "user" in the dataset for a "delete" request to destroy the user.


##### Example:
```
meraki networks createNetworkPiiRequest --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkPiiRequest --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkPiiRequest(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Webhooks Http Server


**Add an HTTP server to a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): A name for easy reference to the HTTP server
- `--url` (string): The URL of the HTTP server. Once set, cannot be updated.
- `--sharedSecret` (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
- `--payloadTemplate` (object): The payload template to use when posting data to the HTTP server.


##### Example:
```
meraki networks createNetworkWebhooksHttpServer --networkId 'STRING' --name 'STRING' --url 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkWebhooksHttpServer --networkId 'STRING' --name 'STRING' --url 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWebhooksHttpServer(networkId:str, name:str, url:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Webhooks Payload Template


**Create a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new template
- `--body` (string): The liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
- `--headers` (array): The liquid template used with the webhook headers.
- `--bodyFile` (string): A file containing liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
- `--headersFile` (string): A file containing the liquid template used with the webhook headers.


##### Example:
```
meraki networks createNetworkWebhooksPayloadTemplate --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkWebhooksPayloadTemplate --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWebhooksPayloadTemplate(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Create Network Webhooks Webhook Test


**Send a test webhook for a network**

https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

##### Arguments
- `--networkId` (string): (required)
- `--url` (string): The URL where the test webhook will be sent
- `--sharedSecret` (string): The shared secret the test webhook will send. Optional. Defaults to an empty string.
- `--payloadTemplateId` (string): The ID of the payload template of the test webhook. Defaults to the HTTP server's template ID if one exists for the given URL, or Generic template ID otherwise
- `--payloadTemplateName` (string): The name of the payload template.
- `--alertTypeId` (string): The type of alert which the test webhook will send. Optional. Defaults to power_supply_down.


##### Example:
```
meraki networks createNetworkWebhooksWebhookTest --networkId 'STRING' --url 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks createNetworkWebhooksWebhookTest --networkId 'STRING' --url 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWebhooksWebhookTest(networkId:str, url:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Defer Network Firmware Upgrades Staged Events


**Postpone by 1 week all pending staged upgrade stages for a network**

https://developer.cisco.com/meraki/api-v1/#!defer-network-firmware-upgrades-staged-events

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks deferNetworkFirmwareUpgradesStagedEvents --networkId 'STRING'
````

##### Method Code:
```python
def deferNetworkFirmwareUpgradesStagedEvents(networkId:str):
    # Code
````



----------------------------------------
## Networks Delete Network


**Delete a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks deleteNetwork --networkId 'STRING'
````

##### Method Code:
```python
def deleteNetwork(networkId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Firmware Upgrades Staged Group


**Delete a Staged Upgrade Group**

https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--groupId` (string): (required)


##### Example:
```
meraki networks deleteNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --groupId 'STRING'
````

##### Method Code:
```python
def deleteNetworkFirmwareUpgradesStagedGroup(networkId:str, groupId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Floor Plan


**Destroy a floor plan**

https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--floorPlanId` (string): (required)


##### Example:
```
meraki networks deleteNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING'
````

##### Method Code:
```python
def deleteNetworkFloorPlan(networkId:str, floorPlanId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Group Policy


**Delete a group policy**

https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--groupPolicyId` (string): (required)


##### Example:
```
meraki networks deleteNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING'
````

##### Method Code:
```python
def deleteNetworkGroupPolicy(networkId:str, groupPolicyId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Meraki Auth User


**Deauthorize a user**

https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--merakiAuthUserId` (string): (required)


##### Example:
```
meraki networks deleteNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING'
````

##### Method Code:
```python
def deleteNetworkMerakiAuthUser(networkId:str, merakiAuthUserId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Mqtt Broker


**Delete an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--mqttBrokerId` (string): (required)


##### Example:
```
meraki networks deleteNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING'
````

##### Method Code:
```python
def deleteNetworkMqttBroker(networkId:str, mqttBrokerId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Pii Request


**Delete a restrict processing PII request**

https://developer.cisco.com/meraki/api-v1/#!delete-network-pii-request

##### Arguments
- `--networkId` (string): (required)
- `--requestId` (string): (required)


##### Example:
```
meraki networks deleteNetworkPiiRequest --networkId 'STRING' --requestId 'STRING'
````

##### Method Code:
```python
def deleteNetworkPiiRequest(networkId:str, requestId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Webhooks Http Server


**Delete an HTTP server from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server

##### Arguments
- `--networkId` (string): (required)
- `--httpServerId` (string): (required)


##### Example:
```
meraki networks deleteNetworkWebhooksHttpServer --networkId 'STRING' --httpServerId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWebhooksHttpServer(networkId:str, httpServerId:str):
    # Code
````



----------------------------------------
## Networks Delete Network Webhooks Payload Template


**Destroy a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--payloadTemplateId` (string): (required)


##### Example:
```
meraki networks deleteNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWebhooksPayloadTemplate(networkId:str, payloadTemplateId:str):
    # Code
````



----------------------------------------
## Networks Get Network


**Return a network**

https://developer.cisco.com/meraki/api-v1/#!get-network

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetwork --networkId 'STRING'
````

##### Method Code:
```python
def getNetwork(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Alerts History


**Return the alert history for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-history

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki networks getNetworkAlertsHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkAlertsHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkAlertsHistory(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Alerts Settings


**Return the alert configuration for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkAlertsSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkAlertsSettings(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Bluetooth Client


**Return a Bluetooth client**

https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

##### Arguments
- `--networkId` (string): (required)
- `--bluetoothClientId` (string): (required)
- `--includeConnectivityHistory` (boolean): Include the connectivity history for this client
- `--connectivityHistoryTimespan` (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.


##### Example:
```
meraki networks getNetworkBluetoothClient --networkId 'STRING' --bluetoothClientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkBluetoothClient --networkId 'STRING' --bluetoothClientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkBluetoothClient(networkId:str, bluetoothClientId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Bluetooth Clients


**List the Bluetooth clients seen by APs in this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--includeConnectivityHistory` (boolean): Include the connectivity history for this client


##### Example:
```
meraki networks getNetworkBluetoothClients --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkBluetoothClients --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkBluetoothClients(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Client


**Return the client associated with the given identifier**

https://developer.cisco.com/meraki/api-v1/#!get-network-client

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)


##### Example:
```
meraki networks getNetworkClient --networkId 'STRING' --clientId 'STRING'
````

##### Method Code:
```python
def getNetworkClient(networkId:str, clientId:str):
    # Code
````



----------------------------------------
## Networks Get Network Client Policy


**Return the policy assigned to a client on the network**

https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)


##### Example:
```
meraki networks getNetworkClientPolicy --networkId 'STRING' --clientId 'STRING'
````

##### Method Code:
```python
def getNetworkClientPolicy(networkId:str, clientId:str):
    # Code
````



----------------------------------------
## Networks Get Network Client Splash Authorization Status


**Return the splash authorization for a client, for each SSID they've associated with through splash**

https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)


##### Example:
```
meraki networks getNetworkClientSplashAuthorizationStatus --networkId 'STRING' --clientId 'STRING'
````

##### Method Code:
```python
def getNetworkClientSplashAuthorizationStatus(networkId:str, clientId:str):
    # Code
````



----------------------------------------
## Networks Get Network Client Traffic History


**Return the client's network traffic data over time**

https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki networks getNetworkClientTrafficHistory --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClientTrafficHistory --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClientTrafficHistory(networkId:str, clientId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Client Usage History


**Return the client's daily usage history**

https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)


##### Example:
```
meraki networks getNetworkClientUsageHistory --networkId 'STRING' --clientId 'STRING'
````

##### Method Code:
```python
def getNetworkClientUsageHistory(networkId:str, clientId:str):
    # Code
````



----------------------------------------
## Networks Get Network Clients


**List the clients that have used this network in the timespan**

https://developer.cisco.com/meraki/api-v1/#!get-network-clients

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--statuses` (array): Filters clients based on status. Can be one of 'Online' or 'Offline'.
- `--ip` (string): Filters clients based on a partial or full match for the ip address field.
- `--ip6` (string): Filters clients based on a partial or full match for the ip6 address field.
- `--ip6Local` (string): Filters clients based on a partial or full match for the ip6Local address field.
- `--mac` (string): Filters clients based on a partial or full match for the mac address field.
- `--os` (string): Filters clients based on a partial or full match for the os (operating system) field.
- `--description` (string): Filters clients based on a partial or full match for the description field.
- `--vlan` (string): Filters clients based on the full match for the VLAN field.
- `--recentDeviceConnections` (array): Filters clients based on recent connection type. Can be one of 'Wired' or 'Wireless'.


##### Example:
```
meraki networks getNetworkClients --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClients --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClients(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Clients Application Usage


**Return the application usage data for clients**

https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

##### Arguments
- `--networkId` (string): (required)
- `--clients` (string): A list of client keys, MACs or IPs separated by comma.
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--ssidNumber` (integer): An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki networks getNetworkClientsApplicationUsage --networkId 'STRING' --clients 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClientsApplicationUsage --networkId 'STRING' --clients 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClientsApplicationUsage(networkId:str, clients:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Clients Bandwidth Usage History


**Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.**

https://developer.cisco.com/meraki/api-v1/#!get-network-clients-bandwidth-usage-history

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki networks getNetworkClientsBandwidthUsageHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClientsBandwidthUsageHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClientsBandwidthUsageHistory(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Clients Overview


**Return overview statistics for network clients**

https://developer.cisco.com/meraki/api-v1/#!get-network-clients-overview

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.


##### Example:
```
meraki networks getNetworkClientsOverview --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClientsOverview --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClientsOverview(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Clients Usage Histories


**Return the usage histories for clients**

https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

##### Arguments
- `--networkId` (string): (required)
- `--clients` (string): A list of client keys, MACs or IPs separated by comma.
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--ssidNumber` (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki networks getNetworkClientsUsageHistories --networkId 'STRING' --clients 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkClientsUsageHistories --networkId 'STRING' --clients 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkClientsUsageHistories(networkId:str, clients:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Devices


**List the devices in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-devices

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkDevices --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkDevices(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Events


**List the events for the network**

https://developer.cisco.com/meraki/api-v1/#!get-network-events

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" or "prev" (default) page
- `--event_log_end_time` (string): ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to retrieve events within a time window
- `--productType` (string): The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
- `--includedEventTypes` (array): A list of event types. The returned events will be filtered to only include events with these types.
- `--excludedEventTypes` (array): A list of event types. The returned events will be filtered to exclude events with these types.
- `--deviceMac` (string): The MAC address of the Meraki device which the list of events will be filtered with
- `--deviceSerial` (string): The serial of the Meraki device which the list of events will be filtered with
- `--deviceName` (string): The name of the Meraki device which the list of events will be filtered with
- `--clientIp` (string): The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
- `--clientMac` (string): The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
- `--clientName` (string): The name, or partial name, of the client which the list of events will be filtered with
- `--smDeviceMac` (string): The MAC address of the Systems Manager device which the list of events will be filtered with
- `--smDeviceName` (string): The name of the Systems Manager device which the list of events will be filtered with
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki networks getNetworkEvents --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkEvents --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkEvents(networkId:str, total_pages=1, direction='prev', event_log_end_time=None, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Events Event Types


**List the event type to human-readable description**

https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkEventsEventTypes --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkEventsEventTypes(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Firmware Upgrades


**Get firmware upgrade information for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkFirmwareUpgrades --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkFirmwareUpgrades(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Firmware Upgrades Staged Events


**Get the Staged Upgrade Event from a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-events

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkFirmwareUpgradesStagedEvents --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkFirmwareUpgradesStagedEvents(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Firmware Upgrades Staged Group


**Get a Staged Upgrade Group from a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--groupId` (string): (required)


##### Example:
```
meraki networks getNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --groupId 'STRING'
````

##### Method Code:
```python
def getNetworkFirmwareUpgradesStagedGroup(networkId:str, groupId:str):
    # Code
````



----------------------------------------
## Networks Get Network Firmware Upgrades Staged Groups


**List of Staged Upgrade Groups in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-groups

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkFirmwareUpgradesStagedGroups --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkFirmwareUpgradesStagedGroups(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Firmware Upgrades Staged Stages


**Order of Staged Upgrade Groups in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades-staged-stages

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkFirmwareUpgradesStagedStages --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkFirmwareUpgradesStagedStages(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Floor Plan


**Find a floor plan by ID**

https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--floorPlanId` (string): (required)


##### Example:
```
meraki networks getNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING'
````

##### Method Code:
```python
def getNetworkFloorPlan(networkId:str, floorPlanId:str):
    # Code
````



----------------------------------------
## Networks Get Network Floor Plans


**List the floor plans that belong to your network**

https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkFloorPlans --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkFloorPlans(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Group Policies


**List the group policies in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkGroupPolicies --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkGroupPolicies(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Group Policy


**Display a group policy**

https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--groupPolicyId` (string): (required)


##### Example:
```
meraki networks getNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING'
````

##### Method Code:
```python
def getNetworkGroupPolicy(networkId:str, groupPolicyId:str):
    # Code
````



----------------------------------------
## Networks Get Network Health Alerts


**Return all global alerts on this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-health-alerts

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkHealthAlerts --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkHealthAlerts(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Meraki Auth User


**Return the Meraki Auth splash guest, RADIUS, or client VPN user**

https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--merakiAuthUserId` (string): (required)


##### Example:
```
meraki networks getNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING'
````

##### Method Code:
```python
def getNetworkMerakiAuthUser(networkId:str, merakiAuthUserId:str):
    # Code
````



----------------------------------------
## Networks Get Network Meraki Auth Users


**List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)**

https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkMerakiAuthUsers --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkMerakiAuthUsers(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Mqtt Broker


**Return an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--mqttBrokerId` (string): (required)


##### Example:
```
meraki networks getNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING'
````

##### Method Code:
```python
def getNetworkMqttBroker(networkId:str, mqttBrokerId:str):
    # Code
````



----------------------------------------
## Networks Get Network Mqtt Brokers


**List the MQTT brokers for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkMqttBrokers --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkMqttBrokers(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Netflow


**Return the NetFlow traffic reporting settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkNetflow --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkNetflow(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Network Health Channel Utilization


**Get the channel utilization over each radio for all APs in a network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki networks getNetworkNetworkHealthChannelUtilization --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkNetworkHealthChannelUtilization --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkNetworkHealthChannelUtilization(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Pii Pii Keys


**List the keys required to access Personally Identifiable Information (PII) for a given identifier**

https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

##### Arguments
- `--networkId` (string): (required)
- `--username` (string): The username of a Systems Manager user
- `--email` (string): The email of a network user account or a Systems Manager device
- `--mac` (string): The MAC of a network client device or a Systems Manager device
- `--serial` (string): The serial of a Systems Manager device
- `--imei` (string): The IMEI of a Systems Manager device
- `--bluetoothMac` (string): The MAC of a Bluetooth client


##### Example:
```
meraki networks getNetworkPiiPiiKeys --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkPiiPiiKeys --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkPiiPiiKeys(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Pii Request


**Return a PII request**

https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

##### Arguments
- `--networkId` (string): (required)
- `--requestId` (string): (required)


##### Example:
```
meraki networks getNetworkPiiRequest --networkId 'STRING' --requestId 'STRING'
````

##### Method Code:
```python
def getNetworkPiiRequest(networkId:str, requestId:str):
    # Code
````



----------------------------------------
## Networks Get Network Pii Requests


**List the PII requests for this network or organization**

https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkPiiRequests --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkPiiRequests(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Pii Sm Devices For Key


**Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier**

https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

##### Arguments
- `--networkId` (string): (required)
- `--username` (string): The username of a Systems Manager user
- `--email` (string): The email of a network user account or a Systems Manager device
- `--mac` (string): The MAC of a network client device or a Systems Manager device
- `--serial` (string): The serial of a Systems Manager device
- `--imei` (string): The IMEI of a Systems Manager device
- `--bluetoothMac` (string): The MAC of a Bluetooth client


##### Example:
```
meraki networks getNetworkPiiSmDevicesForKey --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkPiiSmDevicesForKey --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkPiiSmDevicesForKey(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Pii Sm Owners For Key


**Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier**

https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

##### Arguments
- `--networkId` (string): (required)
- `--username` (string): The username of a Systems Manager user
- `--email` (string): The email of a network user account or a Systems Manager device
- `--mac` (string): The MAC of a network client device or a Systems Manager device
- `--serial` (string): The serial of a Systems Manager device
- `--imei` (string): The IMEI of a Systems Manager device
- `--bluetoothMac` (string): The MAC of a Bluetooth client


##### Example:
```
meraki networks getNetworkPiiSmOwnersForKey --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkPiiSmOwnersForKey --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkPiiSmOwnersForKey(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Policies By Client


**Get policies for all clients with policies**

https://developer.cisco.com/meraki/api-v1/#!get-network-policies-by-client

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki networks getNetworkPoliciesByClient --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkPoliciesByClient --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkPoliciesByClient(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Settings


**Return the settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSettings(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Snmp


**Return the SNMP settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkSnmp --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSnmp(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Splash Login Attempts


**List the splash login attempts for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

##### Arguments
- `--networkId` (string): (required)
- `--ssidNumber` (integer): Only return the login attempts for the specified SSID
- `--loginIdentifier` (string): The username, email, or phone number used during login
- `--timespan` (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months


##### Example:
```
meraki networks getNetworkSplashLoginAttempts --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkSplashLoginAttempts --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSplashLoginAttempts(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Syslog Servers


**List the syslog servers for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkSyslogServers --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSyslogServers(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Topology Link Layer


**List the LLDP and CDP information for all discovered devices and connections in a network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-topology-link-layer

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkTopologyLinkLayer --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkTopologyLinkLayer(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Traffic


**Return the traffic analysis data for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
- `--deviceType` (string): Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage.


##### Example:
```
meraki networks getNetworkTraffic --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks getNetworkTraffic --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkTraffic(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Get Network Traffic Analysis


**Return the traffic analysis settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkTrafficAnalysis --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkTrafficAnalysis(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Traffic Shaping Application Categories


**Returns the application categories for traffic shaping rules.**

https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkTrafficShapingApplicationCategories --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkTrafficShapingApplicationCategories(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Traffic Shaping Dscp Tagging Options


**Returns the available DSCP tagging options for your traffic shaping rules.**

https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkTrafficShapingDscpTaggingOptions --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkTrafficShapingDscpTaggingOptions(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Webhooks Http Server


**Return an HTTP server for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

##### Arguments
- `--networkId` (string): (required)
- `--httpServerId` (string): (required)


##### Example:
```
meraki networks getNetworkWebhooksHttpServer --networkId 'STRING' --httpServerId 'STRING'
````

##### Method Code:
```python
def getNetworkWebhooksHttpServer(networkId:str, httpServerId:str):
    # Code
````



----------------------------------------
## Networks Get Network Webhooks Http Servers


**List the HTTP servers for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkWebhooksHttpServers --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWebhooksHttpServers(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Webhooks Payload Template


**Get the webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--payloadTemplateId` (string): (required)


##### Example:
```
meraki networks getNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING'
````

##### Method Code:
```python
def getNetworkWebhooksPayloadTemplate(networkId:str, payloadTemplateId:str):
    # Code
````



----------------------------------------
## Networks Get Network Webhooks Payload Templates


**List the webhook payload templates for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-payload-templates

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks getNetworkWebhooksPayloadTemplates --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWebhooksPayloadTemplates(networkId:str):
    # Code
````



----------------------------------------
## Networks Get Network Webhooks Webhook Test


**Return the status of a webhook test for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

##### Arguments
- `--networkId` (string): (required)
- `--webhookTestId` (string): (required)


##### Example:
```
meraki networks getNetworkWebhooksWebhookTest --networkId 'STRING' --webhookTestId 'STRING'
````

##### Method Code:
```python
def getNetworkWebhooksWebhookTest(networkId:str, webhookTestId:str):
    # Code
````



----------------------------------------
## Networks Provision Network Clients


**Provisions a client with a name and policy**

https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

##### Arguments
- `--networkId` (string): (required)
- `--clients` (array): The array of clients to provision
- `--devicePolicy` (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
- `--groupPolicyId` (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
- `--policiesBySecurityAppliance` (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
- `--policiesBySsid` (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy


##### Example:
```
meraki networks provisionNetworkClients --networkId 'STRING' --clients ITEM --devicePolicy 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks provisionNetworkClients --networkId 'STRING' --clients ITEM --devicePolicy 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def provisionNetworkClients(networkId:str, clients:list, devicePolicy:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Remove Network Devices


**Remove a single device**

https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

##### Arguments
- `--networkId` (string): (required)
- `--serial` (string): The serial of a device


##### Example:
```
meraki networks removeNetworkDevices --networkId 'STRING' --serial 'STRING'
````

##### Method Code:
```python
def removeNetworkDevices(networkId:str, serial:str):
    # Code
````



----------------------------------------
## Networks Rollbacks Network Firmware Upgrades Staged Events


**Rollback a Staged Upgrade Event for a network**

https://developer.cisco.com/meraki/api-v1/#!rollbacks-network-firmware-upgrades-staged-events

##### Arguments
- `--networkId` (string): (required)
- `--stages` (array): All completed or in-progress stages in the network with their new start times. All pending stages will be canceled
- `--reasons` (array): The reason for rolling back the staged upgrade


##### Example:
```
meraki networks rollbacksNetworkFirmwareUpgradesStagedEvents --networkId 'STRING' --stages ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks rollbacksNetworkFirmwareUpgradesStagedEvents --networkId 'STRING' --stages ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def rollbacksNetworkFirmwareUpgradesStagedEvents(networkId:str, stages:list, **kwargs):
    # Code
````



----------------------------------------
## Networks Split Network


**Split a combined network into individual networks for each type of device**

https://developer.cisco.com/meraki/api-v1/#!split-network

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki networks splitNetwork --networkId 'STRING'
````

##### Method Code:
```python
def splitNetwork(networkId:str):
    # Code
````



----------------------------------------
## Networks Unbind Network


**Unbind a network from a template.**

https://developer.cisco.com/meraki/api-v1/#!unbind-network

##### Arguments
- `--networkId` (string): (required)
- `--retainConfigs` (boolean): Optional boolean to retain all the current configs given by the template.


##### Example:
```
meraki networks unbindNetwork --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks unbindNetwork --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def unbindNetwork(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network


**Update a network**

https://developer.cisco.com/meraki/api-v1/#!update-network

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the network
- `--timeZone` (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- `--tags` (array): A list of tags to be applied to the network
- `--enrollmentString` (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
- `--notes` (string): Add any notes or additional information about this network here.


##### Example:
```
meraki networks updateNetwork --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetwork --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetwork(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Alerts Settings


**Update the alert configuration for this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

##### Arguments
- `--networkId` (string): (required)
- `--defaultDestinations` (object): The network-wide destinations for all alerts on the network.
- `--alerts` (array): Alert-specific configuration for each type. Only alerts that pertain to the network can be updated.


##### Example:
```
meraki networks updateNetworkAlertsSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkAlertsSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkAlertsSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Client Policy


**Update the policy assigned to a client on the network**

https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--devicePolicy` (string): The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
- `--groupPolicyId` (string): [optional] If 'devicePolicy' is set to 'Group policy' this param is used to specify the group policy ID.


##### Example:
```
meraki networks updateNetworkClientPolicy --networkId 'STRING' --clientId 'STRING' --devicePolicy 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkClientPolicy --networkId 'STRING' --clientId 'STRING' --devicePolicy 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkClientPolicy(networkId:str, clientId:str, devicePolicy:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Client Splash Authorization Status


**Update a client's splash authorization**

https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--ssids` (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs


##### Example:
```
meraki networks updateNetworkClientSplashAuthorizationStatus --networkId 'STRING' --clientId 'STRING' --ssids JSON_STRING
````

##### Method Code:
```python
def updateNetworkClientSplashAuthorizationStatus(networkId:str, clientId:str, ssids:dict):
    # Code
````



----------------------------------------
## Networks Update Network Firmware Upgrades


**Update firmware upgrade information for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

##### Arguments
- `--networkId` (string): (required)
- `--upgradeWindow` (object): Upgrade window for devices in network
- `--timezone` (string): The timezone for the network
- `--products` (object): Contains information about the network to update


##### Example:
```
meraki networks updateNetworkFirmwareUpgrades --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkFirmwareUpgrades --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFirmwareUpgrades(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Firmware Upgrades Staged Events


**Update the Staged Upgrade Event for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-events

##### Arguments
- `--networkId` (string): (required)
- `--stages` (array): All firmware upgrade stages in the network with their start time.


##### Example:
```
meraki networks updateNetworkFirmwareUpgradesStagedEvents --networkId 'STRING' --stages ITEM
````

##### Method Code:
```python
def updateNetworkFirmwareUpgradesStagedEvents(networkId:str, stages:list):
    # Code
````



----------------------------------------
## Networks Update Network Firmware Upgrades Staged Group


**Update a Staged Upgrade Group for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-group

##### Arguments
- `--networkId` (string): (required)
- `--groupId` (string): (required)
- `--name` (string): Name of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--isDefault` (boolean): Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group
- `--description` (string): Description of the Staged Upgrade Group. Length must be 1 to 255 characters
- `--assignedDevices` (object): The devices and Switch Stacks assigned to the Group


##### Example:
```
meraki networks updateNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --groupId 'STRING' --name 'STRING' --isDefault --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkFirmwareUpgradesStagedGroup --networkId 'STRING' --groupId 'STRING' --name 'STRING' --isDefault --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFirmwareUpgradesStagedGroup(networkId:str, groupId:str, name:str, isDefault:bool, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Firmware Upgrades Staged Stages


**Assign Staged Upgrade Group order in the sequence.**

https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-stages

##### Arguments
- `--networkId` (string): (required)
- `--_json` (array): Array of Staged Upgrade Groups


##### Example:
```
meraki networks updateNetworkFirmwareUpgradesStagedStages --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkFirmwareUpgradesStagedStages --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFirmwareUpgradesStagedStages(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Floor Plan


**Update a floor plan's geolocation and other meta data**

https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

##### Arguments
- `--networkId` (string): (required)
- `--floorPlanId` (string): (required)
- `--name` (string): The name of your floor plan.
- `--center` (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
- `--bottomLeftCorner` (object): The longitude and latitude of the bottom left corner of your floor plan.
- `--bottomRightCorner` (object): The longitude and latitude of the bottom right corner of your floor plan.
- `--topLeftCorner` (object): The longitude and latitude of the top left corner of your floor plan.
- `--topRightCorner` (object): The longitude and latitude of the top right corner of your floor plan.
- `--imageContents` (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.


##### Example:
```
meraki networks updateNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkFloorPlan --networkId 'STRING' --floorPlanId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkFloorPlan(networkId:str, floorPlanId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Group Policy


**Update a group policy**

https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

##### Arguments
- `--networkId` (string): (required)
- `--groupPolicyId` (string): (required)
- `--name` (string): The name for your group policy.
- `--scheduling` (object):     The schedule for the group policy. Schedules are applied to days of the week.

- `--bandwidth` (object):     The bandwidth settings for clients bound to your group policy.

- `--firewallAndTrafficShaping` (object):     The firewall and traffic shaping rules and settings for your policy.

- `--contentFiltering` (object): The content filtering settings for your group policy
- `--splashAuthSettings` (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- `--vlanTagging` (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- `--bonjourForwarding` (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.


##### Example:
```
meraki networks updateNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkGroupPolicy --networkId 'STRING' --groupPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkGroupPolicy(networkId:str, groupPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Meraki Auth User


**Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)**

https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

##### Arguments
- `--networkId` (string): (required)
- `--merakiAuthUserId` (string): (required)
- `--name` (string): Name of the user. Only allowed If the user is not Dashboard administrator.
- `--password` (string): The password for this user account. Only allowed If the user is not Dashboard administrator.
- `--emailPasswordToUser` (boolean): Whether or not Meraki should email the password to user. Default is false.
- `--authorizations` (array): Authorization zones and expiration dates for the user.


##### Example:
```
meraki networks updateNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkMerakiAuthUser --networkId 'STRING' --merakiAuthUserId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkMerakiAuthUser(networkId:str, merakiAuthUserId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Mqtt Broker


**Update an MQTT broker**

https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

##### Arguments
- `--networkId` (string): (required)
- `--mqttBrokerId` (string): (required)
- `--name` (string): Name of the MQTT broker.
- `--host` (string): Host name/IP address where the MQTT broker runs.
- `--port` (integer): Host port though which the MQTT broker can be reached.
- `--security` (object): Security settings of the MQTT broker.
- `--authentication` (object): Authentication settings of the MQTT broker


##### Example:
```
meraki networks updateNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkMqttBroker --networkId 'STRING' --mqttBrokerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkMqttBroker(networkId:str, mqttBrokerId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Netflow


**Update the NetFlow traffic reporting settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

##### Arguments
- `--networkId` (string): (required)
- `--reportingEnabled` (boolean): Boolean indicating whether NetFlow traffic reporting is enabled (true) or disabled (false).
- `--collectorIp` (string): The IPv4 address of the NetFlow collector.
- `--collectorPort` (integer): The port that the NetFlow collector will be listening on.
- `--etaEnabled` (boolean): Boolean indicating whether Encrypted Traffic Analytics is enabled (true) or disabled (false).
- `--etaDstPort` (integer): The port that the Encrypted Traffic Analytics collector will be listening on.


##### Example:
```
meraki networks updateNetworkNetflow --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkNetflow --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkNetflow(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Settings


**Update the settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-settings

##### Arguments
- `--networkId` (string): (required)
- `--localStatusPageEnabled` (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
- `--remoteStatusPageEnabled` (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
- `--localStatusPage` (object): A hash of Local Status page(s)' authentication options applied to the Network.
- `--securePort` (object): A hash of SecureConnect options applied to the Network.


##### Example:
```
meraki networks updateNetworkSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Snmp


**Update the SNMP settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

##### Arguments
- `--networkId` (string): (required)
- `--access` (string): The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3).
- `--communityString` (string): The SNMP community string. Only relevant if 'access' is set to 'community'.
- `--users` (array): The list of SNMP users. Only relevant if 'access' is set to 'users'.


##### Example:
```
meraki networks updateNetworkSnmp --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkSnmp --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSnmp(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Syslog Servers


**Update the syslog servers for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

##### Arguments
- `--networkId` (string): (required)
- `--servers` (array): A list of the syslog servers for this network


##### Example:
```
meraki networks updateNetworkSyslogServers --networkId 'STRING' --servers ITEM
````

##### Method Code:
```python
def updateNetworkSyslogServers(networkId:str, servers:list):
    # Code
````



----------------------------------------
## Networks Update Network Traffic Analysis


**Update the traffic analysis settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

##### Arguments
- `--networkId` (string): (required)
- `--mode` (string):     The traffic analysis mode for the network. Can be one of 'disabled' (do not collect traffic types),
'basic' (collect generic traffic categories), or 'detailed' (collect destination hostnames).

- `--customPieChartItems` (array): The list of items that make up the custom pie chart for traffic reporting.


##### Example:
```
meraki networks updateNetworkTrafficAnalysis --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkTrafficAnalysis --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkTrafficAnalysis(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Webhooks Http Server


**Update an HTTP server**

https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

##### Arguments
- `--networkId` (string): (required)
- `--httpServerId` (string): (required)
- `--name` (string): A name for easy reference to the HTTP server
- `--sharedSecret` (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
- `--payloadTemplate` (object): The payload template to use when posting data to the HTTP server.


##### Example:
```
meraki networks updateNetworkWebhooksHttpServer --networkId 'STRING' --httpServerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkWebhooksHttpServer --networkId 'STRING' --httpServerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWebhooksHttpServer(networkId:str, httpServerId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Update Network Webhooks Payload Template


**Update a webhook payload template for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-payload-template

##### Arguments
- `--networkId` (string): (required)
- `--payloadTemplateId` (string): (required)
- `--name` (string): The name of the template
- `--body` (string): The liquid template used for the body of the webhook message.
- `--headers` (array): The liquid template used with the webhook headers.
- `--bodyFile` (string): A file containing liquid template used for the body of the webhook message.
- `--headersFile` (string): A file containing the liquid template used with the webhook headers.


##### Example:
```
meraki networks updateNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki networks updateNetworkWebhooksPayloadTemplate --networkId 'STRING' --payloadTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWebhooksPayloadTemplate(networkId:str, payloadTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Networks Vmx Network Devices Claim


**Claim a vMX into a network**

https://developer.cisco.com/meraki/api-v1/#!vmx-network-devices-claim

##### Arguments
- `--networkId` (string): (required)
- `--size` (string): The size of the vMX you claim. It can be one of: small, medium, large, 100


##### Example:
```
meraki networks vmxNetworkDevicesClaim --networkId 'STRING' --size 'STRING'
````

##### Method Code:
```python
def vmxNetworkDevicesClaim(networkId:str, size:str):
    # Code
````

# Organizations


----------------------------------------
## Organizations Assign Organization Licenses Seats


**Assign SM seats to a network**

https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--licenseId` (string): The ID of the SM license to assign seats from
- `--networkId` (string): The ID of the SM network to assign the seats to
- `--seatCount` (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license


##### Example:
```
meraki organizations assignOrganizationLicensesSeats --organizationId 'STRING' --licenseId 'STRING' --networkId 'STRING' --seatCount INT
````

##### Method Code:
```python
def assignOrganizationLicensesSeats(organizationId:str, licenseId:str, networkId:str, seatCount:int):
    # Code
````



----------------------------------------
## Organizations Claim Into Organization


**Claim a list of devices, licenses, and/or orders into an organization**

https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

##### Arguments
- `--organizationId` (string): (required)
- `--orders` (array): The numbers of the orders that should be claimed
- `--serials` (array): The serials of the devices that should be claimed
- `--licenses` (array): The licenses that should be claimed


##### Example:
```
meraki organizations claimIntoOrganization --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations claimIntoOrganization --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def claimIntoOrganization(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Claim Into Organization Inventory


**Claim a list of devices, licenses, and/or orders into an organization inventory**

https://developer.cisco.com/meraki/api-v1/#!claim-into-organization-inventory

##### Arguments
- `--organizationId` (string): (required)
- `--orders` (array): The numbers of the orders that should be claimed
- `--serials` (array): The serials of the devices that should be claimed
- `--licenses` (array): The licenses that should be claimed


##### Example:
```
meraki organizations claimIntoOrganizationInventory --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations claimIntoOrganizationInventory --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def claimIntoOrganizationInventory(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Clone Organization


**Create a new organization by cloning the addressed organization**

https://developer.cisco.com/meraki/api-v1/#!clone-organization

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the new organization


##### Example:
```
meraki organizations cloneOrganization --organizationId 'STRING' --name 'STRING'
````

##### Method Code:
```python
def cloneOrganization(organizationId:str, name:str):
    # Code
````



----------------------------------------
## Organizations Combine Organization Networks


**Combine multiple networks into a single network**

https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the combined network
- `--networkIds` (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
- `--enrollmentString` (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.


##### Example:
```
meraki organizations combineOrganizationNetworks --organizationId 'STRING' --name 'STRING' --networkIds ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations combineOrganizationNetworks --organizationId 'STRING' --name 'STRING' --networkIds ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def combineOrganizationNetworks(organizationId:str, name:str, networkIds:list, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization


**Create a new organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization

##### Arguments
- `--name` (string): The name of the organization
- `--management` (object): Information about the organization's management system


##### Example:
```
meraki organizations createOrganization --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganization --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganization(name:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Action Batch


**Create an action batch**

https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

##### Arguments
- `--organizationId` (string): (required)
- `--actions` (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
- `--confirmed` (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
- `--synchronous` (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.


##### Example:
```
meraki organizations createOrganizationActionBatch --organizationId 'STRING' --actions ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationActionBatch --organizationId 'STRING' --actions ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationActionBatch(organizationId:str, actions:list, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Adaptive Policy Acl


**Creates new adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the adaptive policy ACL
- `--rules` (array): An ordered array of the adaptive policy ACL rules.
- `--ipVersion` (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
- `--description` (string): Description of the adaptive policy ACL


##### Example:
```
meraki organizations createOrganizationAdaptivePolicyAcl --organizationId 'STRING' --name 'STRING' --rules ITEM --ipVersion 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationAdaptivePolicyAcl --organizationId 'STRING' --name 'STRING' --rules ITEM --ipVersion 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyAcl(organizationId:str, name:str, rules:list, ipVersion:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Adaptive Policy Group


**Creates a new adaptive policy group**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the group
- `--sgt` (integer): SGT value of the group
- `--description` (string): Description of the group (default: "")
- `--policyObjects` (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: [])


##### Example:
```
meraki organizations createOrganizationAdaptivePolicyGroup --organizationId 'STRING' --name 'STRING' --sgt INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationAdaptivePolicyGroup --organizationId 'STRING' --name 'STRING' --sgt INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyGroup(organizationId:str, name:str, sgt:int, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Adaptive Policy Policy


**Add an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--sourceGroup` (object): The source adaptive policy group (requires one unique attribute)
- `--destinationGroup` (object): The destination adaptive policy group (requires one unique attribute)
- `--acls` (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])
- `--lastEntryRule` (string): The rule to apply if there is no matching ACL (default: "default")


##### Example:
```
meraki organizations createOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --sourceGroup JSON_STRING --destinationGroup JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --sourceGroup JSON_STRING --destinationGroup JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdaptivePolicyPolicy(organizationId:str, sourceGroup:dict, destinationGroup:dict, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Admin


**Create a new dashboard administrator**

https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

##### Arguments
- `--organizationId` (string): (required)
- `--email` (string): The email of the dashboard administrator. This attribute can not be updated.
- `--name` (string): The name of the dashboard administrator
- `--orgAccess` (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
- `--tags` (array): The list of tags that the dashboard administrator has privileges on
- `--networks` (array): The list of networks that the dashboard administrator has privileges on
- `--authenticationMethod` (string): The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of 'Email' or 'Cisco SecureX Sign-On'. The default is Email authentication


##### Example:
```
meraki organizations createOrganizationAdmin --organizationId 'STRING' --email 'STRING' --name 'STRING' --orgAccess 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationAdmin --organizationId 'STRING' --email 'STRING' --name 'STRING' --orgAccess 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAdmin(organizationId:str, email:str, name:str, orgAccess:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Alerts Profile


**Create an organization-wide alert configuration**

https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--type` (string): The alert type
- `--alertCondition` (object): The conditions that determine if the alert triggers
- `--recipients` (object): List of recipients that will recieve the alert.
- `--networkTags` (array): Networks with these tags will be monitored for the alert
- `--description` (string): User supplied description of the alert


##### Example:
```
meraki organizations createOrganizationAlertsProfile --organizationId 'STRING' --type 'STRING' --alertCondition JSON_STRING --recipients JSON_STRING --networkTags ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationAlertsProfile --organizationId 'STRING' --type 'STRING' --alertCondition JSON_STRING --recipients JSON_STRING --networkTags ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationAlertsProfile(organizationId:str, type:str, alertCondition:dict, recipients:dict, networkTags:list, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Branding Policy


**Add a new branding policy to an organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of the Dashboard branding policy.
- `--enabled` (boolean): Boolean indicating whether this policy is enabled.
- `--adminSettings` (object): Settings for describing which kinds of admins this policy applies to.
- `--helpSettings` (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.
Each property defaults to 'default or inherit' when not provided.
- `--customLogo` (object): Properties describing the custom logo attached to the branding policy.


##### Example:
```
meraki organizations createOrganizationBrandingPolicy --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationBrandingPolicy --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationBrandingPolicy(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Config Template


**Create a new configuration template**

https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the configuration template
- `--timeZone` (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
- `--copyFromNetworkId` (string): The ID of the network or config template to copy configuration from


##### Example:
```
meraki organizations createOrganizationConfigTemplate --organizationId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationConfigTemplate --organizationId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationConfigTemplate(organizationId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Early Access Features Opt In


**Create a new early access feature opt-in for an organization**

https://developer.cisco.com/meraki/api-v1/#!create-organization-early-access-features-opt-in

##### Arguments
- `--organizationId` (string): (required)
- `--shortName` (string): Short name of the early access feature
- `--limitScopeToNetworks` (array): A list of network IDs to apply the opt-in to


##### Example:
```
meraki organizations createOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --shortName 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --shortName 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationEarlyAccessFeaturesOptIn(organizationId:str, shortName:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Inventory Onboarding Cloud Monitoring Export Event


**Imports event logs related to the onboarding app into elastisearch**

https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-export-event

##### Arguments
- `--organizationId` (string): (required)
- `--logEvent` (string): The type of log event this is recording, e.g. download or opening a banner
- `--timestamp` (integer): A JavaScript UTC datetime stamp for when the even occurred
- `--targetOS` (string): The name of the onboarding distro being downloaded
- `--request` (string): Used to describe if this event was the result of a redirect. E.g. a query param if an info banner is being used


##### Example:
```
meraki organizations createOrganizationInventoryOnboardingCloudMonitoringExportEvent --organizationId 'STRING' --logEvent 'STRING' --timestamp INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationInventoryOnboardingCloudMonitoringExportEvent --organizationId 'STRING' --logEvent 'STRING' --timestamp INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationInventoryOnboardingCloudMonitoringExportEvent(organizationId:str, logEvent:str, timestamp:int, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Inventory Onboarding Cloud Monitoring Import


**Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-import

##### Arguments
- `--organizationId` (string): (required)
- `--devices` (array): A set of device imports to commit


##### Example:
```
meraki organizations createOrganizationInventoryOnboardingCloudMonitoringImport --organizationId 'STRING' --devices ITEM
````

##### Method Code:
```python
def createOrganizationInventoryOnboardingCloudMonitoringImport(organizationId:str, devices:list):
    # Code
````



----------------------------------------
## Organizations Create Organization Inventory Onboarding Cloud Monitoring Prepare


**Initiates or updates an import session**

https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare

##### Arguments
- `--organizationId` (string): (required)
- `--devices` (array): A set of devices to import (or update)


##### Example:
```
meraki organizations createOrganizationInventoryOnboardingCloudMonitoringPrepare --organizationId 'STRING' --devices ITEM
````

##### Method Code:
```python
def createOrganizationInventoryOnboardingCloudMonitoringPrepare(organizationId:str, devices:list):
    # Code
````



----------------------------------------
## Organizations Create Organization Network


**Create a network**

https://developer.cisco.com/meraki/api-v1/#!create-organization-network

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the new network
- `--productTypes` (array): The product type(s) of the new network. If more than one type is included, the network will be a combined network.
- `--tags` (array): A list of tags to be applied to the network
- `--timeZone` (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- `--copyFromNetworkId` (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
- `--notes` (string): Add any notes or additional information about this network here.


##### Example:
```
meraki organizations createOrganizationNetwork --organizationId 'STRING' --name 'STRING' --productTypes ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationNetwork --organizationId 'STRING' --name 'STRING' --productTypes ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationNetwork(organizationId:str, name:str, productTypes:list, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Policy Object


**Creates a new Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--category` (string): Category of a policy object (one of: adaptivePolicy, network)
- `--type` (string): Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask)
- `--cidr` (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
- `--fqdn` (string): Fully qualified domain name of policy object (e.g. "example.com")
- `--mask` (string): Mask of a policy object (e.g. "255.255.0.0")
- `--ip` (string): IP Address of a policy object (e.g. "1.2.3.4")
- `--groupIds` (array): The IDs of policy object groups the policy object belongs to


##### Example:
```
meraki organizations createOrganizationPolicyObject --organizationId 'STRING' --name 'STRING' --category 'STRING' --type 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationPolicyObject --organizationId 'STRING' --name 'STRING' --category 'STRING' --type 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationPolicyObject(organizationId:str, name:str, category:str, type:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Policy Objects Group


**Creates a new Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--category` (string): Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup)
- `--objectIds` (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)


##### Example:
```
meraki organizations createOrganizationPolicyObjectsGroup --organizationId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationPolicyObjectsGroup --organizationId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationPolicyObjectsGroup(organizationId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Saml Idp


**Create a SAML IdP for your organization.**

https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--x509certSha1Fingerprint` (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- `--sloLogoutUrl` (string): Dashboard will redirect users to this URL when they sign out.


##### Example:
```
meraki organizations createOrganizationSamlIdp --organizationId 'STRING' --x509certSha1Fingerprint 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationSamlIdp --organizationId 'STRING' --x509certSha1Fingerprint 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationSamlIdp(organizationId:str, x509certSha1Fingerprint:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Create Organization Saml Role


**Create a SAML role**

https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

##### Arguments
- `--organizationId` (string): (required)
- `--role` (string): The role of the SAML administrator
- `--orgAccess` (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise'
- `--tags` (array): The list of tags that the SAML administrator has privleges on
- `--networks` (array): The list of networks that the SAML administrator has privileges on


##### Example:
```
meraki organizations createOrganizationSamlRole --organizationId 'STRING' --role 'STRING' --orgAccess 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations createOrganizationSamlRole --organizationId 'STRING' --role 'STRING' --orgAccess 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createOrganizationSamlRole(organizationId:str, role:str, orgAccess:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Delete Organization


**Delete an organization**

https://developer.cisco.com/meraki/api-v1/#!delete-organization

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations deleteOrganization --organizationId 'STRING'
````

##### Method Code:
```python
def deleteOrganization(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Action Batch


**Delete an action batch**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

##### Arguments
- `--organizationId` (string): (required)
- `--actionBatchId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationActionBatch --organizationId 'STRING' --actionBatchId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationActionBatch(organizationId:str, actionBatchId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Adaptive Policy Acl


**Deletes the specified adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--aclId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyAcl(organizationId:str, aclId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Adaptive Policy Group


**Deletes the specified adaptive policy group and any associated policies and references**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyGroup(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Adaptive Policy Policy


**Delete an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdaptivePolicyPolicy(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Admin


**Revoke all access for a dashboard administrator within this organization**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

##### Arguments
- `--organizationId` (string): (required)
- `--adminId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationAdmin --organizationId 'STRING' --adminId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAdmin(organizationId:str, adminId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Alerts Profile


**Removes an organization-wide alert config**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--alertConfigId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationAlertsProfile(organizationId:str, alertConfigId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Branding Policy


**Delete a branding policy**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationBrandingPolicy(organizationId:str, brandingPolicyId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Config Template


**Remove a configuration template**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationConfigTemplate(organizationId:str, configTemplateId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Early Access Features Opt In


**Delete an early access feature opt-in**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-early-access-features-opt-in

##### Arguments
- `--organizationId` (string): (required)
- `--optInId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationEarlyAccessFeaturesOptIn(organizationId:str, optInId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Policy Object


**Deletes a Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationPolicyObject(organizationId:str, policyObjectId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Policy Objects Group


**Deletes a Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectGroupId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationPolicyObjectsGroup(organizationId:str, policyObjectGroupId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Saml Idp


**Remove a SAML IdP in your organization.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--idpId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationSamlIdp(organizationId:str, idpId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization Saml Role


**Remove a SAML role**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

##### Arguments
- `--organizationId` (string): (required)
- `--samlRoleId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationSamlRole --organizationId 'STRING' --samlRoleId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationSamlRole(organizationId:str, samlRoleId:str):
    # Code
````



----------------------------------------
## Organizations Delete Organization User


**Delete a user and all of its authentication methods.**

https://developer.cisco.com/meraki/api-v1/#!delete-organization-user

##### Arguments
- `--organizationId` (string): (required)
- `--userId` (string): (required)


##### Example:
```
meraki organizations deleteOrganizationUser --organizationId 'STRING' --userId 'STRING'
````

##### Method Code:
```python
def deleteOrganizationUser(organizationId:str, userId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization


**Return an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganization --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganization(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Action Batch


**Return an action batch**

https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

##### Arguments
- `--organizationId` (string): (required)
- `--actionBatchId` (string): (required)


##### Example:
```
meraki organizations getOrganizationActionBatch --organizationId 'STRING' --actionBatchId 'STRING'
````

##### Method Code:
```python
def getOrganizationActionBatch(organizationId:str, actionBatchId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Action Batches


**Return the list of action batches in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

##### Arguments
- `--organizationId` (string): (required)
- `--status` (string): Filter batches by status. Valid types are pending, completed, and failed.


##### Example:
```
meraki organizations getOrganizationActionBatches --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationActionBatches --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationActionBatches(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Acl


**Returns the adaptive policy ACL information**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--aclId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyAcl(organizationId:str, aclId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Acls


**List adaptive policy ACLs in a organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyAcls --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyAcls(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Group


**Returns an adaptive policy group**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyGroup(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Groups


**List adaptive policy groups in a organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyGroups --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyGroups(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Overview


**Returns adaptive policy aggregate statistics for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyOverview --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyOverview(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Policies


**List adaptive policies in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyPolicies --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyPolicies(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Policy


**Return an adaptive policy**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicyPolicy(organizationId:str, id:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Adaptive Policy Settings


**Returns global adaptive policy settings in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdaptivePolicySettings --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdaptivePolicySettings(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Admins


**List the dashboard administrators in this organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAdmins --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAdmins(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Alerts Profiles


**List all organization-wide alert configurations**

https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationAlertsProfiles --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationAlertsProfiles(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Api Requests


**List the API requests made by an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--adminId` (string): Filter the results by the ID of the admin who made the API requests
- `--path` (string): Filter the results by the path of the API requests
- `--method` (string): Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')
- `--responseCode` (integer): Filter the results by the response code of the API requests
- `--sourceIp` (string): Filter the results by the IP address of the originating API request
- `--userAgent` (string): Filter the results by the user agent string of the API request
- `--version` (integer): Filter the results by the API version of the API request
- `--operationIds` (array): Filter the results by one or more operation IDs for the API request


##### Example:
```
meraki organizations getOrganizationApiRequests --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationApiRequests --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApiRequests(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Api Requests Overview


**Return an aggregated overview of API requests data**

https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.


##### Example:
```
meraki organizations getOrganizationApiRequestsOverview --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationApiRequestsOverview --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApiRequestsOverview(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Api Requests Overview Response Codes By Interval


**Tracks organizations' API requests by response code across a given time period**

https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
- `--interval` (integer): The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
- `--version` (integer): Filter by API version of the endpoint. Allowable values are: [0, 1]
- `--operationIds` (array): Filter by operation ID of the endpoint
- `--sourceIps` (array): Filter by source IP that made the API request
- `--adminIds` (array): Filter by admin ID of user that made the API request
- `--userAgent` (string): Filter by user agent string for API request. This will filter by a complete or partial match.


##### Example:
```
meraki organizations getOrganizationApiRequestsOverviewResponseCodesByInterval --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationApiRequestsOverviewResponseCodesByInterval --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationApiRequestsOverviewResponseCodesByInterval(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Branding Policies


**List the branding policies of an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationBrandingPolicies --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationBrandingPolicies(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Branding Policies Priorities


**Return the branding policy IDs of an organization in priority order**

https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationBrandingPoliciesPriorities --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationBrandingPoliciesPriorities(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Branding Policy


**Return a branding policy**

https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyId` (string): (required)


##### Example:
```
meraki organizations getOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING'
````

##### Method Code:
```python
def getOrganizationBrandingPolicy(organizationId:str, brandingPolicyId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Clients Bandwidth Usage History


**Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationClientsBandwidthUsageHistory --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationClientsBandwidthUsageHistory --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationClientsBandwidthUsageHistory(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Clients Overview


**Return summary information around client data usage (in mb) across the given organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-overview

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationClientsOverview --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationClientsOverview --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationClientsOverview(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Clients Search


**Return the client details in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

##### Arguments
- `--organizationId` (string): (required)
- `--mac` (string): The MAC address of the client. Required.
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki organizations getOrganizationClientsSearch --organizationId 'STRING' --mac 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationClientsSearch --organizationId 'STRING' --mac 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationClientsSearch(organizationId:str, mac:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Config Template


**Return a single configuration template**

https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)


##### Example:
```
meraki organizations getOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING'
````

##### Method Code:
```python
def getOrganizationConfigTemplate(organizationId:str, configTemplateId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Config Templates


**List the configuration templates for this organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationConfigTemplates --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationConfigTemplates(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Configuration Changes


**View the Change Log for your organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" or "prev" (default) page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkId` (string): Filters on the given network
- `--adminId` (string): Filters on the given Admin


##### Example:
```
meraki organizations getOrganizationConfigurationChanges --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationConfigurationChanges --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationConfigurationChanges(organizationId:str, total_pages=1, direction='prev', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices


**List the devices in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--configurationUpdatedAfter` (string): Filter results by whether or not the device's configuration has been updated after the given timestamp
- `--networkIds` (array): Optional parameter to filter devices by network.
- `--productTypes` (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
- `--tags` (array): Optional parameter to filter devices by tags.
- `--tagsFilterType` (string): Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
- `--name` (string): Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
- `--mac` (string): Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
- `--serial` (string): Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
- `--model` (string): Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
- `--macs` (array): Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
- `--serials` (array): Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
- `--sensorMetrics` (array): Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
- `--sensorAlertProfileIds` (array): Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
- `--models` (array): Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.


##### Example:
```
meraki organizations getOrganizationDevices --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevices --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevices(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Availabilities


**List the availability information for devices in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
- `--productTypes` (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
- `--serials` (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
- `--tags` (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
- `--tagsFilterType` (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.


##### Example:
```
meraki organizations getOrganizationDevicesAvailabilities --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesAvailabilities --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesAvailabilities(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Power Modules Statuses By Device


**List the power status information for devices in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
- `--productTypes` (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
- `--serials` (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
- `--tags` (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
- `--tagsFilterType` (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.


##### Example:
```
meraki organizations getOrganizationDevicesPowerModulesStatusesByDevice --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesPowerModulesStatusesByDevice --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesPowerModulesStatusesByDevice(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Statuses


**List the status of every Meraki device in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter devices by network ids.
- `--serials` (array): Optional parameter to filter devices by serials.
- `--statuses` (array): Optional parameter to filter devices by statuses. Valid statuses are ["online", "alerting", "offline", "dormant"].
- `--productTypes` (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
- `--models` (array): Optional parameter to filter devices by models.
- `--tags` (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
- `--tagsFilterType` (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.


##### Example:
```
meraki organizations getOrganizationDevicesStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Statuses Overview


**Return an overview of current device statuses**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

##### Arguments
- `--organizationId` (string): (required)
- `--productTypes` (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
- `--networkIds` (array): An optional parameter to filter device statuses by network.


##### Example:
```
meraki organizations getOrganizationDevicesStatusesOverview --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesStatusesOverview --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesStatusesOverview(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Uplinks Addresses By Device


**List the current uplink addresses for devices in an organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
- `--productTypes` (array): Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
- `--serials` (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
- `--tags` (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
- `--tagsFilterType` (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.


##### Example:
```
meraki organizations getOrganizationDevicesUplinksAddressesByDevice --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesUplinksAddressesByDevice --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesUplinksAddressesByDevice(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Devices Uplinks Loss And Latency


**Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**

https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
- `--uplink` (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
- `--ip` (string): Optional filter for a specific destination IP. Default will return all destination IPs.


##### Example:
```
meraki organizations getOrganizationDevicesUplinksLossAndLatency --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationDevicesUplinksLossAndLatency --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationDevicesUplinksLossAndLatency(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Early Access Features


**List the available early access features for organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationEarlyAccessFeatures --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationEarlyAccessFeatures(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Early Access Features Opt In


**Show an early access feature opt-in for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

##### Arguments
- `--organizationId` (string): (required)
- `--optInId` (string): (required)


##### Example:
```
meraki organizations getOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING'
````

##### Method Code:
```python
def getOrganizationEarlyAccessFeaturesOptIn(organizationId:str, optInId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Early Access Features Opt Ins


**List the early access feature opt-ins for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationEarlyAccessFeaturesOptIns --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationEarlyAccessFeaturesOptIns(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Firmware Upgrades


**Get firmware upgrade information for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

##### Arguments
- `--organizationId` (string): (required)
- `--status` (array): The status of an upgrade 
- `--productType` (array): The product type in a given upgrade ID


##### Example:
```
meraki organizations getOrganizationFirmwareUpgrades --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationFirmwareUpgrades --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationFirmwareUpgrades(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Firmware Upgrades By Device


**Get firmware upgrade status for the filtered devices**

https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter by network
- `--serials` (array): Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
- `--macs` (array): Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
- `--firmwareUpgradeIds` (array): Optional parameter to filter by firmware upgrade ids.
- `--firmwareUpgradeBatchIds` (array): Optional parameter to filter by firmware upgrade batch ids.


##### Example:
```
meraki organizations getOrganizationFirmwareUpgradesByDevice --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationFirmwareUpgradesByDevice --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationFirmwareUpgradesByDevice(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Inventory Device


**Return a single device from the inventory of an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

##### Arguments
- `--organizationId` (string): (required)
- `--serial` (string): (required)


##### Example:
```
meraki organizations getOrganizationInventoryDevice --organizationId 'STRING' --serial 'STRING'
````

##### Method Code:
```python
def getOrganizationInventoryDevice(organizationId:str, serial:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Inventory Devices


**Return the device inventory for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--usedState` (string): Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
- `--search` (string): Search for devices in inventory based on serial number, mac address, or model.
- `--macs` (array): Search for devices in inventory based on mac addresses.
- `--networkIds` (array): Search for devices in inventory based on network ids.
- `--serials` (array): Search for devices in inventory based on serials.
- `--models` (array): Search for devices in inventory based on model.
- `--orderNumbers` (array): Search for devices in inventory based on order numbers.
- `--tags` (array): Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
- `--tagsFilterType` (string): To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
- `--productTypes` (array): Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.


##### Example:
```
meraki organizations getOrganizationInventoryDevices --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationInventoryDevices --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationInventoryDevices(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Inventory Onboarding Cloud Monitoring Imports


**Check the status of a committed Import operation**

https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-imports

##### Arguments
- `--organizationId` (string): (required)
- `--importIds` (array): import ids from an imports


##### Example:
```
meraki organizations getOrganizationInventoryOnboardingCloudMonitoringImports --organizationId 'STRING' --importIds ITEM
````

##### Method Code:
```python
def getOrganizationInventoryOnboardingCloudMonitoringImports(organizationId:str, importIds:list):
    # Code
````



----------------------------------------
## Organizations Get Organization Inventory Onboarding Cloud Monitoring Networks


**Returns list of networks eligible for adding cloud monitored device**

https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-networks

##### Arguments
- `--organizationId` (string): (required)
- `--deviceType` (string): Device Type switch or wireless controller
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki organizations getOrganizationInventoryOnboardingCloudMonitoringNetworks --organizationId 'STRING' --deviceType 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationInventoryOnboardingCloudMonitoringNetworks --organizationId 'STRING' --deviceType 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationInventoryOnboardingCloudMonitoringNetworks(organizationId:str, deviceType:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization License


**Display a license**

https://developer.cisco.com/meraki/api-v1/#!get-organization-license

##### Arguments
- `--organizationId` (string): (required)
- `--licenseId` (string): (required)


##### Example:
```
meraki organizations getOrganizationLicense --organizationId 'STRING' --licenseId 'STRING'
````

##### Method Code:
```python
def getOrganizationLicense(organizationId:str, licenseId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Licenses


**List the licenses for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--deviceSerial` (string): Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
- `--networkId` (string): Filter the licenses to those assigned in a particular network
- `--state` (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'


##### Example:
```
meraki organizations getOrganizationLicenses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationLicenses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationLicenses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Licenses Overview


**Return an overview of the license state for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationLicensesOverview --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationLicensesOverview(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Login Security


**Returns the login security settings for an organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationLoginSecurity --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationLoginSecurity(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Networks


**List the networks that the user has privileges on in an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--configTemplateId` (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
- `--isBoundToConfigTemplate` (boolean): An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
- `--tags` (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
- `--tagsFilterType` (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki organizations getOrganizationNetworks --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationNetworks --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationNetworks(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Openapi Spec


**Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**

https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationOpenapiSpec --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationOpenapiSpec(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Policy Object


**Shows details of a Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectId` (string): (required)


##### Example:
```
meraki organizations getOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING'
````

##### Method Code:
```python
def getOrganizationPolicyObject(organizationId:str, policyObjectId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Policy Objects


**Lists Policy Objects belonging to the organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki organizations getOrganizationPolicyObjects --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationPolicyObjects --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationPolicyObjects(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Policy Objects Group


**Shows details of a Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectGroupId` (string): (required)


##### Example:
```
meraki organizations getOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING'
````

##### Method Code:
```python
def getOrganizationPolicyObjectsGroup(organizationId:str, policyObjectGroupId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Policy Objects Groups


**Lists Policy Object Groups belonging to the organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki organizations getOrganizationPolicyObjectsGroups --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationPolicyObjectsGroups --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationPolicyObjectsGroups(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Saml


**Returns the SAML SSO enabled settings for an organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSaml --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSaml(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Saml Idp


**Get a SAML IdP from your organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--idpId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING'
````

##### Method Code:
```python
def getOrganizationSamlIdp(organizationId:str, idpId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Saml Idps


**List the SAML IdPs in your organization.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSamlIdps --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSamlIdps(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Saml Role


**Return a SAML role**

https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

##### Arguments
- `--organizationId` (string): (required)
- `--samlRoleId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSamlRole --organizationId 'STRING' --samlRoleId 'STRING'
````

##### Method Code:
```python
def getOrganizationSamlRole(organizationId:str, samlRoleId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Saml Roles


**List the SAML roles for this organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSamlRoles --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSamlRoles(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Snmp


**Return the SNMP settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki organizations getOrganizationSnmp --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSnmp(organizationId:str):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Appliances By Utilization


**Return the top 10 appliances sorted by utilization over given time range.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopAppliancesByUtilization --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopAppliancesByUtilization --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopAppliancesByUtilization(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Clients By Usage


**Return metrics for organization's top 10 clients by data usage (in mb) over given time range.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopClientsByUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopClientsByUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopClientsByUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Clients Manufacturers By Usage


**Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopClientsManufacturersByUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopClientsManufacturersByUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopClientsManufacturersByUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Devices By Usage


**Return metrics for organization's top 10 devices sorted by data usage over given time range**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopDevicesByUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopDevicesByUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopDevicesByUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Devices Models By Usage


**Return metrics for organization's top 10 device models sorted by data usage over given time range**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopDevicesModelsByUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopDevicesModelsByUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopDevicesModelsByUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Ssids By Usage


**Return metrics for organization's top 10 ssids by data usage over given time range**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopSsidsByUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopSsidsByUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopSsidsByUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Summary Top Switches By Energy Usage


**Return metrics for organization's top 10 switches by energy usage over given time range**

https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

##### Arguments
- `--organizationId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki organizations getOrganizationSummaryTopSwitchesByEnergyUsage --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationSummaryTopSwitchesByEnergyUsage --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSummaryTopSwitchesByEnergyUsage(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Uplinks Statuses


**List the uplink status of every Meraki MX, MG and Z series devices in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- `--serials` (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- `--iccids` (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.


##### Example:
```
meraki organizations getOrganizationUplinksStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationUplinksStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationUplinksStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Webhooks Alert Types


**Return a list of alert types to be used with managing webhook alerts**

https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

##### Arguments
- `--organizationId` (string): (required)
- `--productType` (string): Filter sample alerts to a specific product type


##### Example:
```
meraki organizations getOrganizationWebhooksAlertTypes --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationWebhooksAlertTypes --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationWebhooksAlertTypes(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organization Webhooks Logs


**Return the log of webhook POSTs sent**

https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--url` (string): The URL the webhook was sent to


##### Example:
```
meraki organizations getOrganizationWebhooksLogs --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations getOrganizationWebhooksLogs --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationWebhooksLogs(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Organizations Get Organizations


**List the organizations that the user has privileges on**

https://developer.cisco.com/meraki/api-v1/#!get-organizations

##### Arguments


##### Example:
```
meraki organizations getOrganizations
````

##### Method Code:
```python
def getOrganizations():
    # Code
````



----------------------------------------
## Organizations Move Organization Licenses


**Move licenses to another organization**

https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

##### Arguments
- `--organizationId` (string): (required)
- `--destOrganizationId` (string): The ID of the organization to move the licenses to
- `--licenseIds` (array): A list of IDs of licenses to move to the new organization


##### Example:
```
meraki organizations moveOrganizationLicenses --organizationId 'STRING' --destOrganizationId 'STRING' --licenseIds ITEM
````

##### Method Code:
```python
def moveOrganizationLicenses(organizationId:str, destOrganizationId:str, licenseIds:list):
    # Code
````



----------------------------------------
## Organizations Move Organization Licenses Seats


**Move SM seats to another organization**

https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--destOrganizationId` (string): The ID of the organization to move the SM seats to
- `--licenseId` (string): The ID of the SM license to move the seats from
- `--seatCount` (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license


##### Example:
```
meraki organizations moveOrganizationLicensesSeats --organizationId 'STRING' --destOrganizationId 'STRING' --licenseId 'STRING' --seatCount INT
````

##### Method Code:
```python
def moveOrganizationLicensesSeats(organizationId:str, destOrganizationId:str, licenseId:str, seatCount:int):
    # Code
````



----------------------------------------
## Organizations Release From Organization Inventory


**Release a list of claimed devices from an organization.**

https://developer.cisco.com/meraki/api-v1/#!release-from-organization-inventory

##### Arguments
- `--organizationId` (string): (required)
- `--serials` (array): Serials of the devices that should be released


##### Example:
```
meraki organizations releaseFromOrganizationInventory --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations releaseFromOrganizationInventory --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def releaseFromOrganizationInventory(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Renew Organization Licenses Seats


**Renew SM seats of a license**

https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

##### Arguments
- `--organizationId` (string): (required)
- `--licenseIdToRenew` (string): The ID of the SM license to renew. This license must already be assigned to an SM network
- `--unusedLicenseId` (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'


##### Example:
```
meraki organizations renewOrganizationLicensesSeats --organizationId 'STRING' --licenseIdToRenew 'STRING' --unusedLicenseId 'STRING'
````

##### Method Code:
```python
def renewOrganizationLicensesSeats(organizationId:str, licenseIdToRenew:str, unusedLicenseId:str):
    # Code
````



----------------------------------------
## Organizations Update Organization


**Update an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization

##### Arguments
- `--organizationId` (string): (required)
- `--name` (string): The name of the organization
- `--management` (object): Information about the organization's management system
- `--api` (object): API-specific settings


##### Example:
```
meraki organizations updateOrganization --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganization --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganization(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Action Batch


**Update an action batch**

https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch

##### Arguments
- `--organizationId` (string): (required)
- `--actionBatchId` (string): (required)
- `--confirmed` (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
- `--synchronous` (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.


##### Example:
```
meraki organizations updateOrganizationActionBatch --organizationId 'STRING' --actionBatchId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationActionBatch --organizationId 'STRING' --actionBatchId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationActionBatch(organizationId:str, actionBatchId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Adaptive Policy Acl


**Updates an adaptive policy ACL**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

##### Arguments
- `--organizationId` (string): (required)
- `--aclId` (string): (required)
- `--name` (string): Name of the adaptive policy ACL
- `--description` (string): Description of the adaptive policy ACL
- `--rules` (array): An ordered array of the adaptive policy ACL rules. An empty array will clear the rules.
- `--ipVersion` (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'


##### Example:
```
meraki organizations updateOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAdaptivePolicyAcl --organizationId 'STRING' --aclId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyAcl(organizationId:str, aclId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Adaptive Policy Group


**Updates an adaptive policy group**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)
- `--name` (string): Name of the group
- `--sgt` (integer): SGT value of the group
- `--description` (string): Description of the group
- `--policyObjects` (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute)


##### Example:
```
meraki organizations updateOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAdaptivePolicyGroup --organizationId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyGroup(organizationId:str, id:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Adaptive Policy Policy


**Update an Adaptive Policy**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

##### Arguments
- `--organizationId` (string): (required)
- `--id` (string): (required)
- `--sourceGroup` (object): The source adaptive policy group (requires one unique attribute)
- `--destinationGroup` (object): The destination adaptive policy group (requires one unique attribute)
- `--acls` (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
- `--lastEntryRule` (string): The rule to apply if there is no matching ACL


##### Example:
```
meraki organizations updateOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAdaptivePolicyPolicy --organizationId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicyPolicy(organizationId:str, id:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Adaptive Policy Settings


**Update global adaptive policy settings**

https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

##### Arguments
- `--organizationId` (string): (required)
- `--enabledNetworks` (array): List of network IDs with adaptive policy enabled


##### Example:
```
meraki organizations updateOrganizationAdaptivePolicySettings --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAdaptivePolicySettings --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdaptivePolicySettings(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Admin


**Update an administrator**

https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

##### Arguments
- `--organizationId` (string): (required)
- `--adminId` (string): (required)
- `--name` (string): The name of the dashboard administrator
- `--orgAccess` (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
- `--tags` (array): The list of tags that the dashboard administrator has privileges on
- `--networks` (array): The list of networks that the dashboard administrator has privileges on


##### Example:
```
meraki organizations updateOrganizationAdmin --organizationId 'STRING' --adminId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAdmin --organizationId 'STRING' --adminId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAdmin(organizationId:str, adminId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Alerts Profile


**Update an organization-wide alert config**

https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

##### Arguments
- `--organizationId` (string): (required)
- `--alertConfigId` (string): (required)
- `--enabled` (boolean): Is the alert config enabled
- `--type` (string): The alert type
- `--alertCondition` (object): The conditions that determine if the alert triggers
- `--recipients` (object): List of recipients that will recieve the alert.
- `--networkTags` (array): Networks with these tags will be monitored for the alert
- `--description` (string): User supplied description of the alert


##### Example:
```
meraki organizations updateOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationAlertsProfile --organizationId 'STRING' --alertConfigId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationAlertsProfile(organizationId:str, alertConfigId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Branding Policies Priorities


**Update the priority ordering of an organization's branding policies.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyIds` (array):       An ordered list of branding policy IDs that determines the priority order of how to apply the policies



##### Example:
```
meraki organizations updateOrganizationBrandingPoliciesPriorities --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationBrandingPoliciesPriorities --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationBrandingPoliciesPriorities(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Branding Policy


**Update a branding policy**

https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

##### Arguments
- `--organizationId` (string): (required)
- `--brandingPolicyId` (string): (required)
- `--name` (string): Name of the Dashboard branding policy.
- `--enabled` (boolean): Boolean indicating whether this policy is enabled.
- `--adminSettings` (object): Settings for describing which kinds of admins this policy applies to.
- `--helpSettings` (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.

- `--customLogo` (object): Properties describing the custom logo attached to the branding policy.


##### Example:
```
meraki organizations updateOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationBrandingPolicy --organizationId 'STRING' --brandingPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationBrandingPolicy(organizationId:str, brandingPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Config Template


**Update a configuration template**

https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--name` (string): The name of the configuration template
- `--timeZone` (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>


##### Example:
```
meraki organizations updateOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationConfigTemplate --organizationId 'STRING' --configTemplateId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationConfigTemplate(organizationId:str, configTemplateId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Early Access Features Opt In


**Update an early access feature opt-in for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

##### Arguments
- `--organizationId` (string): (required)
- `--optInId` (string): (required)
- `--limitScopeToNetworks` (array): A list of network IDs to apply the opt-in to


##### Example:
```
meraki organizations updateOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationEarlyAccessFeaturesOptIn --organizationId 'STRING' --optInId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationEarlyAccessFeaturesOptIn(organizationId:str, optInId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization License


**Update a license**

https://developer.cisco.com/meraki/api-v1/#!update-organization-license

##### Arguments
- `--organizationId` (string): (required)
- `--licenseId` (string): (required)
- `--deviceSerial` (string): The serial number of the device to assign this license to. Set this to  null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.


##### Example:
```
meraki organizations updateOrganizationLicense --organizationId 'STRING' --licenseId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationLicense --organizationId 'STRING' --licenseId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationLicense(organizationId:str, licenseId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Login Security


**Update the login security settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

##### Arguments
- `--organizationId` (string): (required)
- `--enforcePasswordExpiration` (boolean): Boolean indicating whether users are forced to change their password every X number of days.
- `--passwordExpirationDays` (integer): Number of days after which users will be forced to change their password.
- `--enforceDifferentPasswords` (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
- `--numDifferentPasswords` (integer): Number of recent passwords that new password must be distinct from.
- `--enforceStrongPasswords` (boolean): Boolean indicating whether users will be forced to choose strong passwords for their accounts. Strong passwords are at least 8 characters that contain 3 of the following: number, uppercase letter, lowercase letter, and symbol
- `--enforceAccountLockout` (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
- `--accountLockoutAttempts` (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
- `--enforceIdleTimeout` (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
- `--idleTimeoutMinutes` (integer): Number of minutes users can remain idle before being logged out of their accounts.
- `--enforceTwoFactorAuth` (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the authenticator application.
- `--enforceLoginIpRanges` (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
- `--loginIpRanges` (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
- `--apiAuthentication` (object): Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.


##### Example:
```
meraki organizations updateOrganizationLoginSecurity --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationLoginSecurity --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationLoginSecurity(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Policy Object


**Updates a Policy Object.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectId` (string): (required)
- `--name` (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--cidr` (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
- `--fqdn` (string): Fully qualified domain name of policy object (e.g. "example.com")
- `--mask` (string): Mask of a policy object (e.g. "255.255.0.0")
- `--ip` (string): IP Address of a policy object (e.g. "1.2.3.4")
- `--groupIds` (array): The IDs of policy object groups the policy object belongs to


##### Example:
```
meraki organizations updateOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationPolicyObject --organizationId 'STRING' --policyObjectId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationPolicyObject(organizationId:str, policyObjectId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Policy Objects Group


**Updates a Policy Object Group.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

##### Arguments
- `--organizationId` (string): (required)
- `--policyObjectGroupId` (string): (required)
- `--name` (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
- `--objectIds` (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)


##### Example:
```
meraki organizations updateOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationPolicyObjectsGroup --organizationId 'STRING' --policyObjectGroupId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationPolicyObjectsGroup(organizationId:str, policyObjectGroupId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Saml


**Updates the SAML SSO enabled settings for an organization.**

https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

##### Arguments
- `--organizationId` (string): (required)
- `--enabled` (boolean): Boolean for updating SAML SSO enabled settings.


##### Example:
```
meraki organizations updateOrganizationSaml --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationSaml --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationSaml(organizationId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Saml Idp


**Update a SAML IdP in your organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

##### Arguments
- `--organizationId` (string): (required)
- `--idpId` (string): (required)
- `--x509certSha1Fingerprint` (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- `--sloLogoutUrl` (string): Dashboard will redirect users to this URL when they sign out.


##### Example:
```
meraki organizations updateOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationSamlIdp --organizationId 'STRING' --idpId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationSamlIdp(organizationId:str, idpId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Saml Role


**Update a SAML role**

https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

##### Arguments
- `--organizationId` (string): (required)
- `--samlRoleId` (string): (required)
- `--role` (string): The role of the SAML administrator
- `--orgAccess` (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise'
- `--tags` (array): The list of tags that the SAML administrator has privleges on
- `--networks` (array): The list of networks that the SAML administrator has privileges on


##### Example:
```
meraki organizations updateOrganizationSamlRole --organizationId 'STRING' --samlRoleId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationSamlRole --organizationId 'STRING' --samlRoleId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationSamlRole(organizationId:str, samlRoleId:str, **kwargs):
    # Code
````



----------------------------------------
## Organizations Update Organization Snmp


**Update the SNMP settings for an organization**

https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

##### Arguments
- `--organizationId` (string): (required)
- `--v2cEnabled` (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
- `--v3Enabled` (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
- `--v3AuthMode` (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
- `--v3AuthPass` (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
- `--v3PrivMode` (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
- `--v3PrivPass` (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
- `--peerIps` (array): The list of IPv4 addresses that are allowed to access the SNMP server.


##### Example:
```
meraki organizations updateOrganizationSnmp --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki organizations updateOrganizationSnmp --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationSnmp(organizationId:str, **kwargs):
    # Code
````

# Sensor


----------------------------------------
## Sensor Create Network Sensor Alerts Profile


**Creates a sensor alert profile for a network.**

https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the sensor alert profile.
- `--conditions` (array): List of conditions that will cause the profile to send an alert.
- `--schedule` (object): The sensor schedule to use with the alert profile.
- `--recipients` (object): List of recipients that will recieve the alert.
- `--serials` (array): List of device serials assigned to this sensor alert profile.


##### Example:
```
meraki sensor createNetworkSensorAlertsProfile --networkId 'STRING' --name 'STRING' --conditions ITEM --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor createNetworkSensorAlertsProfile --networkId 'STRING' --name 'STRING' --conditions ITEM --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSensorAlertsProfile(networkId:str, name:str, conditions:list, **kwargs):
    # Code
````



----------------------------------------
## Sensor Delete Network Sensor Alerts Profile


**Deletes a sensor alert profile from a network.**

https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki sensor deleteNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def deleteNetworkSensorAlertsProfile(networkId:str, id:str):
    # Code
````



----------------------------------------
## Sensor Get Device Sensor Relationships


**List the sensor roles for a given sensor or camera device.**

https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-relationships

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki sensor getDeviceSensorRelationships --serial 'STRING'
````

##### Method Code:
```python
def getDeviceSensorRelationships(serial:str):
    # Code
````



----------------------------------------
## Sensor Get Network Sensor Alerts Current Overview By Metric


**Return an overview of currently alerting sensors by metric**

https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-current-overview-by-metric

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki sensor getNetworkSensorAlertsCurrentOverviewByMetric --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSensorAlertsCurrentOverviewByMetric(networkId:str):
    # Code
````



----------------------------------------
## Sensor Get Network Sensor Alerts Overview By Metric


**Return an overview of alert occurrences over a timespan, by metric**

https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-overview-by-metric

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--interval` (integer): The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.


##### Example:
```
meraki sensor getNetworkSensorAlertsOverviewByMetric --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor getNetworkSensorAlertsOverviewByMetric --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSensorAlertsOverviewByMetric(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sensor Get Network Sensor Alerts Profile


**Show details of a sensor alert profile for a network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): (required)


##### Example:
```
meraki sensor getNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING'
````

##### Method Code:
```python
def getNetworkSensorAlertsProfile(networkId:str, id:str):
    # Code
````



----------------------------------------
## Sensor Get Network Sensor Alerts Profiles


**Lists all sensor alert profiles for a network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profiles

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki sensor getNetworkSensorAlertsProfiles --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSensorAlertsProfiles(networkId:str):
    # Code
````



----------------------------------------
## Sensor Get Network Sensor Relationships


**List the sensor roles for devices in a given network**

https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-relationships

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki sensor getNetworkSensorRelationships --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSensorRelationships(networkId:str):
    # Code
````



----------------------------------------
## Sensor Get Organization Sensor Readings History


**Return all reported readings from sensors in a given timespan, sorted by timestamp**

https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
- `--networkIds` (array): Optional parameter to filter readings by network.
- `--serials` (array): Optional parameter to filter readings by sensor.
- `--metrics` (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.


##### Example:
```
meraki sensor getOrganizationSensorReadingsHistory --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor getOrganizationSensorReadingsHistory --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSensorReadingsHistory(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sensor Get Organization Sensor Readings Latest


**Return the latest available reading for each metric from each sensor, sorted by sensor serial**

https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter readings by network.
- `--serials` (array): Optional parameter to filter readings by sensor.
- `--metrics` (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.


##### Example:
```
meraki sensor getOrganizationSensorReadingsLatest --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor getOrganizationSensorReadingsLatest --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSensorReadingsLatest(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sensor Update Device Sensor Relationships


**Assign one or more sensor roles to a given sensor or camera device.**

https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

##### Arguments
- `--serial` (string): (required)
- `--livestream` (object): A role defined between an MT sensor and an MV camera that adds the camera's livestream to the sensor's details page. Snapshots from the camera will also appear in alert notifications that the sensor triggers.


##### Example:
```
meraki sensor updateDeviceSensorRelationships --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor updateDeviceSensorRelationships --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSensorRelationships(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Sensor Update Network Sensor Alerts Profile


**Updates a sensor alert profile for a network.**

https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

##### Arguments
- `--networkId` (string): (required)
- `--id` (string): (required)
- `--name` (string): Name of the sensor alert profile.
- `--schedule` (object): The sensor schedule to use with the alert profile.
- `--conditions` (array): List of conditions that will cause the profile to send an alert.
- `--recipients` (object): List of recipients that will recieve the alert.
- `--serials` (array): List of device serials assigned to this sensor alert profile.


##### Example:
```
meraki sensor updateNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sensor updateNetworkSensorAlertsProfile --networkId 'STRING' --id 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSensorAlertsProfile(networkId:str, id:str, **kwargs):
    # Code
````

# Sm


----------------------------------------
## Sm Checkin Network Sm Devices


**Force check-in a set of devices**

https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices

##### Arguments
- `--networkId` (string): (required)
- `--wifiMacs` (array): The wifiMacs of the devices to be checked-in.
- `--ids` (array): The ids of the devices to be checked-in.
- `--serials` (array): The serials of the devices to be checked-in.
- `--scope` (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be checked-in.


##### Example:
```
meraki sm checkinNetworkSmDevices --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm checkinNetworkSmDevices --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def checkinNetworkSmDevices(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Create Network Sm Bypass Activation Lock Attempt


**Bypass activation lock attempt**

https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

##### Arguments
- `--networkId` (string): (required)
- `--ids` (array): The ids of the devices to attempt activation lock bypass.


##### Example:
```
meraki sm createNetworkSmBypassActivationLockAttempt --networkId 'STRING' --ids ITEM
````

##### Method Code:
```python
def createNetworkSmBypassActivationLockAttempt(networkId:str, ids:list):
    # Code
````



----------------------------------------
## Sm Create Network Sm Target Group


**Add a target group**

https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of this target group
- `--scope` (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.


##### Example:
```
meraki sm createNetworkSmTargetGroup --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm createNetworkSmTargetGroup --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSmTargetGroup(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Delete Network Sm Target Group


**Delete a target group from a network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

##### Arguments
- `--networkId` (string): (required)
- `--targetGroupId` (string): (required)


##### Example:
```
meraki sm deleteNetworkSmTargetGroup --networkId 'STRING' --targetGroupId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSmTargetGroup(networkId:str, targetGroupId:str):
    # Code
````



----------------------------------------
## Sm Delete Network Sm User Access Device


**Delete a User Access Device**

https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

##### Arguments
- `--networkId` (string): (required)
- `--userAccessDeviceId` (string): (required)


##### Example:
```
meraki sm deleteNetworkSmUserAccessDevice --networkId 'STRING' --userAccessDeviceId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSmUserAccessDevice(networkId:str, userAccessDeviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Bypass Activation Lock Attempt


**Bypass activation lock attempt status**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

##### Arguments
- `--networkId` (string): (required)
- `--attemptId` (string): (required)


##### Example:
```
meraki sm getNetworkSmBypassActivationLockAttempt --networkId 'STRING' --attemptId 'STRING'
````

##### Method Code:
```python
def getNetworkSmBypassActivationLockAttempt(networkId:str, attemptId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Cellular Usage History


**Return the client's daily cellular data usage history**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceCellularUsageHistory --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceCellularUsageHistory(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Certs


**List the certs on a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceCerts --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceCerts(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Connectivity


**Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmDeviceConnectivity --networkId 'STRING' --deviceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmDeviceConnectivity --networkId 'STRING' --deviceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmDeviceConnectivity(networkId:str, deviceId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Desktop Logs


**Return historical records of various Systems Manager network connection details for desktop devices.**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmDeviceDesktopLogs --networkId 'STRING' --deviceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmDeviceDesktopLogs --networkId 'STRING' --deviceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmDeviceDesktopLogs(networkId:str, deviceId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Device Command Logs


**Return historical records of commands sent to Systems Manager devices**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmDeviceDeviceCommandLogs --networkId 'STRING' --deviceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmDeviceDeviceCommandLogs --networkId 'STRING' --deviceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmDeviceDeviceCommandLogs(networkId:str, deviceId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Device Profiles


**Get the installed profiles associated with a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceDeviceProfiles --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceDeviceProfiles(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Network Adapters


**List the network adapters of a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceNetworkAdapters --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceNetworkAdapters(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Performance History


**Return historical records of various Systems Manager client metrics for desktop devices.**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmDevicePerformanceHistory --networkId 'STRING' --deviceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmDevicePerformanceHistory --networkId 'STRING' --deviceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmDevicePerformanceHistory(networkId:str, deviceId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Restrictions


**List the restrictions on a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceRestrictions --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceRestrictions(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Security Centers


**List the security centers on a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceSecurityCenters --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceSecurityCenters(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Softwares


**Get a list of softwares associated with a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceSoftwares --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceSoftwares(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Device Wlan Lists


**List the saved SSID names on a device**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm getNetworkSmDeviceWlanLists --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def getNetworkSmDeviceWlanLists(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Devices


**List the devices enrolled in an SM network with various specified fields and filters**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--fields` (array): Additional fields that will be displayed for each device.
The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url.
- `--wifiMacs` (array): Filter devices by wifi mac(s).
- `--serials` (array): Filter devices by serial(s).
- `--ids` (array): Filter devices by id(s).
- `--scope` (array): Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmDevices --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmDevices --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmDevices(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Profiles


**List all profiles in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki sm getNetworkSmProfiles --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSmProfiles(networkId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Target Group


**Return a target group**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

##### Arguments
- `--networkId` (string): (required)
- `--targetGroupId` (string): (required)
- `--withDetails` (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response


##### Example:
```
meraki sm getNetworkSmTargetGroup --networkId 'STRING' --targetGroupId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmTargetGroup --networkId 'STRING' --targetGroupId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmTargetGroup(networkId:str, targetGroupId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Target Groups


**List the target groups in this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

##### Arguments
- `--networkId` (string): (required)
- `--withDetails` (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response


##### Example:
```
meraki sm getNetworkSmTargetGroups --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmTargetGroups --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmTargetGroups(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm Trusted Access Configs


**List Trusted Access Configs**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-trusted-access-configs

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmTrustedAccessConfigs --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmTrustedAccessConfigs --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmTrustedAccessConfigs(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm User Access Devices


**List User Access Devices and its Trusted Access Connections**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-access-devices

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki sm getNetworkSmUserAccessDevices --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmUserAccessDevices --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmUserAccessDevices(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Sm Get Network Sm User Device Profiles


**Get the profiles associated with a user**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

##### Arguments
- `--networkId` (string): (required)
- `--userId` (string): (required)


##### Example:
```
meraki sm getNetworkSmUserDeviceProfiles --networkId 'STRING' --userId 'STRING'
````

##### Method Code:
```python
def getNetworkSmUserDeviceProfiles(networkId:str, userId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm User Softwares


**Get a list of softwares associated with a user**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

##### Arguments
- `--networkId` (string): (required)
- `--userId` (string): (required)


##### Example:
```
meraki sm getNetworkSmUserSoftwares --networkId 'STRING' --userId 'STRING'
````

##### Method Code:
```python
def getNetworkSmUserSoftwares(networkId:str, userId:str):
    # Code
````



----------------------------------------
## Sm Get Network Sm Users


**List the owners in an SM network with various specified fields and filters**

https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users

##### Arguments
- `--networkId` (string): (required)
- `--ids` (array): Filter users by id(s).
- `--usernames` (array): Filter users by username(s).
- `--emails` (array): Filter users by email(s).
- `--scope` (array): Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.


##### Example:
```
meraki sm getNetworkSmUsers --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm getNetworkSmUsers --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSmUsers(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Get Organization Sm Apns Cert


**Get the organization's APNS certificate**

https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki sm getOrganizationSmApnsCert --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSmApnsCert(organizationId:str):
    # Code
````



----------------------------------------
## Sm Get Organization Sm Vpp Account


**Get a hash containing the unparsed token of the VPP account with the given ID**

https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

##### Arguments
- `--organizationId` (string): (required)
- `--vppAccountId` (string): (required)


##### Example:
```
meraki sm getOrganizationSmVppAccount --organizationId 'STRING' --vppAccountId 'STRING'
````

##### Method Code:
```python
def getOrganizationSmVppAccount(organizationId:str, vppAccountId:str):
    # Code
````



----------------------------------------
## Sm Get Organization Sm Vpp Accounts


**List the VPP accounts in the organization**

https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

##### Arguments
- `--organizationId` (string): (required)


##### Example:
```
meraki sm getOrganizationSmVppAccounts --organizationId 'STRING'
````

##### Method Code:
```python
def getOrganizationSmVppAccounts(organizationId:str):
    # Code
````



----------------------------------------
## Sm Lock Network Sm Devices


**Lock a set of devices**

https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices

##### Arguments
- `--networkId` (string): (required)
- `--wifiMacs` (array): The wifiMacs of the devices to be locked.
- `--ids` (array): The ids of the devices to be locked.
- `--serials` (array): The serials of the devices to be locked.
- `--scope` (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.
- `--pin` (integer): The pin number for locking macOS devices (a six digit number). Required only for macOS devices.


##### Example:
```
meraki sm lockNetworkSmDevices --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm lockNetworkSmDevices --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def lockNetworkSmDevices(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Modify Network Sm Devices Tags


**Add, delete, or update the tags of a set of devices**

https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags

##### Arguments
- `--networkId` (string): (required)
- `--tags` (array): The tags to be added, deleted, or updated.
- `--updateAction` (string): One of add, delete, or update. Only devices that have been modified will be returned.
- `--wifiMacs` (array): The wifiMacs of the devices to be modified.
- `--ids` (array): The ids of the devices to be modified.
- `--serials` (array): The serials of the devices to be modified.
- `--scope` (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.


##### Example:
```
meraki sm modifyNetworkSmDevicesTags --networkId 'STRING' --tags ITEM --updateAction 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm modifyNetworkSmDevicesTags --networkId 'STRING' --tags ITEM --updateAction 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def modifyNetworkSmDevicesTags(networkId:str, tags:list, updateAction:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Move Network Sm Devices


**Move a set of devices to a new network**

https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices

##### Arguments
- `--networkId` (string): (required)
- `--newNetwork` (string): The new network to which the devices will be moved.
- `--wifiMacs` (array): The wifiMacs of the devices to be moved.
- `--ids` (array): The ids of the devices to be moved.
- `--serials` (array): The serials of the devices to be moved.
- `--scope` (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be moved.


##### Example:
```
meraki sm moveNetworkSmDevices --networkId 'STRING' --newNetwork 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm moveNetworkSmDevices --networkId 'STRING' --newNetwork 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def moveNetworkSmDevices(networkId:str, newNetwork:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Refresh Network Sm Device Details


**Refresh the details of a device**

https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm refreshNetworkSmDeviceDetails --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def refreshNetworkSmDeviceDetails(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Unenroll Network Sm Device


**Unenroll a device**

https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

##### Arguments
- `--networkId` (string): (required)
- `--deviceId` (string): (required)


##### Example:
```
meraki sm unenrollNetworkSmDevice --networkId 'STRING' --deviceId 'STRING'
````

##### Method Code:
```python
def unenrollNetworkSmDevice(networkId:str, deviceId:str):
    # Code
````



----------------------------------------
## Sm Update Network Sm Devices Fields


**Modify the fields of a device**

https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

##### Arguments
- `--networkId` (string): (required)
- `--deviceFields` (object): The new fields of the device. Each field of this object is optional.
- `--wifiMac` (string): The wifiMac of the device to be modified.
- `--id` (string): The id of the device to be modified.
- `--serial` (string): The serial of the device to be modified.


##### Example:
```
meraki sm updateNetworkSmDevicesFields --networkId 'STRING' --deviceFields JSON_STRING --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm updateNetworkSmDevicesFields --networkId 'STRING' --deviceFields JSON_STRING --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSmDevicesFields(networkId:str, deviceFields:dict, **kwargs):
    # Code
````



----------------------------------------
## Sm Update Network Sm Target Group


**Update a target group**

https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

##### Arguments
- `--networkId` (string): (required)
- `--targetGroupId` (string): (required)
- `--name` (string): The name of this target group
- `--scope` (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.


##### Example:
```
meraki sm updateNetworkSmTargetGroup --networkId 'STRING' --targetGroupId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm updateNetworkSmTargetGroup --networkId 'STRING' --targetGroupId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSmTargetGroup(networkId:str, targetGroupId:str, **kwargs):
    # Code
````



----------------------------------------
## Sm Wipe Network Sm Devices


**Wipe a device**

https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

##### Arguments
- `--networkId` (string): (required)
- `--wifiMac` (string): The wifiMac of the device to be wiped.
- `--id` (string): The id of the device to be wiped.
- `--serial` (string): The serial of the device to be wiped.
- `--pin` (integer): The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.


##### Example:
```
meraki sm wipeNetworkSmDevices --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki sm wipeNetworkSmDevices --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def wipeNetworkSmDevices(networkId:str, **kwargs):
    # Code
````

# Switch


----------------------------------------
## Switch Add Network Switch Stack


**Add a switch to a stack**

https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--serial` (string): The serial of the switch to be added


##### Example:
```
meraki switch addNetworkSwitchStack --networkId 'STRING' --switchStackId 'STRING' --serial 'STRING'
````

##### Method Code:
```python
def addNetworkSwitchStack(networkId:str, switchStackId:str, serial:str):
    # Code
````



----------------------------------------
## Switch Clone Organization Switch Devices


**Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**

https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

##### Arguments
- `--organizationId` (string): (required)
- `--sourceSerial` (string): Serial number of the source switch (must be on a network not bound to a template)
- `--targetSerials` (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)


##### Example:
```
meraki switch cloneOrganizationSwitchDevices --organizationId 'STRING' --sourceSerial 'STRING' --targetSerials ITEM
````

##### Method Code:
```python
def cloneOrganizationSwitchDevices(organizationId:str, sourceSerial:str, targetSerials:list):
    # Code
````



----------------------------------------
## Switch Create Device Switch Routing Interface


**Create a layer 3 interface for a switch**

https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ospfV3` (object): The OSPFv3 routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki switch createDeviceSwitchRoutingInterface --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createDeviceSwitchRoutingInterface --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceSwitchRoutingInterface(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Device Switch Routing Static Route


**Create a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--name` (string): Name or description for layer 3 static route
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki switch createDeviceSwitchRoutingStaticRoute --serial 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createDeviceSwitchRoutingStaticRoute --serial 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createDeviceSwitchRoutingStaticRoute(serial:str, subnet:str, nextHopIp:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Access Policy


**Create an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): Name of the access policy
- `--radiusServers` (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- `--radiusTestingEnabled` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusCoaSupportEnabled` (boolean): Change of authentication for RADIUS re-authentication and disconnection
- `--radiusAccountingEnabled` (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- `--hostMode` (string): Choose the Host Mode for the access policy.
- `--urlRedirectWalledGardenEnabled` (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- `--radius` (object): Object for RADIUS Settings
- `--guestPortBouncing` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusAccountingServers` (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- `--radiusGroupAttribute` (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
- `--accessPolicyType` (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- `--increaseAccessSpeed` (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- `--guestVlanId` (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- `--dot1x` (object): 802.1x Settings
- `--voiceVlanClients` (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- `--urlRedirectWalledGardenRanges` (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication


##### Example:
```
meraki switch createNetworkSwitchAccessPolicy --networkId 'STRING' --name 'STRING' --radiusServers ITEM --radiusTestingEnabled --radiusCoaSupportEnabled --radiusAccountingEnabled --hostMode 'STRING' --urlRedirectWalledGardenEnabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchAccessPolicy --networkId 'STRING' --name 'STRING' --radiusServers ITEM --radiusTestingEnabled --radiusCoaSupportEnabled --radiusAccountingEnabled --hostMode 'STRING' --urlRedirectWalledGardenEnabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchAccessPolicy(networkId:str, name:str, radiusServers:list, radiusTestingEnabled:bool, radiusCoaSupportEnabled:bool, radiusAccountingEnabled:bool, hostMode:str, urlRedirectWalledGardenEnabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Add a server to be trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--mac` (string): The mac address of the trusted server being added
- `--vlan` (integer): The VLAN of the trusted server being added. It must be between 1 and 4094
- `--ipv4` (object): The IPv4 attributes of the trusted server being added


##### Example:
```
meraki switch createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --mac 'STRING' --vlan INT --ipv4 JSON_STRING
````

##### Method Code:
```python
def createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, mac:str, vlan:int, ipv4:dict):
    # Code
````



----------------------------------------
## Switch Create Network Switch Link Aggregation


**Create a link aggregation group**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--switchPorts` (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
- `--switchProfilePorts` (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.


##### Example:
```
meraki switch createNetworkSwitchLinkAggregation --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchLinkAggregation --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchLinkAggregation(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Port Schedule


**Add a switch port schedule**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name for your port schedule. Required
- `--portSchedule` (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
When it's empty, default schedule with all days of a week are configured.
Any unspecified day in the schedule is added as a default schedule configuration of the day.



##### Example:
```
meraki switch createNetworkSwitchPortSchedule --networkId 'STRING' --name 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchPortSchedule --networkId 'STRING' --name 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchPortSchedule(networkId:str, name:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Qos Rule


**Add a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--vlan` (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- `--protocol` (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY"
- `--srcPort` (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--srcPortRange` (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dstPort` (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--dstPortRange` (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dscp` (integer): DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0


##### Example:
```
meraki switch createNetworkSwitchQosRule --networkId 'STRING' --vlan INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchQosRule --networkId 'STRING' --vlan INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchQosRule(networkId:str, vlan:int, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Routing Multicast Rendezvous Point


**Create a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--interfaceIp` (string): The IP address of the interface where the RP needs to be created.
- `--multicastGroup` (string): 'Any', or the IP address of a multicast group


##### Example:
```
meraki switch createNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --interfaceIp 'STRING' --multicastGroup 'STRING'
````

##### Method Code:
```python
def createNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, interfaceIp:str, multicastGroup:str):
    # Code
````



----------------------------------------
## Switch Create Network Switch Stack


**Create a stack**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new stack
- `--serials` (array): An array of switch serials to be added into the new stack


##### Example:
```
meraki switch createNetworkSwitchStack --networkId 'STRING' --name 'STRING' --serials ITEM
````

##### Method Code:
```python
def createNetworkSwitchStack(networkId:str, name:str, serials:list):
    # Code
````



----------------------------------------
## Switch Create Network Switch Stack Routing Interface


**Create a layer 3 interface for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki switch createNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --name 'STRING' --vlanId INT --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --name 'STRING' --vlanId INT --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, name:str, vlanId:int, **kwargs):
    # Code
````



----------------------------------------
## Switch Create Network Switch Stack Routing Static Route


**Create a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--name` (string): Name or description for layer 3 static route
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki switch createNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch createNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --subnet 'STRING' --nextHopIp 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, subnet:str, nextHopIp:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Cycle Device Switch Ports


**Cycle a set of switch ports**

https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

##### Arguments
- `--serial` (string): (required)
- `--ports` (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]


##### Example:
```
meraki switch cycleDeviceSwitchPorts --serial 'STRING' --ports ITEM
````

##### Method Code:
```python
def cycleDeviceSwitchPorts(serial:str, ports:list):
    # Code
````



----------------------------------------
## Switch Delete Device Switch Routing Interface


**Delete a layer 3 interface from the switch**

https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch deleteDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def deleteDeviceSwitchRoutingInterface(serial:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Delete Device Switch Routing Static Route


**Delete a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki switch deleteDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def deleteDeviceSwitchRoutingStaticRoute(serial:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Access Policy


**Delete an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--accessPolicyNumber` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchAccessPolicy(networkId:str, accessPolicyNumber:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Remove a server from being trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--trustedServerId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, trustedServerId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Link Aggregation


**Split a link aggregation group into separate ports**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--linkAggregationId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchLinkAggregation(networkId:str, linkAggregationId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Port Schedule


**Delete a switch port schedule**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule

##### Arguments
- `--networkId` (string): (required)
- `--portScheduleId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchPortSchedule --networkId 'STRING' --portScheduleId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchPortSchedule(networkId:str, portScheduleId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Qos Rule


**Delete a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--qosRuleId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchQosRule(networkId:str, qosRuleId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Routing Multicast Rendezvous Point


**Delete a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--rendezvousPointId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --rendezvousPointId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, rendezvousPointId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Stack


**Delete a stack**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchStack --networkId 'STRING' --switchStackId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchStack(networkId:str, switchStackId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Stack Routing Interface


**Delete a layer 3 interface from a switch stack**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Delete Network Switch Stack Routing Static Route


**Delete a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki switch deleteNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def deleteNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Port


**Return a switch port**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

##### Arguments
- `--serial` (string): (required)
- `--portId` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchPort --serial 'STRING' --portId 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchPort(serial:str, portId:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Ports


**List the switch ports for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchPorts --serial 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchPorts(serial:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Ports Statuses


**Return the status for all the ports of a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.


##### Example:
```
meraki switch getDeviceSwitchPortsStatuses --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getDeviceSwitchPortsStatuses --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceSwitchPortsStatuses(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Get Device Switch Ports Statuses Packets


**Return the packet counters for all the ports of a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.


##### Example:
```
meraki switch getDeviceSwitchPortsStatusesPackets --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getDeviceSwitchPortsStatusesPackets --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceSwitchPortsStatusesPackets(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Get Device Switch Routing Interface


**Return a layer 3 interface for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchRoutingInterface(serial:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Routing Interface Dhcp


**Return a layer 3 interface DHCP configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchRoutingInterfaceDhcp --serial 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchRoutingInterfaceDhcp(serial:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Routing Interfaces


**List layer 3 interfaces for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchRoutingInterfaces --serial 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchRoutingInterfaces(serial:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Routing Static Route


**Return a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchRoutingStaticRoute(serial:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Routing Static Routes


**List layer 3 static routes for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchRoutingStaticRoutes --serial 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchRoutingStaticRoutes(serial:str):
    # Code
````



----------------------------------------
## Switch Get Device Switch Warm Spare


**Return warm spare configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki switch getDeviceSwitchWarmSpare --serial 'STRING'
````

##### Method Code:
```python
def getDeviceSwitchWarmSpare(serial:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Access Control Lists


**Return the access control lists for a MS network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchAccessControlLists --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchAccessControlLists(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Access Policies


**List the access policies for a switch network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchAccessPolicies --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchAccessPolicies(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Access Policy


**Return a specific access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--accessPolicyNumber` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchAccessPolicy(networkId:str, accessPolicyNumber:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Alternate Management Interface


**Return the switch alternate management interface for the network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchAlternateManagementInterface --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchAlternateManagementInterface(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Dhcp Server Policy


**Return the DHCP server settings**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchDhcpServerPolicy --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchDhcpServerPolicy(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Dhcp Server Policy Arp Inspection Trusted Servers


**Return the list of servers trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-trusted-servers

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki switch getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Switch Get Network Switch Dhcp Server Policy Arp Inspection Warnings By Device


**Return the devices that have a Dynamic ARP Inspection warning and their warnings**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-warnings-by-device

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki switch getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Switch Get Network Switch Dhcp V4 Servers Seen


**Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-v-4-servers-seen

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki switch getNetworkSwitchDhcpV4ServersSeen --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getNetworkSwitchDhcpV4ServersSeen --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkSwitchDhcpV4ServersSeen(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Switch Get Network Switch Dscp To Cos Mappings


**Return the DSCP to CoS mappings**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchDscpToCosMappings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchDscpToCosMappings(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Link Aggregations


**List link aggregation groups**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchLinkAggregations --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchLinkAggregations(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Mtu


**Return the MTU configuration**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchMtu --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchMtu(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Port Schedules


**List switch port schedules**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchPortSchedules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchPortSchedules(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Qos Rule


**Return a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--qosRuleId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchQosRule(networkId:str, qosRuleId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Qos Rules


**List quality of service rules**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchQosRules --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchQosRules(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Qos Rules Order


**Return the quality of service rule IDs by order in which they will be processed by the switch**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchQosRulesOrder --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchQosRulesOrder(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Routing Multicast


**Return multicast settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchRoutingMulticast --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchRoutingMulticast(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Routing Multicast Rendezvous Point


**Return a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--rendezvousPointId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --rendezvousPointId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, rendezvousPointId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Routing Multicast Rendezvous Points


**List multicast rendezvous points**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchRoutingMulticastRendezvousPoints --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchRoutingMulticastRendezvousPoints(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Routing Ospf


**Return layer 3 OSPF routing configuration**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchRoutingOspf --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchRoutingOspf(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Settings


**Returns the switch network settings**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchSettings(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack


**Show a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStack --networkId 'STRING' --switchStackId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStack(networkId:str, switchStackId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack Routing Interface


**Return a layer 3 interface from a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack Routing Interface Dhcp


**Return a layer 3 interface DHCP configuration for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStackRoutingInterfaceDhcp --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStackRoutingInterfaceDhcp(networkId:str, switchStackId:str, interfaceId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack Routing Interfaces


**List layer 3 interfaces for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStackRoutingInterfaces --networkId 'STRING' --switchStackId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStackRoutingInterfaces(networkId:str, switchStackId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack Routing Static Route


**Return a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--staticRouteId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, staticRouteId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stack Routing Static Routes


**List layer 3 static routes for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStackRoutingStaticRoutes --networkId 'STRING' --switchStackId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStackRoutingStaticRoutes(networkId:str, switchStackId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stacks


**List the switch stacks in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStacks --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStacks(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Storm Control


**Return the storm control configuration for a switch network**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStormControl --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStormControl(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Network Switch Stp


**Returns STP settings**

https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki switch getNetworkSwitchStp --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkSwitchStp(networkId:str):
    # Code
````



----------------------------------------
## Switch Get Organization Config Template Switch Profile Port


**Return a switch profile port**

https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--profileId` (string): (required)
- `--portId` (string): (required)


##### Example:
```
meraki switch getOrganizationConfigTemplateSwitchProfilePort --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING' --portId 'STRING'
````

##### Method Code:
```python
def getOrganizationConfigTemplateSwitchProfilePort(organizationId:str, configTemplateId:str, profileId:str, portId:str):
    # Code
````



----------------------------------------
## Switch Get Organization Config Template Switch Profile Ports


**Return all the ports of a switch profile**

https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--profileId` (string): (required)


##### Example:
```
meraki switch getOrganizationConfigTemplateSwitchProfilePorts --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING'
````

##### Method Code:
```python
def getOrganizationConfigTemplateSwitchProfilePorts(organizationId:str, configTemplateId:str, profileId:str):
    # Code
````



----------------------------------------
## Switch Get Organization Config Template Switch Profiles


**List the switch profiles for your switch template configuration**

https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)


##### Example:
```
meraki switch getOrganizationConfigTemplateSwitchProfiles --organizationId 'STRING' --configTemplateId 'STRING'
````

##### Method Code:
```python
def getOrganizationConfigTemplateSwitchProfiles(organizationId:str, configTemplateId:str):
    # Code
````



----------------------------------------
## Switch Get Organization Switch Ports By Switch


**List the switchports in an organization by switch**

https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): Optional parameter to filter switchports by network.
- `--portProfileIds` (array): Optional parameter to filter switchports belonging to the specified switchport profiles.
- `--name` (string): Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
- `--mac` (string): Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
- `--macs` (array): Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
- `--serial` (string): Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
- `--serials` (array): Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
- `--configurationUpdatedAfter` (string): Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.


##### Example:
```
meraki switch getOrganizationSwitchPortsBySwitch --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch getOrganizationSwitchPortsBySwitch --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationSwitchPortsBySwitch(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Switch Remove Network Switch Stack


**Remove a switch from a stack**

https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-stack

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--serial` (string): The serial of the switch to be removed


##### Example:
```
meraki switch removeNetworkSwitchStack --networkId 'STRING' --switchStackId 'STRING' --serial 'STRING'
````

##### Method Code:
```python
def removeNetworkSwitchStack(networkId:str, switchStackId:str, serial:str):
    # Code
````



----------------------------------------
## Switch Update Device Switch Port


**Update a switch port**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

##### Arguments
- `--serial` (string): (required)
- `--portId` (string): (required)
- `--name` (string): The name of the switch port.
- `--tags` (array): The list of tags of the switch port.
- `--enabled` (boolean): The status of the switch port.
- `--poeEnabled` (boolean): The PoE status of the switch port.
- `--type` (string): The type of the switch port ('trunk' or 'access').
- `--vlan` (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
- `--voiceVlan` (integer): The voice VLAN of the switch port. Only applicable to access ports.
- `--allowedVlans` (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
- `--isolationEnabled` (boolean): The isolation status of the switch port.
- `--rstpEnabled` (boolean): The rapid spanning tree protocol status.
- `--stpGuard` (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
- `--linkNegotiation` (string): The link speed for the switch port.
- `--portScheduleId` (string): The ID of the port schedule. A value of null will clear the port schedule.
- `--udld` (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- `--accessPolicyType` (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
- `--accessPolicyNumber` (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
- `--macAllowList` (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
- `--stickyMacAllowList` (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stickyMacAllowListLimit` (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stormControlEnabled` (boolean): The storm control status of the switch port.
- `--adaptivePolicyGroupId` (string): The adaptive policy group ID that will be used to tag traffic through this switch port. This ID must pre-exist during the configuration, else needs to be created using adaptivePolicy/groups API. Cannot be applied to a port on a switch bound to profile.
- `--peerSgtCapable` (boolean): If true, Peer SGT is enabled for traffic through this switch port. Applicable to trunk port only, not access port. Cannot be applied to a port on a switch bound to profile.
- `--flexibleStackingEnabled` (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
- `--daiTrusted` (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
- `--profile` (object): Profile attributes


##### Example:
```
meraki switch updateDeviceSwitchPort --serial 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateDeviceSwitchPort --serial 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchPort(serial:str, portId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Device Switch Routing Interface


**Update a layer 3 interface for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ospfV3` (object): The OSPFv3 routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki switch updateDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateDeviceSwitchRoutingInterface --serial 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingInterface(serial:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Device Switch Routing Interface Dhcp


**Update a layer 3 interface DHCP configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

##### Arguments
- `--serial` (string): (required)
- `--interfaceId` (string): (required)
- `--dhcpMode` (string): The DHCP mode options for the switch interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- `--dhcpRelayServerIps` (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface
- `--dhcpLeaseTime` (string): The DHCP lease time config for the dhcp server running on switch interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- `--dnsNameserversOption` (string): The DHCP name server option for the dhcp server running on the switch interface ('googlePublicDns', 'openDns' or 'custom')
- `--dnsCustomNameservers` (array): The DHCP name server IPs when DHCP name server option is 'custom'
- `--bootOptionsEnabled` (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch interface
- `--bootNextServer` (string): The PXE boot server IP for the DHCP server running on the switch interface
- `--bootFileName` (string): The PXE boot server filename for the DHCP server running on the switch interface
- `--dhcpOptions` (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch interface
- `--reservedIpRanges` (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch interface
- `--fixedIpAssignments` (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch interface


##### Example:
```
meraki switch updateDeviceSwitchRoutingInterfaceDhcp --serial 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateDeviceSwitchRoutingInterfaceDhcp --serial 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingInterfaceDhcp(serial:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Device Switch Routing Static Route


**Update a layer 3 static route for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

##### Arguments
- `--serial` (string): (required)
- `--staticRouteId` (string): (required)
- `--name` (string): Name or description for layer 3 static route
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki switch updateDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateDeviceSwitchRoutingStaticRoute --serial 'STRING' --staticRouteId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchRoutingStaticRoute(serial:str, staticRouteId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Device Switch Warm Spare


**Update warm spare configuration for a switch**

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

##### Arguments
- `--serial` (string): (required)
- `--enabled` (boolean): Enable or disable warm spare for a switch
- `--spareSerial` (string): Serial number of the warm spare switch


##### Example:
```
meraki switch updateDeviceSwitchWarmSpare --serial 'STRING' --enabled --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateDeviceSwitchWarmSpare --serial 'STRING' --enabled --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceSwitchWarmSpare(serial:str, enabled:bool, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Access Control Lists


**Update the access control lists for a MS network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists

##### Arguments
- `--networkId` (string): (required)
- `--rules` (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.


##### Example:
```
meraki switch updateNetworkSwitchAccessControlLists --networkId 'STRING' --rules ITEM
````

##### Method Code:
```python
def updateNetworkSwitchAccessControlLists(networkId:str, rules:list):
    # Code
````



----------------------------------------
## Switch Update Network Switch Access Policy


**Update an access policy for a switch network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

##### Arguments
- `--networkId` (string): (required)
- `--accessPolicyNumber` (string): (required)
- `--name` (string): Name of the access policy
- `--radiusServers` (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- `--radius` (object): Object for RADIUS Settings
- `--guestPortBouncing` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusTestingEnabled` (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- `--radiusCoaSupportEnabled` (boolean): Change of authentication for RADIUS re-authentication and disconnection
- `--radiusAccountingEnabled` (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- `--radiusAccountingServers` (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- `--radiusGroupAttribute` (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
- `--hostMode` (string): Choose the Host Mode for the access policy.
- `--accessPolicyType` (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- `--increaseAccessSpeed` (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- `--guestVlanId` (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- `--dot1x` (object): 802.1x Settings
- `--voiceVlanClients` (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- `--urlRedirectWalledGardenEnabled` (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- `--urlRedirectWalledGardenRanges` (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication


##### Example:
```
meraki switch updateNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchAccessPolicy --networkId 'STRING' --accessPolicyNumber 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchAccessPolicy(networkId:str, accessPolicyNumber:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Alternate Management Interface


**Update the switch alternate management interface for the network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable AMI configuration. If enabled, VLAN and protocols must be set
- `--vlanId` (integer): Alternate management VLAN, must be between 1 and 4094
- `--protocols` (array): Can be one or more of the following values: 'radius', 'snmp' or 'syslog'
- `--switches` (array): Array of switch serial number and IP assignment. If parameter is present, it cannot have empty body. Note: switches parameter is not applicable for template networks, in other words, do not put 'switches' in the body when updating template networks. Also, an empty 'switches' array will remove all previous assignments


##### Example:
```
meraki switch updateNetworkSwitchAlternateManagementInterface --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchAlternateManagementInterface --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchAlternateManagementInterface(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Dhcp Server Policy


**Update the DHCP server settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

##### Arguments
- `--networkId` (string): (required)
- `--alerts` (object): Alert settings for DHCP servers
- `--defaultPolicy` (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
- `--allowedServers` (array): List the MAC addresses of DHCP servers to permit on the network when defaultPolicy is set to block. An empty array will clear the entries.
- `--blockedServers` (array): List the MAC addresses of DHCP servers to block on the network when defaultPolicy is set to allow. An empty array will clear the entries.
- `--arpInspection` (object): Dynamic ARP Inspection settings


##### Example:
```
meraki switch updateNetworkSwitchDhcpServerPolicy --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchDhcpServerPolicy --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchDhcpServerPolicy(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Dhcp Server Policy Arp Inspection Trusted Server


**Update a server that is trusted by Dynamic ARP Inspection on this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy-arp-inspection-trusted-server

##### Arguments
- `--networkId` (string): (required)
- `--trustedServerId` (string): (required)
- `--mac` (string): The updated mac address of the trusted server
- `--vlan` (integer): The updated VLAN of the trusted server. It must be between 1 and 4094
- `--ipv4` (object): The updated IPv4 attributes of the trusted server


##### Example:
```
meraki switch updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer --networkId 'STRING' --trustedServerId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(networkId:str, trustedServerId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Dscp To Cos Mappings


**Update the DSCP to CoS mappings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

##### Arguments
- `--networkId` (string): (required)
- `--mappings` (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.


##### Example:
```
meraki switch updateNetworkSwitchDscpToCosMappings --networkId 'STRING' --mappings ITEM
````

##### Method Code:
```python
def updateNetworkSwitchDscpToCosMappings(networkId:str, mappings:list):
    # Code
````



----------------------------------------
## Switch Update Network Switch Link Aggregation


**Update a link aggregation group**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

##### Arguments
- `--networkId` (string): (required)
- `--linkAggregationId` (string): (required)
- `--switchPorts` (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
- `--switchProfilePorts` (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.


##### Example:
```
meraki switch updateNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchLinkAggregation --networkId 'STRING' --linkAggregationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchLinkAggregation(networkId:str, linkAggregationId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Mtu


**Update the MTU configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

##### Arguments
- `--networkId` (string): (required)
- `--defaultMtuSize` (integer): MTU size for the entire network. Default value is 9578.
- `--overrides` (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.


##### Example:
```
meraki switch updateNetworkSwitchMtu --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchMtu --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchMtu(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Port Schedule


**Update a switch port schedule**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

##### Arguments
- `--networkId` (string): (required)
- `--portScheduleId` (string): (required)
- `--name` (string): The name for your port schedule.
- `--portSchedule` (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
When it's empty, default schedule with all days of a week are configured.
Any unspecified day in the schedule is added as a default schedule configuration of the day.



##### Example:
```
meraki switch updateNetworkSwitchPortSchedule --networkId 'STRING' --portScheduleId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchPortSchedule --networkId 'STRING' --portScheduleId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchPortSchedule(networkId:str, portScheduleId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Qos Rule


**Update a quality of service rule**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

##### Arguments
- `--networkId` (string): (required)
- `--qosRuleId` (string): (required)
- `--vlan` (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- `--protocol` (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY".
- `--srcPort` (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--srcPortRange` (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dstPort` (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- `--dstPortRange` (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- `--dscp` (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0.


##### Example:
```
meraki switch updateNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchQosRule --networkId 'STRING' --qosRuleId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchQosRule(networkId:str, qosRuleId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Qos Rules Order


**Update the order in which the rules should be processed by the switch**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

##### Arguments
- `--networkId` (string): (required)
- `--ruleIds` (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.


##### Example:
```
meraki switch updateNetworkSwitchQosRulesOrder --networkId 'STRING' --ruleIds ITEM
````

##### Method Code:
```python
def updateNetworkSwitchQosRulesOrder(networkId:str, ruleIds:list):
    # Code
````



----------------------------------------
## Switch Update Network Switch Routing Multicast


**Update multicast settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

##### Arguments
- `--networkId` (string): (required)
- `--defaultSettings` (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
- `--overrides` (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.


##### Example:
```
meraki switch updateNetworkSwitchRoutingMulticast --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchRoutingMulticast --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingMulticast(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Routing Multicast Rendezvous Point


**Update a multicast rendezvous point**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

##### Arguments
- `--networkId` (string): (required)
- `--rendezvousPointId` (string): (required)
- `--interfaceIp` (string): The IP address of the interface to use
- `--multicastGroup` (string): 'Any', or the IP address of a multicast group


##### Example:
```
meraki switch updateNetworkSwitchRoutingMulticastRendezvousPoint --networkId 'STRING' --rendezvousPointId 'STRING' --interfaceIp 'STRING' --multicastGroup 'STRING'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingMulticastRendezvousPoint(networkId:str, rendezvousPointId:str, interfaceIp:str, multicastGroup:str):
    # Code
````



----------------------------------------
## Switch Update Network Switch Routing Ospf


**Update layer 3 OSPF routing configuration**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
- `--helloTimerInSeconds` (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds.
- `--deadTimerInSeconds` (integer): Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535
- `--areas` (array): OSPF areas
- `--v3` (object): OSPF v3 configuration
- `--md5AuthenticationEnabled` (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
- `--md5AuthenticationKey` (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true


##### Example:
```
meraki switch updateNetworkSwitchRoutingOspf --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchRoutingOspf --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchRoutingOspf(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Settings


**Update switch network settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

##### Arguments
- `--networkId` (string): (required)
- `--vlan` (integer): Management VLAN
- `--useCombinedPower` (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
- `--powerExceptions` (array): Exceptions on a per switch basis to "useCombinedPower"


##### Example:
```
meraki switch updateNetworkSwitchSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Stack Routing Interface


**Update a layer 3 interface for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)
- `--name` (string): A friendly name or description for the interface or VLAN.
- `--subnet` (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- `--interfaceIp` (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- `--multicastRouting` (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
- `--vlanId` (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- `--defaultGateway` (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- `--ospfSettings` (object): The OSPF routing settings of the interface.
- `--ipv6` (object): The IPv6 settings of the interface.


##### Example:
```
meraki switch updateNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchStackRoutingInterface --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingInterface(networkId:str, switchStackId:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Stack Routing Interface Dhcp


**Update a layer 3 interface DHCP configuration for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--interfaceId` (string): (required)
- `--dhcpMode` (string): The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- `--dhcpRelayServerIps` (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface
- `--dhcpLeaseTime` (string): The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- `--dnsNameserversOption` (string): The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')
- `--dnsCustomNameservers` (array): The DHCP name server IPs when DHCP name server option is 'custom'
- `--bootOptionsEnabled` (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface
- `--bootNextServer` (string): The PXE boot server IP for the DHCP server running on the switch stack interface
- `--bootFileName` (string): The PXE boot server file name for the DHCP server running on the switch stack interface
- `--dhcpOptions` (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface
- `--reservedIpRanges` (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface
- `--fixedIpAssignments` (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface


##### Example:
```
meraki switch updateNetworkSwitchStackRoutingInterfaceDhcp --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchStackRoutingInterfaceDhcp --networkId 'STRING' --switchStackId 'STRING' --interfaceId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingInterfaceDhcp(networkId:str, switchStackId:str, interfaceId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Stack Routing Static Route


**Update a layer 3 static route for a switch stack**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

##### Arguments
- `--networkId` (string): (required)
- `--switchStackId` (string): (required)
- `--staticRouteId` (string): (required)
- `--name` (string): Name or description for layer 3 static route
- `--subnet` (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- `--nextHopIp` (string): IP address of the next hop device to which the device sends its traffic for the subnet
- `--advertiseViaOspfEnabled` (boolean): Option to advertise static route via OSPF
- `--preferOverOspfRoutesEnabled` (boolean): Option to prefer static route over OSPF routes


##### Example:
```
meraki switch updateNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchStackRoutingStaticRoute --networkId 'STRING' --switchStackId 'STRING' --staticRouteId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStackRoutingStaticRoute(networkId:str, switchStackId:str, staticRouteId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Storm Control


**Update the storm control configuration for a switch network**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

##### Arguments
- `--networkId` (string): (required)
- `--broadcastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
- `--multicastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
- `--unknownUnicastThreshold` (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.


##### Example:
```
meraki switch updateNetworkSwitchStormControl --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchStormControl --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStormControl(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Network Switch Stp


**Updates STP settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

##### Arguments
- `--networkId` (string): (required)
- `--rstpEnabled` (boolean): The spanning tree protocol status in network
- `--stpBridgePriority` (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.


##### Example:
```
meraki switch updateNetworkSwitchStp --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateNetworkSwitchStp --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkSwitchStp(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Switch Update Organization Config Template Switch Profile Port


**Update a switch profile port**

https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port

##### Arguments
- `--organizationId` (string): (required)
- `--configTemplateId` (string): (required)
- `--profileId` (string): (required)
- `--portId` (string): (required)
- `--name` (string): The name of the switch profile port.
- `--tags` (array): The list of tags of the switch profile port.
- `--enabled` (boolean): The status of the switch profile port.
- `--poeEnabled` (boolean): The PoE status of the switch profile port.
- `--type` (string): The type of the switch profile port ('trunk' or 'access').
- `--vlan` (integer): The VLAN of the switch profile port. A null value will clear the value set for trunk ports.
- `--voiceVlan` (integer): The voice VLAN of the switch profile port. Only applicable to access ports.
- `--allowedVlans` (string): The VLANs allowed on the switch profile port. Only applicable to trunk ports.
- `--isolationEnabled` (boolean): The isolation status of the switch profile port.
- `--rstpEnabled` (boolean): The rapid spanning tree protocol status.
- `--stpGuard` (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
- `--linkNegotiation` (string): The link speed for the switch profile port.
- `--portScheduleId` (string): The ID of the port schedule. A value of null will clear the port schedule.
- `--udld` (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- `--accessPolicyType` (string): The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
- `--accessPolicyNumber` (integer): The number of a custom access policy to configure on the switch profile port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
- `--macAllowList` (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
- `--stickyMacAllowList` (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stickyMacAllowListLimit` (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
- `--stormControlEnabled` (boolean): The storm control status of the switch profile port.
- `--flexibleStackingEnabled` (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
- `--daiTrusted` (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
- `--profile` (object): Profile attributes


##### Example:
```
meraki switch updateOrganizationConfigTemplateSwitchProfilePort --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING' --portId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki switch updateOrganizationConfigTemplateSwitchProfilePort --organizationId 'STRING' --configTemplateId 'STRING' --profileId 'STRING' --portId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateOrganizationConfigTemplateSwitchProfilePort(organizationId:str, configTemplateId:str, profileId:str, portId:str, **kwargs):
    # Code
````

# Wireless


----------------------------------------
## Wireless Create Network Wireless Rf Profile


**Creates new RF profile for this network**

https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique. This param is required on creation.
- `--bandSelectionType` (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
- `--clientBalancingEnabled` (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
- `--minBitrateType` (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
- `--apBandSettings` (object): Settings that will be enabled if selectionType is set to 'ap'.
- `--twoFourGhzSettings` (object): Settings related to 2.4Ghz band
- `--fiveGhzSettings` (object): Settings related to 5Ghz band
- `--transmission` (object): Settings related to radio transmission.
- `--perSsidSettings` (object): Per-SSID radio settings by number.


##### Example:
```
meraki wireless createNetworkWirelessRfProfile --networkId 'STRING' --name 'STRING' --bandSelectionType 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless createNetworkWirelessRfProfile --networkId 'STRING' --name 'STRING' --bandSelectionType 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWirelessRfProfile(networkId:str, name:str, bandSelectionType:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Create Network Wireless Ssid Identity Psk


**Create an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the Identity PSK
- `--groupPolicyId` (string): The group policy to be applied to clients
- `--passphrase` (string): The passphrase for client authentication. If left blank, one will be auto-generated.


##### Example:
```
meraki wireless createNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --name 'STRING' --groupPolicyId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless createNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --name 'STRING' --groupPolicyId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def createNetworkWirelessSsidIdentityPsk(networkId:str, number:str, name:str, groupPolicyId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Delete Network Wireless Rf Profile


**Delete a RF Profile**

https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--rfProfileId` (string): (required)


##### Example:
```
meraki wireless deleteNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWirelessRfProfile(networkId:str, rfProfileId:str):
    # Code
````



----------------------------------------
## Wireless Delete Network Wireless Ssid Identity Psk


**Delete an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--identityPskId` (string): (required)


##### Example:
```
meraki wireless deleteNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING'
````

##### Method Code:
```python
def deleteNetworkWirelessSsidIdentityPsk(networkId:str, number:str, identityPskId:str):
    # Code
````



----------------------------------------
## Wireless Get Device Wireless Bluetooth Settings


**Return the bluetooth settings for a wireless device**

https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki wireless getDeviceWirelessBluetoothSettings --serial 'STRING'
````

##### Method Code:
```python
def getDeviceWirelessBluetoothSettings(serial:str):
    # Code
````



----------------------------------------
## Wireless Get Device Wireless Connection Stats


**Aggregated connectivity info for a given AP on this network**

https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-connection-stats

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag


##### Example:
```
meraki wireless getDeviceWirelessConnectionStats --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getDeviceWirelessConnectionStats --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceWirelessConnectionStats(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Device Wireless Latency Stats


**Aggregated latency info for a given AP on this network**

https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-latency-stats

##### Arguments
- `--serial` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--fields` (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.


##### Example:
```
meraki wireless getDeviceWirelessLatencyStats --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getDeviceWirelessLatencyStats --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getDeviceWirelessLatencyStats(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Device Wireless Radio Settings


**Return the radio settings of a device**

https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki wireless getDeviceWirelessRadioSettings --serial 'STRING'
````

##### Method Code:
```python
def getDeviceWirelessRadioSettings(serial:str):
    # Code
````



----------------------------------------
## Wireless Get Device Wireless Status


**Return the SSID statuses of an access point**

https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

##### Arguments
- `--serial` (string): (required)


##### Example:
```
meraki wireless getDeviceWirelessStatus --serial 'STRING'
````

##### Method Code:
```python
def getDeviceWirelessStatus(serial:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Air Marshal


**List Air Marshal scan results from a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.


##### Example:
```
meraki wireless getNetworkWirelessAirMarshal --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessAirMarshal --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessAirMarshal(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Alternate Management Interface


**Return alternate management interface and devices with IP assigned**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessAlternateManagementInterface --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessAlternateManagementInterface(networkId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Billing


**Return the billing settings of this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessBilling --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessBilling(networkId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Bluetooth Settings


**Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessBluetoothSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessBluetoothSettings(networkId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Channel Utilization History


**Return AP channel utilization over time for a device or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
- `--deviceSerial` (string): Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
- `--apTag` (string): Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').


##### Example:
```
meraki wireless getNetworkWirelessChannelUtilizationHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessChannelUtilizationHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessChannelUtilizationHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Client Connection Stats


**Aggregated connectivity info for a given client on this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag


##### Example:
```
meraki wireless getNetworkWirelessClientConnectionStats --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientConnectionStats --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientConnectionStats(networkId:str, clientId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Client Connectivity Events


**List the wireless connectivity events for a client within a network in the timespan.**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- `--types` (array): A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
- `--includedSeverities` (array): A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'.
- `--band` (string): Filter results by band (either '2.4', '5', '6').
- `--ssidNumber` (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
- `--deviceSerial` (string): Filter results by an AP's serial number.


##### Example:
```
meraki wireless getNetworkWirelessClientConnectivityEvents --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientConnectivityEvents --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientConnectivityEvents(networkId:str, clientId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Client Count History


**Return wireless client counts over time for a network, device, or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history.
- `--deviceSerial` (string): Filter results by device.
- `--apTag` (string): Filter results by AP tag.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').
- `--ssid` (integer): Filter results by SSID number.


##### Example:
```
meraki wireless getNetworkWirelessClientCountHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientCountHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientCountHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Client Latency History


**Return the latency history for a client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.


##### Example:
```
meraki wireless getNetworkWirelessClientLatencyHistory --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientLatencyHistory --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientLatencyHistory(networkId:str, clientId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Client Latency Stats


**Aggregated latency info for a given client on this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

##### Arguments
- `--networkId` (string): (required)
- `--clientId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--fields` (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.


##### Example:
```
meraki wireless getNetworkWirelessClientLatencyStats --networkId 'STRING' --clientId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientLatencyStats --networkId 'STRING' --clientId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientLatencyStats(networkId:str, clientId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Clients Connection Stats


**Aggregated connectivity info for this network, grouped by clients**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag


##### Example:
```
meraki wireless getNetworkWirelessClientsConnectionStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientsConnectionStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientsConnectionStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Clients Latency Stats


**Aggregated latency info for this network, grouped by clients**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--fields` (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.


##### Example:
```
meraki wireless getNetworkWirelessClientsLatencyStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessClientsLatencyStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessClientsLatencyStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Connection Stats


**Aggregated connectivity info for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag


##### Example:
```
meraki wireless getNetworkWirelessConnectionStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessConnectionStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessConnectionStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Data Rate History


**Return PHY data rates over time for a network, device, or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client.
- `--deviceSerial` (string): Filter results by device.
- `--apTag` (string): Filter results by AP tag.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').
- `--ssid` (integer): Filter results by SSID number.


##### Example:
```
meraki wireless getNetworkWirelessDataRateHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessDataRateHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessDataRateHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Devices Connection Stats


**Aggregated connectivity info for this network, grouped by node**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag


##### Example:
```
meraki wireless getNetworkWirelessDevicesConnectionStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessDevicesConnectionStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessDevicesConnectionStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Devices Latency Stats


**Aggregated latency info for this network, grouped by node**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--fields` (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.


##### Example:
```
meraki wireless getNetworkWirelessDevicesLatencyStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessDevicesLatencyStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessDevicesLatencyStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Failed Connections


**List of all failed client connection events on this network in a given time range**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--serial` (string): Filter by AP
- `--clientId` (string): Filter by client MAC


##### Example:
```
meraki wireless getNetworkWirelessFailedConnections --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessFailedConnections --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessFailedConnections(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Latency History


**Return average wireless latency over time for a network, device, or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client.
- `--deviceSerial` (string): Filter results by device.
- `--apTag` (string): Filter results by AP tag.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').
- `--ssid` (integer): Filter results by SSID number.
- `--accessCategory` (string): Filter by access category.


##### Example:
```
meraki wireless getNetworkWirelessLatencyHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessLatencyHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessLatencyHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Latency Stats


**Aggregated latency info for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- `--band` (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
- `--ssid` (integer): Filter results by SSID
- `--vlan` (integer): Filter results by VLAN
- `--apTag` (string): Filter results by AP Tag
- `--fields` (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.


##### Example:
```
meraki wireless getNetworkWirelessLatencyStats --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessLatencyStats --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessLatencyStats(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Mesh Statuses


**List wireless mesh statuses for repeaters**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

##### Arguments
- `--networkId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.


##### Example:
```
meraki wireless getNetworkWirelessMeshStatuses --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessMeshStatuses --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessMeshStatuses(networkId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Rf Profile


**Return a RF profile**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--rfProfileId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessRfProfile(networkId:str, rfProfileId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Rf Profiles


**List the non-basic RF profiles for this network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

##### Arguments
- `--networkId` (string): (required)
- `--includeTemplateProfiles` (boolean): If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.


##### Example:
```
meraki wireless getNetworkWirelessRfProfiles --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessRfProfiles --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessRfProfiles(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Settings


**Return the wireless settings for a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSettings --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSettings(networkId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Signal Quality History


**Return signal quality (SNR/RSSI) over time for a device or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client.
- `--deviceSerial` (string): Filter results by device.
- `--apTag` (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').
- `--ssid` (integer): Filter results by SSID number.


##### Example:
```
meraki wireless getNetworkWirelessSignalQualityHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessSignalQualityHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessSignalQualityHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid


**Return a single MR SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsid --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsid(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Bonjour Forwarding


**List the Bonjour forwarding setting and rules for the SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidBonjourForwarding --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidBonjourForwarding(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Device Type Group Policies


**List the device type group policies for the SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidDeviceTypeGroupPolicies --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidDeviceTypeGroupPolicies(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Eap Override


**Return the EAP overridden parameters for an SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidEapOverride --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidEapOverride(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Firewall L3 Firewall Rules


**Return the L3 firewall rules for an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidFirewallL3FirewallRules --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidFirewallL3FirewallRules(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Firewall L7 Firewall Rules


**Return the L7 firewall rules for an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidFirewallL7FirewallRules --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidFirewallL7FirewallRules(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Hotspot20


**Return the Hotspot 2.0 settings for an SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidHotspot20 --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidHotspot20(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Identity Psk


**Return an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--identityPskId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidIdentityPsk(networkId:str, number:str, identityPskId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Identity Psks


**List all Identity PSKs in a wireless network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidIdentityPsks --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidIdentityPsks(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Schedules


**List the outage schedule for the SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidSchedules --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidSchedules(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Splash Settings


**Display the splash page settings for the given SSID**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidSplashSettings --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidSplashSettings(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Traffic Shaping Rules


**Display the traffic shaping settings for a SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidTrafficShapingRules --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidTrafficShapingRules(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssid Vpn


**List the VPN settings for the SSID.**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsidVpn --networkId 'STRING' --number 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsidVpn(networkId:str, number:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Ssids


**List the MR SSIDs in a network**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

##### Arguments
- `--networkId` (string): (required)


##### Example:
```
meraki wireless getNetworkWirelessSsids --networkId 'STRING'
````

##### Method Code:
```python
def getNetworkWirelessSsids(networkId:str):
    # Code
````



----------------------------------------
## Wireless Get Network Wireless Usage History


**Return AP usage over time for a device or network client**

https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

##### Arguments
- `--networkId` (string): (required)
- `--t0` (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- `--t1` (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- `--timespan` (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- `--resolution` (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- `--autoResolution` (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- `--clientId` (string): Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history.
- `--deviceSerial` (string): Filter results by device. Requires :band.
- `--apTag` (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
- `--band` (string): Filter results by band (either '2.4', '5' or '6').
- `--ssid` (integer): Filter results by SSID number.


##### Example:
```
meraki wireless getNetworkWirelessUsageHistory --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getNetworkWirelessUsageHistory --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getNetworkWirelessUsageHistory(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Get Organization Wireless Devices Ethernet Statuses


**Endpoint to see power status for wireless devices**

https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-ethernet-statuses

##### Arguments
- `--organizationId` (string): (required)
- `--total_pages` (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- `--direction` (string): direction to paginate, either "next" (default) or "prev" page
- `--perPage` (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- `--startingAfter` (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--endingBefore` (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- `--networkIds` (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456


##### Example:
```
meraki wireless getOrganizationWirelessDevicesEthernetStatuses --organizationId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless getOrganizationWirelessDevicesEthernetStatuses --organizationId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def getOrganizationWirelessDevicesEthernetStatuses(organizationId:str, total_pages=1, direction='next', **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Device Wireless Bluetooth Settings


**Update the bluetooth settings for a wireless device**

https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

##### Arguments
- `--serial` (string): (required)
- `--uuid` (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- `--major` (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- `--minor` (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.


##### Example:
```
meraki wireless updateDeviceWirelessBluetoothSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateDeviceWirelessBluetoothSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceWirelessBluetoothSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Device Wireless Radio Settings


**Update the radio settings of a device**

https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

##### Arguments
- `--serial` (string): (required)
- `--rfProfileId` (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
- `--twoFourGhzSettings` (object): Manual radio settings for 2.4 GHz.
- `--fiveGhzSettings` (object): Manual radio settings for 5 GHz.


##### Example:
```
meraki wireless updateDeviceWirelessRadioSettings --serial 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateDeviceWirelessRadioSettings --serial 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateDeviceWirelessRadioSettings(serial:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Alternate Management Interface


**Update alternate management interface and device static IP**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

##### Arguments
- `--networkId` (string): (required)
- `--enabled` (boolean): Boolean value to enable or disable alternate management interface
- `--vlanId` (integer): Alternate management interface VLAN, must be between 1 and 4094
- `--protocols` (array): Can be one or more of the following values: 'radius', 'snmp', 'syslog' or 'ldap'
- `--accessPoints` (array): Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put 'accessPoints' in the body when updating template networks. Also, an empty 'accessPoints' array will remove all previous static IP assignments


##### Example:
```
meraki wireless updateNetworkWirelessAlternateManagementInterface --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessAlternateManagementInterface --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessAlternateManagementInterface(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Billing


**Update the billing settings**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

##### Arguments
- `--networkId` (string): (required)
- `--currency` (string): The currency code of this node group's billing plans
- `--plans` (array): Array of billing plans in the node group. (Can configure a maximum of 5)


##### Example:
```
meraki wireless updateNetworkWirelessBilling --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessBilling --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessBilling(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Bluetooth Settings


**Update the Bluetooth settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-bluetooth-settings

##### Arguments
- `--networkId` (string): (required)
- `--scanningEnabled` (boolean): Whether APs will scan for Bluetooth enabled clients.
- `--advertisingEnabled` (boolean): Whether APs will advertise beacons.
- `--uuid` (string): The UUID to be used in the beacon identifier.
- `--majorMinorAssignmentMode` (string): The way major and minor number should be assigned to nodes in the network. ('Unique', 'Non-unique')
- `--major` (integer): The major number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
- `--minor` (integer): The minor number to be used in the beacon identifier. Only valid in 'Non-unique' mode.


##### Example:
```
meraki wireless updateNetworkWirelessBluetoothSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessBluetoothSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessBluetoothSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Rf Profile


**Updates specified RF profile for this network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

##### Arguments
- `--networkId` (string): (required)
- `--rfProfileId` (string): (required)
- `--name` (string): The name of the new profile. Must be unique.
- `--clientBalancingEnabled` (boolean): Steers client to best available access point. Can be either true or false.
- `--minBitrateType` (string): Minimum bitrate can be set to either 'band' or 'ssid'.
- `--bandSelectionType` (string): Band selection can be set to either 'ssid' or 'ap'.
- `--apBandSettings` (object): Settings that will be enabled if selectionType is set to 'ap'.
- `--twoFourGhzSettings` (object): Settings related to 2.4Ghz band
- `--fiveGhzSettings` (object): Settings related to 5Ghz band
- `--transmission` (object): Settings related to radio transmission.
- `--perSsidSettings` (object): Per-SSID radio settings by number.


##### Example:
```
meraki wireless updateNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessRfProfile --networkId 'STRING' --rfProfileId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessRfProfile(networkId:str, rfProfileId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Settings


**Update the wireless settings for a network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

##### Arguments
- `--networkId` (string): (required)
- `--meshingEnabled` (boolean): Toggle for enabling or disabling meshing in a network
- `--ipv6BridgeEnabled` (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
- `--locationAnalyticsEnabled` (boolean): Toggle for enabling or disabling location analytics for your network
- `--upgradeStrategy` (string): The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
- `--ledLightsOn` (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)


##### Example:
```
meraki wireless updateNetworkWirelessSettings --networkId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSettings --networkId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSettings(networkId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid


**Update the attributes of an MR SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--name` (string): The name of the SSID
- `--enabled` (boolean): Whether or not the SSID is enabled
- `--authMode` (string): The association control method for the SSID ('open', 'open-enhanced', 'psk', 'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius', '8021x-google', '8021x-localradius', 'ipsk-with-radius' or 'ipsk-without-radius')
- `--enterpriseAdminAccess` (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
- `--encryptionMode` (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
- `--psk` (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
- `--wpaEncryptionMode` (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security')
- `--dot11w` (object): The current setting for Protected Management Frames (802.11w).
- `--dot11r` (object): The current setting for 802.11r
- `--splashPage` (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain'). This attribute is not supported for template children.
- `--splashGuestSponsorDomains` (array): Array of valid sponsor email domains for sponsored guest splash type.
- `--oauth` (object): The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
- `--localRadius` (object): The current setting for Local Authentication, a built-in RADIUS server on the access point. Only valid if authMode is '8021x-localradius'.
- `--ldap` (object): The current setting for LDAP. Only valid if splashPage is 'Password-protected with LDAP'.
- `--activeDirectory` (object): The current setting for Active Directory. Only valid if splashPage is 'Password-protected with Active Directory'
- `--radiusServers` (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- `--radiusProxyEnabled` (boolean): If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.
- `--radiusTestingEnabled` (boolean): If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity 'meraki_8021x_test' to ensure that the RADIUS servers are reachable.
- `--radiusCalledStationId` (string): The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
- `--radiusAuthenticationNasId` (string): The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$:$VAP_NUM$).
- `--radiusServerTimeout` (integer): The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds).
- `--radiusServerAttemptsLimit` (integer): The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5).
- `--radiusFallbackEnabled` (boolean): Whether or not higher priority RADIUS servers should be retried after 60 seconds.
- `--radiusCoaEnabled` (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
- `--radiusFailoverPolicy` (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
- `--radiusLoadBalancingPolicy` (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
- `--radiusAccountingEnabled` (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- `--radiusAccountingServers` (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
- `--radiusAccountingInterimInterval` (integer): The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server.
- `--radiusAttributeForGroupPolicies` (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
- `--ipAssignmentMode` (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator' or 'VPN')
- `--useVlanTagging` (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--concentratorNetworkId` (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
- `--secondaryConcentratorNetworkId` (string): The secondary concentrator to use when the ipAssignmentMode is 'VPN'. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. ('disabled' represents no secondary concentrator.)
- `--disassociateClientsOnVpnFailover` (boolean): Disassociate clients when 'VPN' concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is 'VPN'.
- `--vlanId` (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
- `--defaultVlanId` (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--apTagsAndVlanIds` (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- `--walledGardenEnabled` (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
- `--walledGardenRanges` (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
- `--gre` (object): Ethernet over GRE settings
- `--radiusOverride` (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
- `--radiusGuestVlanEnabled` (boolean): Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- `--radiusGuestVlanId` (integer): VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- `--minBitrate` (number): The minimum bitrate in Mbps of this SSID in the default indoor RF profile. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
- `--bandSelection` (string): The client-serving radio frequencies of this SSID in the default indoor RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
- `--perClientBandwidthLimitUp` (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
- `--perClientBandwidthLimitDown` (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
- `--perSsidBandwidthLimitUp` (integer): The total upload bandwidth limit in Kbps. (0 represents no limit.)
- `--perSsidBandwidthLimitDown` (integer): The total download bandwidth limit in Kbps. (0 represents no limit.)
- `--lanIsolationEnabled` (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
- `--visible` (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
- `--availableOnAllAps` (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
- `--availabilityTags` (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
- `--mandatoryDhcpEnabled` (boolean): If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate.
- `--adultContentFilteringEnabled` (boolean): Boolean indicating whether or not adult content will be blocked
- `--dnsRewrite` (object): DNS servers rewrite settings
- `--speedBurst` (object): The SpeedBurst setting for this SSID'


##### Example:
```
meraki wireless updateNetworkWirelessSsid --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsid --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsid(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Bonjour Forwarding


**Update the bonjour forwarding setting and rules for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, Bonjour forwarding is enabled on this SSID.
- `--rules` (array): List of bonjour forwarding rules.


##### Example:
```
meraki wireless updateNetworkWirelessSsidBonjourForwarding --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidBonjourForwarding --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidBonjourForwarding(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Device Type Group Policies


**Update the device type group policies for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, the SSID device type group policies are enabled.
- `--deviceTypePolicies` (array): List of device type policies.


##### Example:
```
meraki wireless updateNetworkWirelessSsidDeviceTypeGroupPolicies --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidDeviceTypeGroupPolicies --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidDeviceTypeGroupPolicies(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Eap Override


**Update the EAP overridden parameters for an SSID.**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--timeout` (integer): General EAP timeout in seconds.
- `--identity` (object): EAP settings for identity requests.
- `--maxRetries` (integer): Maximum number of general EAP retries.
- `--eapolKey` (object): EAPOL Key settings.


##### Example:
```
meraki wireless updateNetworkWirelessSsidEapOverride --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidEapOverride --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidEapOverride(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Firewall L3 Firewall Rules


**Update the L3 firewall rules of an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--rules` (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
- `--allowLanAccess` (boolean): Allow wireless client access to local LAN (boolean value - `--true` allows access and false denies access) (optional)


##### Example:
```
meraki wireless updateNetworkWirelessSsidFirewallL3FirewallRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidFirewallL3FirewallRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidFirewallL3FirewallRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Firewall L7 Firewall Rules


**Update the L7 firewall rules of an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--rules` (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.


##### Example:
```
meraki wireless updateNetworkWirelessSsidFirewallL7FirewallRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidFirewallL7FirewallRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidFirewallL7FirewallRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Hotspot20


**Update the Hotspot 2.0 settings of an SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): Whether or not Hotspot 2.0 for this SSID is enabled
- `--operator` (object): Operator settings for this SSID
- `--venue` (object): Venue settings for this SSID
- `--networkAccessType` (string): The network type of this SSID ('Private network', 'Private network with guest access', 'Chargeable public network', 'Free public network', 'Personal device network', 'Emergency services only network', 'Test or experimental', 'Wildcard')
- `--domains` (array): An array of domain names
- `--roamConsortOis` (array): An array of roaming consortium OIs (hexadecimal number 3-5 octets in length)
- `--mccMncs` (array): An array of MCC/MNC pairs
- `--naiRealms` (array): An array of NAI realms


##### Example:
```
meraki wireless updateNetworkWirelessSsidHotspot20 --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidHotspot20 --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidHotspot20(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Identity Psk


**Update an Identity PSK**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--identityPskId` (string): (required)
- `--name` (string): The name of the Identity PSK
- `--passphrase` (string): The passphrase for client authentication
- `--groupPolicyId` (string): The group policy to be applied to clients


##### Example:
```
meraki wireless updateNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidIdentityPsk --networkId 'STRING' --number 'STRING' --identityPskId 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidIdentityPsk(networkId:str, number:str, identityPskId:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Schedules


**Update the outage schedule for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--enabled` (boolean): If true, the SSID outage schedule is enabled.
- `--ranges` (array): List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.
- `--rangesInSeconds` (array): List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.


##### Example:
```
meraki wireless updateNetworkWirelessSsidSchedules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidSchedules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidSchedules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Splash Settings


**Modify the splash page settings for the given SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--splashUrl` (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
- `--useSplashUrl` (boolean): [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
- `--splashTimeout` (integer): Splash timeout in minutes. This will determine how often users will see the splash page.
- `--redirectUrl` (string): The custom redirect URL where the users will go after the splash page.
- `--useRedirectUrl` (boolean): The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
- `--welcomeMessage` (string): The welcome message for the users on the splash page.
- `--splashLogo` (object): The logo used in the splash page.
- `--splashImage` (object): The image used in the splash page.
- `--splashPrepaidFront` (object): The prepaid front image used in the splash page.
- `--blockAllTrafficBeforeSignOn` (boolean): How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
- `--controllerDisconnectionBehavior` (string): How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.
- `--allowSimultaneousLogins` (boolean): Whether or not to allow simultaneous logins from different devices.
- `--guestSponsorship` (object): Details associated with guest sponsored splash.
- `--billing` (object): Details associated with billing splash.
- `--sentryEnrollment` (object): Systems Manager sentry enrollment splash settings.


##### Example:
```
meraki wireless updateNetworkWirelessSsidSplashSettings --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidSplashSettings --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidSplashSettings(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Traffic Shaping Rules


**Update the traffic shaping settings for an SSID on an MR network**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--trafficShapingEnabled` (boolean): Whether traffic shaping rules are applied to clients on your SSID.
- `--defaultRulesEnabled` (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- `--rules` (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.



##### Example:
```
meraki wireless updateNetworkWirelessSsidTrafficShapingRules --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidTrafficShapingRules --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidTrafficShapingRules(networkId:str, number:str, **kwargs):
    # Code
````



----------------------------------------
## Wireless Update Network Wireless Ssid Vpn


**Update the VPN settings for the SSID**

https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

##### Arguments
- `--networkId` (string): (required)
- `--number` (string): (required)
- `--concentrator` (object): The VPN concentrator settings for this SSID.
- `--splitTunnel` (object): The VPN split tunnel settings for this SSID.
- `--failover` (object): Secondary VPN concentrator settings. This is only used when two VPN concentrators are configured on the SSID.


##### Example:
```
meraki wireless updateNetworkWirelessSsidVpn --networkId 'STRING' --number 'STRING' --optionalArg1 "optionalarg1value" --optionalArg2 "optionalarg2value"
````

##### Example using `--kwargs` (Advanced):
```
meraki wireless updateNetworkWirelessSsidVpn --networkId 'STRING' --number 'STRING' --kwargs '{"key1": "value1", "key2": "value2"}'
````

##### Method Code:
```python
def updateNetworkWirelessSsidVpn(networkId:str, number:str, **kwargs):
    # Code
````
