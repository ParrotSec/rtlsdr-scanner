#
# rtlsdr_scan
#
# http://eartoearoak.com/software/rtlsdr-scanner
#
# Copyright 2012 - 2015 Al Brown
#
# A frequency scanning GUI for the OsmoSDR rtl-sdr library at
# http://sdr.osmocom.org/trac/wiki/rtl-sdr
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from rtlsdr_scanner.constants import APP_NAME, LOCATION_PORT


def create_gearth(handle):
    handle.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
                 '\t<NetworkLink>\n'
                 '\t\t<name>{}</name>\n'
                 '\t\t<flyToView>1</flyToView>\n'
                 '\t\t<open>1</open>\n'
                 '\t\t<Link>\n'
                 '\t\t\t<href>http://localhost:{}/kml</href>\n'
                 '\t\t\t<refreshMode>onInterval</refreshMode>\n'
                 '\t\t\t<refreshInterval>10</refreshInterval>\n'
                 '\t\t</Link>\n'
                 '\t</NetworkLink>\n'
                 '</kml>\n'.format(APP_NAME, LOCATION_PORT).encode())


if __name__ == '__main__':
    print('Please run rtlsdr_scan.py')
    exit(1)
