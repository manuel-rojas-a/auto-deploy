# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
    vb.cpus = 1
  end

  config.vm.provider :libvirt do |libvirt|
    libvirt.management_network_name = 'default'
    libvirt.management_network_address = '192.168.122.0/24'
  end

  config.vm.define "web1" do |web|
    web.vm.network "private_network", ip: "192.168.122.10"
    web.vm.hostname = "web1.example.com"
  end

  config.vm.define "web2" do |web|
    web.vm.network "private_network", ip: "192.168.122.11"
    web.vm.hostname = "web2.example.com"
  end

  config.vm.define "db1" do |db|
    db.vm.network "private_network", ip: "192.168.122.20"
    db.vm.hostname = "db1.example.com"
  end

  config.vm.define "monitor" do |mon|
    mon.vm.network "private_network", ip: "192.168.122.30"
    mon.vm.hostname = "monitor.example.com"
    mon.vm.provider :libvirt do |libvirt|
      libvirt.memory = 1024
    end
  end
end
