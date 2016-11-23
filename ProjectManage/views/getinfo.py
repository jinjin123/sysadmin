#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ansible.runner


def get_info(ip):
    data = {}
    runner = ansible.runner.Runner(module_name='setup', module_args = '', pattern = 'all', forks = 2)
    datastructure = runner.run()
    sn = datastructure['contacted'][ip]['ansible_facts']['ansible_product_serial']
    hostname = datastructure['contacted'][ip]['ansible_facts']['ansible_hostname']
   #  description = datastructure['contacted'][ip]['ansible_lsb']['ansible_description']
    ansible_machine = datastructure['contacted'][ip]['ansible_facts']['ansible_machine']
    os_kernel = datastructure['contacted'][ip]['ansible_facts']['ansible_kernel']
    cpu = datastructure['contacted'][ip]['ansible_facts']['ansible_processor'][1]
    cpu_count = datastructure['contacted'][ip]['ansible_facts']['ansible_processor_count']
    cpu_core = datastructure['contacted'][ip]['ansible_facts']['ansible_processor_cores']
    mem = datastructure['contacted'][ip]['ansible_facts']['ansible_memtotal_mb']
    ipadd_in = datastructure['contacted'][ip]['ansible_facts']['ansible_all_ipv4_addresses'][0]
    disk = datastructure['contacted'][ip]['ansible_facts']['ansible_devices']['sda']['size']
    
    data['sn'] = sn
    data['hostname'] = hostname
   # data['description'] = description
    data['ansible_machine'] = ansible_machine
    data['os_kernel'] = os_kernel
    data['cpu'] = cpu
    data['cpu_count'] = cpu_count
    data['cpu_core'] = cpu_core
    data['mem'] = mem
    data['ipadd_in'] = ipadd_in
    data['disk'] = disk
    
    return data
    if __name__ == '__main__':
        data = get_info('')





