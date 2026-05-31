# API Test Cases

## API_TC_001

### Test Scenario
Verify API returns status code 200.

### Expected Result
Status code should be 200.

---

## API_TC_002

### Test Scenario
Verify response time is below 2 seconds.

### Expected Result
Response time should be less than 2000 ms.

---

## API_TC_003

### Test Scenario
Verify response body is not empty.

### Expected Result
Response contains valid data.

---

## API_TC_004

### Test Scenario
Verify Content-Type header.

### Expected Result
application/json

---

## API_TC_005

### Test Scenario
Verify invalid endpoint handling.

### Expected Result
404 response returned.

---

## API_TC_006

### Test Scenario
Verify unauthorized request handling.

### Expected Result
401 or appropriate authorization response.

---

## API_TC_007

### Test Scenario
Verify JSON structure.

### Expected Result
JSON format is valid.

---

## API_TC_008

### Test Scenario
Verify mandatory fields exist.

### Expected Result
Required fields present.

---

## API_TC_009

### Test Scenario
Verify special character handling.

### Expected Result
API handles input correctly.

---

## API_TC_010

### Test Scenario
Verify server stability.

### Expected Result
API remains available and responsive.