import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PriceListInquirySvc
// Description: Price List Inquiry contains tables of price breaks for price lists based on parts.
The records of those tables  represent an "at least this quantity"
which needs to be ordered to kick in the corresponding discount percent
or unit price.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/$metadata", {
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
   Summary: Invoke method ChangeCustID
   Description: Get filter values from the Customer.
   OperationID: ChangeCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCustID(requestBody:ChangeCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ChangeCustID", {
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
         resolve(data as ChangeCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDiscountPercent
   Description: Update NetPrice when the discount percent changes.
   OperationID: ChangeDiscountPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDiscountPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDiscountPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDiscountPercent(requestBody:ChangeDiscountPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDiscountPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ChangeDiscountPercent", {
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
         resolve(data as ChangeDiscountPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: Get filter values from the Part.
   OperationID: ChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:ChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ChangePartNum", {
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
         resolve(data as ChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeShipToNum
   Description: Get filter values from the ShipTo.
   OperationID: ChangeShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeShipToNum(requestBody:ChangeShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ChangeShipToNum", {
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
         resolve(data as ChangeShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCurrencyByCustID
   Description: Get currency values from the Customer.
   OperationID: GetCurrencyByCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCurrencyByCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyByCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCurrencyByCustID(requestBody:GetCurrencyByCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCurrencyByCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/GetCurrencyByCustID", {
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
         resolve(data as GetCurrencyByCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:GetPartXRefInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartXRefInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/GetPartXRefInfo", {
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
         resolve(data as GetPartXRefInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceListInquiry
   Description: Get the PriceListInquiry records for the inquiry parameters.
   OperationID: GetPriceListInquiry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPriceListInquiry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInquiry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceListInquiry(requestBody:GetPriceListInquiry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPriceListInquiry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/GetPriceListInquiry", {
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
         resolve(data as GetPriceListInquiry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidUOM(requestBody:ValidUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ValidUOM", {
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
         resolve(data as ValidUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/FindPart", {
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
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/GetPartFromRowID", {
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
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ColumnChangingCustID
   Description: Called when Customer ID changes.  Returns default values for the customer.
   OperationID: ColumnChangingCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ColumnChangingCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnChangingCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ColumnChangingCustID(requestBody:ColumnChangingCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ColumnChangingCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ColumnChangingCustID", {
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
         resolve(data as ColumnChangingCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ColumnChangingShipToNum
   Description: Called when Ship To Num changes.  Returns default values for the ship To.
   OperationID: ColumnChangingShipToNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ColumnChangingShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnChangingShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ColumnChangingShipToNum(requestBody:ColumnChangingShipToNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ColumnChangingShipToNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/ColumnChangingShipToNum", {
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
         resolve(data as ColumnChangingShipToNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPriceListInquiryCriteriaDefaults
   Description: Assigns default values for Price List Inquiry criteria
   OperationID: GetPriceListInquiryCriteriaDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPriceListInquiryCriteriaDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceListInquiryCriteriaDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPriceListInquiryCriteriaDefaults(requestBody:GetPriceListInquiryCriteriaDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPriceListInquiryCriteriaDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PriceListInquirySvc/GetPriceListInquiryCriteriaDefaults", {
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
         resolve(data as GetPriceListInquiryCriteriaDefaults_output)
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
   /** Required : 
      @param cCustID
   */  
export interface ChangeCustID_input{
      /**  The Customer ID  */  
   cCustID:string,
}

export interface ChangeCustID_output{
parameters : {
      /**  output parameters  */  
   cCustName:string,
   cShipToNum:string,
   cCustGroupCode:string,
   dDiscountPercent:number,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeDiscountPercent_input{
   ds:Erp_Tablesets_PriceListInquiryTableset[],
}

export interface ChangeDiscountPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceListInquiryTableset,
}
}

   /** Required : 
      @param cPartNum
   */  
export interface ChangePartNum_input{
      /**  The part number  */  
   cPartNum:string,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   cProdCode:string,
   cPartDesc:string,
}
}

   /** Required : 
      @param cCustID
      @param cShipToNum
   */  
export interface ChangeShipToNum_input{
      /**  The Customer ID  */  
   cCustID:string,
      /**  The Ship To Number  */  
   cShipToNum:string,
}

export interface ChangeShipToNum_output{
parameters : {
      /**  output parameters  */  
   cCustName:string,
}
}

   /** Required : 
      @param custID
   */  
export interface ColumnChangingCustID_input{
      /**  Customer ID  */  
   custID:string,
}

export interface ColumnChangingCustID_output{
parameters : {
      /**  output parameters  */  
   custNum:number,
   customerName:string,
   groupCode:string,
   currencyCode:string,
}
}

   /** Required : 
      @param custID
      @param shipToNum
   */  
export interface ColumnChangingShipToNum_input{
   custID:string,
   shipToNum:string,
}

export interface ColumnChangingShipToNum_output{
parameters : {
      /**  output parameters  */  
   customerName:string,
}
}

export interface Erp_Tablesets_PLGrupBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique set of characters entered by the user to identify the Price List master within the company.  */  
   ListCode:string,
      /**  Descriptive code assigned by the user to uniquely identify a Product Group master.  */  
   ProdCode:string,
      /**  The price break quantity  */  
   Quantity:number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   DiscountPercent:number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity.  */  
   UnitPrice:number,
      /**   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PLGrupBrk as global, available to be sent out to other companies.  */  
   GlobalPLGrupBrk:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of radio button (P or D)  */  
   RadioButtonValue:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   ProdCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PLPartBrkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Unique set of characters entered by the user to identify
the Price List master within the company.  */  
   ListCode:string,
      /**  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  */  
   PartNum:string,
      /**  The price break quantity  */  
   Quantity:number,
      /**  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  */  
   DiscountPercent:number,
      /**  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  */  
   UnitPrice:number,
      /**   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PLPartBrk as global, available to be sent out to other companies.  */  
   GlobalPLPartBrk:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of radio button. (D or P)  */  
   RadioButtonValue:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumTrackDimension:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceListInquiryCriteriaRow{
   Company:string,
   CurrencyCode:string,
   CustID:string,
   CustNum:number,
   GroupCode:string,
   PartDescription:string,
   PartNum:string,
   ProdCode:string,
   Quantity:number,
      /**  Retrieve for (C)ustomer or Customer (G)roup  */  
   SelectCustomer:string,
      /**  Retrieve for (P)art or Product (G)roup  */  
   SelectPart:string,
   ShipToName:string,
   ShipToNum:string,
   UOMCode:string,
   Warehouse:string,
   PartTrackDimension:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceListInquiryCriteriaTableset{
   PriceListInquiryCriteria:Erp_Tablesets_PriceListInquiryCriteriaRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PriceListInquiryRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of the price list assigned by the user.  */  
   ListCode:string,
      /**  Currency.CurrencyCode of the currency assigned to the price list.  */  
   CurrencyCode:string,
      /**  Description of the price list.  */  
   ListDescription:string,
      /**  Date the price list become effective.  */  
   StartDate:string,
      /**  Date that the price list expires on.  */  
   EndDate:string,
      /**  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  */  
   WarehouseList:string,
      /**  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  */  
   ListType:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BasePriceList:string,
   QuantityBreakList:string,
   DiscountPercent:number,
   BasePrice:number,
   BreakPrice:number,
   NetPrice:number,
   Warehouse:string,
   Quantity:number,
   UOMCode:string,
      /**  Discount List code selected for the inquiry selection  */  
   DiscountListCode:string,
      /**  Part Unit Price saved from Part master record  */  
   PartUnitPrice:number,
      /**  Value to store the discount amount for the selected price list  */  
   DiscountAmt:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceListInquiryTableset{
   PriceListInquiry:Erp_Tablesets_PriceListInquiryRow[],
   PriceLstGroups:Erp_Tablesets_PriceLstGroupsRow[],
   PLGrupBrk:Erp_Tablesets_PLGrupBrkRow[],
   PriceLstParts:Erp_Tablesets_PriceLstPartsRow[],
   PLPartBrk:Erp_Tablesets_PLPartBrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PriceLstGroupsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   ListCode:string,
      /**  ProdGrup.ProdCode value of the Product Group that this record is related to.  */  
   ProdCode:string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   BasePrice:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent1:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent2:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent3:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent4:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent5:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak1:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak2:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak3:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak4:number,
      /**  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  */  
   QtyBreak5:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice1:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice2:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice3:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice4:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice5:number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   CommentText:string,
      /**   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PriceLstGroups as global, available to be sent out to other companies.  */  
   GlobalPriceLstGroups:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Product group description  */  
   ProdGrpDescription:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   BitFlag:number,
   ListCodeListDescription:string,
   ProdCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PriceLstPartsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  PriceLst.ListCode value of the price list that this record is related to.  */  
   ListCode:string,
      /**  Part.PartNum value of the Part that this record is related to.  */  
   PartNum:string,
      /**  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  */  
   BasePrice:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent1:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent2:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent3:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent4:number,
      /**  Contains the Discount Percent that is to be given for a corresponding price break quantity.  */  
   DiscountPercent5:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak1:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak2:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak3:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak4:number,
      /**  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  */  
   QtyBreak5:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice1:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice2:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice3:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice4:number,
      /**  Contains a flat unit price that is to be given for the corresponding price break quantity.  */  
   UnitPrice5:number,
      /**  Additional comments that will be used as a default for customer price lists.  */  
   CommentText:string,
      /**   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  */  
   UOMCode:string,
      /**  Marks this PriceLstParts as global, available to be sent out to other companies.  */  
   GlobalPriceLstParts:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Part sales unit of measure  */  
   PartSalesUM:string,
      /**  Part selling factor  */  
   PartSellingFactor:number,
      /**  Part price per code  */  
   PartPricePerCode:string,
      /**  Part description  */  
   PartDescription:string,
   SellingFactorDirection:string,
      /**  Currency Code  */  
   CurrencyCode:string,
   CurrencyCodeCurrSymbol:string,
   BitFlag:number,
   ListCodeListDescription:string,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

   /** Required : 
      @param cCustID
   */  
export interface GetCurrencyByCustID_input{
      /**  The Customer ID  */  
   cCustID:string,
}

export interface GetCurrencyByCustID_output{
parameters : {
      /**  output parameters  */  
   cCurrencyCode:string,
   cCurrencyCurrDesc:string,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param custNum
      @param SysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  Customer number  */  
   custNum:number,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetPriceListInquiryCriteriaDefaults_input{
   ds:Erp_Tablesets_PriceListInquiryCriteriaTableset[],
}

export interface GetPriceListInquiryCriteriaDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PriceListInquiryCriteriaTableset,
}
}

   /** Required : 
      @param icCustID
      @param icShipToNum
      @param icPartNum
      @param icCustGroupCode
      @param icProductCode
      @param idQuantity
      @param icUOMCode
      @param icWarehouseCode
      @param icCurrencyCode
      @param pageSize
      @param absolutePage
   */  
export interface GetPriceListInquiry_input{
      /**  The Customer ID  */  
   icCustID:string,
      /**  The Part Number  */  
   icShipToNum:string,
      /**  The Ship To Number  */  
   icPartNum:string,
      /**  The Customer Group Code  */  
   icCustGroupCode:string,
      /**  The Product Code  */  
   icProductCode:string,
      /**  The Quantity  */  
   idQuantity:number,
      /**  The UOM Code  */  
   icUOMCode:string,
      /**  The Warehouse Code  */  
   icWarehouseCode:string,
      /**  The Currency Code  */  
   icCurrencyCode:string,
      /**  The pageSize parameter  */  
   pageSize:number,
      /**  The absolutePages parameter  */  
   absolutePage:number,
}

export interface GetPriceListInquiry_output{
   returnObj:Erp_Tablesets_PriceListInquiryTableset[],
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

   /** Required : 
      @param prodGroup
      @param iPartNum
      @param iUOM
   */  
export interface ValidUOM_input{
   prodGroup:string,
   iPartNum:string,
   iUOM:string,
}

export interface ValidUOM_output{
   returnObj:boolean,
}

