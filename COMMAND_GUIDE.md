# Meraki-CLI Command Guide

Below is a list of commands supported by the Meraki-CLI tool.

This documentation is built automatically by parsing the [Meraki Dashboard API Python SDK](https://github.com/meraki/dashboard-api-python) and may not be 100% up to date since that library changes regularly.


## Version

This command guide is based on version **v1.4.3** of the [Meraki Dashboard API Python SDK](https://github.com/meraki/dashboard-api-python). If you want to see the version of the SDK you have installed, issue the command `meraki -v`.


# TABLE OF CONTENTS
- [Organizations](#organizations)
    - [Assign Organization Licenses Seats](#assign-organization-licenses-seats)
    - [Claim Into Organization](#claim-into-organization)
    - [Clone Organization](#clone-organization)
    - [Combine Organization Networks](#combine-organization-networks)
    - [Create Organization](#create-organization)
    - [Create Organization Action Batch](#create-organization-action-batch)
    - [Create Organization Admin](#create-organization-admin)
    - [Create Organization Branding Policy](#create-organization-branding-policy)
    - [Create Organization Config Template](#create-organization-config-template)
    - [Create Organization Network](#create-organization-network)
    - [Create Organization Saml Idp](#create-organization-saml-idp)
    - [Create Organization Saml Role](#create-organization-saml-role)
    - [Delete Organization](#delete-organization)
    - [Delete Organization Action Batch](#delete-organization-action-batch)
    - [Delete Organization Admin](#delete-organization-admin)
    - [Delete Organization Branding Policy](#delete-organization-branding-policy)
    - [Delete Organization Config Template](#delete-organization-config-template)
    - [Delete Organization Saml Idp](#delete-organization-saml-idp)
    - [Delete Organization Saml Role](#delete-organization-saml-role)
    - [Get Organization](#get-organization)
    - [Get Organization Action Batch](#get-organization-action-batch)
    - [Get Organization Action Batches](#get-organization-action-batches)
    - [Get Organization Admins](#get-organization-admins)
    - [Get Organization Api Requests](#get-organization-api-requests)
    - [Get Organization Api Requests Overview](#get-organization-api-requests-overview)
    - [Get Organization Branding Policies](#get-organization-branding-policies)
    - [Get Organization Branding Policies Priorities](#get-organization-branding-policies-priorities)
    - [Get Organization Branding Policy](#get-organization-branding-policy)
    - [Get Organization Config Template](#get-organization-config-template)
    - [Get Organization Config Templates](#get-organization-config-templates)
    - [Get Organization Configuration Changes](#get-organization-configuration-changes)
    - [Get Organization Devices](#get-organization-devices)
    - [Get Organization Devices Statuses](#get-organization-devices-statuses)
    - [Get Organization Devices Uplinks Loss And Latency](#get-organization-devices-uplinks-loss-and-latency)
    - [Get Organization Inventory Device](#get-organization-inventory-device)
    - [Get Organization Inventory Devices](#get-organization-inventory-devices)
    - [Get Organization License](#get-organization-license)
    - [Get Organization Licenses](#get-organization-licenses)
    - [Get Organization Licenses Overview](#get-organization-licenses-overview)
    - [Get Organization Login Security](#get-organization-login-security)
    - [Get Organization Networks](#get-organization-networks)
    - [Get Organization Openapi Spec](#get-organization-openapi-spec)
    - [Get Organization Saml](#get-organization-saml)
    - [Get Organization Saml Idp](#get-organization-saml-idp)
    - [Get Organization Saml Idps](#get-organization-saml-idps)
    - [Get Organization Saml Role](#get-organization-saml-role)
    - [Get Organization Saml Roles](#get-organization-saml-roles)
    - [Get Organization Snmp](#get-organization-snmp)
    - [Get Organization Uplinks Statuses](#get-organization-uplinks-statuses)
    - [Get Organization Webhooks Alert Types](#get-organization-webhooks-alert-types)
    - [Get Organization Webhooks Logs](#get-organization-webhooks-logs)
    - [Get Organizations](#get-organizations)
    - [Move Organization Licenses](#move-organization-licenses)
    - [Move Organization Licenses Seats](#move-organization-licenses-seats)
    - [Renew Organization Licenses Seats](#renew-organization-licenses-seats)
    - [Update Organization](#update-organization)
    - [Update Organization Action Batch](#update-organization-action-batch)
    - [Update Organization Admin](#update-organization-admin)
    - [Update Organization Branding Policies Priorities](#update-organization-branding-policies-priorities)
    - [Update Organization Branding Policy](#update-organization-branding-policy)
    - [Update Organization Config Template](#update-organization-config-template)
    - [Update Organization License](#update-organization-license)
    - [Update Organization Login Security](#update-organization-login-security)
    - [Update Organization Saml](#update-organization-saml)
    - [Update Organization Saml Idp](#update-organization-saml-idp)
    - [Update Organization Saml Role](#update-organization-saml-role)
    - [Update Organization Snmp](#update-organization-snmp)
- [Networks](#networks)
    - [Bind Network](#bind-network)
    - [Claim Network Devices](#claim-network-devices)
    - [Create Network Floor Plan](#create-network-floor-plan)
    - [Create Network Group Policy](#create-network-group-policy)
    - [Create Network Meraki Auth User](#create-network-meraki-auth-user)
    - [Create Network Mqtt Broker](#create-network-mqtt-broker)
    - [Create Network Pii Request](#create-network-pii-request)
    - [Create Network Webhooks Http Server](#create-network-webhooks-http-server)
    - [Create Network Webhooks Webhook Test](#create-network-webhooks-webhook-test)
    - [Delete Network](#delete-network)
    - [Delete Network Floor Plan](#delete-network-floor-plan)
    - [Delete Network Group Policy](#delete-network-group-policy)
    - [Delete Network Meraki Auth User](#delete-network-meraki-auth-user)
    - [Delete Network Mqtt Broker](#delete-network-mqtt-broker)
    - [Delete Network Pii Request](#delete-network-pii-request)
    - [Delete Network Webhooks Http Server](#delete-network-webhooks-http-server)
    - [Get Network](#get-network)
    - [Get Network Alerts Settings](#get-network-alerts-settings)
    - [Get Network Bluetooth Client](#get-network-bluetooth-client)
    - [Get Network Bluetooth Clients](#get-network-bluetooth-clients)
    - [Get Network Client](#get-network-client)
    - [Get Network Client Policy](#get-network-client-policy)
    - [Get Network Client Splash Authorization Status](#get-network-client-splash-authorization-status)
    - [Get Network Client Traffic History](#get-network-client-traffic-history)
    - [Get Network Client Usage History](#get-network-client-usage-history)
    - [Get Network Clients](#get-network-clients)
    - [Get Network Clients Application Usage](#get-network-clients-application-usage)
    - [Get Network Clients Usage Histories](#get-network-clients-usage-histories)
    - [Get Network Devices](#get-network-devices)
    - [Get Network Events](#get-network-events)
    - [Get Network Events Event Types](#get-network-events-event-types)
    - [Get Network Firmware Upgrades](#get-network-firmware-upgrades)
    - [Get Network Floor Plan](#get-network-floor-plan)
    - [Get Network Floor Plans](#get-network-floor-plans)
    - [Get Network Group Policies](#get-network-group-policies)
    - [Get Network Group Policy](#get-network-group-policy)
    - [Get Network Meraki Auth User](#get-network-meraki-auth-user)
    - [Get Network Meraki Auth Users](#get-network-meraki-auth-users)
    - [Get Network Mqtt Broker](#get-network-mqtt-broker)
    - [Get Network Mqtt Brokers](#get-network-mqtt-brokers)
    - [Get Network Netflow](#get-network-netflow)
    - [Get Network Network Health Channel Utilization](#get-network-network-health-channel-utilization)
    - [Get Network Pii Pii Keys](#get-network-pii-pii-keys)
    - [Get Network Pii Request](#get-network-pii-request)
    - [Get Network Pii Requests](#get-network-pii-requests)
    - [Get Network Pii Sm Devices For Key](#get-network-pii-sm-devices-for-key)
    - [Get Network Pii Sm Owners For Key](#get-network-pii-sm-owners-for-key)
    - [Get Network Settings](#get-network-settings)
    - [Get Network Snmp](#get-network-snmp)
    - [Get Network Splash Login Attempts](#get-network-splash-login-attempts)
    - [Get Network Syslog Servers](#get-network-syslog-servers)
    - [Get Network Traffic](#get-network-traffic)
    - [Get Network Traffic Analysis](#get-network-traffic-analysis)
    - [Get Network Traffic Shaping Application Categories](#get-network-traffic-shaping-application-categories)
    - [Get Network Traffic Shaping Dscp Tagging Options](#get-network-traffic-shaping-dscp-tagging-options)
    - [Get Network Webhooks Http Server](#get-network-webhooks-http-server)
    - [Get Network Webhooks Http Servers](#get-network-webhooks-http-servers)
    - [Get Network Webhooks Webhook Test](#get-network-webhooks-webhook-test)
    - [Provision Network Clients](#provision-network-clients)
    - [Remove Network Devices](#remove-network-devices)
    - [Split Network](#split-network)
    - [Unbind Network](#unbind-network)
    - [Update Network](#update-network)
    - [Update Network Alerts Settings](#update-network-alerts-settings)
    - [Update Network Client Policy](#update-network-client-policy)
    - [Update Network Client Splash Authorization Status](#update-network-client-splash-authorization-status)
    - [Update Network Firmware Upgrades](#update-network-firmware-upgrades)
    - [Update Network Floor Plan](#update-network-floor-plan)
    - [Update Network Group Policy](#update-network-group-policy)
    - [Update Network Meraki Auth User](#update-network-meraki-auth-user)
    - [Update Network Mqtt Broker](#update-network-mqtt-broker)
    - [Update Network Netflow](#update-network-netflow)
    - [Update Network Settings](#update-network-settings)
    - [Update Network Snmp](#update-network-snmp)
    - [Update Network Syslog Servers](#update-network-syslog-servers)
    - [Update Network Traffic Analysis](#update-network-traffic-analysis)
    - [Update Network Webhooks Http Server](#update-network-webhooks-http-server)
- [Devices](#devices)
    - [Blink Device Leds](#blink-device-leds)
    - [Get Device](#get-device)
    - [Get Device Clients](#get-device-clients)
    - [Get Device Lldp Cdp](#get-device-lldp-cdp)
    - [Get Device Loss And Latency History](#get-device-loss-and-latency-history)
    - [Get Device Management Interface](#get-device-management-interface)
    - [Reboot Device](#reboot-device)
    - [Update Device](#update-device)
    - [Update Device Management Interface](#update-device-management-interface)
- [Appliance](#appliance)
    - [Create Network Appliance Static Route](#create-network-appliance-static-route)
    - [Create Network Appliance Traffic Shaping Custom Performance Class](#create-network-appliance-traffic-shaping-custom-performance-class)
    - [Create Network Appliance Vlan](#create-network-appliance-vlan)
    - [Delete Network Appliance Static Route](#delete-network-appliance-static-route)
    - [Delete Network Appliance Traffic Shaping Custom Performance Class](#delete-network-appliance-traffic-shaping-custom-performance-class)
    - [Delete Network Appliance Vlan](#delete-network-appliance-vlan)
    - [Get Device Appliance Dhcp Subnets](#get-device-appliance-dhcp-subnets)
    - [Get Device Appliance Performance](#get-device-appliance-performance)
    - [Get Network Appliance Client Security Events](#get-network-appliance-client-security-events)
    - [Get Network Appliance Connectivity Monitoring Destinations](#get-network-appliance-connectivity-monitoring-destinations)
    - [Get Network Appliance Content Filtering](#get-network-appliance-content-filtering)
    - [Get Network Appliance Content Filtering Categories](#get-network-appliance-content-filtering-categories)
    - [Get Network Appliance Firewall Cellular Firewall Rules](#get-network-appliance-firewall-cellular-firewall-rules)
    - [Get Network Appliance Firewall Firewalled Service](#get-network-appliance-firewall-firewalled-service)
    - [Get Network Appliance Firewall Firewalled Services](#get-network-appliance-firewall-firewalled-services)
    - [Get Network Appliance Firewall Inbound Firewall Rules](#get-network-appliance-firewall-inbound-firewall-rules)
    - [Get Network Appliance Firewall L3 Firewall Rules](#get-network-appliance-firewall-l3-firewall-rules)
    - [Get Network Appliance Firewall L7 Firewall Rules](#get-network-appliance-firewall-l7-firewall-rules)
    - [Get Network Appliance Firewall L7 Firewall Rules Application Categories](#get-network-appliance-firewall-l7-firewall-rules-application-categories)
    - [Get Network Appliance Firewall One To Many Nat Rules](#get-network-appliance-firewall-one-to-many-nat-rules)
    - [Get Network Appliance Firewall One To One Nat Rules](#get-network-appliance-firewall-one-to-one-nat-rules)
    - [Get Network Appliance Firewall Port Forwarding Rules](#get-network-appliance-firewall-port-forwarding-rules)
    - [Get Network Appliance Port](#get-network-appliance-port)
    - [Get Network Appliance Ports](#get-network-appliance-ports)
    - [Get Network Appliance Security Events](#get-network-appliance-security-events)
    - [Get Network Appliance Security Intrusion](#get-network-appliance-security-intrusion)
    - [Get Network Appliance Security Malware](#get-network-appliance-security-malware)
    - [Get Network Appliance Settings](#get-network-appliance-settings)
    - [Get Network Appliance Single Lan](#get-network-appliance-single-lan)
    - [Get Network Appliance Static Route](#get-network-appliance-static-route)
    - [Get Network Appliance Static Routes](#get-network-appliance-static-routes)
    - [Get Network Appliance Traffic Shaping](#get-network-appliance-traffic-shaping)
    - [Get Network Appliance Traffic Shaping Custom Performance Class](#get-network-appliance-traffic-shaping-custom-performance-class)
    - [Get Network Appliance Traffic Shaping Custom Performance Classes](#get-network-appliance-traffic-shaping-custom-performance-classes)
    - [Get Network Appliance Traffic Shaping Rules](#get-network-appliance-traffic-shaping-rules)
    - [Get Network Appliance Traffic Shaping Uplink Bandwidth](#get-network-appliance-traffic-shaping-uplink-bandwidth)
    - [Get Network Appliance Traffic Shaping Uplink Selection](#get-network-appliance-traffic-shaping-uplink-selection)
    - [Get Network Appliance Vlan](#get-network-appliance-vlan)
    - [Get Network Appliance Vlans](#get-network-appliance-vlans)
    - [Get Network Appliance Vlans Settings](#get-network-appliance-vlans-settings)
    - [Get Network Appliance Vpn Bgp](#get-network-appliance-vpn-bgp)
    - [Get Network Appliance Vpn Site To Site Vpn](#get-network-appliance-vpn-site-to-site-vpn)
    - [Get Network Appliance Warm Spare](#get-network-appliance-warm-spare)
    - [Get Organization Appliance Security Events](#get-organization-appliance-security-events)
    - [Get Organization Appliance Security Intrusion](#get-organization-appliance-security-intrusion)
    - [Get Organization Appliance Uplink Statuses](#get-organization-appliance-uplink-statuses)
    - [Get Organization Appliance Vpn Stats](#get-organization-appliance-vpn-stats)
    - [Get Organization Appliance Vpn Statuses](#get-organization-appliance-vpn-statuses)
    - [Get Organization Appliance Vpn Third Party V P N Peers](#get-organization-appliance-vpn-third-party-v-p-n-peers)
    - [Get Organization Appliance Vpn Vpn Firewall Rules](#get-organization-appliance-vpn-vpn-firewall-rules)
    - [Swap Network Appliance Warm Spare](#swap-network-appliance-warm-spare)
    - [Update Network Appliance Connectivity Monitoring Destinations](#update-network-appliance-connectivity-monitoring-destinations)
    - [Update Network Appliance Content Filtering](#update-network-appliance-content-filtering)
    - [Update Network Appliance Firewall Cellular Firewall Rules](#update-network-appliance-firewall-cellular-firewall-rules)
    - [Update Network Appliance Firewall Firewalled Service](#update-network-appliance-firewall-firewalled-service)
    - [Update Network Appliance Firewall Inbound Firewall Rules](#update-network-appliance-firewall-inbound-firewall-rules)
    - [Update Network Appliance Firewall L3 Firewall Rules](#update-network-appliance-firewall-l3-firewall-rules)
    - [Update Network Appliance Firewall L7 Firewall Rules](#update-network-appliance-firewall-l7-firewall-rules)
    - [Update Network Appliance Firewall One To Many Nat Rules](#update-network-appliance-firewall-one-to-many-nat-rules)
    - [Update Network Appliance Firewall One To One Nat Rules](#update-network-appliance-firewall-one-to-one-nat-rules)
    - [Update Network Appliance Firewall Port Forwarding Rules](#update-network-appliance-firewall-port-forwarding-rules)
    - [Update Network Appliance Port](#update-network-appliance-port)
    - [Update Network Appliance Security Intrusion](#update-network-appliance-security-intrusion)
    - [Update Network Appliance Security Malware](#update-network-appliance-security-malware)
    - [Update Network Appliance Single Lan](#update-network-appliance-single-lan)
    - [Update Network Appliance Static Route](#update-network-appliance-static-route)
    - [Update Network Appliance Traffic Shaping](#update-network-appliance-traffic-shaping)
    - [Update Network Appliance Traffic Shaping Custom Performance Class](#update-network-appliance-traffic-shaping-custom-performance-class)
    - [Update Network Appliance Traffic Shaping Rules](#update-network-appliance-traffic-shaping-rules)
    - [Update Network Appliance Traffic Shaping Uplink Bandwidth](#update-network-appliance-traffic-shaping-uplink-bandwidth)
    - [Update Network Appliance Traffic Shaping Uplink Selection](#update-network-appliance-traffic-shaping-uplink-selection)
    - [Update Network Appliance Vlan](#update-network-appliance-vlan)
    - [Update Network Appliance Vlans Settings](#update-network-appliance-vlans-settings)
    - [Update Network Appliance Vpn Bgp](#update-network-appliance-vpn-bgp)
    - [Update Network Appliance Vpn Site To Site Vpn](#update-network-appliance-vpn-site-to-site-vpn)
    - [Update Network Appliance Warm Spare](#update-network-appliance-warm-spare)
    - [Update Organization Appliance Security Intrusion](#update-organization-appliance-security-intrusion)
    - [Update Organization Appliance Vpn Third Party V P N Peers](#update-organization-appliance-vpn-third-party-v-p-n-peers)
    - [Update Organization Appliance Vpn Vpn Firewall Rules](#update-organization-appliance-vpn-vpn-firewall-rules)
- [Camera](#camera)
    - [Create Network Camera Quality Retention Profile](#create-network-camera-quality-retention-profile)
    - [Delete Network Camera Quality Retention Profile](#delete-network-camera-quality-retention-profile)
    - [Generate Device Camera Snapshot](#generate-device-camera-snapshot)
    - [Get Device Camera Analytics Live](#get-device-camera-analytics-live)
    - [Get Device Camera Analytics Overview](#get-device-camera-analytics-overview)
    - [Get Device Camera Analytics Recent](#get-device-camera-analytics-recent)
    - [Get Device Camera Analytics Zone History](#get-device-camera-analytics-zone-history)
    - [Get Device Camera Analytics Zones](#get-device-camera-analytics-zones)
    - [Get Device Camera Quality And Retention](#get-device-camera-quality-and-retention)
    - [Get Device Camera Sense](#get-device-camera-sense)
    - [Get Device Camera Sense Object Detection Models](#get-device-camera-sense-object-detection-models)
    - [Get Device Camera Video Link](#get-device-camera-video-link)
    - [Get Device Camera Video Settings](#get-device-camera-video-settings)
    - [Get Network Camera Quality Retention Profile](#get-network-camera-quality-retention-profile)
    - [Get Network Camera Quality Retention Profiles](#get-network-camera-quality-retention-profiles)
    - [Get Network Camera Schedules](#get-network-camera-schedules)
    - [Update Device Camera Quality And Retention](#update-device-camera-quality-and-retention)
    - [Update Device Camera Sense](#update-device-camera-sense)
    - [Update Device Camera Video Settings](#update-device-camera-video-settings)
    - [Update Network Camera Quality Retention Profile](#update-network-camera-quality-retention-profile)
- [Cellular Gateway](#cellular-gateway)
    - [Get Device Cellular Gateway Lan](#get-device-cellular-gateway-lan)
    - [Get Device Cellular Gateway Port Forwarding Rules](#get-device-cellular-gateway-port-forwarding-rules)
    - [Get Network Cellular Gateway Connectivity Monitoring Destinations](#get-network-cellular-gateway-connectivity-monitoring-destinations)
    - [Get Network Cellular Gateway Dhcp](#get-network-cellular-gateway-dhcp)
    - [Get Network Cellular Gateway Subnet Pool](#get-network-cellular-gateway-subnet-pool)
    - [Get Network Cellular Gateway Uplink](#get-network-cellular-gateway-uplink)
    - [Get Organization Cellular Gateway Uplink Statuses](#get-organization-cellular-gateway-uplink-statuses)
    - [Update Device Cellular Gateway Lan](#update-device-cellular-gateway-lan)
    - [Update Device Cellular Gateway Port Forwarding Rules](#update-device-cellular-gateway-port-forwarding-rules)
    - [Update Network Cellular Gateway Connectivity Monitoring Destinations](#update-network-cellular-gateway-connectivity-monitoring-destinations)
    - [Update Network Cellular Gateway Dhcp](#update-network-cellular-gateway-dhcp)
    - [Update Network Cellular Gateway Subnet Pool](#update-network-cellular-gateway-subnet-pool)
    - [Update Network Cellular Gateway Uplink](#update-network-cellular-gateway-uplink)
- [Insight](#insight)
    - [Create Organization Insight Monitored Media Server](#create-organization-insight-monitored-media-server)
    - [Delete Organization Insight Monitored Media Server](#delete-organization-insight-monitored-media-server)
    - [Get Organization Insight Monitored Media Server](#get-organization-insight-monitored-media-server)
    - [Get Organization Insight Monitored Media Servers](#get-organization-insight-monitored-media-servers)
    - [Update Organization Insight Monitored Media Server](#update-organization-insight-monitored-media-server)
- [Sm](#sm)
    - [Checkin Network Sm Devices](#checkin-network-sm-devices)
    - [Create Network Sm Bypass Activation Lock Attempt](#create-network-sm-bypass-activation-lock-attempt)
    - [Create Network Sm Target Group](#create-network-sm-target-group)
    - [Delete Network Sm Target Group](#delete-network-sm-target-group)
    - [Delete Network Sm User Access Device](#delete-network-sm-user-access-device)
    - [Get Network Sm Bypass Activation Lock Attempt](#get-network-sm-bypass-activation-lock-attempt)
    - [Get Network Sm Device Cellular Usage History](#get-network-sm-device-cellular-usage-history)
    - [Get Network Sm Device Certs](#get-network-sm-device-certs)
    - [Get Network Sm Device Connectivity](#get-network-sm-device-connectivity)
    - [Get Network Sm Device Desktop Logs](#get-network-sm-device-desktop-logs)
    - [Get Network Sm Device Device Command Logs](#get-network-sm-device-device-command-logs)
    - [Get Network Sm Device Device Profiles](#get-network-sm-device-device-profiles)
    - [Get Network Sm Device Network Adapters](#get-network-sm-device-network-adapters)
    - [Get Network Sm Device Performance History](#get-network-sm-device-performance-history)
    - [Get Network Sm Device Restrictions](#get-network-sm-device-restrictions)
    - [Get Network Sm Device Security Centers](#get-network-sm-device-security-centers)
    - [Get Network Sm Device Softwares](#get-network-sm-device-softwares)
    - [Get Network Sm Device Wlan Lists](#get-network-sm-device-wlan-lists)
    - [Get Network Sm Devices](#get-network-sm-devices)
    - [Get Network Sm Profiles](#get-network-sm-profiles)
    - [Get Network Sm Target Group](#get-network-sm-target-group)
    - [Get Network Sm Target Groups](#get-network-sm-target-groups)
    - [Get Network Sm User Access Devices](#get-network-sm-user-access-devices)
    - [Get Network Sm User Device Profiles](#get-network-sm-user-device-profiles)
    - [Get Network Sm User Softwares](#get-network-sm-user-softwares)
    - [Get Network Sm Users](#get-network-sm-users)
    - [Get Organization Sm Apns Cert](#get-organization-sm-apns-cert)
    - [Get Organization Sm Vpp Account](#get-organization-sm-vpp-account)
    - [Get Organization Sm Vpp Accounts](#get-organization-sm-vpp-accounts)
    - [Lock Network Sm Devices](#lock-network-sm-devices)
    - [Modify Network Sm Devices Tags](#modify-network-sm-devices-tags)
    - [Move Network Sm Devices](#move-network-sm-devices)
    - [Refresh Network Sm Device Details](#refresh-network-sm-device-details)
    - [Unenroll Network Sm Device](#unenroll-network-sm-device)
    - [Update Network Sm Devices Fields](#update-network-sm-devices-fields)
    - [Update Network Sm Target Group](#update-network-sm-target-group)
    - [Wipe Network Sm Devices](#wipe-network-sm-devices)
- [Switch](#switch)
    - [Add Network Switch Stack](#add-network-switch-stack)
    - [Clone Organization Switch Devices](#clone-organization-switch-devices)
    - [Create Device Switch Routing Interface](#create-device-switch-routing-interface)
    - [Create Device Switch Routing Static Route](#create-device-switch-routing-static-route)
    - [Create Network Switch Access Policy](#create-network-switch-access-policy)
    - [Create Network Switch Link Aggregation](#create-network-switch-link-aggregation)
    - [Create Network Switch Port Schedule](#create-network-switch-port-schedule)
    - [Create Network Switch Qos Rule](#create-network-switch-qos-rule)
    - [Create Network Switch Routing Multicast Rendezvous Point](#create-network-switch-routing-multicast-rendezvous-point)
    - [Create Network Switch Stack](#create-network-switch-stack)
    - [Create Network Switch Stack Routing Interface](#create-network-switch-stack-routing-interface)
    - [Create Network Switch Stack Routing Static Route](#create-network-switch-stack-routing-static-route)
    - [Cycle Device Switch Ports](#cycle-device-switch-ports)
    - [Delete Device Switch Routing Interface](#delete-device-switch-routing-interface)
    - [Delete Device Switch Routing Static Route](#delete-device-switch-routing-static-route)
    - [Delete Network Switch Access Policy](#delete-network-switch-access-policy)
    - [Delete Network Switch Link Aggregation](#delete-network-switch-link-aggregation)
    - [Delete Network Switch Port Schedule](#delete-network-switch-port-schedule)
    - [Delete Network Switch Qos Rule](#delete-network-switch-qos-rule)
    - [Delete Network Switch Routing Multicast Rendezvous Point](#delete-network-switch-routing-multicast-rendezvous-point)
    - [Delete Network Switch Stack](#delete-network-switch-stack)
    - [Delete Network Switch Stack Routing Interface](#delete-network-switch-stack-routing-interface)
    - [Delete Network Switch Stack Routing Static Route](#delete-network-switch-stack-routing-static-route)
    - [Get Device Switch Port](#get-device-switch-port)
    - [Get Device Switch Ports](#get-device-switch-ports)
    - [Get Device Switch Ports Statuses](#get-device-switch-ports-statuses)
    - [Get Device Switch Ports Statuses Packets](#get-device-switch-ports-statuses-packets)
    - [Get Device Switch Routing Interface](#get-device-switch-routing-interface)
    - [Get Device Switch Routing Interface Dhcp](#get-device-switch-routing-interface-dhcp)
    - [Get Device Switch Routing Interfaces](#get-device-switch-routing-interfaces)
    - [Get Device Switch Routing Static Route](#get-device-switch-routing-static-route)
    - [Get Device Switch Routing Static Routes](#get-device-switch-routing-static-routes)
    - [Get Device Switch Warm Spare](#get-device-switch-warm-spare)
    - [Get Network Switch Access Control Lists](#get-network-switch-access-control-lists)
    - [Get Network Switch Access Policies](#get-network-switch-access-policies)
    - [Get Network Switch Access Policy](#get-network-switch-access-policy)
    - [Get Network Switch Dhcp Server Policy](#get-network-switch-dhcp-server-policy)
    - [Get Network Switch Dscp To Cos Mappings](#get-network-switch-dscp-to-cos-mappings)
    - [Get Network Switch Link Aggregations](#get-network-switch-link-aggregations)
    - [Get Network Switch Mtu](#get-network-switch-mtu)
    - [Get Network Switch Port Schedules](#get-network-switch-port-schedules)
    - [Get Network Switch Qos Rule](#get-network-switch-qos-rule)
    - [Get Network Switch Qos Rules](#get-network-switch-qos-rules)
    - [Get Network Switch Qos Rules Order](#get-network-switch-qos-rules-order)
    - [Get Network Switch Routing Multicast](#get-network-switch-routing-multicast)
    - [Get Network Switch Routing Multicast Rendezvous Point](#get-network-switch-routing-multicast-rendezvous-point)
    - [Get Network Switch Routing Multicast Rendezvous Points](#get-network-switch-routing-multicast-rendezvous-points)
    - [Get Network Switch Routing Ospf](#get-network-switch-routing-ospf)
    - [Get Network Switch Settings](#get-network-switch-settings)
    - [Get Network Switch Stack](#get-network-switch-stack)
    - [Get Network Switch Stack Routing Interface](#get-network-switch-stack-routing-interface)
    - [Get Network Switch Stack Routing Interface Dhcp](#get-network-switch-stack-routing-interface-dhcp)
    - [Get Network Switch Stack Routing Interfaces](#get-network-switch-stack-routing-interfaces)
    - [Get Network Switch Stack Routing Static Route](#get-network-switch-stack-routing-static-route)
    - [Get Network Switch Stack Routing Static Routes](#get-network-switch-stack-routing-static-routes)
    - [Get Network Switch Stacks](#get-network-switch-stacks)
    - [Get Network Switch Storm Control](#get-network-switch-storm-control)
    - [Get Network Switch Stp](#get-network-switch-stp)
    - [Get Organization Config Template Switch Profile Port](#get-organization-config-template-switch-profile-port)
    - [Get Organization Config Template Switch Profile Ports](#get-organization-config-template-switch-profile-ports)
    - [Get Organization Config Template Switch Profiles](#get-organization-config-template-switch-profiles)
    - [Remove Network Switch Stack](#remove-network-switch-stack)
    - [Update Device Switch Port](#update-device-switch-port)
    - [Update Device Switch Routing Interface](#update-device-switch-routing-interface)
    - [Update Device Switch Routing Interface Dhcp](#update-device-switch-routing-interface-dhcp)
    - [Update Device Switch Routing Static Route](#update-device-switch-routing-static-route)
    - [Update Device Switch Warm Spare](#update-device-switch-warm-spare)
    - [Update Network Switch Access Control Lists](#update-network-switch-access-control-lists)
    - [Update Network Switch Access Policy](#update-network-switch-access-policy)
    - [Update Network Switch Dhcp Server Policy](#update-network-switch-dhcp-server-policy)
    - [Update Network Switch Dscp To Cos Mappings](#update-network-switch-dscp-to-cos-mappings)
    - [Update Network Switch Link Aggregation](#update-network-switch-link-aggregation)
    - [Update Network Switch Mtu](#update-network-switch-mtu)
    - [Update Network Switch Port Schedule](#update-network-switch-port-schedule)
    - [Update Network Switch Qos Rule](#update-network-switch-qos-rule)
    - [Update Network Switch Qos Rules Order](#update-network-switch-qos-rules-order)
    - [Update Network Switch Routing Multicast](#update-network-switch-routing-multicast)
    - [Update Network Switch Routing Multicast Rendezvous Point](#update-network-switch-routing-multicast-rendezvous-point)
    - [Update Network Switch Routing Ospf](#update-network-switch-routing-ospf)
    - [Update Network Switch Settings](#update-network-switch-settings)
    - [Update Network Switch Stack Routing Interface](#update-network-switch-stack-routing-interface)
    - [Update Network Switch Stack Routing Interface Dhcp](#update-network-switch-stack-routing-interface-dhcp)
    - [Update Network Switch Stack Routing Static Route](#update-network-switch-stack-routing-static-route)
    - [Update Network Switch Storm Control](#update-network-switch-storm-control)
    - [Update Network Switch Stp](#update-network-switch-stp)
    - [Update Organization Config Template Switch Profile Port](#update-organization-config-template-switch-profile-port)
- [Wireless](#wireless)
    - [Create Network Wireless Rf Profile](#create-network-wireless-rf-profile)
    - [Create Network Wireless Ssid Identity Psk](#create-network-wireless-ssid-identity-psk)
    - [Delete Network Wireless Rf Profile](#delete-network-wireless-rf-profile)
    - [Delete Network Wireless Ssid Identity Psk](#delete-network-wireless-ssid-identity-psk)
    - [Get Device Wireless Bluetooth Settings](#get-device-wireless-bluetooth-settings)
    - [Get Device Wireless Connection Stats](#get-device-wireless-connection-stats)
    - [Get Device Wireless Latency Stats](#get-device-wireless-latency-stats)
    - [Get Device Wireless Radio Settings](#get-device-wireless-radio-settings)
    - [Get Device Wireless Status](#get-device-wireless-status)
    - [Get Network Wireless Air Marshal](#get-network-wireless-air-marshal)
    - [Get Network Wireless Alternate Management Interface](#get-network-wireless-alternate-management-interface)
    - [Get Network Wireless Bluetooth Settings](#get-network-wireless-bluetooth-settings)
    - [Get Network Wireless Channel Utilization History](#get-network-wireless-channel-utilization-history)
    - [Get Network Wireless Client Connection Stats](#get-network-wireless-client-connection-stats)
    - [Get Network Wireless Client Connectivity Events](#get-network-wireless-client-connectivity-events)
    - [Get Network Wireless Client Count History](#get-network-wireless-client-count-history)
    - [Get Network Wireless Client Latency History](#get-network-wireless-client-latency-history)
    - [Get Network Wireless Client Latency Stats](#get-network-wireless-client-latency-stats)
    - [Get Network Wireless Clients Connection Stats](#get-network-wireless-clients-connection-stats)
    - [Get Network Wireless Clients Latency Stats](#get-network-wireless-clients-latency-stats)
    - [Get Network Wireless Connection Stats](#get-network-wireless-connection-stats)
    - [Get Network Wireless Data Rate History](#get-network-wireless-data-rate-history)
    - [Get Network Wireless Devices Connection Stats](#get-network-wireless-devices-connection-stats)
    - [Get Network Wireless Devices Latency Stats](#get-network-wireless-devices-latency-stats)
    - [Get Network Wireless Failed Connections](#get-network-wireless-failed-connections)
    - [Get Network Wireless Latency History](#get-network-wireless-latency-history)
    - [Get Network Wireless Latency Stats](#get-network-wireless-latency-stats)
    - [Get Network Wireless Mesh Statuses](#get-network-wireless-mesh-statuses)
    - [Get Network Wireless Rf Profile](#get-network-wireless-rf-profile)
    - [Get Network Wireless Rf Profiles](#get-network-wireless-rf-profiles)
    - [Get Network Wireless Settings](#get-network-wireless-settings)
    - [Get Network Wireless Signal Quality History](#get-network-wireless-signal-quality-history)
    - [Get Network Wireless Ssid](#get-network-wireless-ssid)
    - [Get Network Wireless Ssid Firewall L3 Firewall Rules](#get-network-wireless-ssid-firewall-l3-firewall-rules)
    - [Get Network Wireless Ssid Firewall L7 Firewall Rules](#get-network-wireless-ssid-firewall-l7-firewall-rules)
    - [Get Network Wireless Ssid Identity Psk](#get-network-wireless-ssid-identity-psk)
    - [Get Network Wireless Ssid Identity Psks](#get-network-wireless-ssid-identity-psks)
    - [Get Network Wireless Ssid Splash Settings](#get-network-wireless-ssid-splash-settings)
    - [Get Network Wireless Ssid Traffic Shaping Rules](#get-network-wireless-ssid-traffic-shaping-rules)
    - [Get Network Wireless Ssids](#get-network-wireless-ssids)
    - [Get Network Wireless Usage History](#get-network-wireless-usage-history)
    - [Update Device Wireless Bluetooth Settings](#update-device-wireless-bluetooth-settings)
    - [Update Device Wireless Radio Settings](#update-device-wireless-radio-settings)
    - [Update Network Wireless Alternate Management Interface](#update-network-wireless-alternate-management-interface)
    - [Update Network Wireless Bluetooth Settings](#update-network-wireless-bluetooth-settings)
    - [Update Network Wireless Rf Profile](#update-network-wireless-rf-profile)
    - [Update Network Wireless Settings](#update-network-wireless-settings)
    - [Update Network Wireless Ssid](#update-network-wireless-ssid)
    - [Update Network Wireless Ssid Firewall L3 Firewall Rules](#update-network-wireless-ssid-firewall-l3-firewall-rules)
    - [Update Network Wireless Ssid Firewall L7 Firewall Rules](#update-network-wireless-ssid-firewall-l7-firewall-rules)
    - [Update Network Wireless Ssid Identity Psk](#update-network-wireless-ssid-identity-psk)
    - [Update Network Wireless Ssid Splash Settings](#update-network-wireless-ssid-splash-settings)
    - [Update Network Wireless Ssid Traffic Shaping Rules](#update-network-wireless-ssid-traffic-shaping-rules)



----------------------------------------

-----------------------------------------
# COMMANDS

## Organizations


### Assign Organization Licenses Seats

**Assign SM seats to a network**
https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

- organizationId (string): (required)
- licenseId (string): The ID of the SM license to assign seats from
- networkId (string): The ID of the SM network to assign the seats to
- seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license




### Claim Into Organization

**Claim a list of devices, licenses, and/or orders into an organization**
https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

- organizationId (string): (required)
- orders (array): The numbers of the orders that should be claimed
- serials (array): The serials of the devices that should be claimed
- licenses (array): The licenses that should be claimed




### Clone Organization

**Create a new organization by cloning the addressed organization**
https://developer.cisco.com/meraki/api-v1/#!clone-organization

- organizationId (string): (required)
- name (string): The name of the new organization




### Combine Organization Networks

**Combine multiple networks into a single network**
https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

- organizationId (string): (required)
- name (string): The name of the combined network
- networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
- enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.




### Create Organization

**Create a new organization**
https://developer.cisco.com/meraki/api-v1/#!create-organization

- name (string): The name of the organization




### Create Organization Action Batch

**Create an action batch**
https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

- organizationId (string): (required)
- actions (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
- confirmed (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
- synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.




### Create Organization Admin

**Create a new dashboard administrator**
https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

- organizationId (string): (required)
- email (string): The email of the dashboard administrator. This attribute can not be updated.
- name (string): The name of the dashboard administrator
- orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
- tags (array): The list of tags that the dashboard administrator has privileges on
- networks (array): The list of networks that the dashboard administrator has privileges on
- authenticationMethod (string): The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of 'Email' or 'Cisco SecureX Sign-On'. The default is Email authentication




### Create Organization Branding Policy

**Add a new branding policy to an organization**
https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

- organizationId (string): (required)
- name (string): Name of the Dashboard branding policy.
- enabled (boolean): Boolean indicating whether this policy is enabled.
- adminSettings (object): Settings for describing which kinds of admins this policy applies to.
- helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.
Each property defaults to 'default or inherit' when not provided.




### Create Organization Config Template

**Create a new configuration template**
https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

- organizationId (string): (required)
- name (string): The name of the configuration template
- timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
- copyFromNetworkId (string): The ID of the network or config template to copy configuration from




### Create Organization Network

**Create a network**
https://developer.cisco.com/meraki/api-v1/#!create-organization-network

- organizationId (string): (required)
- name (string): The name of the new network
- productTypes (array): The product type(s) of the new network. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, environmental. If more than one type is included, the network will be a combined network.
- tags (array): A list of tags to be applied to the network
- timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.




### Create Organization Saml Idp

**Create a SAML IdP for your organization.**
https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

- organizationId (string): (required)
- x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.




### Create Organization Saml Role

**Create a SAML role**
https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

- organizationId (string): (required)
- role (string): The role of the SAML administrator
- orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only' or 'full'
- tags (array): The list of tags that the SAML administrator has privleges on
- networks (array): The list of networks that the SAML administrator has privileges on




### Delete Organization

**Delete an organization**
https://developer.cisco.com/meraki/api-v1/#!delete-organization

- organizationId (string): (required)




### Delete Organization Action Batch

**Delete an action batch**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

- organizationId (string): (required)
- actionBatchId (string): (required)




### Delete Organization Admin

**Revoke all access for a dashboard administrator within this organization**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

- organizationId (string): (required)
- adminId (string): (required)




### Delete Organization Branding Policy

**Delete a branding policy**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

- organizationId (string): (required)
- brandingPolicyId (string): (required)




### Delete Organization Config Template

**Remove a configuration template**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

- organizationId (string): (required)
- configTemplateId (string): (required)




### Delete Organization Saml Idp

**Remove a SAML IdP in your organization.**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

- organizationId (string): (required)
- idpId (string): (required)




### Delete Organization Saml Role

**Remove a SAML role**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

- organizationId (string): (required)
- samlRoleId (string): (required)




### Get Organization

**Return an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization

- organizationId (string): (required)




### Get Organization Action Batch

**Return an action batch**
https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

- organizationId (string): (required)
- actionBatchId (string): (required)




### Get Organization Action Batches

**Return the list of action batches in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

- organizationId (string): (required)
- status (string): Filter batches by status. Valid types are pending, completed, and failed.




### Get Organization Admins

**List the dashboard administrators in this organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

- organizationId (string): (required)




### Get Organization Api Requests

**List the API requests made by an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- adminId (string): Filter the results by the ID of the admin who made the API requests
- path (string): Filter the results by the path of the API requests
- method (string): Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')
- responseCode (integer): Filter the results by the response code of the API requests
- sourceIp (string): Filter the results by the IP address of the originating API request




### Get Organization Api Requests Overview

**Return an aggregated overview of API requests data**
https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

- organizationId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.




### Get Organization Branding Policies

**List the branding policies of an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

- organizationId (string): (required)




### Get Organization Branding Policies Priorities

**Return the branding policy IDs of an organization in priority order**
https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

- organizationId (string): (required)




### Get Organization Branding Policy

**Return a branding policy**
https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

- organizationId (string): (required)
- brandingPolicyId (string): (required)




### Get Organization Config Template

**Return a single configuration template**
https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

- organizationId (string): (required)
- configTemplateId (string): (required)




### Get Organization Config Templates

**List the configuration templates for this organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

- organizationId (string): (required)




### Get Organization Configuration Changes

**View the Change Log for your organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" or "prev" (default) page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkId (string): Filters on the given network
- adminId (string): Filters on the given Admin




### Get Organization Devices

**List the devices in an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp




### Get Organization Devices Statuses

**List the status of every Meraki device in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Organization Devices Uplinks Loss And Latency

**Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

- organizationId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
- uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
- ip (string): Optional filter for a specific destination IP. Default will return all destination IPs.




### Get Organization Inventory Device

**Return a single device from the inventory of an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

- organizationId (string): (required)
- serial (string): (required)




### Get Organization Inventory Devices

**Return the device inventory for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- usedState (string): Filter results by used or unused inventory. Accepted values are "used" or "unused".
- search (string): Search for devices in inventory based on serial number, mac address, or model.




### Get Organization License

**Display a license**
https://developer.cisco.com/meraki/api-v1/#!get-organization-license

- organizationId (string): (required)
- licenseId (string): (required)




### Get Organization Licenses

**List the licenses for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- deviceSerial (string): Filter the licenses to those assigned to a particular device
- networkId (string): Filter the licenses to those assigned in a particular network
- state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'unused', 'unusedActive' or 'recentlyQueued'




### Get Organization Licenses Overview

**Return an overview of the license state for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

- organizationId (string): (required)




### Get Organization Login Security

**Returns the login security settings for an organization.**
https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

- organizationId (string): (required)




### Get Organization Networks

**List the networks that the user has privileges on in an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
- tags (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
- tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Organization Openapi Spec

**Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

- organizationId (string): (required)




### Get Organization Saml

**Returns the SAML SSO enabled settings for an organization.**
https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

- organizationId (string): (required)




### Get Organization Saml Idp

**Get a SAML IdP from your organization.**
https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

- organizationId (string): (required)
- idpId (string): (required)




### Get Organization Saml Idps

**List the SAML IdPs in your organization.**
https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

- organizationId (string): (required)




### Get Organization Saml Role

**Return a SAML role**
https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

- organizationId (string): (required)
- samlRoleId (string): (required)




### Get Organization Saml Roles

**List the SAML roles for this organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

- organizationId (string): (required)




### Get Organization Snmp

**Return the SNMP settings for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

- organizationId (string): (required)




### Get Organization Uplinks Statuses

**List the uplink status of every Meraki MX, MG and Z series devices in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.




### Get Organization Webhooks Alert Types

**Return a list of alert types to be used with managing webhook alerts**
https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

- organizationId (string): (required)




### Get Organization Webhooks Logs

**Return the log of webhook POSTs sent**
https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- url (string): The URL the webhook was sent to




### Get Organizations

**List the organizations that the user has privileges on**
https://developer.cisco.com/meraki/api-v1/#!get-organizations





### Move Organization Licenses

**Move licenses to another organization**
https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

- organizationId (string): (required)
- destOrganizationId (string): The ID of the organization to move the licenses to
- licenseIds (array): A list of IDs of licenses to move to the new organization




### Move Organization Licenses Seats

**Move SM seats to another organization**
https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

- organizationId (string): (required)
- destOrganizationId (string): The ID of the organization to move the SM seats to
- licenseId (string): The ID of the SM license to move the seats from
- seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license




### Renew Organization Licenses Seats

**Renew SM seats of a license**
https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

- organizationId (string): (required)
- licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
- unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'




### Update Organization

**Update an organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization

- organizationId (string): (required)
- name (string): The name of the organization




### Update Organization Action Batch

**Update an action batch**
https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch

- organizationId (string): (required)
- actionBatchId (string): (required)
- confirmed (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
- synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.




### Update Organization Admin

**Update an administrator**
https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

- organizationId (string): (required)
- adminId (string): (required)
- name (string): The name of the dashboard administrator
- orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
- tags (array): The list of tags that the dashboard administrator has privileges on
- networks (array): The list of networks that the dashboard administrator has privileges on




### Update Organization Branding Policies Priorities

**Update the priority ordering of an organization's branding policies.**
https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

- organizationId (string): (required)
- brandingPolicyIds (array): A list of branding policy IDs arranged in ascending priority order (IDs later in the array have higher priority).




### Update Organization Branding Policy

**Update a branding policy**
https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

- organizationId (string): (required)
- brandingPolicyId (string): (required)
- name (string): Name of the Dashboard branding policy.
- enabled (boolean): Boolean indicating whether this policy is enabled.
- adminSettings (object): Settings for describing which kinds of admins this policy applies to.
- helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
Dashboard; see the documentation for each property to see the allowed values.





### Update Organization Config Template

**Update a configuration template**
https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

- organizationId (string): (required)
- configTemplateId (string): (required)
- name (string): The name of the configuration template
- timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>




### Update Organization License

**Update a license**
https://developer.cisco.com/meraki/api-v1/#!update-organization-license

- organizationId (string): (required)
- licenseId (string): (required)
- deviceSerial (string): The serial number of the device to assign this license to. Set this to null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.




### Update Organization Login Security

**Update the login security settings for an organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

- organizationId (string): (required)
- enforcePasswordExpiration (boolean): Boolean indicating whether users are forced to change their password every X number of days.
- passwordExpirationDays (integer): Number of days after which users will be forced to change their password.
- enforceDifferentPasswords (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
- numDifferentPasswords (integer): Number of recent passwords that new password must be distinct from.
- enforceStrongPasswords (boolean): Boolean indicating whether users will be forced to choose strong passwords for their accounts. Strong passwords are at least 8 characters that contain 3 of the following: number, uppercase letter, lowercase letter, and symbol
- enforceAccountLockout (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
- accountLockoutAttempts (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
- enforceIdleTimeout (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
- idleTimeoutMinutes (integer): Number of minutes users can remain idle before being logged out of their accounts.
- enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the Google Authenticator application.
- enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
- loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.




### Update Organization Saml

**Updates the SAML SSO enabled settings for an organization.**
https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

- organizationId (string): (required)
- enabled (boolean): Boolean for updating SAML SSO enabled settings.




### Update Organization Saml Idp

**Update a SAML IdP in your organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

- organizationId (string): (required)
- idpId (string): (required)
- x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
- sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.




### Update Organization Saml Role

**Update a SAML role**
https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

- organizationId (string): (required)
- samlRoleId (string): (required)
- role (string): The role of the SAML administrator
- orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only' or 'full'
- tags (array): The list of tags that the SAML administrator has privleges on
- networks (array): The list of networks that the SAML administrator has privileges on




### Update Organization Snmp

**Update the SNMP settings for an organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

- organizationId (string): (required)
- v2cEnabled (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
- v3Enabled (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
- v3AuthMode (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
- v3AuthPass (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
- v3PrivMode (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
- v3PrivPass (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
- peerIps (array): The list of IPv4 addresses that are allowed to access the SNMP server.



## Networks


### Bind Network

**Bind a network to a template.**
https://developer.cisco.com/meraki/api-v1/#!bind-network

- networkId (string): (required)
- configTemplateId (string): The ID of the template to which the network should be bound.
- autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.




### Claim Network Devices

**Claim devices into a network**
https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

- networkId (string): (required)
- serials (array): A list of serials of devices to claim




### Create Network Floor Plan

**Upload a floor plan**
https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

- networkId (string): (required)
- name (string): The name of your floor plan.
- imageContents (string): The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
- center (object): The longitude and latitude of the center of your floor plan. The 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
- bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
- bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
- topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
- topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.




### Create Network Group Policy

**Create a group policy**
https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

- networkId (string): (required)
- name (string): The name for your group policy. Required.
- scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

- bandwidth (object):     The bandwidth settings for clients bound to your group policy.

- firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

- contentFiltering (object): The content filtering settings for your group policy
- splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.




### Create Network Meraki Auth User

**Create a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)**
https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

- networkId (string): (required)
- email (string): Email address of the user
- name (string): Name of the user
- password (string): The password for this user account
- authorizations (array): Authorization zones and expiration dates for the user.
- accountType (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for wired networks. Defaults to '802.1X'.
- emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.




### Create Network Mqtt Broker

**Add an MQTT broker**
https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

- networkId (string): (required)
- name (string): Name of the MQTT broker
- host (string): Host name/IP address where MQTT broker runs
- port (integer): Host port though which MQTT broker can be reached




### Create Network Pii Request

**Submit a new delete or restrict processing PII request**
https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

- networkId (string): (required)
- type (string): One of "delete" or "restrict processing"
- datasets (array): The datasets related to the provided key that should be deleted. Only applies to "delete" requests. The value "all" will be expanded to all datasets applicable to this type. The datasets by applicable to each type are: mac (usage, events, traffic), email (users, loginAttempts), username (users, loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device), smUserId (user)
- username (string): The username of a network log in. Only applies to "delete" requests.
- email (string): The email of a network user account. Only applies to "delete" requests.
- mac (string): The MAC of a network client device. Applies to both "restrict processing" and "delete" requests.
- smDeviceId (string): The sm_device_id of a Systems Manager device. The only way to "restrict processing" or "delete" a Systems Manager device. Must include "device" in the dataset for a "delete" request to destroy the device.
- smUserId (string): The sm_user_id of a Systems Manager user. The only way to "restrict processing" or "delete" a Systems Manager user. Must include "user" in the dataset for a "delete" request to destroy the user.




### Create Network Webhooks Http Server

**Add an HTTP server to a network**
https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

- networkId (string): (required)
- name (string): A name for easy reference to the HTTP server
- url (string): The URL of the HTTP server
- sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.




### Create Network Webhooks Webhook Test

**Send a test webhook for a network**
https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

- networkId (string): (required)
- url (string): The URL where the test webhook will be sent
- sharedSecret (string): The shared secret the test webhook will send. Optional. Defaults to an empty string.




### Delete Network

**Delete a network**
https://developer.cisco.com/meraki/api-v1/#!delete-network

- networkId (string): (required)




### Delete Network Floor Plan

**Destroy a floor plan**
https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

- networkId (string): (required)
- floorPlanId (string): (required)




### Delete Network Group Policy

**Delete a group policy**
https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

- networkId (string): (required)
- groupPolicyId (string): (required)




### Delete Network Meraki Auth User

**Delete a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be deleted)**
https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

- networkId (string): (required)
- merakiAuthUserId (string): (required)




### Delete Network Mqtt Broker

**Delete an MQTT broker**
https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

- networkId (string): (required)
- mqttBrokerId (string): (required)




### Delete Network Pii Request

**Delete a restrict processing PII request**
https://developer.cisco.com/meraki/api-v1/#!delete-network-pii-request

- networkId (string): (required)
- requestId (string): (required)




### Delete Network Webhooks Http Server

**Delete an HTTP server from a network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server

- networkId (string): (required)
- httpServerId (string): (required)




### Get Network

**Return a network**
https://developer.cisco.com/meraki/api-v1/#!get-network

- networkId (string): (required)




### Get Network Alerts Settings

**Return the alert configuration for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

- networkId (string): (required)




### Get Network Bluetooth Client

**Return a Bluetooth client**
https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

- networkId (string): (required)
- bluetoothClientId (string): (required)
- includeConnectivityHistory (boolean): Include the connectivity history for this client
- connectivityHistoryTimespan (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.




### Get Network Bluetooth Clients

**List the Bluetooth clients seen by APs in this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
- perPage (integer): The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- includeConnectivityHistory (boolean): Include the connectivity history for this client




### Get Network Client

**Return the client associated with the given identifier**
https://developer.cisco.com/meraki/api-v1/#!get-network-client

- networkId (string): (required)
- clientId (string): (required)




### Get Network Client Policy

**Return the policy assigned to a client on the network**
https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

- networkId (string): (required)
- clientId (string): (required)




### Get Network Client Splash Authorization Status

**Return the splash authorization for a client, for each SSID they've associated with through splash**
https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

- networkId (string): (required)
- clientId (string): (required)




### Get Network Client Traffic History

**Return the client's network traffic data over time**
https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

- networkId (string): (required)
- clientId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Client Usage History

**Return the client's daily usage history**
https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

- networkId (string): (required)
- clientId (string): (required)




### Get Network Clients

**List the clients that have used this network in the timespan**
https://developer.cisco.com/meraki/api-v1/#!get-network-clients

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Clients Application Usage

**Return the application usage data for clients**
https://developer.cisco.com/meraki/api-v1/#!get-network-clients-application-usage

- networkID (string): (required)
- clients (string): A list of client keys, MACs or IPs separated by comma.
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- ssidNumber (integer): An SSID number to include. If not specified, eveusage histories application usagents for all SSIDs will be returned.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.




### Get Network Clients Usage Histories

**Return the usage histories for clients**
https://developer.cisco.com/meraki/api-v1/#!get-network-clients-usage-histories

- networkID (string): (required)
- clients (string): A list of client keys, MACs or IPs separated by comma.
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.




### Get Network Devices

**List the devices in a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-devices

- networkId (string): (required)




### Get Network Events

**List the events for the network**
https://developer.cisco.com/meraki/api-v1/#!get-network-events

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" or "prev" (default) page
- event_log_end_time (string): ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, to retrieve events within a time window
- productType (string): The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and environmental
- includedEventTypes (array): A list of event types. The returned events will be filtered to only include events with these types.
- excludedEventTypes (array): A list of event types. The returned events will be filtered to exclude events with these types.
- deviceMac (string): The MAC address of the Meraki device which the list of events will be filtered with
- deviceSerial (string): The serial of the Meraki device which the list of events will be filtered with
- deviceName (string): The name of the Meraki device which the list of events will be filtered with
- clientIp (string): The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
- clientMac (string): The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
- clientName (string): The name, or partial name, of the client which the list of events will be filtered with
- smDeviceMac (string): The MAC address of the Systems Manager device which the list of events will be filtered with
- smDeviceName (string): The name of the Systems Manager device which the list of events will be filtered with
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Events Event Types

**List the event type to human-readable description**
https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

- networkId (string): (required)




### Get Network Firmware Upgrades

**Get current maintenance window for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

- networkId (string): (required)




### Get Network Floor Plan

**Find a floor plan by ID**
https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

- networkId (string): (required)
- floorPlanId (string): (required)




### Get Network Floor Plans

**List the floor plans that belong to your network**
https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

- networkId (string): (required)




### Get Network Group Policies

**List the group policies in a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

- networkId (string): (required)




### Get Network Group Policy

**Display a group policy**
https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

- networkId (string): (required)
- groupPolicyId (string): (required)




### Get Network Meraki Auth User

**Return the Meraki Auth splash guest, RADIUS, or client VPN user**
https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

- networkId (string): (required)
- merakiAuthUserId (string): (required)




### Get Network Meraki Auth Users

**List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)**
https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

- networkId (string): (required)




### Get Network Mqtt Broker

**Return an MQTT broker**
https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

- networkId (string): (required)
- mqttBrokerId (string): (required)




### Get Network Mqtt Brokers

**List the MQTT brokers for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

- networkId (string): (required)




### Get Network Netflow

**Return the NetFlow traffic reporting settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

- networkId (string): (required)




### Get Network Network Health Channel Utilization

**Get the channel utilization over each radio for all APs in a network.**
https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Pii Pii Keys

**List the keys required to access Personally Identifiable Information (PII) for a given identifier**
https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

- networkId (string): (required)
- username (string): The username of a Systems Manager user
- email (string): The email of a network user account or a Systems Manager device
- mac (string): The MAC of a network client device or a Systems Manager device
- serial (string): The serial of a Systems Manager device
- imei (string): The IMEI of a Systems Manager device
- bluetoothMac (string): The MAC of a Bluetooth client




### Get Network Pii Request

**Return a PII request**
https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

- networkId (string): (required)
- requestId (string): (required)




### Get Network Pii Requests

**List the PII requests for this network or organization**
https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

- networkId (string): (required)




### Get Network Pii Sm Devices For Key

**Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier**
https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

- networkId (string): (required)
- username (string): The username of a Systems Manager user
- email (string): The email of a network user account or a Systems Manager device
- mac (string): The MAC of a network client device or a Systems Manager device
- serial (string): The serial of a Systems Manager device
- imei (string): The IMEI of a Systems Manager device
- bluetoothMac (string): The MAC of a Bluetooth client




### Get Network Pii Sm Owners For Key

**Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier**
https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

- networkId (string): (required)
- username (string): The username of a Systems Manager user
- email (string): The email of a network user account or a Systems Manager device
- mac (string): The MAC of a network client device or a Systems Manager device
- serial (string): The serial of a Systems Manager device
- imei (string): The IMEI of a Systems Manager device
- bluetoothMac (string): The MAC of a Bluetooth client




### Get Network Settings

**Return the settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-settings

- networkId (string): (required)




### Get Network Snmp

**Return the SNMP settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

- networkId (string): (required)




### Get Network Splash Login Attempts

**List the splash login attempts for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

- networkId (string): (required)
- ssidNumber (integer): Only return the login attempts for the specified SSID
- loginIdentifier (string): The username, email, or phone number used during login
- timespan (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months




### Get Network Syslog Servers

**List the syslog servers for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

- networkId (string): (required)




### Get Network Traffic

**Return the traffic analysis data for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
- deviceType (string): Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage.




### Get Network Traffic Analysis

**Return the traffic analysis settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

- networkId (string): (required)




### Get Network Traffic Shaping Application Categories

**Returns the application categories for traffic shaping rules.**
https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

- networkId (string): (required)




### Get Network Traffic Shaping Dscp Tagging Options

**Returns the available DSCP tagging options for your traffic shaping rules.**
https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

- networkId (string): (required)




### Get Network Webhooks Http Server

**Return an HTTP server for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

- networkId (string): (required)
- httpServerId (string): (required)




### Get Network Webhooks Http Servers

**List the HTTP servers for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

- networkId (string): (required)




### Get Network Webhooks Webhook Test

**Return the status of a webhook test for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

- networkId (string): (required)
- webhookTestId (string): (required)




### Provision Network Clients

**Provisions a client with a name and policy**
https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

- networkId (string): (required)
- clients (array): The array of clients to provision
- devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
- groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
- policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
- policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy




### Remove Network Devices

**Remove a single device**
https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

- networkId (string): (required)
- serial (string): The serial of a device




### Split Network

**Split a combined network into individual networks for each type of device**
https://developer.cisco.com/meraki/api-v1/#!split-network

- networkId (string): (required)




### Unbind Network

**Unbind a network from a template.**
https://developer.cisco.com/meraki/api-v1/#!unbind-network

- networkId (string): (required)




### Update Network

**Update a network**
https://developer.cisco.com/meraki/api-v1/#!update-network

- networkId (string): (required)
- name (string): The name of the network
- timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
- tags (array): A list of tags to be applied to the network
- enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.




### Update Network Alerts Settings

**Update the alert configuration for this network**
https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

- networkId (string): (required)
- defaultDestinations (object): The network-wide destinations for all alerts on the network.
- alerts (array): Alert-specific configuration for each type. Only alerts that pertain to the network can be updated.




### Update Network Client Policy

**Update the policy assigned to a client on the network**
https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

- networkId (string): (required)
- clientId (string): (required)
- devicePolicy (string): The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
- groupPolicyId (string): [optional] If 'devicePolicy' is set to 'Group policy' this param is used to specify the group policy ID.




### Update Network Client Splash Authorization Status

**Update a client's splash authorization**
https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status

- networkId (string): (required)
- clientId (string): (required)
- ssids (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs




### Update Network Firmware Upgrades

**Update current maintenance window for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

- networkId (string): (required)
- upgradeWindow (object): Upgrade window for devices in network




### Update Network Floor Plan

**Update a floor plan's geolocation and other meta data**
https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

- networkId (string): (required)
- floorPlanId (string): (required)
- name (string): The name of your floor plan.
- center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
- bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
- bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
- topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
- topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
- imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.




### Update Network Group Policy

**Update a group policy**
https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

- networkId (string): (required)
- groupPolicyId (string): (required)
- name (string): The name for your group policy.
- scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

- bandwidth (object):     The bandwidth settings for clients bound to your group policy.

- firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

- contentFiltering (object): The content filtering settings for your group policy
- splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
- vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
- bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.




### Update Network Meraki Auth User

**Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be deleted)**
https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

- networkId (string): (required)
- merakiAuthUserId (string): (required)
- name (string): Name of the user
- password (string): The password for this user account
- emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
- authorizations (array): Authorization zones and expiration dates for the user.




### Update Network Mqtt Broker

**Update an MQTT broker**
https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

- networkId (string): (required)
- mqttBrokerId (string): (required)
- name (string): Name of the mqtt config
- host (string): Host name where mqtt broker runs
- port (integer): Host port though which mqtt broker can be reached




### Update Network Netflow

**Update the NetFlow traffic reporting settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

- networkId (string): (required)
- reportingEnabled (boolean): Boolean indicating whether NetFlow traffic reporting is enabled (true) or disabled (false).
- collectorIp (string): The IPv4 address of the NetFlow collector.
- collectorPort (integer): The port that the NetFlow collector will be listening on.




### Update Network Settings

**Update the settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-settings

- networkId (string): (required)
- localStatusPageEnabled (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
- remoteStatusPageEnabled (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true




### Update Network Snmp

**Update the SNMP settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

- networkId (string): (required)
- access (string): The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3).
- communityString (string): The SNMP community string. Only relevant if 'access' is set to 'community'.
- users (array): The list of SNMP users. Only relevant if 'access' is set to 'users'.




### Update Network Syslog Servers

**Update the syslog servers for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

- networkId (string): (required)
- servers (array): A list of the syslog servers for this network




### Update Network Traffic Analysis

**Update the traffic analysis settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

- networkId (string): (required)
- mode (string):     The traffic analysis mode for the network. Can be one of 'disabled' (do not collect traffic types),
'basic' (collect generic traffic categories), or 'detailed' (collect destination hostnames).

- customPieChartItems (array): The list of items that make up the custom pie chart for traffic reporting.




### Update Network Webhooks Http Server

**Update an HTTP server**
https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

- networkId (string): (required)
- httpServerId (string): (required)
- name (string): A name for easy reference to the HTTP server
- url (string): The URL of the HTTP server
- sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.



## Devices


### Blink Device Leds

**Blink the LEDs on a device**
https://developer.cisco.com/meraki/api-v1/#!blink-device-leds

- serial (string): (required)
- duration (integer): The duration in seconds. Must be between 5 and 120. Default is 20 seconds
- period (integer): The period in milliseconds. Must be between 100 and 1000. Default is 160 milliseconds
- duty (integer): The duty cycle as the percent active. Must be between 10 and 90. Default is 50.




### Get Device

**Return a single device**
https://developer.cisco.com/meraki/api-v1/#!get-device

- serial (string): (required)




### Get Device Clients

**List the clients of a device, up to a maximum of a month ago**
https://developer.cisco.com/meraki/api-v1/#!get-device-clients

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.




### Get Device Lldp Cdp

**List LLDP and CDP information for a device**
https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp

- serial (string): (required)




### Get Device Loss And Latency History

**Get the uplink loss percentage and latency in milliseconds for a wired network device.**
https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history

- serial (string): (required)
- ip (string): The destination IP used to obtain the requested stats. This is required.
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
- uplink (string): The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.




### Get Device Management Interface

**Return the management interface settings for a device**
https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

- serial (string): (required)




### Reboot Device

**Reboot a device**
https://developer.cisco.com/meraki/api-v1/#!reboot-device

- serial (string): (required)




### Update Device

**Update the attributes of a device**
https://developer.cisco.com/meraki/api-v1/#!update-device

- serial (string): (required)
- name (string): The name of a device
- tags (array): The list of tags of a device
- lat (number): The latitude of a device
- lng (number): The longitude of a device
- address (string): The address of a device
- notes (string): The notes for the device. String. Limited to 255 characters.
- moveMapMarker (boolean): Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
- switchProfileId (string): The ID of a switch profile to bind to the device (for available switch profiles, see the 'Switch Profiles' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch profile, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
- floorPlanId (string): The floor plan to associate to this device. null disassociates the device from the floorplan.




### Update Device Management Interface

**Update the management interface settings for a device**
https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface

- serial (string): (required)
- wan1 (object): WAN 1 settings
- wan2 (object): WAN 2 settings (only for MX devices)



## Appliance


### Create Network Appliance Static Route

**Add a static route for an MX or teleworker network**
https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route

- networkId (string): (required)
- name (string): The name of the new static route
- subnet (string): The subnet of the static route
- gatewayIp (string): The gateway IP (next hop) of the static route




### Create Network Appliance Traffic Shaping Custom Performance Class

**Add a custom performance class for an MX network**
https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

- networkId (string): (required)
- name (string): Name of the custom performance class
- maxLatency (integer): Maximum latency in milliseconds
- maxJitter (integer): Maximum jitter in milliseconds
- maxLossPercentage (integer): Maximum percentage of packet loss




### Create Network Appliance Vlan

**Add a VLAN**
https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

- networkId (string): (required)
- id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
- name (string): The name of the new VLAN
- subnet (string): The subnet of the VLAN
- applianceIp (string): The local IP of the appliance on the VLAN
- groupPolicyId (string): The id of the desired group policy to apply to the VLAN




### Delete Network Appliance Static Route

**Delete a static route from an MX or teleworker network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route

- networkId (string): (required)
- staticRouteId (string): (required)




### Delete Network Appliance Traffic Shaping Custom Performance Class

**Delete a custom performance class from an MX network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

- networkId (string): (required)
- customPerformanceClassId (string): (required)




### Delete Network Appliance Vlan

**Delete a VLAN from a network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

- networkId (string): (required)
- vlanId (string): (required)




### Get Device Appliance Dhcp Subnets

**Return the DHCP subnet information for an appliance**
https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets

- serial (string): (required)




### Get Device Appliance Performance

**Return the performance score for a single MX**
https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance

- serial (string): (required)




### Get Network Appliance Client Security Events

**List the security events for a client**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events

- networkId (string): (required)
- clientId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.




### Get Network Appliance Connectivity Monitoring Destinations

**Return the connectivity testing destinations for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations

- networkId (string): (required)




### Get Network Appliance Content Filtering

**Return the content filtering settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering

- networkId (string): (required)




### Get Network Appliance Content Filtering Categories

**List all available content filtering categories for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories

- networkId (string): (required)




### Get Network Appliance Firewall Cellular Firewall Rules

**Return the cellular firewall rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules

- networkId (string): (required)




### Get Network Appliance Firewall Firewalled Service

**Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service

- networkId (string): (required)
- service (string): (required)




### Get Network Appliance Firewall Firewalled Services

**List the appliance services and their accessibility rules**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services

- networkId (string): (required)




### Get Network Appliance Firewall Inbound Firewall Rules

**Return the inbound firewall rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules

- networkId (string): (required)




### Get Network Appliance Firewall L3 Firewall Rules

**Return the L3 firewall rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules

- networkId (string): (required)




### Get Network Appliance Firewall L7 Firewall Rules

**List the MX L7 firewall rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules

- networkId (string): (required)




### Get Network Appliance Firewall L7 Firewall Rules Application Categories

**Return the L7 firewall application categories and their associated applications for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories

- networkId (string): (required)




### Get Network Appliance Firewall One To Many Nat Rules

**Return the 1:Many NAT mapping rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules

- networkId (string): (required)




### Get Network Appliance Firewall One To One Nat Rules

**Return the 1:1 NAT mapping rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules

- networkId (string): (required)




### Get Network Appliance Firewall Port Forwarding Rules

**Return the port forwarding rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules

- networkId (string): (required)




### Get Network Appliance Port

**Return per-port VLAN settings for a single MX port.**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port

- networkId (string): (required)
- portId (string): (required)




### Get Network Appliance Ports

**List per-port VLAN settings for all ports of a MX.**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports

- networkId (string): (required)




### Get Network Appliance Security Events

**List the security events for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.




### Get Network Appliance Security Intrusion

**Returns all supported intrusion settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion

- networkId (string): (required)




### Get Network Appliance Security Malware

**Returns all supported malware settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware

- networkId (string): (required)




### Get Network Appliance Settings

**Return the appliance settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-settings

- networkId (string): (required)




### Get Network Appliance Single Lan

**Return single LAN configuration**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan

- networkId (string): (required)




### Get Network Appliance Static Route

**Return a static route for an MX or teleworker network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route

- networkId (string): (required)
- staticRouteId (string): (required)




### Get Network Appliance Static Routes

**List the static routes for an MX or teleworker network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes

- networkId (string): (required)




### Get Network Appliance Traffic Shaping

**Display the traffic shaping settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping

- networkId (string): (required)




### Get Network Appliance Traffic Shaping Custom Performance Class

**Return a custom performance class for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class

- networkId (string): (required)
- customPerformanceClassId (string): (required)




### Get Network Appliance Traffic Shaping Custom Performance Classes

**List all custom performance classes for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes

- networkId (string): (required)




### Get Network Appliance Traffic Shaping Rules

**Display the traffic shaping settings rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules

- networkId (string): (required)




### Get Network Appliance Traffic Shaping Uplink Bandwidth

**Returns the uplink bandwidth settings for your MX network.**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth

- networkId (string): (required)




### Get Network Appliance Traffic Shaping Uplink Selection

**Show uplink selection settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection

- networkId (string): (required)




### Get Network Appliance Vlan

**Return a VLAN**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan

- networkId (string): (required)
- vlanId (string): (required)




### Get Network Appliance Vlans

**List the VLANs for an MX network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans

- networkId (string): (required)




### Get Network Appliance Vlans Settings

**Returns the enabled status of VLANs for the network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings

- networkId (string): (required)




### Get Network Appliance Vpn Bgp

**Return a Hub BGP Configuration**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-bgp

- networkId (string): (required)




### Get Network Appliance Vpn Site To Site Vpn

**Return the site-to-site VPN settings of a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn

- networkId (string): (required)




### Get Network Appliance Warm Spare

**Return MX warm spare settings**
https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare

- networkId (string): (required)




### Get Organization Appliance Security Events

**List the security events for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.




### Get Organization Appliance Security Intrusion

**Returns all supported intrusion settings for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion

- organizationId (string): (required)




### Get Organization Appliance Uplink Statuses

**List the uplink status of every Meraki MX and Z series appliances in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.




### Get Organization Appliance Vpn Stats

**Show VPN history stat for networks in an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-stats

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.




### Get Organization Appliance Vpn Statuses

**Show VPN status for networks in an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-statuses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456




### Get Organization Appliance Vpn Third Party V P N Peers

**Return the third party VPN peers for an organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-third-party-v-p-n-peers

- organizationId (string): (required)




### Get Organization Appliance Vpn Vpn Firewall Rules

**Return the firewall rules for an organization's site-to-site VPN**
https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules

- organizationId (string): (required)




### Swap Network Appliance Warm Spare

**Swap MX primary and warm spare appliances**
https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

- networkId (string): (required)




### Update Network Appliance Connectivity Monitoring Destinations

**Update the connectivity testing destinations for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

- networkId (string): (required)
- destinations (array): The list of connectivity monitoring destinations




### Update Network Appliance Content Filtering

**Update the content filtering settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-content-filtering

- networkId (string): (required)
- allowedUrlPatterns (array): A list of URL patterns that are allowed
- blockedUrlPatterns (array): A list of URL patterns that are blocked
- blockedUrlCategories (array): A list of URL categories to block
- urlCategoryListSize (string): URL category list size which is either 'topSites' or 'fullList'




### Update Network Appliance Firewall Cellular Firewall Rules

**Update the cellular firewall rules of an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules

- networkId (string): (required)
- rules (array): An ordered array of the firewall rules (not including the default rule)




### Update Network Appliance Firewall Firewalled Service

**Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-firewalled-service

- networkId (string): (required)
- service (string): (required)
- access (string): A string indicating the rule for which IPs are allowed to use the specified service. Acceptable values are "blocked" (no remote IPs can access the service), "restricted" (only allowed IPs can access the service), and "unrestriced" (any remote IP can access the service). This field is required
- allowedIps (array): An array of allowed IPs that can access the service. This field is required if "access" is set to "restricted". Otherwise this field is ignored




### Update Network Appliance Firewall Inbound Firewall Rules

**Update the inbound firewall rules of an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-firewall-rules

- networkId (string): (required)
- rules (array): An ordered array of the firewall rules (not including the default rule)
- syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)




### Update Network Appliance Firewall L3 Firewall Rules

**Update the L3 firewall rules of an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules

- networkId (string): (required)
- rules (array): An ordered array of the firewall rules (not including the default rule)
- syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)




### Update Network Appliance Firewall L7 Firewall Rules

**Update the MX L7 firewall rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

- networkId (string): (required)
- rules (array): An ordered array of the MX L7 firewall rules




### Update Network Appliance Firewall One To Many Nat Rules

**Set the 1:Many NAT mapping rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-many-nat-rules

- networkId (string): (required)
- rules (array): An array of 1:Many nat rules




### Update Network Appliance Firewall One To One Nat Rules

**Set the 1:1 NAT mapping rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-one-nat-rules

- networkId (string): (required)
- rules (array): An array of 1:1 nat rules




### Update Network Appliance Firewall Port Forwarding Rules

**Update the port forwarding rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-port-forwarding-rules

- networkId (string): (required)
- rules (array): An array of port forwarding params




### Update Network Appliance Port

**Update the per-port VLAN settings for a single MX port.**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

- networkId (string): (required)
- portId (string): (required)
- enabled (boolean): The status of the port
- dropUntaggedTraffic (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
- type (string): The type of the port: 'access' or 'trunk'.
- vlan (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
- allowedVlans (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
- accessPolicy (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.




### Update Network Appliance Security Intrusion

**Set the supported intrusion settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-intrusion

- networkId (string): (required)
- mode (string): Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave current config unchanged)
- idsRulesets (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - omitting will leave current config unchanged). Default value is 'balanced' if none currently saved
- protectedNetworks (object): Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode




### Update Network Appliance Security Malware

**Set the supported malware settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-malware

- networkId (string): (required)
- mode (string): Set mode to 'enabled' to enable malware prevention, otherwise 'disabled'
- allowedUrls (array): The urls that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing
- allowedFiles (array): The sha256 digests of files that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing




### Update Network Appliance Single Lan

**Update single LAN configuration**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

- networkId (string): (required)
- subnet (string): The subnet of the single LAN configuration
- applianceIp (string): The appliance IP address of the single LAN




### Update Network Appliance Static Route

**Update a static route for an MX or teleworker network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route

- networkId (string): (required)
- staticRouteId (string): (required)
- name (string): The name of the static route
- subnet (string): The subnet of the static route
- gatewayIp (string): The gateway IP (next hop) of the static route
- enabled (boolean): The enabled state of the static route
- fixedIpAssignments (object): The DHCP fixed IP assignments on the static route. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
- reservedIpRanges (array): The DHCP reserved IP ranges on the static route




### Update Network Appliance Traffic Shaping

**Update the traffic shaping settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping

- networkId (string): (required)
- globalBandwidthLimits (object): Global per-client bandwidth limit




### Update Network Appliance Traffic Shaping Custom Performance Class

**Update a custom performance class for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

- networkId (string): (required)
- customPerformanceClassId (string): (required)
- name (string): Name of the custom performance class
- maxLatency (integer): Maximum latency in milliseconds
- maxJitter (integer): Maximum jitter in milliseconds
- maxLossPercentage (integer): Maximum percentage of packet loss




### Update Network Appliance Traffic Shaping Rules

**Update the traffic shaping settings rules for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

- networkId (string): (required)
- defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- rules (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.





### Update Network Appliance Traffic Shaping Uplink Bandwidth

**Updates the uplink bandwidth settings for your MX network.**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

- networkId (string): (required)
- bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)




### Update Network Appliance Traffic Shaping Uplink Selection

**Update uplink selection settings for an MX network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

- networkId (string): (required)
- activeActiveAutoVpnEnabled (boolean): Toggle for enabling or disabling active-active AutoVPN
- defaultUplink (string): The default uplink. Must be one of: 'wan1' or 'wan2'
- loadBalancingEnabled (boolean): Toggle for enabling or disabling load balancing
- wanTrafficUplinkPreferences (array): Array of uplink preference rules for WAN traffic
- vpnTrafficUplinkPreferences (array): Array of uplink preference rules for VPN traffic




### Update Network Appliance Vlan

**Update a VLAN**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

- networkId (string): (required)
- vlanId (string): (required)
- name (string): The name of the VLAN
- subnet (string): The subnet of the VLAN
- applianceIp (string): The local IP of the appliance on the VLAN
- groupPolicyId (string): The id of the desired group policy to apply to the VLAN
- vpnNatSubnet (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
- dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
- dhcpRelayServerIps (array): The IPs of the DHCP servers that DHCP requests should be relayed to
- dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
- dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
- dhcpBootNextServer (string): DHCP boot option to direct boot clients to the server to load the boot file from
- dhcpBootFilename (string): DHCP boot option for boot filename
- fixedIpAssignments (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
- reservedIpRanges (array): The DHCP reserved IP ranges on the VLAN
- dnsNameservers (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
- dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.




### Update Network Appliance Vlans Settings

**Enable/Disable VLANs for the given network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

- networkId (string): (required)
- vlansEnabled (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network




### Update Network Appliance Vpn Bgp

**Update a Hub BGP Configuration**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

- networkId (string): (required)
- enabled (boolean): Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.
- asNumber (integer): An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512.
- ibgpHoldTimer (integer): The IBGP holdtimer in seconds. The IBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240.
- neighbors (array): List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated.




### Update Network Appliance Vpn Site To Site Vpn

**Update the site-to-site VPN settings of a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

- networkId (string): (required)
- mode (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
- hubs (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
- subnets (array): The list of subnets and their VPN presence.




### Update Network Appliance Warm Spare

**Update MX warm spare settings**
https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

- networkId (string): (required)
- enabled (boolean): Enable warm spare
- spareSerial (string): Serial number of the warm spare appliance
- uplinkMode (string): Uplink mode, either virtual or public
- virtualIp1 (string): The WAN 1 shared IP
- virtualIp2 (string): The WAN 2 shared IP




### Update Organization Appliance Security Intrusion

**Sets supported intrusion settings for an organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion

- organizationId (string): (required)
- allowedRules (array): Sets a list of specific SNORT(r) signatures to allow




### Update Organization Appliance Vpn Third Party V P N Peers

**Update the third party VPN peers for an organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

- organizationId (string): (required)
- peers (array): The list of VPN peers




### Update Organization Appliance Vpn Vpn Firewall Rules

**Update the firewall rules of an organization's site-to-site VPN**
https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules

- organizationId (string): (required)
- rules (array): An ordered array of the firewall rules (not including the default rule)
- syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)



## Camera


### Create Network Camera Quality Retention Profile

**Creates new quality retention profile for this network.**
https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile

- networkId (string): (required)
- name (string): The name of the new profile. Must be unique. This parameter is required.
- motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false.
- restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false.
- audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
- cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
- motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
- scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
- maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days
- videoSettings (object): Video quality and resolution settings for all the camera models.




### Delete Network Camera Quality Retention Profile

**Delete an existing quality retention profile for this network.**
https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile

- networkId (string): (required)
- qualityRetentionProfileId (string): (required)




### Generate Device Camera Snapshot

**Generate a snapshot of what the camera sees at the specified time and return a link to that image.**
https://developer.cisco.com/meraki/api-v1/#!generate-device-camera-snapshot

- serial (string): (required)
- timestamp (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
- fullframe (boolean): [optional] If set to "true" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.




### Get Device Camera Analytics Live

**Returns live state from camera of analytics zones**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-live

- serial (string): (required)




### Get Device Camera Analytics Overview

**Returns an overview of aggregate analytics data for a timespan**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
- objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].




### Get Device Camera Analytics Recent

**Returns most recent record for analytics zones**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-recent

- serial (string): (required)
- objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].




### Get Device Camera Analytics Zone History

**Return historical records for analytic zones**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zone-history

- serial (string): (required)
- zoneId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
- objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].




### Get Device Camera Analytics Zones

**Returns all configured analytic zones for this camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zones

- serial (string): (required)




### Get Device Camera Quality And Retention

**Returns quality and retention settings for the given camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-quality-and-retention

- serial (string): (required)




### Get Device Camera Sense

**Returns sense settings for a given camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense

- serial (string): (required)




### Get Device Camera Sense Object Detection Models

**Returns the MV Sense object detection model list for the given camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense-object-detection-models

- serial (string): (required)




### Get Device Camera Video Link

**Returns video link to the specified camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-link

- serial (string): (required)
- timestamp (string): [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.




### Get Device Camera Video Settings

**Returns video settings for the given camera**
https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-settings

- serial (string): (required)




### Get Network Camera Quality Retention Profile

**Retrieve a single quality retention profile**
https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile

- networkId (string): (required)
- qualityRetentionProfileId (string): (required)




### Get Network Camera Quality Retention Profiles

**List the quality retention profiles for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles

- networkId (string): (required)




### Get Network Camera Schedules

**Returns a list of all camera recording schedules.**
https://developer.cisco.com/meraki/api-v1/#!get-network-camera-schedules

- networkId (string): (required)




### Update Device Camera Quality And Retention

**Update quality and retention settings for the given camera**
https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

- serial (string): (required)
- profileId (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
- motionBasedRetentionEnabled (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera
- audioRecordingEnabled (boolean): Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
- restrictedBandwidthModeEnabled (boolean): Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera
- quality (string): Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
- resolution (string): Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080' or '2058x2058'. Not all resolutions are supported by every camera model.
- motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.




### Update Device Camera Sense

**Update sense settings for the given camera**
https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

- serial (string): (required)
- senseEnabled (boolean): Boolean indicating if sense(license) is enabled(true) or disabled(false) on the camera
- mqttBrokerId (string): The ID of the MQTT broker to be enabled on the camera. A value of null will disable MQTT on the camera
- detectionModelId (string): The ID of the object detection model




### Update Device Camera Video Settings

**Update video settings for the given camera**
https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

- serial (string): (required)
- externalRtspEnabled (boolean): Boolean indicating if external rtsp stream is exposed




### Update Network Camera Quality Retention Profile

**Update an existing quality retention profile for this network.**
https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile

- networkId (string): (required)
- qualityRetentionProfileId (string): (required)
- name (string): The name of the new profile. Must be unique.
- motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false.
- restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false.
- audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
- cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
- motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
- scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
- maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days
- videoSettings (object): Video quality and resolution settings for all the camera models.



## Cellular Gateway


### Get Device Cellular Gateway Lan

**Show the LAN Settings of a MG**
https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

- serial (string): (required)




### Get Device Cellular Gateway Port Forwarding Rules

**Returns the port forwarding rules for a single MG.**
https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

- serial (string): (required)




### Get Network Cellular Gateway Connectivity Monitoring Destinations

**Return the connectivity testing destinations for an MG network**
https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

- networkId (string): (required)




### Get Network Cellular Gateway Dhcp

**List common DHCP settings of MGs**
https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

- networkId (string): (required)




### Get Network Cellular Gateway Subnet Pool

**Return the subnet pool and mask configured for MGs in the network.**
https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

- networkId (string): (required)




### Get Network Cellular Gateway Uplink

**Returns the uplink settings for your MG network.**
https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

- networkId (string): (required)




### Get Organization Cellular Gateway Uplink Statuses

**List the uplink status of every Meraki MG cellular gateway in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

- organizationId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
- serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
- iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.




### Update Device Cellular Gateway Lan

**Update the LAN Settings for a single MG.**
https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

- serial (string): (required)
- reservedIpRanges (array): list of all reserved IP ranges for a single MG
- fixedIpAssignments (array): list of all fixed IP assignments for a single MG




### Update Device Cellular Gateway Port Forwarding Rules

**Updates the port forwarding rules for a single MG.**
https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules

- serial (string): (required)
- rules (array): An array of port forwarding params




### Update Network Cellular Gateway Connectivity Monitoring Destinations

**Update the connectivity testing destinations for an MG network**
https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations

- networkId (string): (required)
- destinations (array): The list of connectivity monitoring destinations




### Update Network Cellular Gateway Dhcp

**Update common DHCP settings of MGs**
https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp

- networkId (string): (required)
- dhcpLeaseTime (string): DHCP Lease time for all MG of the network. It can be '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
- dnsNameservers (string): DNS name servers mode for all MG of the network. It can take 4 different values: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
- dnsCustomNameservers (array): list of fixed IP representing the the DNS Name servers when the mode is 'custom'




### Update Network Cellular Gateway Subnet Pool

**Update the subnet pool and mask configuration for MGs in the network.**
https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool

- networkId (string): (required)
- mask (integer): Mask used for the subnet of all MGs in  this network.
- cidr (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.




### Update Network Cellular Gateway Uplink

**Updates the uplink settings for your MG network.**
https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink

- networkId (string): (required)
- bandwidthLimits (object): The bandwidth settings for the 'cellular' uplink



## Insight


### Create Organization Insight Monitored Media Server

**Add a media server to be monitored for this organization**
https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

- organizationId (string): (required)
- name (string): The name of the VoIP provider
- address (string): The IP address (IPv4 only) or hostname of the media server to monitor
- bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.




### Delete Organization Insight Monitored Media Server

**Delete a monitored media server from this organization**
https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

- organizationId (string): (required)
- monitoredMediaServerId (string): (required)




### Get Organization Insight Monitored Media Server

**Return a monitored media server for this organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

- organizationId (string): (required)
- monitoredMediaServerId (string): (required)




### Get Organization Insight Monitored Media Servers

**List the monitored media servers for this organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

- organizationId (string): (required)




### Update Organization Insight Monitored Media Server

**Update a monitored media server for this organization**
https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

- organizationId (string): (required)
- monitoredMediaServerId (string): (required)
- name (string): The name of the VoIP provider
- address (string): The IP address (IPv4 only) or hostname of the media server to monitor
- bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.



## Sm


### Checkin Network Sm Devices

**Force check-in a set of devices**
https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices

- networkId (string): (required)
- wifiMacs (array): The wifiMacs of the devices to be checked-in.
- ids (array): The ids of the devices to be checked-in.
- serials (array): The serials of the devices to be checked-in.
- scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be checked-in.




### Create Network Sm Bypass Activation Lock Attempt

**Bypass activation lock attempt**
https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

- networkId (string): (required)
- ids (array): The ids of the devices to attempt activation lock bypass.




### Create Network Sm Target Group

**Add a target group**
https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

- networkId (string): (required)
- name (string): The name of this target group
- scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.




### Delete Network Sm Target Group

**Delete a target group from a network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

- networkId (string): (required)
- targetGroupId (string): (required)




### Delete Network Sm User Access Device

**Delete a User Access Device**
https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

- networkId (string): (required)
- userAccessDeviceId (string): (required)




### Get Network Sm Bypass Activation Lock Attempt

**Bypass activation lock attempt status**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

- networkId (string): (required)
- attemptId (string): (required)




### Get Network Sm Device Cellular Usage History

**Return the client's daily cellular data usage history**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Certs

**List the certs on a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Connectivity

**Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

- networkId (string): (required)
- deviceId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm Device Desktop Logs

**Return historical records of various Systems Manager network connection details for desktop devices.**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

- networkId (string): (required)
- deviceId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm Device Device Command Logs

**Return historical records of commands sent to Systems Manager devices**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

- networkId (string): (required)
- deviceId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm Device Device Profiles

**Get the profiles associated with a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Network Adapters

**List the network adapters of a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Performance History

**Return historical records of various Systems Manager client metrics for desktop devices.**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

- networkId (string): (required)
- deviceId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm Device Restrictions

**List the restrictions on a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Security Centers

**List the security centers on a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Softwares

**Get a list of softwares associated with a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Device Wlan Lists

**List the saved SSID names on a device**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

- networkId (string): (required)
- deviceId (string): (required)




### Get Network Sm Devices

**List the devices enrolled in an SM network with various specified fields and filters**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- fields (array): Additional fields that will be displayed for each device.
The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion.
- wifiMacs (array): Filter devices by wifi mac(s).
- serials (array): Filter devices by serial(s).
- ids (array): Filter devices by id(s).
- scope (array): Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm Profiles

**List all profiles in a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

- networkId (string): (required)




### Get Network Sm Target Group

**Return a target group**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

- networkId (string): (required)
- targetGroupId (string): (required)
- withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response




### Get Network Sm Target Groups

**List the target groups in this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

- networkId (string): (required)
- withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response




### Get Network Sm User Access Devices

**List User Access Devices and its Trusted Access Connections**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-access-devices

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Sm User Device Profiles

**Get the profiles associated with a user**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

- networkId (string): (required)
- userId (string): (required)




### Get Network Sm User Softwares

**Get a list of softwares associated with a user**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

- networkId (string): (required)
- userId (string): (required)




### Get Network Sm Users

**List the owners in an SM network with various specified fields and filters**
https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users

- networkId (string): (required)
- ids (array): Filter users by id(s).
- usernames (array): Filter users by username(s).
- emails (array): Filter users by email(s).
- scope (array): Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.




### Get Organization Sm Apns Cert

**Get the organization's APNS certificate**
https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

- organizationId (string): (required)




### Get Organization Sm Vpp Account

**Get a hash containing the unparsed token of the VPP account with the given ID**
https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

- organizationId (string): (required)
- vppAccountId (string): (required)




### Get Organization Sm Vpp Accounts

**List the VPP accounts in the organization**
https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

- organizationId (string): (required)




### Lock Network Sm Devices

**Lock a set of devices**
https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices

- networkId (string): (required)
- wifiMacs (array): The wifiMacs of the devices to be locked.
- ids (array): The ids of the devices to be locked.
- serials (array): The serials of the devices to be locked.
- scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.
- pin (integer): The pin number for locking macOS devices (a six digit number). Required only for macOS devices.




### Modify Network Sm Devices Tags

**Add, delete, or update the tags of a set of devices**
https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags

- networkId (string): (required)
- tags (array): The tags to be added, deleted, or updated.
- updateAction (string): One of add, delete, or update. Only devices that have been modified will be returned.
- wifiMacs (array): The wifiMacs of the devices to be modified.
- ids (array): The ids of the devices to be modified.
- serials (array): The serials of the devices to be modified.
- scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.




### Move Network Sm Devices

**Move a set of devices to a new network**
https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices

- networkId (string): (required)
- newNetwork (string): The new network to which the devices will be moved.
- wifiMacs (array): The wifiMacs of the devices to be moved.
- ids (array): The ids of the devices to be moved.
- serials (array): The serials of the devices to be moved.
- scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be moved.




### Refresh Network Sm Device Details

**Refresh the details of a device**
https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

- networkId (string): (required)
- deviceId (string): (required)




### Unenroll Network Sm Device

**Unenroll a device**
https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

- networkId (string): (required)
- deviceId (string): (required)




### Update Network Sm Devices Fields

**Modify the fields of a device**
https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

- networkId (string): (required)
- deviceFields (object): The new fields of the device. Each field of this object is optional.
- wifiMac (string): The wifiMac of the device to be modified.
- id (string): The id of the device to be modified.
- serial (string): The serial of the device to be modified.




### Update Network Sm Target Group

**Update a target group**
https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

- networkId (string): (required)
- targetGroupId (string): (required)
- name (string): The name of this target group
- scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.




### Wipe Network Sm Devices

**Wipe a device**
https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

- networkId (string): (required)
- wifiMac (string): The wifiMac of the device to be wiped.
- id (string): The id of the device to be wiped.
- serial (string): The serial of the device to be wiped.
- pin (integer): The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.



## Switch


### Add Network Switch Stack

**Add a switch to a stack**
https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack

- networkId (string): (required)
- switchStackId (string): (required)
- serial (string): The serial of the switch to be added




### Clone Organization Switch Devices

**Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**
https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

- organizationId (string): (required)
- sourceSerial (string): Serial number of the source switch (must be on a network not bound to a template)
- targetSerials (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)




### Create Device Switch Routing Interface

**Create a layer 3 interface for a switch**
https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

- serial (string): (required)
- name (string): A friendly name or description for the interface or VLAN.
- interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- ospfSettings (object): The OSPF routing settings of the interface.




### Create Device Switch Routing Static Route

**Create a layer 3 static route for a switch**
https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

- serial (string): (required)
- subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
- name (string): Name or description for layer 3 static route
- advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
- preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes




### Create Network Switch Access Policy

**Create an access policy for a switch network**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

- networkId (string): (required)
- name (string): Name of the access policy
- radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
- radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- hostMode (string): Choose the Host Mode for the access policy.
- urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication




### Create Network Switch Link Aggregation

**Create a link aggregation group**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

- networkId (string): (required)
- switchPorts (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
- switchProfilePorts (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.




### Create Network Switch Port Schedule

**Add a switch port schedule**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule

- networkId (string): (required)
- name (string): The name for your port schedule. Required
- portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
When it's empty, default schedule with all days of a week are configured.
Any unspecified day in the schedule is added as a default schedule configuration of the day.





### Create Network Switch Qos Rule

**Add a quality of service rule**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

- networkId (string): (required)
- vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY"
- srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- dscp (integer): DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0




### Create Network Switch Routing Multicast Rendezvous Point

**Create a multicast rendezvous point**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

- networkId (string): (required)
- interfaceIp (string): The IP address of the interface where the RP needs to be created.
- multicastGroup (string): 'Any', or the IP address of a multicast group




### Create Network Switch Stack

**Create a stack**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack

- networkId (string): (required)
- name (string): The name of the new stack
- serials (array): An array of switch serials to be added into the new stack




### Create Network Switch Stack Routing Interface

**Create a layer 3 interface for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

- networkId (string): (required)
- switchStackId (string): (required)
- name (string): A friendly name or description for the interface or VLAN.
- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
- defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
- ospfSettings (object): The OSPF routing settings of the interface.




### Create Network Switch Stack Routing Static Route

**Create a layer 3 static route for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

- networkId (string): (required)
- switchStackId (string): (required)
- subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
- name (string): Name or description for layer 3 static route
- advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
- preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes




### Cycle Device Switch Ports

**Cycle a set of switch ports**
https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

- serial (string): (required)
- ports (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]




### Delete Device Switch Routing Interface

**Delete a layer 3 interface from the switch**
https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

- serial (string): (required)
- interfaceId (string): (required)




### Delete Device Switch Routing Static Route

**Delete a layer 3 static route for a switch**
https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

- serial (string): (required)
- staticRouteId (string): (required)




### Delete Network Switch Access Policy

**Delete an access policy for a switch network**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

- networkId (string): (required)
- accessPolicyNumber (string): (required)




### Delete Network Switch Link Aggregation

**Split a link aggregation group into separate ports**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

- networkId (string): (required)
- linkAggregationId (string): (required)




### Delete Network Switch Port Schedule

**Delete a switch port schedule**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule

- networkId (string): (required)
- portScheduleId (string): (required)




### Delete Network Switch Qos Rule

**Delete a quality of service rule**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

- networkId (string): (required)
- qosRuleId (string): (required)




### Delete Network Switch Routing Multicast Rendezvous Point

**Delete a multicast rendezvous point**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

- networkId (string): (required)
- rendezvousPointId (string): (required)




### Delete Network Switch Stack

**Delete a stack**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack

- networkId (string): (required)
- switchStackId (string): (required)




### Delete Network Switch Stack Routing Interface

**Delete a layer 3 interface from a switch stack**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface

- networkId (string): (required)
- switchStackId (string): (required)
- interfaceId (string): (required)




### Delete Network Switch Stack Routing Static Route

**Delete a layer 3 static route for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-static-route

- networkId (string): (required)
- switchStackId (string): (required)
- staticRouteId (string): (required)




### Get Device Switch Port

**Return a switch port**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

- serial (string): (required)
- portId (string): (required)




### Get Device Switch Ports

**List the switch ports for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

- serial (string): (required)




### Get Device Switch Ports Statuses

**Return the status for all the ports of a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.




### Get Device Switch Ports Statuses Packets

**Return the packet counters for all the ports of a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.




### Get Device Switch Routing Interface

**Return a layer 3 interface for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

- serial (string): (required)
- interfaceId (string): (required)




### Get Device Switch Routing Interface Dhcp

**Return a layer 3 interface DHCP configuration for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

- serial (string): (required)
- interfaceId (string): (required)




### Get Device Switch Routing Interfaces

**List layer 3 interfaces for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

- serial (string): (required)




### Get Device Switch Routing Static Route

**Return a layer 3 static route for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

- serial (string): (required)
- staticRouteId (string): (required)




### Get Device Switch Routing Static Routes

**List layer 3 static routes for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

- serial (string): (required)




### Get Device Switch Warm Spare

**Return warm spare configuration for a switch**
https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

- serial (string): (required)




### Get Network Switch Access Control Lists

**Return the access control lists for a MS network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

- networkId (string): (required)




### Get Network Switch Access Policies

**List the access policies for a switch network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

- networkId (string): (required)




### Get Network Switch Access Policy

**Return a specific access policy for a switch network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

- networkId (string): (required)
- accessPolicyNumber (string): (required)




### Get Network Switch Dhcp Server Policy

**Return the DHCP server policy**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

- networkId (string): (required)




### Get Network Switch Dscp To Cos Mappings

**Return the DSCP to CoS mappings**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

- networkId (string): (required)




### Get Network Switch Link Aggregations

**List link aggregation groups**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

- networkId (string): (required)




### Get Network Switch Mtu

**Return the MTU configuration**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

- networkId (string): (required)




### Get Network Switch Port Schedules

**List switch port schedules**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

- networkId (string): (required)




### Get Network Switch Qos Rule

**Return a quality of service rule**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

- networkId (string): (required)
- qosRuleId (string): (required)




### Get Network Switch Qos Rules

**List quality of service rules**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

- networkId (string): (required)




### Get Network Switch Qos Rules Order

**Return the quality of service rule IDs by order in which they will be processed by the switch**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

- networkId (string): (required)




### Get Network Switch Routing Multicast

**Return multicast settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

- networkId (string): (required)




### Get Network Switch Routing Multicast Rendezvous Point

**Return a multicast rendezvous point**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

- networkId (string): (required)
- rendezvousPointId (string): (required)




### Get Network Switch Routing Multicast Rendezvous Points

**List multicast rendezvous points**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

- networkId (string): (required)




### Get Network Switch Routing Ospf

**Return layer 3 OSPF routing configuration**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

- networkId (string): (required)




### Get Network Switch Settings

**Returns the switch network settings**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

- networkId (string): (required)




### Get Network Switch Stack

**Show a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

- networkId (string): (required)
- switchStackId (string): (required)




### Get Network Switch Stack Routing Interface

**Return a layer 3 interface from a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface

- networkId (string): (required)
- switchStackId (string): (required)
- interfaceId (string): (required)




### Get Network Switch Stack Routing Interface Dhcp

**Return a layer 3 interface DHCP configuration for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp

- networkId (string): (required)
- switchStackId (string): (required)
- interfaceId (string): (required)




### Get Network Switch Stack Routing Interfaces

**List layer 3 interfaces for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

- networkId (string): (required)
- switchStackId (string): (required)




### Get Network Switch Stack Routing Static Route

**Return a layer 3 static route for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-route

- networkId (string): (required)
- switchStackId (string): (required)
- staticRouteId (string): (required)




### Get Network Switch Stack Routing Static Routes

**List layer 3 static routes for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

- networkId (string): (required)
- switchStackId (string): (required)




### Get Network Switch Stacks

**List the switch stacks in a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

- networkId (string): (required)




### Get Network Switch Storm Control

**Return the storm control configuration for a switch network**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

- networkId (string): (required)




### Get Network Switch Stp

**Returns STP settings**
https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

- networkId (string): (required)




### Get Organization Config Template Switch Profile Port

**Return a switch profile port**
https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

- organizationId (string): (required)
- configTemplateId (string): (required)
- profileId (string): (required)
- portId (string): (required)




### Get Organization Config Template Switch Profile Ports

**Return all the ports of a switch profile**
https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports

- organizationId (string): (required)
- configTemplateId (string): (required)
- profileId (string): (required)




### Get Organization Config Template Switch Profiles

**List the switch profiles for your switch template configuration**
https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

- organizationId (string): (required)
- configTemplateId (string): (required)




### Remove Network Switch Stack

**Remove a switch from a stack**
https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-stack

- networkId (string): (required)
- switchStackId (string): (required)
- serial (string): The serial of the switch to be removed




### Update Device Switch Port

**Update a switch port**
https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

- serial (string): (required)
- portId (string): (required)
- name (string): The name of the switch port
- tags (array): The list of tags of the switch port
- enabled (boolean): The status of the switch port
- type (string): The type of the switch port ('trunk' or 'access')
- vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
- voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
- allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
- poeEnabled (boolean): The PoE status of the switch port
- isolationEnabled (boolean): The isolation status of the switch port
- rstpEnabled (boolean): The rapid spanning tree protocol status
- stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
- linkNegotiation (string): The link speed for the switch port
- portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
- udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- accessPolicyType (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'
- accessPolicyNumber (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'
- macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'
- stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
- stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
- stormControlEnabled (boolean): The storm control status of the switch port
- flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.




### Update Device Switch Routing Interface

**Update a layer 3 interface for a switch**
https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

- serial (string): (required)
- interfaceId (string): (required)
- name (string): A friendly name or description for the interface or VLAN.
- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- ospfSettings (object): The OSPF routing settings of the interface.




### Update Device Switch Routing Interface Dhcp

**Update a layer 3 interface DHCP configuration for a switch**
https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

- serial (string): (required)
- interfaceId (string): (required)
- dhcpMode (string): The DHCP mode options for the switch interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface
- dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch interface ('googlePublicDns', 'openDns' or 'custom')
- dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is 'custom'
- bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch interface
- bootNextServer (string): The PXE boot server IP for the DHCP server running on the switch interface
- bootFileName (string): The PXE boot server filename for the DHCP server running on the switch interface
- dhcpOptions (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch interface
- reservedIpRanges (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch interface
- fixedIpAssignments (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch interface




### Update Device Switch Routing Static Route

**Update a layer 3 static route for a switch**
https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

- serial (string): (required)
- staticRouteId (string): (required)
- name (string): Name or description for layer 3 static route
- subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
- advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
- preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes




### Update Device Switch Warm Spare

**Update warm spare configuration for a switch**
https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

- serial (string): (required)
- enabled (boolean): Enable or disable warm spare for a switch
- spareSerial (string): Serial number of the warm spare switch




### Update Network Switch Access Control Lists

**Update the access control lists for a MS network**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists

- networkId (string): (required)
- rules (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.




### Update Network Switch Access Policy

**Update an access policy for a switch network**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

- networkId (string): (required)
- accessPolicyNumber (string): (required)
- name (string): Name of the access policy
- radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
- radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
- radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
- radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
- radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
- hostMode (string): Choose the Host Mode for the access policy.
- accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
- increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
- guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
- voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
- urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
- urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication




### Update Network Switch Dhcp Server Policy

**Update the DHCP server policy**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

- networkId (string): (required)
- defaultPolicy (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
- allowedServers (array): List the MAC addresses of DHCP servers to permit on the network. Applicable only if defaultPolicy is set to block. An empty array will clear the entries.
- blockedServers (array): List the MAC addresses of DHCP servers to block on the network. Applicable only if defaultPolicy is set to allow. An empty array will clear the entries.




### Update Network Switch Dscp To Cos Mappings

**Update the DSCP to CoS mappings**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

- networkId (string): (required)
- mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.




### Update Network Switch Link Aggregation

**Update a link aggregation group**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

- networkId (string): (required)
- linkAggregationId (string): (required)
- switchPorts (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
- switchProfilePorts (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.




### Update Network Switch Mtu

**Update the MTU configuration**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

- networkId (string): (required)
- defaultMtuSize (integer): MTU size for the entire network. Default value is 9578.
- overrides (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.




### Update Network Switch Port Schedule

**Update a switch port schedule**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

- networkId (string): (required)
- portScheduleId (string): (required)
- name (string): The name for your port schedule.
- portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
When it's empty, default schedule with all days of a week are configured.
Any unspecified day in the schedule is added as a default schedule configuration of the day.





### Update Network Switch Qos Rule

**Update a quality of service rule**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

- networkId (string): (required)
- qosRuleId (string): (required)
- vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
- protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY".
- srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
- srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
- dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
- dscp (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0.




### Update Network Switch Qos Rules Order

**Update the order in which the rules should be processed by the switch**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

- networkId (string): (required)
- ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.




### Update Network Switch Routing Multicast

**Update multicast settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

- networkId (string): (required)
- defaultSettings (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
- overrides (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.




### Update Network Switch Routing Multicast Rendezvous Point

**Update a multicast rendezvous point**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

- networkId (string): (required)
- rendezvousPointId (string): (required)
- interfaceIp (string): The IP address of the interface to use
- multicastGroup (string): 'Any', or the IP address of a multicast group




### Update Network Switch Routing Ospf

**Update layer 3 OSPF routing configuration**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

- networkId (string): (required)
- enabled (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
- helloTimerInSeconds (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds
- deadTimerInSeconds (integer): Time interval to determine when the peer will be declare inactive/dead. Value must be between 1 and 65535
- areas (array): OSPF areas
- md5AuthenticationEnabled (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
- md5AuthenticationKey (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true




### Update Network Switch Settings

**Update switch network settings**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

- networkId (string): (required)
- vlan (integer): Management VLAN
- useCombinedPower (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
- powerExceptions (array): Exceptions on a per switch basis to "useCombinedPower"




### Update Network Switch Stack Routing Interface

**Update a layer 3 interface for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

- networkId (string): (required)
- switchStackId (string): (required)
- interfaceId (string): (required)
- name (string): A friendly name or description for the interface or VLAN.
- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
- interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
- ospfSettings (object): The OSPF routing settings of the interface.




### Update Network Switch Stack Routing Interface Dhcp

**Update a layer 3 interface DHCP configuration for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

- networkId (string): (required)
- switchStackId (string): (required)
- interfaceId (string): (required)
- dhcpMode (string): The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
- dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface
- dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
- dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')
- dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is 'custom'
- bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface
- bootNextServer (string): The PXE boot server IP for the DHCP server running on the switch stack interface
- bootFileName (string): The PXE boot server file name for the DHCP server running on the switch stack interface
- dhcpOptions (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface
- reservedIpRanges (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface
- fixedIpAssignments (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface




### Update Network Switch Stack Routing Static Route

**Update a layer 3 static route for a switch stack**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

- networkId (string): (required)
- switchStackId (string): (required)
- staticRouteId (string): (required)
- name (string): Name or description for layer 3 static route
- subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
- nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
- advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
- preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes




### Update Network Switch Storm Control

**Update the storm control configuration for a switch network**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

- networkId (string): (required)
- broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
- multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
- unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.




### Update Network Switch Stp

**Updates STP settings**
https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

- networkId (string): (required)
- rstpEnabled (boolean): The spanning tree protocol status in network
- stpBridgePriority (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.




### Update Organization Config Template Switch Profile Port

**Update a switch profile port**
https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port

- organizationId (string): (required)
- configTemplateId (string): (required)
- profileId (string): (required)
- portId (string): (required)
- name (string): The name of the switch profile port
- tags (array): The list of tags of the switch profile port
- enabled (boolean): The status of the switch profile port
- type (string): The type of the switch profile port ('trunk' or 'access')
- vlan (integer): The VLAN of the switch profile port. A null value will clear the value set for trunk ports.
- voiceVlan (integer): The voice VLAN of the switch profile port. Only applicable to access ports
- allowedVlans (string): The VLANs allowed on the switch profile port. Only applicable to trunk ports
- poeEnabled (boolean): The PoE status of the switch profile port
- isolationEnabled (boolean): The isolation status of the switch profile port
- rstpEnabled (boolean): The rapid spanning tree protocol status
- stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
- linkNegotiation (string): The link speed for the switch profile port
- portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
- udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
- accessPolicyType (string): The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'
- accessPolicyNumber (integer): The number of a custom access policy to configure on the switch profile port. Only applicable when 'accessPolicyType' is 'Custom access policy'
- macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'
- stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
- stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
- stormControlEnabled (boolean): The storm control status of the switch profile port
- flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.



## Wireless


### Create Network Wireless Rf Profile

**Creates new RF profile for this network**
https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

- networkId (string): (required)
- name (string): The name of the new profile. Must be unique. This param is required on creation.
- bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
- clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
- minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
- apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
- twoFourGhzSettings (object): Settings related to 2.4Ghz band
- fiveGhzSettings (object): Settings related to 5Ghz band




### Create Network Wireless Ssid Identity Psk

**Create an Identity PSK**
https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

- networkId (string): (required)
- number (string): (required)
- name (string): The name of the Identity PSK
- passphrase (string): The passphrase for client authentication
- groupPolicyId (string): The group policy to be applied to clients




### Delete Network Wireless Rf Profile

**Delete a RF Profile**
https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

- networkId (string): (required)
- rfProfileId (string): (required)




### Delete Network Wireless Ssid Identity Psk

**Delete an Identity PSK**
https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

- networkId (string): (required)
- number (string): (required)
- identityPskId (string): (required)




### Get Device Wireless Bluetooth Settings

**Return the bluetooth settings for a wireless device**
https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

- serial (string): (required)




### Get Device Wireless Connection Stats

**Aggregated connectivity info for a given AP on this network**
https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-connection-stats

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag




### Get Device Wireless Latency Stats

**Aggregated latency info for a given AP on this network**
https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-latency-stats

- serial (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.




### Get Device Wireless Radio Settings

**Return the radio settings of a device**
https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

- serial (string): (required)




### Get Device Wireless Status

**Return the SSID statuses of an access point**
https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

- serial (string): (required)




### Get Network Wireless Air Marshal

**List Air Marshal scan results from a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.




### Get Network Wireless Alternate Management Interface

**Return alternate management interface and devices with IP assigned**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

- networkId (string): (required)




### Get Network Wireless Bluetooth Settings

**Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

- networkId (string): (required)




### Get Network Wireless Channel Utilization History

**Return AP channel utilization over time for a device or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
- deviceSerial (string): Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
- apTag (string): Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
- band (string): Filter results by band (either '2.4' or '5').




### Get Network Wireless Client Connection Stats

**Aggregated connectivity info for a given client on this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

- networkId (string): (required)
- clientId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag




### Get Network Wireless Client Connectivity Events

**List the wireless connectivity events for a client within a network in the timespan.**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

- networkId (string): (required)
- clientId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
- types (array): A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
- includedSeverities (array): A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'.
- band (string): Filter results by band (either '2.4' or '5').
- ssidNumber (integer): An SSID number to include. If not specified, events for all SSIDs will be returned.
- deviceSerial (string): Filter results by an AP's serial number.




### Get Network Wireless Client Count History

**Return wireless client counts over time for a network, device, or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history.
- deviceSerial (string): Filter results by device.
- apTag (string): Filter results by AP tag.
- band (string): Filter results by band (either '2.4' or '5').
- ssid (integer): Filter results by SSID number.




### Get Network Wireless Client Latency History

**Return the latency history for a client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

- networkId (string): (required)
- clientId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.




### Get Network Wireless Client Latency Stats

**Aggregated latency info for a given client on this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

- networkId (string): (required)
- clientId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.




### Get Network Wireless Clients Connection Stats

**Aggregated connectivity info for this network, grouped by clients**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag




### Get Network Wireless Clients Latency Stats

**Aggregated latency info for this network, grouped by clients**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.




### Get Network Wireless Connection Stats

**Aggregated connectivity info for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag




### Get Network Wireless Data Rate History

**Return PHY data rates over time for a network, device, or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client.
- deviceSerial (string): Filter results by device.
- apTag (string): Filter results by AP tag.
- band (string): Filter results by band (either '2.4' or '5').
- ssid (integer): Filter results by SSID number.




### Get Network Wireless Devices Connection Stats

**Aggregated connectivity info for this network, grouped by node**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag




### Get Network Wireless Devices Latency Stats

**Aggregated latency info for this network, grouped by node**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.




### Get Network Wireless Failed Connections

**List of all failed client connection events on this network in a given time range**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- serial (string): Filter by AP
- clientId (string): Filter by client MAC




### Get Network Wireless Latency History

**Return average wireless latency over time for a network, device, or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client.
- deviceSerial (string): Filter results by device.
- apTag (string): Filter results by AP tag.
- band (string): Filter results by band (either '2.4' or '5').
- ssid (integer): Filter results by SSID number.
- accessCategory (string): Filter by access category.




### Get Network Wireless Latency Stats

**Aggregated latency info for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
- band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
- ssid (integer): Filter results by SSID
- vlan (integer): Filter results by VLAN
- apTag (string): Filter results by AP Tag
- fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.




### Get Network Wireless Mesh Statuses

**List wireless mesh statuses for repeaters**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

- networkId (string): (required)
- total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
- direction (string): direction to paginate, either "next" (default) or "prev" page
- perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
- startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
- endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.




### Get Network Wireless Rf Profile

**Return a RF profile**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

- networkId (string): (required)
- rfProfileId (string): (required)




### Get Network Wireless Rf Profiles

**List the non-basic RF profiles for this network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

- networkId (string): (required)
- includeTemplateProfiles (boolean): If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.




### Get Network Wireless Settings

**Return the wireless settings for a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

- networkId (string): (required)




### Get Network Wireless Signal Quality History

**Return signal quality (SNR/RSSI) over time for a device or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client.
- deviceSerial (string): Filter results by device.
- apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
- band (string): Filter results by band (either '2.4' or '5').
- ssid (integer): Filter results by SSID number.




### Get Network Wireless Ssid

**Return a single MR SSID**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssid Firewall L3 Firewall Rules

**Return the L3 firewall rules for an SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssid Firewall L7 Firewall Rules

**Return the L7 firewall rules for an SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssid Identity Psk

**Return an Identity PSK**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

- networkId (string): (required)
- number (string): (required)
- identityPskId (string): (required)




### Get Network Wireless Ssid Identity Psks

**List all Identity PSKs in a wireless network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssid Splash Settings

**Display the splash page settings for the given SSID**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssid Traffic Shaping Rules

**Display the traffic shaping settings for a SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

- networkId (string): (required)
- number (string): (required)




### Get Network Wireless Ssids

**List the MR SSIDs in a network**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

- networkId (string): (required)




### Get Network Wireless Usage History

**Return AP usage over time for a device or network client**
https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

- networkId (string): (required)
- t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
- t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
- timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
- resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
- autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
- clientId (string): Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history.
- deviceSerial (string): Filter results by device. Requires :band.
- apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
- band (string): Filter results by band (either '2.4' or '5').
- ssid (integer): Filter results by SSID number.




### Update Device Wireless Bluetooth Settings

**Update the bluetooth settings for a wireless device**
https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

- serial (string): (required)
- uuid (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- major (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
- minor (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.




### Update Device Wireless Radio Settings

**Update the radio settings of a device**
https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

- serial (string): (required)
- rfProfileId (integer): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
- twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
- fiveGhzSettings (object): Manual radio settings for 5 GHz.




### Update Network Wireless Alternate Management Interface

**Update alternate management interface and device static IP**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

- networkId (string): (required)
- enabled (boolean): Boolean value to enable or disable alternate management interface
- vlanId (integer): Alternate management interface VLAN, must be between 1 and 4094
- protocols (array): Can be one or more of the following values: 'radius', 'snmp', 'syslog' or 'ldap'
- accessPoints (array): Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put 'accessPoints' in the body when updating template networks. Also, an empty 'accessPoints' array will remove all previous static IP assignments




### Update Network Wireless Bluetooth Settings

**Update the Bluetooth settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-bluetooth-settings

- networkId (string): (required)
- scanningEnabled (boolean): Whether APs will scan for Bluetooth enabled clients. (true, false)
- advertisingEnabled (boolean): Whether APs will advertise beacons. (true, false)
- uuid (string): The UUID to be used in the beacon identifier.
- majorMinorAssignmentMode (string): The way major and minor number should be assigned to nodes in the network. ('Unique', 'Non-unique')
- major (integer): The major number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
- minor (integer): The minor number to be used in the beacon identifier. Only valid in 'Non-unique' mode.




### Update Network Wireless Rf Profile

**Updates specified RF profile for this network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

- networkId (string): (required)
- rfProfileId (string): (required)
- name (string): The name of the new profile. Must be unique.
- clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false.
- minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'.
- bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'.
- apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
- twoFourGhzSettings (object): Settings related to 2.4Ghz band
- fiveGhzSettings (object): Settings related to 5Ghz band




### Update Network Wireless Settings

**Update the wireless settings for a network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

- networkId (string): (required)
- meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
- ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
- locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
- upgradeStrategy (string): The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
- ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)




### Update Network Wireless Ssid

**Update the attributes of an MR SSID**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

- networkId (string): (required)
- number (string): (required)
- name (string): The name of the SSID
- enabled (boolean): Whether or not the SSID is enabled
- authMode (string): The association control method for the SSID ('open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius' or 'ipsk-without-radius')
- enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
- encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
- psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
- wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only')
- dot11w (object): The current setting for Protected Management Frames (802.11w).
- dot11r (object): The current setting for 802.11r
- splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest' or 'Cisco ISE'). This attribute is not supported for template children.
- radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- radiusProxyEnabled (boolean): If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.
- radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
- radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
- radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
- radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
- radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
- radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
- ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a concentrator' or 'VPN')
- useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
- vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
- defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
- walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
- walledGardenRanges (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
- radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
- radiusGuestVlanEnabled (boolean): Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- radiusGuestVlanId (integer): VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
- minBitrate (number): The minimum bitrate in Mbps. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
- bandSelection (string): The client-serving radio frequencies. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
- perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
- perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
- perSsidBandwidthLimitUp (integer): The total upload bandwidth limit in Kbps. (0 represents no limit.)
- perSsidBandwidthLimitDown (integer): The total download bandwidth limit in Kbps. (0 represents no limit.)
- lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
- visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
- availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
- availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
- mandatoryDhcpEnabled (boolean): If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate.




### Update Network Wireless Ssid Firewall L3 Firewall Rules

**Update the L3 firewall rules of an SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

- networkId (string): (required)
- number (string): (required)
- rules (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
- allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)




### Update Network Wireless Ssid Firewall L7 Firewall Rules

**Update the L7 firewall rules of an SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

- networkId (string): (required)
- number (string): (required)
- rules (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.




### Update Network Wireless Ssid Identity Psk

**Update an Identity PSK**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

- networkId (string): (required)
- number (string): (required)
- identityPskId (string): (required)
- name (string): The name of the Identity PSK
- passphrase (string): The passphrase for client authentication
- groupPolicyId (string): The group policy to be applied to clients




### Update Network Wireless Ssid Splash Settings

**Modify the splash page settings for the given SSID**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

- networkId (string): (required)
- number (string): (required)
- splashUrl (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
- useSplashUrl (boolean): [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
- splashTimeout (integer): Splash timeout in minutes. This will determine how often users will see the splash page.
- redirectUrl (string): The custom redirect URL where the users will go after the splash page.
- useRedirectUrl (boolean): The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
- welcomeMessage (string): The welcome message for the users on the splash page.
- splashLogo (object): The logo used in the splash page.
- splashImage (object): The image used in the splash page.
- splashPrepaidFront (object): The prepaid front image used in the splash page.




### Update Network Wireless Ssid Traffic Shaping Rules

**Update the traffic shaping settings for an SSID on an MR network**
https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

- networkId (string): (required)
- number (string): (required)
- trafficShapingEnabled (boolean): Whether traffic shaping rules are applied to clients on your SSID.
- defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
- rules (array):     An array of traffic shaping rules. Rules are applied in the order that
they are specified in. An empty list (or null) means no rules. Note that
you are allowed a maximum of 8 rules.




