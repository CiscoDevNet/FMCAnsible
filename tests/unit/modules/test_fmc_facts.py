"""
Simple test script to verify the FmcFactsBase class works correctly
"""

import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

# Now we can import our module
from plugins.module_utils.facts import FmcFactsBase


# Mock resource class for testing
class MockResource:
    def execute_operation(self, operation_name, params):
        """Mock API responses for testing"""
        if operation_name == 'getAllDomain':
            return [
                {'uuid': 'domain-1', 'name': 'Global', 'type': 'Domain'},
                {'uuid': 'domain-2', 'name': 'Test Domain', 'type': 'Domain'}
            ]
        elif operation_name == 'getAllDevice':
            return [
                {'id': 'device-1', 'name': 'FTD-1', 'type': 'Device'},
                {'id': 'device-2', 'name': 'FTD-2', 'type': 'Device'}
            ]
        elif operation_name == 'getAllAccessPolicy':
            return [
                {'id': 'policy-1', 'name': 'AccessPolicy1', 'type': 'AccessPolicy'}
            ]
        elif operation_name == 'getAllFilePolicy':
            return [
                {'id': 'file-policy-1', 'name': 'FilePolicy1', 'type': 'FilePolicy'}
            ]
        elif operation_name == 'getAllIntrusionPolicy':
            return [
                {'id': 'intrusion-policy-1', 'name': 'IntrusionPolicy1', 'type': 'IntrusionPolicy'}
            ]
        else:
            return []


def test_facts_gathering():
    """Test that facts gathering works correctly"""

    print("Testing FmcFactsBase...")

    # Create mock resource
    mock_resource = MockResource()

    # Create facts gatherer
    facts_gatherer = FmcFactsBase(mock_resource)

    # Test minimal facts gathering
    print("Testing minimal facts gathering...")
    facts = facts_gatherer.gather_facts(['min'])

    assert 'fmc' in facts
    assert 'domains' in facts['fmc']
    assert 'devices' in facts['fmc']
    assert 'access_policies' in facts['fmc']

    print("✓ Minimal facts gathering works")

    # Test file and intrusion policies
    print("Testing file and intrusion policies...")
    facts = facts_gatherer.gather_facts(['domains', 'file_policies', 'intrusion_policies'])

    assert 'file_policies' in facts['fmc']
    assert 'intrusion_policies' in facts['fmc']

    print("✓ File and intrusion policies work")

    # Test all facts gathering
    print("Testing all facts gathering...")
    facts = facts_gatherer.gather_facts(['all'])

    expected_keys = ['domains', 'devices', 'access_policies', 'file_policies',
                     'intrusion_policies', 'physical_interfaces', 'network_objects',
                     'port_objects', 'security_zones', 'device_groups']

    for key in expected_keys:
        assert key in facts['fmc'], f"Missing key: {key}"

    print("✓ All facts gathering works")

    print("All tests passed! ✅")


if __name__ == '__main__':
    test_facts_gathering()
