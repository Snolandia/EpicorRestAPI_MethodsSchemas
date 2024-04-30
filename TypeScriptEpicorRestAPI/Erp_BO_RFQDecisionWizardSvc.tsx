import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.RFQDecisionWizardSvc
// Description: The Decision Wizard from Buyer Workbench.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/$metadata", {
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
   Summary: Invoke method Accept
   Description: This method will do the following (text from 6.1 procedure):
Find Related JobMtl/JobOper/QuoteMtl/QuoteOpr (must be avail), and update estunitcost.
Note, if related to Job, the JobMtl write trigger was changed to fire off and create a POSuggestion -
like it should have done when you marked it "Purchase/direct" but we changed it so that if you flag
RFQNeeded also, would create an RFQSuggestion INSTEAD of a POSuggestion.
Once the RFQ has been created and vendor responds, the trigger will create a POSuggestion.
Set rest of vendor responses for this rfq to status = NO,
close rfqLine/item
   OperationID: Accept
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Accept_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Accept_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Accept(requestBody:Accept_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Accept_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/Accept", {
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
         resolve(data as Accept_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Apply
   Description: This method will create the RFQReadyVend records associated with the RFQFilterDW
record and the selected filter and sort options.
   OperationID: Apply
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Apply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Apply_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Apply(requestBody:Apply_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Apply_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/Apply", {
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
         resolve(data as Apply_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBeforeCreatePO
   Description: Asks user before create the PO for a Quoted Item
   OperationID: CheckBeforeCreatePO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBeforeCreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeCreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforeCreatePO(requestBody:CheckBeforeCreatePO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBeforeCreatePO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/CheckBeforeCreatePO", {
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
         resolve(data as CheckBeforeCreatePO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreatePO
   Description: This method create the purchase order for this rfqitem.
   OperationID: CreatePO
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreatePO(requestBody:CreatePO_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreatePO_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/CreatePO", {
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
         resolve(data as CreatePO_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetHeaderRecord
   Description: This method will create a RFQFilterDW record with information from the RFQ and
populate the attributes to include/exclude and sort options.  The record created
here will then be used for the Apply method to generate the RFQReadyVend records.
Run this as the first method.
   OperationID: GetHeaderRecord
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetHeaderRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHeaderRecord(requestBody:GetHeaderRecord_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetHeaderRecord_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/GetHeaderRecord", {
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
         resolve(data as GetHeaderRecord_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLineQty
   Description: This method gets the Job Qty (if job related) and sets a flag to tell the UI
to update the Qty, duedate and promise date fields.
Run this before CreatePO.
   OperationID: GetLineQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLineQty(requestBody:GetLineQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLineQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/GetLineQty", {
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
         resolve(data as GetLineQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreAccept
   Description: This method will potentially produce a message that will provide the user with
a choice of continuing with the Accept.  Call this before the Accept method and
then pass into the Accept method the logical choice from the user's response
to the potential message from this method.
   OperationID: PreAccept
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreAccept_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreAccept_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreAccept(requestBody:PreAccept_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreAccept_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.RFQDecisionWizardSvc/PreAccept", {
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
         resolve(data as PreAccept_output)
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
      @param ipRFQNum
      @param ipRFQLine
      @param ipVendorNum
      @param ipPurPoint
      @param ipAnswer
      @param ds
   */  
export interface Accept_input{
      /**  The rfq number to accept for.  */  
   ipRFQNum:number,
      /**  The rfq line number to accept for.  */  
   ipRFQLine:number,
      /**  The vendor num to accept for.  */  
   ipVendorNum:number,
      /**  The purchase point to accept for.  */  
   ipPurPoint:string,
      /**  The user answer to PreAccept potential message.  */  
   ipAnswer:boolean,
   ds:Erp_Tablesets_RFQDecisionWizardTableset[],
}

export interface Accept_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQDecisionWizardTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Apply_input{
   ds:Erp_Tablesets_RFQDecisionWizardTableset[],
}

export interface Apply_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RFQDecisionWizardTableset,
}
}

   /** Required : 
      @param iQuoteNum
   */  
export interface CheckBeforeCreatePO_input{
      /**  Quote Number on RFQItem. Can be zero  */  
   iQuoteNum:number,
}

export interface CheckBeforeCreatePO_output{
parameters : {
      /**  output parameters  */  
   oMsg:string,
}
}

   /** Required : 
      @param ipRFQNum
      @param ipRFQLine
      @param ipVendorNum
      @param ipPurPoint
      @param ipLineQty
      @param ipDueDate
      @param ipPromiseDate
      @param ds
   */  
export interface CreatePO_input{
      /**  The rfq number to create po for.  */  
   ipRFQNum:number,
      /**  The rfq line number to create po for.  */  
   ipRFQLine:number,
      /**  The vendor num to create po for.  */  
   ipVendorNum:number,
      /**  The purchase point to create po for.  */  
   ipPurPoint:string,
      /**  The line quantity.  */  
   ipLineQty:number,
      /**  The due date.  */  
   ipDueDate:string,
      /**  The promise date.  */  
   ipPromiseDate:string,
   ds:Erp_Tablesets_RFQDecisionWizardTableset[],
}

export interface CreatePO_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
   ds:Erp_Tablesets_RFQDecisionWizardTableset,
}
}

export interface Erp_Tablesets_RFQDecisionWizardTableset{
   RFQFilterDW:Erp_Tablesets_RFQFilterDWRow[],
   RFQReadyVend:Erp_Tablesets_RFQReadyVendRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RFQFilterDWRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  The rfq line number.  */  
   RFQLine:number,
      /**  The attribute list of options to include or exclude.  */  
   AttributeList:string,
      /**  The list of attributes to include.  */  
   IncludeList:string,
      /**  The list of attributes to exclude.  */  
   ExcludeList:string,
      /**  The quantity field.  */  
   Quantity:number,
      /**  The required quantity.  */  
   RequiredQty:number,
      /**  The part number.  */  
   PartNum:string,
      /**  The description for the part number.  */  
   PartDescription:string,
      /**  The list of available sort choices.  */  
   AvailSortChoices:string,
      /**  The selected sort choices.  */  
   SelectedSortChoices:string,
      /**  Compliance List that Vendor must accomplish in order to be retrieved  */  
   ComplianceList:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  OUR revision number of the OUR part.  An optional field. Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RFQReadyVendRow{
      /**  The company identifier.  */  
   Company:string,
      /**  The vendor id.  */  
   VendorID:string,
      /**  The vendor number.  */  
   VendorNum:number,
      /**  The on time rating.  */  
   OnTimeRating:string,
      /**  The vendor name  */  
   VendName:string,
      /**  The service rating.  */  
   ServiceRating:string,
      /**  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  */  
   PriceRating:string,
      /**  The quality rating.  */  
   QualityRating:string,
      /**  The lead time.  */  
   LeadTime:number,
      /**  The break quantity.  */  
   BreakQty:number,
      /**  The price.  */  
   Price:number,
      /**  The on hand quantity.  */  
   OnHandQty:number,
      /**  The on hand date.  */  
   OnHandDate:string,
      /**  The purchase point.  */  
   PurPoint:string,
      /**  The response.  */  
   Response:string,
      /**  The rfq number.  */  
   RFQNum:number,
      /**  The rfq line number.  */  
   RFQLine:number,
      /**  Enable Create PO button?  */  
   EnableCreatePO:boolean,
      /**  Enable Accept button?  */  
   EnableAccept:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ipRFQNum
      @param ipRFQLine
   */  
export interface GetHeaderRecord_input{
      /**  The rfq number to get data for.  */  
   ipRFQNum:number,
      /**  The rfq line number to get data for.  */  
   ipRFQLine:number,
}

export interface GetHeaderRecord_output{
   returnObj:Erp_Tablesets_RFQDecisionWizardTableset[],
}

   /** Required : 
      @param ipRFQNum
      @param ipRFQLine
      @param ipVendorNum
      @param ipPurPoint
   */  
export interface GetLineQty_input{
      /**  RFQ Number  */  
   ipRFQNum:number,
      /**  RFQ Line Number  */  
   ipRFQLine:number,
      /**  Vendor Number  */  
   ipVendorNum:number,
      /**  Vendor Purchase Point  */  
   ipPurPoint:string,
}

export interface GetLineQty_output{
parameters : {
      /**  output parameters  */  
   opTmpLineQty:string,
   opPromptQty:boolean,
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
      @param ipRFQNum
      @param ipRFQLine
      @param ipVendorNum
      @param ipPurPoint
   */  
export interface PreAccept_input{
      /**  The rfq number to validate for.  */  
   ipRFQNum:number,
      /**  The rfq line number to validate for.  */  
   ipRFQLine:number,
      /**  The vendor num to validate for.  */  
   ipVendorNum:number,
      /**  The purchase point to validate for.  */  
   ipPurPoint:string,
}

export interface PreAccept_output{
parameters : {
      /**  output parameters  */  
   opStatusMsg:string,
}
}

