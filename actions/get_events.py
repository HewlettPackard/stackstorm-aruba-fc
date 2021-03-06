# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"


from pyhpecfm import system
from lib.actions import AfcBaseAction
import datetime

class alarmLookup(AfcBaseAction):
    def run(self):
        afc_audits = system.get_audit_logs(self.client)
        if isinstance(afc_audits, list):
            # Create a empty list for alarms
            alarm_data = []
            # Loop through cfm_audits and process ALARMS
            for alarm in afc_audits:
                typex = alarm['record_type']
                if typex == 'ALARM':
                    # Build dictionary to add to list
                    created = int(alarm['log_date'] / 10)
                    out = {
                          'u_eventtype': alarm['data']['event_type'],
                          'u_typex': alarm['record_type'],
                          'u_sev': alarm['severity'],
                          'u_uuid': alarm['uuid'],
                          'u_desc': alarm['description'],
                          'u_created': created,
                          'u_snowack' : 'no'
                          }
                    alarm_data.append(out)

            return (True, alarm_data)
        return (False, afc_audits)