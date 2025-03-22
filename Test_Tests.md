## Test Case Development

| Test Case ID | Requirement ID | Description                        | Steps                                                                 | Expected Result                                        | Status (Pass/Fail) |
|--------------|----------------|------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------|--------------------|
| TC-001       | FR1            | Add a new product to inventory     | 1. Navigate to 'Inventory Management'<br>2. Click 'Add Product'<br>3. Enter product details<br>4. Click 'Save' | Product is added and visible in inventory list         | ...                |
| TC-002       | FR1            | Update an existing product in inventory | 1. Navigate to 'Inventory Management'<br>2. Select an existing product<br>3. Modify details<br>4. Click 'Save' | Product details are updated successfully               | ...                |
| TC-003       | FR2            | Generate an automated financial summary | 1. Navigate to 'Reports'<br>2. Click 'Generate Summary'<br>3. Select date range<br>4. Click 'Download' | A formatted financial summary is generated and downloadable | ...            |
| TC-004       | FR3            | Send promotional messages to customers | 1. Navigate to 'Promotions'<br>2. Select customer group<br>3. Compose message<br>4. Click 'Send' | Customers receive messages via WhatsApp                | ...                |
| TC-005       | FR4            | Offline inventory management and sync | 1. Disable internet connection<br>2. Add a new product<br>3. Reconnect to internet<br>4. Check inventory sync | Inventory updates sync automatically once online       | ...                |
| TC-006       | FR4            | Offline sales tracking and sync   | 1. Disable internet connection<br>2. Record a sale<br>3. Reconnect to internet<br>4. Check sales report | Sales transactions sync automatically once online      | ...                |
| TC-007       | FR5            | User login via Firebase authentication | 1. Open login screen<br>2. Enter credentials<br>3. Click 'Login'      | Only verified users are allowed access                 | ...                |
| TC-008       | FR5            | Access restriction for unverified users | 1. Enter incorrect credentials<br>2. Click 'Login'                   | Access is denied and an error message is displayed     | ...                |


