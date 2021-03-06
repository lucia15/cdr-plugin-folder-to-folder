#  ┏┳┓┏━┓╻┏┓╻
#  ┃┃┃┣━┫┃┃┗┫
#  ╹ ╹╹ ╹╹╹ ╹

terraform {
  required_providers {
    vsphere = {
      source  = "hashicorp/vsphere"
      version = "1.15.0"
    }
  }
}

#  ╻ ╻┏━┓┏━┓╻┏━┓┏┓ ╻  ┏━╸┏━┓
#  ┃┏┛┣━┫┣┳┛┃┣━┫┣┻┓┃  ┣╸ ┗━┓
#  ┗┛ ╹ ╹╹┗╸╹╹ ╹┗━┛┗━╸┗━╸┗━┛

variable "network" {
  type        = string
  description = "Name of the network to attach"
  default     = "VMs"
}

variable "datastore" {
  type        = string
  description = "Datastore name to search VMDK in"
  default     = "datastore1"
}

#  ╺┳┓┏━┓╺┳╸┏━┓
#   ┃┃┣━┫ ┃ ┣━┫
#  ╺┻┛╹ ╹ ╹ ╹ ╹

data "vsphere_datacenter" "this" {}

data "vsphere_resource_pool" "this" {}

data "vsphere_host" "this" {
  datacenter_id = data.vsphere_datacenter.this.id
}

data "vsphere_datastore" "this" {
  name          = var.datastore
  datacenter_id = data.vsphere_datacenter.this.id
}

data "vsphere_network" "this" {
  name          = var.network
  datacenter_id = data.vsphere_datacenter.this.id
}

#  ┏━┓╻ ╻╺┳╸┏━┓╻ ╻╺┳╸
#  ┃ ┃┃ ┃ ┃ ┣━┛┃ ┃ ┃ 
#  ┗━┛┗━┛ ╹ ╹  ┗━┛ ╹ 

output "pool_id" {
  value = data.vsphere_resource_pool.this.id
}

output "datastore_id" {
  value = data.vsphere_datastore.this.id
}

output "datastore_name" {
  value = var.datastore
}

output "host_id" {
  value = data.vsphere_host.this.id
}

output "network_id" {
  value = data.vsphere_network.this.id
}
