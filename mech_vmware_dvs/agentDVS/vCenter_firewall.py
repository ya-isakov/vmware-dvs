# Copyright 2012, Nachi Ueno, NTT MCL, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from neutron.agent import firewall
#from neutron.i18n import _LI
#from oslo_config import cfg
from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class vCenterFirewallDriver(firewall.FirewallDriver):

    def prepare_port_filter(self, port):
        pass

    def apply_port_filter(self, port):
        pass

    def update_port_filter(self, port):
        pass

    def remove_port_filter(self, port):
        pass

    def filter_defer_apply_on(self):
        pass

    def filter_defer_apply_off(self):
        pass

    @property
    def ports(self):
        return {}

    def update_security_group_members(self, sg_id, ips):
        pass

    def update_security_group_rules(self, sg_id, rules):
        pass

    def security_group_updated(self, action_type, sec_group_ids,
                               device_id=None):
        pass
