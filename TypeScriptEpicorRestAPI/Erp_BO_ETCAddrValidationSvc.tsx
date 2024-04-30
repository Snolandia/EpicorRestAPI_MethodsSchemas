import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ETCAddrValidationSvc
// Description: 
// Version: v1
*/ 



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Invoke method Getit
   Description: Called when the user chooses a new valid address.
   OperationID: Getit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Getit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Getit(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Getit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/Getit", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Getit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofValidAddr
   Description: Called when the user chooses a new valid address.
   OperationID: OnChangeofValidAddr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofValidAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofValidAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofValidAddr(requestBody:OnChangeofValidAddr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofValidAddr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/OnChangeofValidAddr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofValidAddr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofAddr
   Description: Called when the user changes the address.
   OperationID: OnChangeofAddr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofAddr(requestBody:OnChangeofAddr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofAddr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/OnChangeofAddr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofAddr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetAddr
   Description: Purpose:
Parameters:  none
Notes:
<param name="RequestID">RequestID</param><param name="ds">ETCAddrValidation data set</param>
   OperationID: SetAddr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAddr(requestBody:SetAddr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetAddr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ETCAddrValidationSvc/SetAddr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetAddr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Erp_Tablesets_ETCAddrValidationTableset{
   ETCAddress:Erp_Tablesets_ETCAddressRow[],
   ETCMessage:Erp_Tablesets_ETCMessageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ETCAddressRow{
      /**  Company  */  
   Company:string,
      /**  City name  */  
   City:string,
      /**  Country name  */  
   Country:string,
      /**  Address line 1  */  
   Line1:string,
      /**  Address line 2  */  
   Line2:string,
      /**  Address line 3  */  
   Line3:string,
      /**  Postal or ZIP code  */  
   PostalCode:string,
      /**  State or province name  */  
   Region:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  */  
   UpdateAddr:boolean,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  */  
   TransactionID:string,
      /**  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  */  
   UpdateAllowed:boolean,
      /**  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  */  
   RequestID:string,
      /**  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  */  
   AddressCode:string,
      /**  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  */  
   AddressType:string,
      /**  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  */  
   CarrierRoute:string,
      /**  City name  */  
   ValidCity:string,
      /**  Country name  */  
   ValidCountry:string,
      /**  County name  */  
   County:string,
      /**  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  */  
   FipsCode:string,
      /**  Line one of the valid address returned by the tax integration.  */  
   ValidLine1:string,
      /**  Line two of the valid address returned by the tax integration.  */  
   ValidLine2:string,
      /**  Line three of the valid address returned by the tax integration.  */  
   ValidLine3:string,
      /**  Line four of the valid address returned by the tax integration.  */  
   ValidLine4:string,
      /**  Postal code returned by the tax integration.  */  
   ValidPostalCode:string,
      /**  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  */  
   PostNet:string,
      /**  State or province name or abbreviation returned by the tax integration.  */  
   ValidRegion:string,
      /**  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  */  
   ResultSeq:number,
      /**  Carrier Route description  */  
   CarrierRouteDesc:string,
      /**  Address type description  */  
   AddressTypeDesc:string,
   OTSCountry:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  */  
   ACWPercentage:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ETCMessageRow{
      /**  Company  */  
   Company:string,
   Details:string,
      /**  URL to help page for this message  */  
   Helplink:string,
      /**  Gets the name of the message  */  
   Name:string,
      /**  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  */  
   RefersTo:string,
      /**  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   Severity:string,
      /**  source of the message  */  
   Source:string,
      /**  concise summary of the message  */  
   Summary:string,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  */  
   TransactionID:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  Programitically assigned.  */  
   RequestID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Getit_output{
   returnObj:Erp_Tablesets_ETCAddrValidationTableset[],
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
      @param RequestID
      @param ds
   */  
export interface OnChangeofAddr_input{
      /**  RequestID  */  
   RequestID:string,
   ds:Erp_Tablesets_ETCAddrValidationTableset[],
}

export interface OnChangeofAddr_output{
parameters : {
      /**  output parameters  */  
   StatusFlag:boolean,
   ErrorFlag:boolean,
   ErrorMsg:string,
   ds:Erp_Tablesets_ETCAddrValidationTableset,
}
}

   /** Required : 
      @param RequestID
      @param ds
   */  
export interface OnChangeofValidAddr_input{
      /**  RequestID  */  
   RequestID:string,
   ds:Erp_Tablesets_ETCAddrValidationTableset[],
}

export interface OnChangeofValidAddr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ETCAddrValidationTableset,
}
}

   /** Required : 
      @param RequestID
      @param ds
   */  
export interface SetAddr_input{
   RequestID:string,
   ds:Erp_Tablesets_ETCAddrValidationTableset[],
}

export interface SetAddr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ETCAddrValidationTableset,
}
}

