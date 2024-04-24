import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.SalesPersonWBSvc
// Description: SalesPersonWorkbench Business Object
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => application/json
   */  
export function getServiceDocument(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<JSON>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as JSON)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: Returns metadata document => content
   */  
export function get_metadata(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method GetCustomers
   Description: Retrieve all the records from Customer table
   OperationID: GetCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomers(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetCustomers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfContacts
   Description: Retrieve a list of Contacts
   OperationID: GetListOfContacts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfContacts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfContacts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfContacts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfContacts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfCRMCalls
   Description: Retrieve a list of CRM Calls
   OperationID: GetListOfCRMCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfCRMCalls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfCRMCalls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfCRMCalls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfCRMCalls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfInvoices
   Description: Retrieve a list of invoice
   OperationID: GetListOfInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfInvoices(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfJobs
   Description: Retrieve all the records from JobHead, OrderHed,OrderRel and OrderDtl table
   OperationID: GetListOfJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfJobs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfJobs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfOrders
   Description: Retrieve a list of orders
   OperationID: GetListOfOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfOrders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfOrders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfQuotes
   Description: Retrieve a list of Quotes
   OperationID: GetListOfQuotes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfQuotes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfQuotes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfQuotes(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfQuotes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfRMAs
   Description: Retrieve a list of RMAs
   OperationID: GetListOfRMAs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfRMAs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfRMAs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfRMAs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfRMAs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfServiceCalls
   Description: Retrieve a list of Service Call
   OperationID: GetListOfServiceCalls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfServiceCalls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfServiceCalls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfServiceCalls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfServiceCalls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfSites
   Description: Retrieve a list of Ship To
   OperationID: GetListOfSites
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfSites_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfSites_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfSites(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfSites", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfShipments
   Description: Retrieve a list of Shipments
   OperationID: GetListOfShipments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfShipments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfShipments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfShipments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfShipments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListOfTasks
   Description: Retrieve a list of Task
   OperationID: GetListOfTasks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListOfTasks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListOfTasks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListOfTasks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SalesPersonWBSvc/GetListOfTasks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_SalesPersonWBCRMCallRow{
      /**  The unique internal number assigned to the customer for which the contact is related to. Used when CallContactType is "Customer"  */  
   CallCustNum:number,
      /**  An abbreviated description of what the Call is about.  */  
   CallDesc:string,
      /**  The Quote that this call is related to.  */  
   CallQuoteNum:number,
      /**  Used to uniquely identify the record.  Used so more than 1 PCE can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   CallSeqNum:number,
      /**  The number that the user assigned to the ship to that this contact is related to.  Note that this field is blank for contacts related to the customer only.  Blank when there is no ship to.  */  
   CallShipToNum:string,
      /**  Call Text contains the textual content of the Call. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records.  */  
   CallText:string,
      /**  Used to uniquely identify the contact record for the related vendor or purchase point.  */  
   CallVConNum:number,
      /**  Company Identifier.  */  
   Company:string,
   ConNum:number,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  Major component of the foreign key of the related master record. For example: For a "QuotHed"  PCE this field would contain the related Quote Number,  for a "Customer" PCE it contains the Customers CustNum value.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteDtl"  memo this field would contain the Quote Line # of the related Quote detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "QuoteHed" memo's do not use this field.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "OrderQty"  memo this field would contain the Quote Qty # of the related Quote Qty record.  The usage of this field is dependent on the type of record the memo is related to.  */  
   Key3:string,
      /**  The date the PCE was last modified.  */  
   LastDate:string,
      /**  The DCD user ID that last updated the record  */  
   LastDcdUserID:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  The date the PCE was created.  */  
   OrigDate:string,
      /**  The DCD user ID that created the record  */  
   OrigDcdUserID:string,
      /**  The time the PCE was created.  */  
   OrigTime:number,
      /**   The master file to which the PCE is related to.  This field is used to properly  isolate PCE's to the master table they are related to.
records.  */  
   RelatedToFile:string,
   SalesRepName:string,
   SysRowID:string,
      /**  Contact's first name.  */  
   ContactFirstName:string,
      /**  Contact's last name.  */  
   ContactLastName:string,
      /**  Full name of the contact.  */  
   ContactName:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBContactRow{
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  The contact's alternate phone numbe  */  
   AltNum:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   City:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  The contact's title.  */  
   ContactTitle:string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   Country:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   CustNum:number,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  The contact's Home number.  */  
   HomeNum:string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   Inactive:boolean,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
   Name:string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   NoContact:boolean,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
   RoleDescription:string,
   ShipToName:string,
   ShipToNum:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
   SysRowID:string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   Zip:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBCustomerRow{
      /**  The first line of the customer's main address.  */  
   Address1:string,
      /**  The city portion of the customer's main address.  */  
   City:string,
      /**  Company Identifier.  */  
   Company:string,
   Country:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Used to define the type of the customer record.  */  
   CustomerType:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  The zip or postal code portion of the customer's main address.  */  
   Zip:string,
      /**  Indicates if the record is inactive.  */  
   Inactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBInvoiceRow{
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  Company Identifier.  */  
   Company:string,
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**   There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments,  and "Mis" = Miscellaneous.
The setting of this field affects invoice entry:
"Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.
"Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.
"Deposit" invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.
"Miscellaneous" - These invoices may or may not reference a Sales Order.
If Invoice is generated in Project Billing then there are following options:
"PFF" - Fixed Fee project;
"PCP" - Cost Plus project;
"PTM" - Time and Material project;
"PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  */  
   LineDesc:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The associated sales order line number.  */  
   OrderLine:number,
      /**  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  */  
   OrderNum:number,
      /**  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  */  
   PartNum:string,
      /**  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  */  
   POLine:string,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
   ProdGrupDesc:string,
      /**  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  */  
   ShipToNum:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  */  
   ShpConNum:number,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBJobRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Related Sales order line number.  */  
   OrderLine:number,
      /**  Related sales order number. For build to stock demands the OrderNum, OrderLine and OrderRel fields are all zero  */  
   OrderNum:number,
      /**  Related sales order release number.  */  
   OrderRelNum:number,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Site Identifier.  Mirror image of JobHead.Site. Duplicated for performance reasons  */  
   Plant:string,
      /**   The planned production quantity for a  Job to fill the demand.
Note: updates the JobHead.ProdQty via JobProd write trigger.  */  
   ProdQty:number,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**   Quantity Shipped against this allocation.
Updated via the ShipDtl write triggers.  */  
   ShippedQty:number,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
   SysRowID:string,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  When creating a new Service Call the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  Can have 3 values High, normal and, Low  */  
   CallPriority:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Contract Number if this item is under a contract  */  
   ContractNum:number,
      /**  The drop shipment packing slip line that holds the warranty information for this service call  */  
   DropShipPackLine:number,
      /**  The drop shipment packing slip number that this Service call is linked with  */  
   DropShipPackSlip:string,
      /**  Contains the Customer number that the Service Call is for.  This must be valid in the Customer table.  */  
   FSCustNum:number,
      /**  The PartNum field identifies the Part  */  
   FSPartNum:string,
      /**  Indicate that the call is open.  */  
   OpenCall:boolean,
      /**  The packing slip line that holds the warranty information for this service call  */  
   PackLine:number,
      /**  Packing slip number that this Service call is linked with.  */  
   PackNum:number,
      /**  The date that the service is requested for.  */  
   RequestDate:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBOrderRow{
      /**  Company Identifier.  */  
   Company:string,
   Country:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the OrderDtl.NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDateDtl:string,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   OrderHeld:boolean,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  */  
   OrderNum:number,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.  */  
   PartNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
   ProdGrupDesc:string,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderDtl.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDateDtl:string,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Not editable, When SF Synch creates orders, this flag is set to YES.  */  
   WebOrder:boolean,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBQuoteRow{
      /**  Best case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   BestCsRevenue:number,
      /**  Company Identifier.  */  
   Company:string,
   Country:string,
      /**   Duplicated from QuoteHed for Query's.  Describe the type of Quote this is.
LEAD = Lead
OPPO = Opportunity  */  
   CurrentStage:string,
   CustID:string,
   CustNum:number,
      /**  Best case revenue for this line in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and BestCsPct.  */  
   DocBestCsRevenue:number,
      /**  Expected revenue for this line  in customer currency.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   DocExpectedRevenue:number,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   DocWorstCsRevenue:number,
      /**  Date that quoted needs to be quoted by.  Defaulted as Today + EQSyst.DueDays. This will be used to browse unquoted quotes in order by when they need to get quoted. Like a work queue for the quoters.  */  
   DueDate:string,
      /**  Date that quote was created in the system. Not user maintainable. Set equal to the system date when record was created.  */  
   EntryDate:string,
      /**  Expected revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and SalesRepFactor  */  
   ExpectedRevenue:number,
      /**  The date when this quote expires. This field is not maintainable until the quote is marked as Quoted = Yes. At which time the DateQuoted is generated and then the ExpirationDate is set to DateQuoted + EQSyst.ExpirationDays.  */  
   ExpirationDate:string,
      /**  Indicates if the Quote has expired.  A quote is expired when QuoteHed.ExpirationDate < Today.  Each time a user logs on the system does a quick check for any unexpired quotes that have an expiration date < Today and sets them as expired. This field is also set during the QuoteHed write trigger.  */  
   Expired:boolean,
   MktgCampaignID:string,
      /**  Link to the marketing event associated with this record.  */  
   MktgEvntSeq:number,
      /**  The full name of the customer.  */  
   Name:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the QuoteDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
   ProdCodeDesc:string,
      /**  Indicates if the quote has been quoted.  That is, the details have been entered, prices have been determined and is ready to be sent to the customer.  The quoter considers this quote complete.  Toggling this field also sets the DateQuoted equal to the current system date.  */  
   Quoted:boolean,
      /**  This field along with Company and QuoteNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the QuoteDtl record for the Quote and the adding 1 to it.  */  
   QuoteLine:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to OrderHed file.  */  
   QuoteNum:number,
      /**  Indicates which customer ship to is to be used as the default for the Order release record created from this Quote. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new Quotes or when the QuoteHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Worst case revenue for this line.  Calculated from SellingExpectedQty and Unit Price, discount and WorstCsPct.  */  
   WorstCsRevenue:number,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBRMARow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Reference to a customers accounts payable debit memo.  */  
   DebitMemoRef:string,
      /**  The help desk case that created this RMA.  */  
   HDCaseNum:number,
      /**  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  */  
   LineDesc:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Indicates if this RA is in an "open" status.  The user can toggle the setting of this field in header maintenance. It is also set automatically as the details are "Closed/Opened".  If there are no RMADtl records, then it is still considered as "open".  */  
   OpenRMA:boolean,
      /**  Mirror image of RMAHead.OpenRMA.  */  
   OpenRMADtl:boolean,
      /**  Sales order line that the Return detail is related to.  If entered it must be valid in the OrderDtl file. If entered the OrderDtl supplies the Part Number, LineDesc, IUM . . .  */  
   OrderLine:number,
      /**   The sales order number that the Return detail is related to.
Must be an order of the customer identified in the RMAHead.  When entered the OrderLine is then mandatory.  */  
   OrderNum:number,
      /**  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  */  
   PartNum:string,
      /**  Quantity that is to be returned  */  
   ReturnQty:number,
      /**  Unit Of Measure of the  ReturnQty.  */  
   ReturnQtyUOM:string,
      /**  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  */  
   ReturnReasonCode:string,
      /**  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  */  
   RevisionNum:string,
      /**  Set from RMAHead.RMADate, used by Customer Tracker  */  
   RMADate:string,
      /**  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  */  
   RMALine:number,
      /**  Return Authorization Number. Used to relate RMADtl to RMAHead.  */  
   RMANum:number,
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBServiceCallRow{
      /**  The date that the service was performed on.  */  
   ActualDate:string,
      /**  A unique code that identifies the type of service call  */  
   CallCode:string,
      /**  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  */  
   CallLine:number,
      /**  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  */  
   CallNum:number,
      /**  Can have 3 values High, normal and, Low  */  
   CallPriority:string,
      /**  TotalCall Quantity for the line item.  */  
   CallQty:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the Contract  */  
   ContractCode:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Indicated the invoice processing has been done for this call.  */  
   Invoiced:boolean,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Indicate that the call is open.  */  
   OpenCall:boolean,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Indicates that the call is closed and can be invoiced.  */  
   ReadyToInvoice:boolean,
      /**  The date that the service is requested for.  */  
   RequestDate:string,
      /**  The date that the service is scheduled for.  */  
   SchedDate:string,
      /**  Indicates which customer ship to is to be used  for the Service Call. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Establishes the Shipping Contact to be used.  In this case the contact at the location where the item the service call is covering are. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
   SysRowID:string,
      /**  No information can be entered when this flag is set. It won't be invoiced, labor and materials cannot be entered.  */  
   VoidCall:boolean,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBShipmentRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  Line Description  */  
   LineDesc:string,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
   OnTime:number,
      /**  The sales order line that this shipment detail line is linked to.  Must be valid in the OrderDtl file.  */  
   OrderLine:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable, It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  */  
   PackLine:number,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  */  
   PartNum:string,
      /**  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  */  
   Plant:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderRel.ReqDate.  */  
   ReqDate:string,
      /**  Selling Unit of Measure...duplicated from the OrderDtl.SUM...Not user maintainable.  */  
   SalesUM:string,
      /**  Quantity shipped from inventory. This quantity reduces PartWhse.Onhand. This quantity is a mirror of field OurInventoryShipQty except it is in the SUM unit of measure.  */  
   SellingInventoryShipQty:number,
      /**  Quantity shipped from a Job. This is only valid when the OrderRel.JobNum is not blank.  This field is a mirror of OurJobShipQty except it is in the SUM unit of measure.  */  
   SellingJobShipQty:number,
      /**  The actual ship date for the packing slip. Default as system date.  This field comes directly from the ShipHead table.  */  
   ShipDate:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
   SysRowID:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBSiteRow{
      /**  The first line of the ShipTo address.  */  
   Address1:string,
      /**  The city portion of the ShipTo address.  */  
   City:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  The country portion of the ShipTo address.  */  
   Country:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  The email address of the ShipTo location.  */  
   EMailAddress:string,
      /**  The fax number for the ShipTo location. isplayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   FaxNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   Name:string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  The SalesRep.SalesRepCode value of the default salesperson for the customer. Used as a default in Order Entry and Invoice entry. The SalesRep from the customer master is used as an initial default when creating new ship to.  */  
   SalesRepCode:string,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   TerritoryID:string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   ZIP:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SalesPersonWBTableset{
   SalesPersonWBCustomer:Erp_Tablesets_SalesPersonWBCustomerRow[],
   SalesPersonWBContact:Erp_Tablesets_SalesPersonWBContactRow[],
   SalesPersonWBCRMCall:Erp_Tablesets_SalesPersonWBCRMCallRow[],
   SalesPersonWBInvoice:Erp_Tablesets_SalesPersonWBInvoiceRow[],
   SalesPersonWBJob:Erp_Tablesets_SalesPersonWBJobRow[],
   SalesPersonWBOrder:Erp_Tablesets_SalesPersonWBOrderRow[],
   SalesPersonWBQuote:Erp_Tablesets_SalesPersonWBQuoteRow[],
   SalesPersonWBRMA:Erp_Tablesets_SalesPersonWBRMARow[],
   SalesPersonWBServiceCall:Erp_Tablesets_SalesPersonWBServiceCallRow[],
   SalesPersonWBShipment:Erp_Tablesets_SalesPersonWBShipmentRow[],
   SalesPersonWBSite:Erp_Tablesets_SalesPersonWBSiteRow[],
   SalesPersonWBTask:Erp_Tablesets_SalesPersonWBTaskRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SalesPersonWBTaskRow{
   ChangeDate:string,
      /**  The UserID that last changed the task  */  
   ChangeDcdUserID:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  */  
   Complete:boolean,
      /**  User entered completion date.  Default to TODAY when the complete flag is checked.  */  
   CompleteDate:string,
      /**  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  */  
   Conclusion:string,
      /**  The date the task was created.  */  
   CreateDate:string,
      /**  The UserID that created the task  */  
   CreateDcdUserID:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  The Task should be completed by this date.  */  
   DueDate:string,
      /**  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  */  
   Key1:string,
      /**  2nd component of the foreign key to the related master record.  */  
   Key2:string,
      /**  3rd component of the foreign key to the related master record.  */  
   Key3:string,
      /**  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  */  
   Mandatory:boolean,
      /**  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  */  
   Milestone:boolean,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Percent of task that is complete.  Valid values are 0-100. User maintained.  */  
   PercentComplete:number,
      /**  Valid values are 1 - 99 1 = HIGH,  99 = LOW  */  
   PriorityCode:number,
      /**  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  */  
   RelatedToFile:string,
      /**  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  */  
   RoleCode:string,
      /**  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  */  
   SalesRepCode:string,
      /**  Defaults is TODAY.  */  
   StartDate:string,
      /**  Status Code. From TaskStat table  */  
   StatusCode:string,
   SysRowID:string,
      /**  The Customer contact that this Task is related to.  */  
   TaskConNum:number,
      /**  The Customer that this task is related to  */  
   TaskCustNum:number,
      /**  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  */  
   TaskDescription:string,
      /**  The Quote that this Task is related to.  */  
   TaskQuoteNum:number,
      /**  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  */  
   TaskSeqNum:number,
      /**  Link to the task set.  */  
   TaskSetID:string,
      /**  The Customer Ship To that this task is related to  */  
   TaskShipToNum:string,
      /**  List of all ship to territories for the customer  */  
   ShipToTerrList:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**  Indicates if the record is inactive.  */  
   ShipToNumInactive:boolean,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param whereClause
      @param sortBy
      @param pageSize
   */  
export interface GetCustomers_input{
      /**  Where Clause to restrict data from Customers  */  
   whereClause:string,
      /**  sortBy Selected  */  
   sortBy:string,
      /**  The page size, used only for UI adapter  */  
   pageSize:number,
}

export interface GetCustomers_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param callDesc
      @param origDateStart
      @param origDateEnd
      @param salesRepCode
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfCRMCalls_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Customer Number  */  
   custNum:number,
      /**  Call Description  */  
   callDesc:string,
      /**  Create Date Start  */  
   origDateStart:string,
      /**  Create Date End  */  
   origDateEnd:string,
      /**  Sales Rep Code  */  
   salesRepCode:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfCRMCalls_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param perConID
      @param custNum
      @param name
      @param firstName
      @param middleName
      @param lastName
      @param func
      @param faxNum
      @param phoneNum
      @param eMailAddress
      @param cellPhoneNum
      @param pagerNum
      @param homeNum
      @param altNum
      @param prefix
      @param suffix
      @param initials
      @param webSite
      @param iM
      @param twitter
      @param linkedIn
      @param faceBook
      @param address1
      @param address2
      @param address3
      @param city
      @param state
      @param zip
      @param corpName
      @param comment
      @param contactTitle
      @param reportsTo
      @param roleCode
      @param countryNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfContacts_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Person Contac ID  */  
   perConID:number,
      /**  Customer Number  */  
   custNum:number,
      /**  Name  */  
   name:string,
      /**  First Name  */  
   firstName:string,
      /**  Middle Name  */  
   middleName:string,
      /**  Last Name  */  
   lastName:string,
      /**  Func  */  
   func:string,
      /**  Fax Number  */  
   faxNum:string,
      /**  Phone Number  */  
   phoneNum:string,
      /**  Email Address  */  
   eMailAddress:string,
      /**  CellPhone Number  */  
   cellPhoneNum:string,
      /**  Pager Number  */  
   pagerNum:string,
      /**  Home Number  */  
   homeNum:string,
      /**  Alt Number  */  
   altNum:string,
      /**  Prefix  */  
   prefix:string,
      /**  Suffix  */  
   suffix:string,
      /**  Initials  */  
   initials:string,
      /**  WebSite  */  
   webSite:string,
      /**  IM  */  
   iM:string,
      /**  Twitter  */  
   twitter:string,
      /**  LinkedIn  */  
   linkedIn:string,
      /**  Facebook  */  
   faceBook:string,
      /**  Address 1  */  
   address1:string,
      /**  Address 2  */  
   address2:string,
      /**  Address 3  */  
   address3:string,
      /**  City  */  
   city:string,
      /**  Satte  */  
   state:string,
      /**  Zip Code  */  
   zip:string,
      /**  Corp Name  */  
   corpName:string,
      /**  Comment  */  
   comment:string,
      /**  Contact Title  */  
   contactTitle:string,
      /**  Report To  */  
   reportsTo:string,
      /**  Role Code  */  
   roleCode:string,
      /**  Country Number  */  
   countryNum:number,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfContacts_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param invoiceNum
      @param orderNum
      @param legalNumber
      @param custNum
      @param startDueDate
      @param endDueDate
      @param status
      @param type
      @param prodCode
      @param packSlip
      @param partNum
      @param plant
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfInvoices_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Invoice Numbre  */  
   invoiceNum:number,
      /**  Order Number  */  
   orderNum:number,
      /**  Legal Number  */  
   legalNumber:string,
      /**  Customer Number  */  
   custNum:number,
      /**  Start Due Date  */  
   startDueDate:string,
      /**  End Due Date  */  
   endDueDate:string,
      /**  Invoice Status  */  
   status:boolean,
      /**  Invoice Type  */  
   type:string,
      /**  Product Group  */  
   prodCode:string,
      /**  Pack Slip  */  
   packSlip:number,
      /**  Part Number  */  
   partNum:string,
      /**  Plant  */  
   plant:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfInvoices_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
      @param jobNumStart
      @param jobNumEnd
      @param custNum
      @param equipID
      @param orderShipByStart
      @param orderShipByEnd
      @param jobStartDate
      @param jobDueDate
      @param jobType
      @param jobClosed
      @param jobComplete
      @param jobReleased
      @param jobEngineered
      @param jobFirm
      @param jobHeld
      @param prodQty
      @param orderNum
      @param callNum
      @param prodCode
      @param partNum
      @param plant
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfJobs_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Job Number  */  
   jobNum:string,
      /**  Job Number Start  */  
   jobNumStart:string,
      /**  Job Number End  */  
   jobNumEnd:string,
      /**  Customer Number  */  
   custNum:number,
      /**  Equip ID  */  
   equipID:string,
      /**  Order Ship By Start  */  
   orderShipByStart:string,
      /**  Order Ship By End  */  
   orderShipByEnd:string,
      /**  Job Start Date  */  
   jobStartDate:string,
      /**  Job Due Date  */  
   jobDueDate:string,
      /**  Job Type  */  
   jobType:string,
      /**  Job Closed  */  
   jobClosed:boolean,
      /**  Job Complete  */  
   jobComplete:boolean,
      /**  Job Released  */  
   jobReleased:boolean,
      /**  Job Engineered  */  
   jobEngineered:boolean,
      /**  Job Firm  */  
   jobFirm:boolean,
      /**  Job Held  */  
   jobHeld:boolean,
      /**  Production Quantity  */  
   prodQty:number,
      /**  Order Number  */  
   orderNum:number,
      /**  Call Number  */  
   callNum:number,
      /**  Product Group  */  
   prodCode:string,
      /**  Part Number  */  
   partNum:string,
      /**  Plant  */  
   plant:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfJobs_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param orderNum
      @param custNum
      @param poNum
      @param needByStart
      @param needByEnd
      @param shipByStart
      @param shipByEnd
      @param status
      @param prodCode
      @param partNum
      @param plant
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfOrders_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Order Number  */  
   orderNum:number,
      /**  Customer Number  */  
   custNum:number,
      /**  Purchase Order Number  */  
   poNum:string,
   needByStart:string,
      /**  Need By End  */  
   needByEnd:string,
      /**  Ship By Start  */  
   shipByStart:string,
      /**  Ship By End  */  
   shipByEnd:string,
      /**  Order Status  */  
   status:boolean,
      /**  Product Group  */  
   prodCode:string,
      /**  Part Num  */  
   partNum:string,
      /**  Plant  */  
   plant:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfOrders_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param quoteNum
      @param custNum
      @param poNum
      @param dueDateStart
      @param dueDateEnd
      @param expirationDateStart
      @param expirationDateEnd
      @param expired
      @param quoted
      @param prodCode
      @param partNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfQuotes_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Quote Number  */  
   quoteNum:number,
      /**  Customer Number  */  
   custNum:number,
      /**  Purchase Order Number  */  
   poNum:string,
      /**  Due Date Start  */  
   dueDateStart:string,
      /**  Due Date End  */  
   dueDateEnd:string,
      /**  Expiration Date Start  */  
   expirationDateStart:string,
      /**  Expiration Date End  */  
   expirationDateEnd:string,
      /**  Expired  */  
   expired:boolean,
      /**  Quoted  */  
   quoted:boolean,
      /**  Product Group  */  
   prodCode:string,
      /**  Part Number  */  
   partNum:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfQuotes_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rmaNum
      @param custNum
      @param rmaStatus
      @param orderNum
      @param partNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfRMAs_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  RMA Number  */  
   rmaNum:number,
      /**  Customer Number  */  
   custNum:number,
      /**  RMA Status  */  
   rmaStatus:boolean,
      /**  Order Number  */  
   orderNum:number,
      /**  Part Number  */  
   partNum:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfRMAs_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param callNum
      @param custNum
      @param shipToNum
      @param callPriority
      @param callCode
      @param hdCaseNum
      @param openCall
      @param invoiced
      @param voidCall
      @param partNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfServiceCalls_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Call Number  */  
   callNum:number,
      /**  Customer Number  */  
   custNum:number,
      /**  Ship To Number  */  
   shipToNum:string,
      /**  Call Priority  */  
   callPriority:string,
      /**  Call Code  */  
   callCode:string,
      /**  HD Case  */  
   hdCaseNum:number,
      /**  Open Call  */  
   openCall:boolean,
      /**  Invoiced  */  
   invoiced:boolean,
      /**  Void Call  */  
   voidCall:boolean,
      /**  Part Number  */  
   partNum:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfServiceCalls_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param packNum
      @param custNum
      @param shipPerson
      @param shipDateStart
      @param shipDateEnd
      @param shipStatus
      @param readyToInvoice
      @param invoiced
      @param voided
      @param orderNum
      @param shipToNum
      @param partNum
      @param plant
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfShipments_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Pack Number  */  
   packNum:number,
      /**  Customer Number  */  
   custNum:number,
      /**  Ship Person  */  
   shipPerson:string,
      /**  Ship Date Start  */  
   shipDateStart:string,
      /**  Ship Date End  */  
   shipDateEnd:string,
      /**  Ship Status  */  
   shipStatus:string,
      /**  Ready to Invoice  */  
   readyToInvoice:boolean,
      /**  Invoiced  */  
   invoiced:boolean,
      /**  Voided  */  
   voided:boolean,
      /**  Order Number  */  
   orderNum:number,
      /**  Ship To Num  */  
   shipToNum:string,
      /**  Part Number  */  
   partNum:string,
      /**  Plant  */  
   plant:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfShipments_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param shipToNum
      @param custNum
      @param name
      @param city
      @param state
      @param zip
      @param phoneNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfSites_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Ship To Number  */  
   shipToNum:string,
      /**  Customer Number  */  
   custNum:number,
      /**  Name  */  
   name:string,
      /**  City  */  
   city:string,
      /**  State  */  
   state:string,
      /**  Zip Code  */  
   zip:string,
      /**  Phone Number  */  
   phoneNum:string,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfSites_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param custNum
      @param taskDescription
      @param dueDateStart
      @param dueDateEnd
      @param startDateStart
      @param startDateEnd
      @param taskStatus
      @param taskConclusion
      @param quoteNum
      @param dataTag
      @param sortBy
      @param pageSize
   */  
export interface GetListOfTasks_input{
   ds:Erp_Tablesets_SalesPersonWBTableset[],
      /**  Customer Number  */  
   custNum:number,
      /**  Task Description  */  
   taskDescription:string,
      /**  Due Date Start  */  
   dueDateStart:string,
      /**  Due Date End  */  
   dueDateEnd:string,
      /**  Start Date Start  */  
   startDateStart:string,
      /**  Start Date End  */  
   startDateEnd:string,
      /**  Task Status  */  
   taskStatus:boolean,
      /**  Task Conclusion  */  
   taskConclusion:string,
      /**  Quote Number  */  
   quoteNum:number,
      /**  Data Tag  */  
   dataTag:string,
      /**  The sort by, used to define the field to be used to sort the records  */  
   sortBy:string,
      /**  The page size, used to define the amount of records to retrieve  */  
   pageSize:number,
}

export interface GetListOfTasks_output{
   returnObj:Erp_Tablesets_SalesPersonWBTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_Extensions_ExtensionRow{
   ColumnValues:object
   RowMod:string,
   SysRowID:string,
}

export interface Ice_Extensions_ExtensionTableColumn{
   ColumnName:string,
   ColumnType:string,
}

export interface Ice_Extensions_ExtensionTableData{
   Table:Ice_Extensions_ExtensionRow[],
   SystemCode:string,
   TableName:string,
   Columns:Ice_Extensions_ExtensionTableColumn[],
   PrimaryKeyColumns:string,
   PeerTableSystemCode:string,
   PeerTableName:string,
}

