import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ARAgingTrackerSvc
// Description: ARAgingTracker.
           AR Aging for Trackers.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/$metadata", {
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
   Summary: Invoke method GenerateTrackerForECC
   Description: This method should be called to populate the dataset for the AR Aging Tracker for ECC.
   OperationID: GenerateTrackerForECC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateTrackerForECC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTrackerForECC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTrackerForECC(requestBody:GenerateTrackerForECC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateTrackerForECC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GenerateTrackerForECC", {
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
         resolve(data as GenerateTrackerForECC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateReport
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GenerateReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateReport(requestBody:GenerateReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GenerateReport", {
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
         resolve(data as GenerateReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateTracker
   Description: This method should be called to populate the dataset for the AR Aging Tracker.
   OperationID: GenerateTracker
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateTracker(requestBody:GenerateTracker_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateTracker_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GenerateTracker", {
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
         resolve(data as GenerateTracker_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAgeBy
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GetAgeBy
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgeBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAgeBy(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAgeBy_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetAgeBy", {
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
         resolve(data as GetAgeBy_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAgingFormatCode
   Description: This method returns a list of valid 'AgingFormatCode' codes
UI note - user should  select only ONE of the valid codes.
   OperationID: GetAgingFormatCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAgingFormatCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAgingFormatCode(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAgingFormatCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetAgingFormatCode", {
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
         resolve(data as GetAgingFormatCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARAccounts
   Description: This method returns a list of ARAccounts and descriptions
   OperationID: GetARAccounts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARAccounts(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetARAccounts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetARAccounts", {
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
         resolve(data as GetARAccounts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParams
   Description: This method should be called after all the input parameters have been entered.
It will generate a dataset containing records for the AR Aging report used
by a tracker.
   OperationID: GetNewParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewParams(requestBody:GetNewParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetNewParams", {
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
         resolve(data as GetNewParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectBy
   Description: This method returns a select by list.
   OperationID: GetSelectBy
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectBy(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectBy_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetSelectBy", {
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
         resolve(data as GetSelectBy_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSortByList
   Description: This method returns a sort by list.
   OperationID: GetSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/GetSortByList", {
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
         resolve(data as GetSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Killtask
   OperationID: Killtask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Killtask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Killtask(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Killtask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/Killtask", {
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
         resolve(data as Killtask_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DumpARDtls
   OperationID: DumpARDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DumpARDtls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DumpARDtls(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DumpARDtls_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/DumpARDtls", {
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
         resolve(data as DumpARDtls_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DumpARPrnt
   OperationID: DumpARPrnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DumpARPrnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DumpARPrnt(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DumpARPrnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ARAgingTrackerSvc/DumpARPrnt", {
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
         resolve(data as DumpARPrnt_output)
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
export interface DumpARDtls_output{
}

export interface DumpARPrnt_output{
}

export interface Erp_Tablesets_ARAgedRecReportParamRow{
   SelectBy:string,
   AgeBy:string,
   AgingDate:string,
   AgingDateToken:string,
   ARAccounts:string,
   CustList:string,
   SummaryOnly:boolean,
   AgingFormatCode:string,
   SortBy:string,
      /**  B) for sorting detail by bill to customer and S) for sort by sold to.  */  
   CustType:string,
   CurrDesc:string,
   CurrencyCode:string,
   GLControlCodeList:string,
   GLControlType:string,
   GLControlTypeDesc:string,
      /**  Sort by GL Control Type  */  
   SortGLControlType:string,
      /**  SortGLControlTypeDesc  */  
   SortGLControlTypeDesc:string,
   FiscalYear:number,
   FiscalYearSuffix:string,
   FiscalPeriod:number,
   PrintSelCriteria:boolean,
      /**  Allow printing of legal numbers  */  
   PrintLegNum:boolean,
   SortByDesc:string,
      /**  Allow printing of payment instruments  */  
   PrintPromissoryNote:boolean,
   CustListID:string,
   SysRowID:string,
   AutoAction:string,
   PrinterName:string,
   AgentSchedNum:number,
   AgentID:string,
   AgentTaskNum:number,
   RecurringTask:boolean,
   RptPageSettings:string,
   RptPrinterSettings:string,
   RptVersion:string,
   ReportStyleNum:number,
   WorkstationID:string,
   TaskNote:string,
   ArchiveCode:number,
   DateFormat:string,
   NumericFormat:string,
   AgentCompareString:string,
   ProcessID:string,
   ProcessCompany:string,
   ProcessSystemCode:string,
   ProcessTaskNum:number,
   DecimalsGeneral:number,
   DecimalsCost:number,
   DecimalsPrice:number,
   GlbDecimalsGeneral:number,
   GlbDecimalsCost:number,
   GlbDecimalsPrice:number,
   FaxSubject:string,
   FaxTo:string,
   FaxNumber:string,
   EMailTo:string,
   EMailCC:string,
   EMailBCC:string,
   EMailBody:string,
   AttachmentType:string,
   ReportCurrencyCode:string,
   ReportCultureCode:string,
   SSRSRenderFormat:string,
   UIXml:string,
   PrintReportParameters:boolean,
   SSRSEnableRouting:boolean,
   DesignMode:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARDtlsRow{
      /**  Company  */  
   Company:string,
      /**  AgeBaseAll  */  
   AgeBaseAll:number,
      /**  AgeCurAll  */  
   AgeCurAll:number,
      /**  AgeCurTotal1  */  
   AgeCurTotal1:number,
      /**  AgeCurTotal2  */  
   AgeCurTotal2:number,
      /**  AgeCurTotal3  */  
   AgeCurTotal3:number,
      /**  AgeCurTotal4  */  
   AgeCurTotal4:number,
      /**  AgeCurTotal5  */  
   AgeCurTotal5:number,
      /**  AgeCurTotal6  */  
   AgeCurTotal6:number,
      /**  AgeInvAmt1  */  
   AgeInvAmt1:number,
      /**  AgeInvAmt2  */  
   AgeInvAmt2:number,
      /**  AgeInvAmt3  */  
   AgeInvAmt3:number,
      /**  AgeInvAmt4  */  
   AgeInvAmt4:number,
      /**  AgeInvAmt5  */  
   AgeInvAmt5:number,
      /**  AgeInvAmt6  */  
   AgeInvAmt6:number,
      /**  AgeLbl1  */  
   AgeLbl1:string,
      /**  AgeLbl2  */  
   AgeLbl2:string,
      /**  AgeLbl3  */  
   AgeLbl3:string,
      /**  AgeLbl4  */  
   AgeLbl4:string,
      /**  AgeLbl5  */  
   AgeLbl5:string,
      /**  AgeLbl6  */  
   AgeLbl6:string,
      /**  AgeParentAll  */  
   AgeParentAll:number,
      /**  AgeParentTotal1  */  
   AgeParentTotal1:number,
      /**  AgeParentTotal2  */  
   AgeParentTotal2:number,
      /**  AgeParentTotal3  */  
   AgeParentTotal3:number,
      /**  AgeParentTotal4  */  
   AgeParentTotal4:number,
      /**  AgeParentTotal5  */  
   AgeParentTotal5:number,
      /**  AgeParentTotal6  */  
   AgeParentTotal6:number,
      /**  Contact Person  */  
   ContPer:string,
      /**  Phone  */  
   ContPh:string,
      /**  crMemo  */  
   crMemo:string,
      /**  Currency  */  
   curDesc:string,
      /**  CurDueDate  */  
   CurDueDate:string,
      /**  CurrCode  */  
   CurrCode:string,
      /**  Customer  */  
   CustID:string,
      /**  CustName Parent:  */  
   CustName:string,
      /**  DispCurTot  */  
   DispCurTot:boolean,
      /**  ParentCustID  */  
   ParentCustID:string,
      /**  A/R Account  */  
   RptARAcctID:string,
      /**  RptUserID  */  
   RptUserID:string,
      /**  SInvcNum  */  
   SInvcNum:string,
   InvoiceNum:number,
   PONum:string,
   InvoiceDate:string,
   CreditMemo:boolean,
      /**  For Debit Note type invoices this is Debit Note number assigned by the customer, for regular invoice this field is PO number  */  
   PoDnNbr:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARDtlsTableset{
   ARDtls:Erp_Tablesets_ARDtlsRow[],
   ARAgedRecReportParam:Erp_Tablesets_ARAgedRecReportParamRow[],
   ARPrnt:Erp_Tablesets_ARPrntRow[],
   Company:Erp_Tablesets_CompanyRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPrntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  RptUserID  */  
   RptUserID:string,
      /**   The ARAcct.ARAcctID value of the specific set of AR accounts that will be used by the invoice and payment transactions related to the customer. If left blank then the default AR accounts are used.
(see ARSyst.ArAcctID).  */  
   RptARAcctID:string,
      /**  A unique code that identifies the currency.  */  
   CurrCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  The full name of the customer.  */  
   CustName:string,
      /**  Summary  */  
   Summary:boolean,
      /**  Ar total1  */  
   ARTot1:number,
      /**  Ar total 2  */  
   ARTot2:number,
      /**  AR total3  */  
   ARTot3:number,
      /**  AR total4  */  
   ARTot4:number,
      /**  AR total 5  */  
   ARTot5:number,
      /**  AR total 6  */  
   ARTot6:number,
      /**  MulChildren  */  
   MulChildren:boolean,
      /**  ParentCustID  */  
   ParentCustID:string,
      /**  RptTitle1  */  
   RptTitle1:string,
      /**  RptTitle2  */  
   RptTitle2:string,
      /**  RptTitle3  */  
   RptTitle3:string,
      /**  SubTitle1  */  
   SubTitle1:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARTrackerTotRow{
      /**  Company  */  
   Company:string,
      /**  Curent number of invoices  */  
   CurNumInv:number,
      /**  Total by Invoice Date  */  
   InvTotal:number,
      /**  Paid YTD  */  
   PaidYtd:number,
      /**  Last Payment  */  
   LastPymt:number,
      /**  Last Pymt Date  */  
   LastPymtDate:string,
      /**  Number of Invoices  */  
   YTDNumInv:number,
      /**  Revenue  */  
   YTDRevenue:number,
      /**  Profit  */  
   YTDProfit:number,
      /**  Gross Margin  */  
   YTDMargin:number,
      /**  Avg Invoice Amount  */  
   YTDAvgInvAmt:number,
      /**  Avg Days to Pay  */  
   YTDAvgDaysToPay:number,
      /**  Last year number of invoices  */  
   PYTDNumInv:number,
      /**  Last year revenue  */  
   PYTDRevenue:number,
      /**  Last year profit  */  
   PYTDProfit:number,
      /**  Last year margain  */  
   PYTDMargin:number,
      /**  Last year average invoice amount  */  
   PYTDAvgInvAmt:number,
      /**  Last year average days to pay  */  
   PYTDAvgDaysToPay:number,
      /**  Current due amount  */  
   CurrDueAmt:number,
      /**  Current due percent  */  
   CurrDuePct:number,
      /**  Current invoice amount  */  
   CurrInvAmt:number,
      /**  Current invoice percent  */  
   CurrInvPct:number,
      /**  Future days due amount  */  
   FutureDueAmt:number,
      /**  Future due percent  */  
   FutureDuePct:number,
      /**  Future invoice amount  */  
   FutureInvAmt:number,
      /**  Future invoice percent  */  
   FutureInvPct:number,
      /**  Over 30 days due amount  */  
   Due30Amt:number,
      /**  Over 30 days due percent  */  
   Due30Pct:number,
      /**  Over 30 days invoice amount  */  
   Inv30Amt:number,
      /**  Over 30 days invoice percent  */  
   Inv30Pct:number,
      /**  Over 60 days due amount  */  
   Due60Amt:number,
      /**  Over 60 days due percent  */  
   Due60Pct:number,
      /**  Over 60 days invoice percent  */  
   Inv60Amt:number,
      /**  Over 60 days invoice percent  */  
   Inv60Pct:number,
      /**  90 days due amount  */  
   Due90Amt:number,
      /**  90 days due percent  */  
   Due90Pct:number,
      /**  90 days invoice amount  */  
   Inv90Amt:number,
      /**  90 days invoice percent  */  
   Inv90Pct:number,
      /**  120 days due amount  */  
   Due120Amt:number,
      /**  120 days invoice amount  */  
   Inv120Amt:number,
      /**  120 days due percent  */  
   Due120Pct:number,
      /**  120 days invoice percent  */  
   Inv120Pct:number,
      /**  Column one heading (Current)  */  
   ColHead1:string,
      /**  Column 2 heading (Over 30)  */  
   ColHead2:string,
      /**  Coumn heading 3 (Over 60)  */  
   ColHead3:string,
      /**  Coumn heading 4 (Over 90)  */  
   ColHead4:string,
      /**  Column heading 5 (Over 120)  */  
   ColHead5:string,
      /**  Coumn heading 6 (Future)  */  
   ColHead6:string,
      /**  Customer name  */  
   CustName:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Year to Date Net Invoice Total. This is the sum of all invoice type total amount including Credit Memos with exception of Unapplied Cash Receipt Invoices and Debit Notes.  */  
   YTDNetInvoiceTotal:number,
      /**  Last Year Net Invoice Total. This is the sum of all invoice type total amount including Credit Memos with exception of Unapplied Cash Receipt Invoices and Debit Notes.  */  
   PYTDNetInvoiceTotal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARTrackerTotTableset{
   ARTrackerTot:Erp_Tablesets_ARTrackerTotRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  First company address line.  */  
   Address1:string,
      /**  Second company address line.  */  
   Address2:string,
      /**  Third company address line.  */  
   Address3:string,
      /**  City portion of company address.  */  
   City:string,
      /**  State portion of company address.  */  
   State:string,
      /**  Postal code or zip code portion of company address.  */  
   Zip:string,
      /**  Country portion of company address.  */  
   Country:string,
      /**  Company phone number  */  
   PhoneNum:string,
      /**  Company fax number  */  
   FaxNum:string,
      /**  Federal Income Tax Number  */  
   FEIN:string,
      /**  State Tax ID  */  
   StateTaxID:string,
      /**  Current fiscal year  */  
   CurrentFiscalYear:number,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   EDICode:string,
      /**  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  */  
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  */  
   Number:number,
      /**  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  */  
   FRxDSN:string,
      /**  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  */  
   EschedFileSet:string,
      /**  Unique identifier from and external G/L interface  */  
   ExternalID:string,
      /**  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  */  
   LogoFile:string,
      /**  Path the Employee Photos are stored in.  */  
   EmpPhotoPath:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  The User ID for FRx.  */  
   FrxUserid:string,
      /**  FRxUserID password  */  
   FRxPassWord:string,
      /**  The fiscal calendar id for the company.  */  
   FiscalCalendarID:string,
      /**  Company legal name  */  
   LegalName:string,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Economic Activity Type  */  
   ActTypeCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Chief Executive Officerr name  */  
   ManagerName:string,
      /**  Chief Financial Officer Name  */  
   ChiefAcctName:string,
      /**  Type of report  */  
   ReportTypePref:string,
      /**  WIApplication  */  
   WIApplication:string,
      /**  WIAutoCreateJob  */  
   WIAutoCreateJob:boolean,
      /**  WIGetDetails  */  
   WIGetDetails:boolean,
      /**  WISchedule  */  
   WISchedule:boolean,
      /**  WIRelease  */  
   WIRelease:boolean,
      /**  WIShippingCosts  */  
   WIShippingCosts:boolean,
      /**  DeepCopy  */  
   DeepCopy:boolean,
      /**  DeepCopyDupOrRevEst  */  
   DeepCopyDupOrRevEst:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MapURL  */  
   MapURL:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  APBOE Check  */  
   APBOECheck:number,
      /**  COSequenceCert  */  
   COSequenceCert:number,
      /**  Determines if the Company has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Epicor client number for CRE  */  
   EpicorAccountNum:number,
      /**  StartDate  */  
   StartDate:string,
      /**  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  */  
   KindOfEmp:string,
      /**  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  */  
   EmploymentCode:string,
      /**  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  */  
   PurchaseScheduleMode:string,
      /**  Currency.BaseCurrCode field  */  
   BaseCurrCode:string,
   ExtPRConfig:boolean,
      /**  Has Currency Transactions  */  
   HasCurrTrans:boolean,
   Intrastat:boolean,
      /**  Name of product (MFGSYS Name)  */  
   ProductName:string,
   AllowSchedulingBeforeToday:boolean,
   BitFlag:number,
   CalendarDescription:string,
   FiscalCalDescription:string,
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface GenerateReport_input{
   ds:Erp_Tablesets_ARDtlsTableset[],
}

export interface GenerateReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARDtlsTableset,
}
}

   /** Required : 
      @param CustID
   */  
export interface GenerateTrackerForECC_input{
      /**  Customer ID.  */  
   CustID:string,
}

export interface GenerateTrackerForECC_output{
   returnObj:Erp_Tablesets_ARTrackerTotTableset[],
}

   /** Required : 
      @param CustID
   */  
export interface GenerateTracker_input{
      /**  Customer ID.  */  
   CustID:string,
}

export interface GenerateTracker_output{
   returnObj:Erp_Tablesets_ARTrackerTotTableset[],
}

export interface GetARAccounts_output{
parameters : {
      /**  output parameters  */  
   arActsList:string,
}
}

export interface GetAgeBy_output{
parameters : {
      /**  output parameters  */  
   AgeBylist:string,
}
}

export interface GetAgingFormatCode_output{
parameters : {
      /**  output parameters  */  
   AgingFormatCodelist:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewParams_input{
   ds:Erp_Tablesets_ARDtlsTableset[],
}

export interface GetNewParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ARDtlsTableset,
}
}

export interface GetSelectBy_output{
parameters : {
      /**  output parameters  */  
   selectbylist:string,
}
}

export interface GetSortByList_output{
parameters : {
      /**  output parameters  */  
   sortbylist:string,
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

export interface Killtask_output{
   returnObj:boolean,
}

