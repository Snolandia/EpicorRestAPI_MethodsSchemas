import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.IMCustomerSvc
// Description: Business Object to handle: Count, Get, Ack, Add, Update and Delete of Customer, ShipTo, CustCnt, CustBillTo
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/$metadata", {
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
   Summary: Invoke method AckCustomer
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AckCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/AckCustomer", {
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
   Summary: Invoke method CountCustomer
   Description: Returns the count of existing IntQueOut records along with the count of updated customers in the database that IntQueOut records have not yet been created for
   OperationID: CountCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CountCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/CountCustomer", {
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
   Summary: Invoke method GetAllCustomer
   Description: Generates IntQueOut and IMCustomer rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAllCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/GetAllCustomer", {
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
   Summary: Invoke method GetCustomer
   Description: Generates IntQueOut and IMCustomer rows since the last time this was called and then returns these along with any existing
   OperationID: GetCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/GetCustomer", {
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
   Summary: Invoke method AddCustomer
   Description: Add customer and customer related tables
   OperationID: AddCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/AddCustomer", {
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
   Summary: Invoke method DeleteCustomer
   Description: Delete customer and customer related tables
   OperationID: DeleteCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/DeleteCustomer", {
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
   Summary: Invoke method UpdateCustomer
   Description: Update customer and customer related tables
   OperationID: UpdateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCustomer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.IMCustomerSvc/UpdateCustomer", {
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
   /** Required : 
      @param IMCustomerTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface AckCustomer_input{
   IMCustomerTableset:Erp_Tablesets_IMCustomerTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface AckCustomer_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param IMCustomerTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param saveAddOnError
      @param imIntegrationKey
   */  
export interface AddCustomer_input{
   IMCustomerTableset:Erp_Tablesets_IMCustomerTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
   saveAddOnError:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}

export interface AddCustomer_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
   imIntegrationKey:Erp_Tablesets_IMIntegrationKeyTableset[],
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface CountCustomer_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface CountCustomer_output{
parameters : {
      /**  output parameters  */  
   totalCount:number,
}
}

   /** Required : 
      @param IMCustomerTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface DeleteCustomer_input{
   IMCustomerTableset:Erp_Tablesets_IMCustomerTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface DeleteCustomer_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

export interface Erp_Tablesets_IMCustBillToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  Indicates the CustNum of the alternate Bill To Customer.  */  
   BTCustNum:number,
      /**  Indicates whether this Alt Bill To is the default record or not.  */  
   DefaultBillTo:boolean,
      /**  If checked, the invoice print routine will use the address from this alternate customer as the invoice address.  */  
   InvoiceAddress:boolean,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Our Bank Code  */  
   OurBankCode:string,
      /**  Full Legal name  */  
   BTLegalName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  If this value is true, the Customer that is designated as the Alternate Bill To has not been sent to FSA.  */  
   FSACustomerNotSent:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMCustCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   CustNum:number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address2:string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address3:string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   City:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   Zip:string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   Country:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   CountryNum:number,
      /**  The contact's title.  */  
   ContactTitle:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Contact's Website.  */  
   WebSite:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMCustomerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The full name of the customer.  */  
   Name:string,
      /**  The first line of the customer's main address.  */  
   Address1:string,
      /**  The second line of the customer's main address.  */  
   Address2:string,
      /**  The third line of the customer's main address.  */  
   Address3:string,
      /**  The city portion of the customer's main address.  */  
   City:string,
      /**  The state or province portion of the customer's main address.  */  
   State:string,
      /**  The zip or postal code portion of the customer's main address.  */  
   Zip:string,
      /**  The country of the main customer address.  */  
   Country:string,
      /**  The SalesTer.TerritoryID value of the territory assigned to the customer.  */  
   TerritoryID:string,
      /**   The Terms.TermsCode value of the default sales terms associated with the customer. A default may be supplied by XaSyst.TermsCode if not blank. The terms will default into quotes and orders for this customer.
For invoices not related to a sales order, these terms will also default into the invoice.  */  
   TermsCode:string,
      /**  Contains the ShipVia.ShipViaCode value of the default ShipVia for the customer.  */  
   ShipViaCode:string,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The Fax Number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  */  
   FaxNum:string,
      /**  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  Contains the Currency.CurrencyCode value of the customer's base currency.  */  
   CurrencyCode:string,
      /**  Contains the Country.CountryNum value of the country the customer is located in.  */  
   CountryNum:number,
      /**  Contains the LangName.LangNameID value of the customer's language. This controls which language will be selected when extracting part descriptions from PartLangDesc table and report labels for customer related forms such as orders, packing slips and invoices.  */  
   LangNameID:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   BTName:string,
      /**  The first line of the customer's Bill To address.  */  
   BTAddress1:string,
      /**  The second line of the customer's Bill To address.  */  
   BTAddress2:string,
      /**  The second line of the customer's Bill To address.  */  
   BTAddress3:string,
      /**  The city portion of the customer's Bill To address.  */  
   BTCity:string,
      /**  The state or province portion of the customer's Bill To address.  */  
   BTState:string,
      /**  The zip or postal code portion of the customer's Bill To address.  */  
   BTZip:string,
      /**  The Country.Countrynum value of the Country portion of the customer's Bill To address.  */  
   BTCountryNum:number,
      /**  Contains the Country.Description value of the Country portion of the customer's Bill To address.  */  
   BTCountry:string,
      /**  The phone number related to the customer's Bill To Address.  */  
   BTPhoneNum:string,
      /**  The fax number of the customer's Bill To address.  */  
   BTFaxNum:string,
      /**  The day of the month that service contracts for the customer marked for recurring invoicing are billed on.  If the invoice group's invoice date is greater than or equal to this date then the invoice will be generated.  */  
   ContBillDay:number,
      /**  Default email address for the customer.  */  
   EMailAddress:string,
      /**  Used to define the type of the customer record.  */  
   CustomerType:string,
      /**  The Customer's website URL.  */  
   CustURL:string,
      /**  BillFrequency  */  
   BillFrequency:string,
      /**  Specifies the current customer can be an alternate bill to customer.  */  
   AllowAltBillTo:boolean,
      /**  Sold to customer in the AR Invoice Entry. The user will not be able to enter invoices for customers without this authorization  */  
   ValidSoldTo:boolean,
      /**  Receive shipments for orders entered in OE. Unless the user selects this option, the user must enter a Ship-to address in the Order Entry form.  */  
   ValidShipTo:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Determines if the customer has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   IntRunChangeCountry:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMCustomerTableset{
   IntQueInOut:Erp_Tablesets_IntQueInOutRow[],
   IMCustBillTo:Erp_Tablesets_IMCustBillToRow[],
   IMCustCnt:Erp_Tablesets_IMCustCntRow[],
   IMCustomer:Erp_Tablesets_IMCustomerRow[],
   IMShipTo:Erp_Tablesets_IMShipToRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMIntegrationKeyRow{
      /**  The master file which the integration is related to.  */  
   TableName:string,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMIntegrationKeyTableset{
   IMIntegrationKey:Erp_Tablesets_IMIntegrationKeyRow[],
   IMNaturalKeys:Erp_Tablesets_IMNaturalKeysRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMNaturalKeysRow{
   KeyValue:string,
   KeyColumn:string,
   Sequence:number,
   PrimaryKey:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMShipToRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the record is related to.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  */  
   Name:string,
      /**  The first line of the ShipTo address.  */  
   Address1:string,
      /**  The second line of the ShipTo address.  */  
   Address2:string,
      /**  The third line of the ShipTo address.  */  
   Address3:string,
      /**  The city portion of the ShipTo address.  */  
   City:string,
      /**  The state or province portion of the ShipTo address.  */  
   State:string,
      /**  The zip or postal code portion of the ShipTo address.  */  
   ZIP:string,
      /**  The country portion of the ShipTo address.  */  
   Country:string,
      /**  The SalesTer.TerritoryID value of the territory the customer is assigned to.  */  
   TerritoryID:string,
      /**  The ShipVia.ShipViaCode value of the default ShipVia assigned to the customer. Used as a default in Order Entry, Shipping and Invoicing.  The shipvia from the customer record for this shipto is used as the initial default when creating new ShipTo records.  */  
   ShipViaCode:string,
      /**  The business phone number for the ShipTo location. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  */  
   PhoneNum:string,
      /**  The Country.CountryNum value of the country selected in the ShipTo.Country field.  */  
   CountryNum:number,
      /**  Contains the TaxRgn.TaxRegionCode value of the customer's tax region for purposes of Sales Tax calculations.  */  
   TaxRegionCode:string,
      /**  The email address of the ShipTo location.  */  
   EMailAddress:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
      /**  Unique identifier of related integration record.  The value is a GUID.  */  
   ExternalKey:string,
      /**  Unique identifier of row in actual table  */  
   IntSysRowID:string,
      /**  Flag used for integrations whether to run the on change country logic.  */  
   IntRunChangeCountry:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IntQueInOutRow{
      /**  The unique key from IntQueIn or IntQueOut  */  
   IntQueID:number,
      /**  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  */  
   Action:string,
      /**  "I" for incoming or "O" for outgoing  */  
   IncomingOutgoing:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetAllCustomer_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetAllCustomer_output{
   returnObj:Erp_Tablesets_IMCustomerTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
      @param pageSize
      @param absolutePage
   */  
export interface GetCustomer_input{
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
      /**  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  */  
   pageSize:number,
      /**  Optional. If this is greater than one it will skip to this page when returning data.  */  
   absolutePage:number,
}

export interface GetCustomer_output{
   returnObj:Erp_Tablesets_IMCustomerTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

   /** Required : 
      @param IMCustomerTableset
      @param company
      @param extSystemID
      @param transferMethod
      @param extCompanyID
   */  
export interface UpdateCustomer_input{
   IMCustomerTableset:Erp_Tablesets_IMCustomerTableset[],
   company:string,
   extSystemID:string,
   transferMethod:string,
   extCompanyID:string,
}

export interface UpdateCustomer_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   errorsOccurred:boolean,
}
}

