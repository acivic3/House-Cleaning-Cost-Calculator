# Program Design and Structure

### Inputs

- **Number of rooms** in the house (integer or spelled-out number).
- **Type(s) of cleaning services** required (string, can be multiple).
- **Type of cleaning quality** (string, only one selection allowed).

### Constants

- **Room Sizes**:  
  - **Small House**: Maximum of 3 rooms.  
  - **Medium House**: Maximum of 6 rooms.  
  - **Large House**: More than 6 rooms.  

- **Cleaning Service Costs (per room)**:  
  - **Floors**: $50  
  - **Windows**: $40  
  - **Bathrooms**: $60  
  - **Dusting**: $30  

- **Numbered Words**: `'one'` to `'twenty'`.  

- **Similarity Score Threshold**: 75 (for fuzzy matching in input validation).  

- **Cleaning Qualities**:  
  - **Light**: 40% off.  
  - **Complete**: 10% more.  

### Outputs

- **Total cost** of the cleaning service based on the number of rooms, selected services, and quality of cleaning.
- **House size determination** (Small, Medium, Large) based on the number of rooms.
- **Listing of selected cleaning services**.
- **Cleaning quality** selected.

---

## Algorithm / Pseudocode

1. **Prompt User for Number of Rooms**:  
   - Validate input (numeric or spelled-out numbers).  
   - Use fuzzy matching for spelled-out numbers.  
   - Limit attempts to 3, then exit if unsuccessful.

2. **Prompt User for Cleaning Services**:  
   - Display available services.  
   - Allow multiple selections (comma- or space-separated).  
   - Validate input using fuzzy matching.

3. **Prompt User for Cleaning Quality**:  
   - Display the 2 different cleaning qualities.  
   - Allow only 1 selection.  
   - Validate input using fuzzy matching.

4. **Calculate Total Cost**:  
   - Determine house size based on the number of rooms.  
   - Calculate cost by multiplying the number of rooms by the cost of each selected service.  
   - Apply the light/complete cleaning multiplier to the total cost.

5. **Output**:  
   - Display house size.  
   - List selected cleaning services.  
   - Show the selected cleaning quality.  
   - Display the total calculated cost.

---

## Programming Considerations

- **Fuzzy Matching**: Enhances usability by interpreting user input even if it contains small mistakes, but may introduce inaccuracies in certain edge cases.
- **Similarity Score Threshold**: Set at 75 to balance accuracy and flexibility.
- **Error Handling**: The program exits after 3 invalid attempts.
- **Efficiency**: Use of sets for storing selected services avoids duplicates.
- **Cost Calculation**: Straightforward multiplication of the cost per service by the number of rooms.
- **Flexibility**: Easy to modify or expand services, costs, and qualities.

---

## Testing Plan

### Test Case 1

- **Inputs**:  
  - Number of rooms: `"Tree"` (misspelling of "Three").  
  - Services: `"Flor"` and `"Bath"` (misspellings of "Floor" and "Bathroom").  
  - Quality: `"lig"` (misspelling of "light").  

- **Expected Outputs**:  
  - Recognize 3 rooms.  
  - Identify services as Floors and Bathrooms.  
  - Evaluate this as a light cleaning.

**Purpose**:  
To test inaccurate spellings/abbreviations for the number of rooms, cleaning services, and cleaning quality.

![Test Case 1](HCCC%20-%20Test%20Case%201.png)

---

### Test Case 2

- **Inputs**:  
  - Number of rooms: `"7"` (exceeding the medium house cutoff).  
  - Services: `"floors, dusting"` (correct input using a comma separator).  
  - Quality:  
    - First attempt: `"light and complete"` (invalid).  
    - Second attempt: `"complee"` (misspelling of "complete").  

- **Expected Outputs**:  
  - Recognize 7 rooms (Large House).  
  - Identify services as Floors and Dusting.  
  - Validate cleaning quality as complete.  
  - Calculate the cost accordingly.

**Purpose**:  
To evaluate house size classification, cost calculation for a large house, and validation of cleaning quality input.

![Test Case 2](HCCC%20-%20Test%20Case%202.png)

---

### Test Case 3

- **Inputs**:  
  - Number of rooms: `"0"` (edge case).  
  - Service: `"bathrooms"`.  
  - Quality: `"light"`.

- **Expected Outputs**:  
  - Recognize 0 rooms.  
  - Identify the service as Bathrooms.  
  - Calculate a total cost of $0 or handle it as an invalid input.

**Purpose**:  
To assess how the program handles non-positive room numbers and validates correct spelling for cleaning quality.

![Test Case 3](HCCC%20-%20Test%20Case%203.png)
