from mock import Mock

from bravado_core.request import IncomingRequest, unmarshal_request


def test_request_with_path_parameter(petstore_spec):
    request = Mock(spec=IncomingRequest, path={'petId': '1234'})
    # /pet/{pet_id} fits the bill
    op = petstore_spec.resources['pet'].operations['getPetById']
    request_data = unmarshal_request(request, op)
    assert request_data['petId'] == 1234


def test_request_with_no_parameters(petstore_spec):
    request = Mock(spec=IncomingRequest)
    # /user/logout conveniently has no params
    op = petstore_spec.resources['user'].operations['logoutUser']
    request_data = unmarshal_request(request, op)
    assert 0 == len(request_data)
