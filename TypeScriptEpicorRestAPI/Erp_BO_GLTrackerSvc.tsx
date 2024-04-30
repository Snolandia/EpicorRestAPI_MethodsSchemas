import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLTrackerSvc
// Description: GL Account Period Balance for Tracker
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", {
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
   Summary: Invoke method GetRows
   Description: This method replaces the standard GetRows method
   OperationID: Get_GetRows
      @param vBookID Desc: Book ID   Required: True   Allow empty value : True
      @param vBalanceType Desc: Balance Type P or T   Required: True   Allow empty value : True
      @param vUseCarryFwdBal Desc: Use Carry Forward Balance   Required: True
      @param sBalanceAcct Desc: Balance Account   Required: True   Allow empty value : True
      @param fiscalYear Desc: Fiscal Year   Required: True
      @param fiscalYearSuffix Desc: Fiscal Year Suffix   Required: True   Allow empty value : True
      @param budgetCodeID Desc: Fiscal Year Suffix   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(vBookID:string, vBalanceType:string, vUseCarryFwdBal:string, sBalanceAcct:string, fiscalYear:string, fiscalYearSuffix:string, budgetCodeID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof vBookID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vBookID=" + vBookID
   }
   if(typeof vBalanceType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vBalanceType=" + vBalanceType
   }
   if(typeof vUseCarryFwdBal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vUseCarryFwdBal=" + vUseCarryFwdBal
   }
   if(typeof sBalanceAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sBalanceAcct=" + sBalanceAcct
   }
   if(typeof fiscalYear!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYear=" + fiscalYear
   }
   if(typeof fiscalYearSuffix!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiscalYearSuffix=" + fiscalYearSuffix
   }
   if(typeof budgetCodeID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "budgetCodeID=" + budgetCodeID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDBalanceAccount
   Description: Performs a GLAcctDspSvc.GetByID of the GLAccount based on the balance type.
   OperationID: GetByIDBalanceAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDBalanceAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDBalanceAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDBalanceAccount(requestBody:GetByIDBalanceAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDBalanceAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetByIDBalanceAccount", {
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
         resolve(data as GetByIDBalanceAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultChartTrackerFilters
   Description: Get the default Chart Tracker filters
   OperationID: GetDefaultChartTrackerFilters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultChartTrackerFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultChartTrackerFilters(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultChartTrackerFilters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetDefaultChartTrackerFilters", {
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
         resolve(data as GetDefaultChartTrackerFilters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalPerDate
   OperationID: GetFiscalPerDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFiscalPerDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPerDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalPerDate(requestBody:GetFiscalPerDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFiscalPerDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetFiscalPerDate", {
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
         resolve(data as GetFiscalPerDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalPeriods
   OperationID: GetFiscalPeriods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFiscalPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalPeriods(requestBody:GetFiscalPeriods_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFiscalPeriods_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetFiscalPeriods", {
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
         resolve(data as GetFiscalPeriods_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalYear
   OperationID: GetFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalYear(requestBody:GetFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetFiscalYear", {
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
         resolve(data as GetFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultBudgetCode
   Description: Get default BudgetCode
   OperationID: GetDefaultBudgetCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultBudgetCode(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultBudgetCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetDefaultBudgetCode", {
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
         resolve(data as GetDefaultBudgetCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFiscalYearSuffix
   Description: Returns the Current Fiscal Year Suffix
   OperationID: GetFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFiscalYearSuffix(requestBody:GetFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetFiscalYearSuffix", {
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
         resolve(data as GetFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJournalHeaderComments
   Description: Returns GL Journal header comments.
   OperationID: GetJournalHeaderComments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJournalHeaderComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalHeaderComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournalHeaderComments(requestBody:GetJournalHeaderComments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJournalHeaderComments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetJournalHeaderComments", {
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
         resolve(data as GetJournalHeaderComments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsSpecificGLAccount
   Description: This method overloads GetRows method
   OperationID: GetRowsSpecificGLAccount
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsSpecificGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsSpecificGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsSpecificGLAccount(requestBody:GetRowsSpecificGLAccount_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsSpecificGLAccount_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRowsSpecificGLAccount", {
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
         resolve(data as GetRowsSpecificGLAccount_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCurrBal
   Description: Get currency balance rows for specified balance account.
   OperationID: GetRowsCurrBal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCurrBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCurrBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCurrBal(requestBody:GetRowsCurrBal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCurrBal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRowsCurrBal", {
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
         resolve(data as GetRowsCurrBal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsCurrBalWithOpeningBalance
   OperationID: GetRowsCurrBalWithOpeningBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsCurrBalWithOpeningBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCurrBalWithOpeningBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsCurrBalWithOpeningBalance(requestBody:GetRowsCurrBalWithOpeningBalance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsCurrBalWithOpeningBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRowsCurrBalWithOpeningBalance", {
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
         resolve(data as GetRowsCurrBalWithOpeningBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsGLAccountList
   Description: Invokes GetRowsMultiple using a delimited list of GL accounts
   OperationID: GetRowsGLAccountList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsGLAccountList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsGLAccountList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsGLAccountList(requestBody:GetRowsGLAccountList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsGLAccountList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRowsGLAccountList", {
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
         resolve(data as GetRowsGLAccountList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsMultiple
   Description: This method gets all the rows for a group of glaccounts specified GLAccount table
   OperationID: GetRowsMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsMultiple(requestBody:GetRowsMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetRowsMultiple", {
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
         resolve(data as GetRowsMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBookID
   Description: On change of BookID
   OperationID: OnChangeBookID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBookID(requestBody:OnChangeBookID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBookID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeBookID", {
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
         resolve(data as OnChangeBookID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBudgetCodeID
   Description: On change of BudgetCodeID
   OperationID: OnChangeBudgetCodeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBudgetCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBudgetCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBudgetCodeID(requestBody:OnChangeBudgetCodeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBudgetCodeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeBudgetCodeID", {
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
         resolve(data as OnChangeBudgetCodeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFiscalYear
   Description: On change of FiscalYear
   OperationID: OnChangeFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFiscalYear(requestBody:OnChangeFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeFiscalYear", {
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
         resolve(data as OnChangeFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFiscalYearSuffix
   Description: On change of FiscalYearSuffix
   OperationID: OnChangeFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFiscalYearSuffix(requestBody:OnChangeFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeFiscalYearSuffix", {
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
         resolve(data as OnChangeFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeStartEndDate
   Description: On change of StartDate or EndDate
   OperationID: OnChangeStartEndDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeStartEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStartEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeStartEndDate(requestBody:OnChangeStartEndDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeStartEndDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeStartEndDate", {
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
         resolve(data as OnChangeStartEndDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeStartEndPeriod
   Description: On change of StartPeriod or EndPeriod
   OperationID: OnChangeStartEndPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeStartEndPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStartEndPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeStartEndPeriod(requestBody:OnChangeStartEndPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeStartEndPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/OnChangeStartEndPeriod", {
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
         resolve(data as OnChangeStartEndPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalPerDate
   Description: Returns the Fiscal Year periods
   OperationID: ValidateFiscalPerDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPerDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPerDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalPerDate(requestBody:ValidateFiscalPerDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalPerDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/ValidateFiscalPerDate", {
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
         resolve(data as ValidateFiscalPerDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalPeriod
   Description: Validate the Fiscal Period
   OperationID: ValidateFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalPeriod(requestBody:ValidateFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/ValidateFiscalPeriod", {
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
         resolve(data as ValidateFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalYearSuffix
   Description: Validate the Fiscal Year Suffix
   OperationID: ValidateFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalYearSuffix(requestBody:ValidateFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/ValidateFiscalYearSuffix", {
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
         resolve(data as ValidateFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFiscalYear
   Description: Validate the Fiscal Year
   OperationID: ValidateFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFiscalYear(requestBody:ValidateFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/ValidateFiscalYear", {
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
         resolve(data as ValidateFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBudgetCode
   Description: Validate Budget Code
   OperationID: ValidateBudgetCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBudgetCode(requestBody:ValidateBudgetCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBudgetCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/ValidateBudgetCode", {
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
         resolve(data as ValidateBudgetCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBalAcctFromGlAcct
   Description: Get Balance Accounts
   OperationID: GetBalAcctFromGlAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBalAcctFromGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBalAcctFromGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBalAcctFromGlAcct(requestBody:GetBalAcctFromGlAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBalAcctFromGlAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetBalAcctFromGlAcct", {
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
         resolve(data as GetBalAcctFromGlAcct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateSiteFilter
   Description: Creates siteFilter query based on selected Sites and allowed sites
   OperationID: GenerateSiteFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateSiteFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSiteFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateSiteFilter(requestBody:GenerateSiteFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateSiteFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GenerateSiteFilter", {
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
         resolve(data as GenerateSiteFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSiteFilterAndText
   Description: Gets site filter string for record retrieval and sites selected text
   OperationID: GetSiteFilterAndText
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSiteFilterAndText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteFilterAndText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSiteFilterAndText(requestBody:GetSiteFilterAndText_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSiteFilterAndText_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetSiteFilterAndText", {
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
         resolve(data as GetSiteFilterAndText_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGLTrackerSites
   Description: Returns Sites that can be selected for filtering tracker results
   OperationID: GetGLTrackerSites
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLTrackerSites_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGLTrackerSites(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGLTrackerSites_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/GetGLTrackerSites", {
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
         resolve(data as GetGLTrackerSites_output)
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
export interface Erp_Tablesets_ChartTrackerFiltersRow{
   FiscalYear:number,
   FiscalYearSuffix:string,
   FiscalCalendarID:string,
   StartPeriod:number,
   EndPeriod:number,
   StartDate:string,
   EndDate:string,
   BookID:string,
   BookIDDesc:string,
   COACode:string,
      /**  Balance Type of either Detailed Balances or Summary Balances  */  
   BalanceType:string,
   UseCarryFwdBal:boolean,
   UseCarryFwdBalTotal:boolean,
   UseCarryFwdBalCurr:boolean,
   BookCurrencyCode:string,
   BookCurrencyDesc:string,
   TransCurrencyCode:string,
   TransCurrencyDesc:string,
   BudgetCodeID:string,
   BudgetCodeDesc:string,
   GLAccount:string,
      /**  List of GL Accounts separated by tilde  */  
   GLAccountList:string,
      /**  The current fiscal year  */  
   CurrentFiscalYear:number,
   JournalCode:string,
      /**  List of Journal Codes separated by tilde  */  
   JournalCodeList:string,
   SiteList:string,
      /**  Calculated filter based on selected Sites. This is partial SQL where clause.  */  
   SiteFilter:string,
      /**  Setting from XbSyst datatable.  */  
   SiteIsLegalEntity:boolean,
      /**  Determine it current filter book contains site segment  */  
   BookContainsSiteSegment:boolean,
      /**  Text indicating what sites are selected  */  
   SitesSelectedText:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ChartTrackerFiltersTableset{
   ChartTrackerFilters:Erp_Tablesets_ChartTrackerFiltersRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CurrOpenBalRow{
      /**  Current Year Opening Balance Book Currency  */  
   CYOpenBBookC:number,
      /**  Current Year Opening Balance Transaction Currency  */  
   CYOpenBTranC:number,
      /**  Currency Book  */  
   CurrencyBook:string,
      /**  Currency Transaction  */  
   CurrencyTran:string,
      /**  GLAccount  */  
   GLAccount:string,
      /**  Current Year Opening Balance  */  
   CYOpenBalance:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccountTrackerRow{
      /**  Company  */  
   Company:string,
   SegValue1:string,
   SegValue2:string,
   SegValue3:string,
   SegValue4:string,
   SegValue5:string,
   SegValue6:string,
   SegValue7:string,
   SegValue8:string,
   SegValue9:string,
   SegValue10:string,
   SegValue11:string,
   SegValue12:string,
   SegValue13:string,
   SegValue14:string,
   SegValue15:string,
   SegValue16:string,
   SegValue17:string,
   SegValue18:string,
   SegValue19:string,
   SegValue20:string,
   BalanceType:string,
   BookID:string,
   FiscalCalendarID:string,
   FiscalPeriod:number,
   FiscalYear:number,
   FiscalYearSuffix:string,
   GLAccount:string,
   GLAcctDisp:string,
   AccountDesc:string,
   CategoryDesc:string,
   NormalBalDesc:string,
   CanUseCarryFwdBal:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccountTrackerTableset{
   GLAccountTracker:Erp_Tablesets_GLAccountTrackerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLTrackerCurrBalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  A unique code that identifies the document currency.  */  
   DocCurrency:string,
      /**  The GL Account used to record balances.  */  
   CurrBalAcct:string,
      /**  The fiscal year.  */  
   FiscalYear:number,
      /**  the fiscal period's number in the fiscal year.  */  
   FiscalPeriod:number,
      /**  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  This is the natural account.  */  
   SegValue1:string,
      /**  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SegValue2:string,
      /**  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SegValue3:string,
      /**  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SegValue4:string,
      /**  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SegValue5:string,
      /**  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SegValue6:string,
      /**  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SegValue7:string,
      /**  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SegValue8:string,
      /**  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SegValue9:string,
      /**  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SegValue10:string,
      /**  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SegValue11:string,
      /**  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SegValue12:string,
      /**  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SegValue13:string,
      /**  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SegValue14:string,
      /**  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SegValue15:string,
      /**  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SegValue16:string,
      /**  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SegValue17:string,
      /**  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SegValue18:string,
      /**  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SegValue19:string,
      /**  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SegValue20:string,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  This is in document currency.  */  
   DocDebitAmt:number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  This is in document currency.  */  
   DocCreditAmt:number,
      /**  Total debit amount that has been posted to the account for a specific fisccal year/period.  This is in base currency.  */  
   BaseDebitAmt:number,
      /**  Total Credit amount that has been posted to the account for a specific fiscal year/period.  This is in base currency.  */  
   BaseCreditAmt:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Base Opening Balance  */  
   BaseOpenBal:number,
      /**  Doc Opening Balance  */  
   DocOpenBal:number,
      /**  Base Running Balance  */  
   BaseRunningBal:number,
      /**  Doc Running Balance  */  
   DocRunningBal:number,
   CurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLTrackerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The fiscal year of this record.  */  
   FiscalYear:number,
      /**  Fiscal period of the balance record.  */  
   FiscalPeriod:number,
      /**  The Total Debit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.DebitAmt.  */  
   DebitAmt:number,
      /**  The Total Credit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.CreditAmt.  Note the negative sign has been removed for display purposes.  */  
   CreditAmt:number,
      /**  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  */  
   CYBalance:number,
      /**  Current Fiscal period Budget amount.  Created from GLBudgetDtl.BudgetAmt.  */  
   CPBudget:number,
      /**  The Current Year Account Budget Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetAmt.  */  
   CYBudget:number,
      /**  Current period percent of budget.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / GLBudgetDtl.BudgetAmt.  */  
   CPBudgetPct:number,
      /**  Current Year Account Balance percent of budget.  Calculated as CurYrBalance / CurYrBudget.  */  
   CYBudgetPct:number,
      /**  The Prior fiscal years transaction activity summary amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitAmt + CreditAmt.  */  
   PYCPAmt:number,
      /**  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  */  
   PYBalance:number,
      /**  The Current fiscal period to prior year fiscal period amount comparative percentage.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / PYCPAmt.  */  
   PYCPPct:number,
      /**  Current years balance to prior years balance comparative percent.  Calculated as CYBalance / PYBalance.  */  
   PYPct:number,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Current Fiscal period Budget Statistical amount.  Created from GLBudgetDtl.BudgetStatAmt.  */  
   CPStatBudget:number,
      /**  The Current Year Account Budget Statistical Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetStatAmt.  */  
   CYStatBudget:number,
      /**  Current period percent of statisctical budget.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / GLBudgetDtl.BudgetStatAmt.  */  
   CPStatBudgetPct:number,
      /**  Current Year Account Balance percent of statistical budget.  Calculated as CurYrStatBalance / CurYrStatBudget.  */  
   CYStatBudgetPct:number,
      /**  Current Year Opening Balance  */  
   CYOpenBalance:number,
   GLAccount:string,
   SegValue1:string,
   SegValue2:string,
   SegValue3:string,
   SegValue4:string,
   SegValue5:string,
   SegValue6:string,
   SegValue7:string,
   SegValue8:string,
   SegValue9:string,
   SegValue10:string,
   SegValue11:string,
   SegValue12:string,
   SegValue13:string,
   SegValue14:string,
   SegValue15:string,
   SegValue16:string,
   SegValue17:string,
   SegValue18:string,
   SegValue19:string,
   SegValue20:string,
      /**  COA Code  */  
   COACode:string,
   PeriodStartDate:string,
   PeriodEndDate:string,
   CurrencyCode:string,
   CYStatBalance:number,
   PYStatBalance:number,
   StatAmount:number,
   StatUOMDesc:string,
      /**  The Prior fiscal years transaction activity summary statistical amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitStatAmt + CreditStatAmt.  */  
   PYCPStatAmt:number,
      /**  Current years statistical balance to prior years statistical balance comparative percent.  Calculated as CYStatBalance / PYStatBalance.  */  
   PYStatPct:number,
      /**  The Current fiscal period to prior year fiscal period statistical amount comparative percentage.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / PYCPStatAmt.  */  
   PYCPStatPct:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLTrackerSitesRow{
   Company:string,
   Name:string,
   Plant:string,
      /**  Row is selected  */  
   Selected:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLTrackerSitesTableset{
   GLTrackerSites:Erp_Tablesets_GLTrackerSitesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLTrackerTableset{
   GLTracker:Erp_Tablesets_GLTrackerRow[],
   CurrOpenBal:Erp_Tablesets_CurrOpenBalRow[],
   GLTrackerCurrBal:Erp_Tablesets_GLTrackerCurrBalRow[],
   GLTrackerTotals:Erp_Tablesets_GLTrackerTotalsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLTrackerTotalsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The fiscal year of this record.  */  
   FiscalYear:number,
      /**  Fiscal period of the balance record.  */  
   FiscalPeriod:number,
      /**  The Total Debit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.DebitAmt.  */  
   DebitAmt:number,
      /**  The Total Credit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.CreditAmt.  Note the negative sign has been removed for display purposes.  */  
   CreditAmt:number,
      /**  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  */  
   CYBalance:number,
      /**  Current Fiscal period Budget amount.  Created from GLBudgetDtl.BudgetAmt.  */  
   CPBudget:number,
      /**  The Current Year Account Budget Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetAmt.  */  
   CYBudget:number,
      /**  Current period percent of budget.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / GLBudgetDtl.BudgetAmt.  */  
   CPBudgetPct:number,
      /**  Current Year Account Balance percent of budget.  Calculated as CurYrBalance / CurYrBudget.  */  
   CYBudgetPct:number,
      /**  The Prior fiscal years transaction activity summary amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitAmt + CreditAmt.  */  
   PYCPAmt:number,
      /**  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  */  
   PYBalance:number,
      /**  The Current fiscal period to prior year fiscal period amount comparative percentage.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / PYCPAmt.  */  
   PYCPPct:number,
      /**  Current years balance to prior years balance comparative percent.  Calculated as CYBalance / PYBalance.  */  
   PYPct:number,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Current Fiscal period Budget Statistical amount.  Created from GLBudgetDtl.BudgetStatAmt.  */  
   CPStatBudget:number,
      /**  The Current Year Account Budget Statistical Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetStatAmt.  */  
   CYStatBudget:number,
      /**  Current period percent of statisctical budget.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / GLBudgetDtl.BudgetStatAmt.  */  
   CPStatBudgetPct:number,
      /**  Current Year Account Balance percent of statistical budget.  Calculated as CurYrStatBalance / CurYrStatBudget.  */  
   CYStatBudgetPct:number,
      /**  Current Year Opening Balance  */  
   CYOpenBalance:number,
   CurrencyCode:string,
   CYStatBalance:number,
   PYStatBalance:number,
   StatAmount:number,
   StatUOMDesc:string,
      /**  The Prior fiscal years transaction activity summary statistical amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitStatAmt + CreditStatAmt.  */  
   PYCPStatAmt:number,
      /**  Current years statistical balance to prior years statistical balance comparative percent.  Calculated as CYStatBalance / PYStatBalance.  */  
   PYStatPct:number,
      /**  The Current fiscal period to prior year fiscal period statistical amount comparative percentage.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / PYCPStatAmt.  */  
   PYCPStatPct:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param bookID
      @param siteList
   */  
export interface GenerateSiteFilter_input{
   bookID:string,
   siteList:string,
}

export interface GenerateSiteFilter_output{
   returnObj:string,
}

   /** Required : 
      @param ipCOACode
      @param ipGLAccount
   */  
export interface GetBalAcctFromGlAcct_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  GL Row  */  
   ipGLAccount:string,
}

export interface GetBalAcctFromGlAcct_output{
parameters : {
      /**  output parameters  */  
   outPerBalAcct:string,
   outTBBalAcct:string,
}
}

   /** Required : 
      @param coaCode
      @param balanceType
      @param glAccountList
      @param ds
   */  
export interface GetByIDBalanceAccount_input{
   coaCode:string,
   balanceType:string,
      /**  Tilde separated list of GL Accounts  */  
   glAccountList:string,
   ds:Erp_Tablesets_GLAccountTrackerTableset[],
}

export interface GetByIDBalanceAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLAccountTrackerTableset,
}
}

export interface GetDefaultBudgetCode_output{
parameters : {
      /**  output parameters  */  
   outBudgetCodeID:string,
   outBudgetCodeDesc:string,
}
}

export interface GetDefaultChartTrackerFilters_output{
   returnObj:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalPeriod
      @param ipStartOrEndDate
   */  
export interface GetFiscalPerDate_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
   ipFiscalPeriod:number,
   ipStartOrEndDate:string,
}

export interface GetFiscalPerDate_output{
parameters : {
      /**  output parameters  */  
   opFiscalPerDate:string,
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
   */  
export interface GetFiscalPeriods_input{
   ipBookID:string,
   ipFiscalYear:number,
   ipFiscalYearSuffix:string,
}

export interface GetFiscalPeriods_output{
parameters : {
      /**  output parameters  */  
   opFiscalPerStart:number,
   opFiscalPerEnd:number,
   opStartDate:string,
   opEndDate:string,
}
}

   /** Required : 
      @param vBookID
      @param vFiscalYear
   */  
export interface GetFiscalYearSuffix_input{
      /**  Book ID if not specified values will be based on Company.FiscalCalendarID"  */  
   vBookID:string,
      /**  Current Fiscal Year  */  
   vFiscalYear:number,
}

export interface GetFiscalYearSuffix_output{
parameters : {
      /**  output parameters  */  
   outFiscalYearSuffix:string,
}
}

   /** Required : 
      @param vBookID
   */  
export interface GetFiscalYear_input{
   vBookID:string,
}

export interface GetFiscalYear_output{
parameters : {
      /**  output parameters  */  
   outFiscalCalendarID:string,
   outFiscalYear:number,
   outFiscalYearSuffix:string,
   outFiscalPeriod:number,
   outStartDate:string,
   outEndDate:string,
}
}

export interface GetGLTrackerSites_output{
   returnObj:Erp_Tablesets_GLTrackerSitesTableset[],
}

   /** Required : 
      @param ipBookID
      @param ipJournalCode
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipJournalNum
   */  
export interface GetJournalHeaderComments_input{
      /**  Book ID value  */  
   ipBookID:string,
      /**  Journal Code  */  
   ipJournalCode:string,
      /**  Current Fiscal Year  */  
   ipFiscalYear:number,
      /**  Current Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Journal number  */  
   ipJournalNum:number,
}

export interface GetJournalHeaderComments_output{
parameters : {
      /**  output parameters  */  
   opCommentText:string,
}
}

   /** Required : 
      @param vBookID
      @param vBalanceType
      @param vTransCurrencyCode
      @param vUseCarryFwdBal
      @param sBalanceAcct
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface GetRowsCurrBalWithOpeningBalance_input{
   vBookID:string,
   vBalanceType:string,
   vTransCurrencyCode:string,
   vUseCarryFwdBal:boolean,
   sBalanceAcct:string,
   fiscalYear:number,
   fiscalYearSuffix:string,
}

export interface GetRowsCurrBalWithOpeningBalance_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
}

   /** Required : 
      @param vBookID
      @param vTransCurrencyCode
      @param vUseCarryFwdBal
      @param sBalanceAcct
      @param fiscalYear
      @param fiscalYearSuffix
   */  
export interface GetRowsCurrBal_input{
      /**  Book ID  */  
   vBookID:string,
      /**  Transactional CurrencyCode  */  
   vTransCurrencyCode:string,
      /**  Use Carry Forward Balance  */  
   vUseCarryFwdBal:boolean,
      /**  Balance Account  */  
   sBalanceAcct:string,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
}

export interface GetRowsCurrBal_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
}

   /** Required : 
      @param vBookID
      @param vBalanceType
      @param vUseCarryFwdBal
      @param fiscalYear
      @param fiscalYearSuffix
      @param budgetCodeID
      @param glAccountList
   */  
export interface GetRowsGLAccountList_input{
   vBookID:string,
   vBalanceType:string,
   vUseCarryFwdBal:boolean,
   fiscalYear:number,
   fiscalYearSuffix:string,
   budgetCodeID:string,
      /**  Tilde delimited list of GL Accounts  */  
   glAccountList:string,
}

export interface GetRowsGLAccountList_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
}

   /** Required : 
      @param vBookID
      @param vBalanceType
      @param vUseCarryFwdBal
      @param fiscalYear
      @param fiscalYearSuffix
      @param budgetCodeID
      @param ds
   */  
export interface GetRowsMultiple_input{
      /**  Book ID  */  
   vBookID:string,
      /**  Balance Type  */  
   vBalanceType:string,
      /**  Use Carry Forward Balance  */  
   vUseCarryFwdBal:boolean,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Budget Code  */  
   budgetCodeID:string,
   ds:Erp_Tablesets_GLAccountTrackerTableset[],
}

export interface GetRowsMultiple_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
}

   /** Required : 
      @param vBookID
      @param vBalanceType
      @param vUseCarryFwdBal
      @param sBalanceAcct
      @param fiscalYear
      @param fiscalYearSuffix
      @param budgetCodeID
   */  
export interface GetRowsSpecificGLAccount_input{
      /**  Book ID  */  
   vBookID:string,
      /**  Balance Type P or T  */  
   vBalanceType:string,
      /**  Use Carry Forward Balance  */  
   vUseCarryFwdBal:boolean,
      /**  Balance Account  */  
   sBalanceAcct:string,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Fiscal Year Suffix  */  
   budgetCodeID:string,
}

export interface GetRowsSpecificGLAccount_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
parameters : {
      /**  output parameters  */  
   openBalance:number,
}
}

   /** Required : 
      @param vBookID
      @param vBalanceType
      @param vUseCarryFwdBal
      @param sBalanceAcct
      @param fiscalYear
      @param fiscalYearSuffix
      @param budgetCodeID
   */  
export interface GetRows_input{
      /**  Book ID  */  
   vBookID:string,
      /**  Balance Type P or T  */  
   vBalanceType:string,
      /**  Use Carry Forward Balance  */  
   vUseCarryFwdBal:boolean,
      /**  Balance Account  */  
   sBalanceAcct:string,
      /**  Fiscal Year  */  
   fiscalYear:number,
      /**  Fiscal Year Suffix  */  
   fiscalYearSuffix:string,
      /**  Fiscal Year Suffix  */  
   budgetCodeID:string,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLTrackerTableset[],
parameters : {
      /**  output parameters  */  
   openBalance:number,
}
}

   /** Required : 
      @param ds
      @param bookID
   */  
export interface GetSiteFilterAndText_input{
   ds:Erp_Tablesets_GLTrackerSitesTableset[],
      /**  Book ID  */  
   bookID:string,
}

export interface GetSiteFilterAndText_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLTrackerSitesTableset,
   siteFilter:string,
   sitesSelectedText:string,
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
      @param bookID
      @param ds
   */  
export interface OnChangeBookID_input{
   bookID:string,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeBookID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param budgetCodeID
      @param ds
   */  
export interface OnChangeBudgetCodeID_input{
   budgetCodeID:string,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeBudgetCodeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param fiscalYearSuffix
      @param ds
   */  
export interface OnChangeFiscalYearSuffix_input{
   fiscalYearSuffix:string,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeFiscalYearSuffix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param fiscalYear
      @param ds
   */  
export interface OnChangeFiscalYear_input{
   fiscalYear:number,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param startEndDate
      @param isStartDate
      @param ds
   */  
export interface OnChangeStartEndDate_input{
   startEndDate:string,
   isStartDate:boolean,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeStartEndDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param startEndPeriod
      @param isStartDate
      @param ds
   */  
export interface OnChangeStartEndPeriod_input{
   startEndPeriod:number,
   isStartDate:boolean,
   ds:Erp_Tablesets_ChartTrackerFiltersTableset[],
}

export interface OnChangeStartEndPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ChartTrackerFiltersTableset,
}
}

   /** Required : 
      @param budgetCodeID
   */  
export interface ValidateBudgetCode_input{
      /**  Budget Code ID  */  
   budgetCodeID:string,
}

export interface ValidateBudgetCode_output{
parameters : {
      /**  output parameters  */  
   budgetCodeID:string,
   budgetCodeDesc:string,
}
}

   /** Required : 
      @param ipBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalPerDate
      @param ipFiscalPer
   */  
export interface ValidateFiscalPerDate_input{
      /**  Book ID if not specified values will be based on Company.FiscalCalendarID"  */  
   ipBookID:string,
      /**  Current Fiscal Year  */  
   ipFiscalYear:number,
      /**  Current Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Date to validate  */  
   ipFiscalPerDate:string,
      /**  old Fiscal Period  */  
   ipFiscalPer:number,
}

export interface ValidateFiscalPerDate_output{
parameters : {
      /**  output parameters  */  
   ipOutFiscalPeriod:number,
}
}

   /** Required : 
      @param vBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
      @param ipFiscalPer
   */  
export interface ValidateFiscalPeriod_input{
      /**  Book ID if not specified values will be based on Company.FiscalCalendarID"  */  
   vBookID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Suffix  */  
   ipFiscalYearSuffix:string,
      /**  Fiscal Period  */  
   ipFiscalPer:number,
}

export interface ValidateFiscalPeriod_output{
}

   /** Required : 
      @param vBookID
      @param ipFiscalYear
      @param ipFiscalYearSuffix
   */  
export interface ValidateFiscalYearSuffix_input{
      /**  Book ID if not specified values will be based on Company.FiscalCalendarID"  */  
   vBookID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
      /**  Fiscal Year Suffix  */  
   ipFiscalYearSuffix:string,
}

export interface ValidateFiscalYearSuffix_output{
}

   /** Required : 
      @param vBookID
      @param ipFiscalYear
   */  
export interface ValidateFiscalYear_input{
      /**  Book ID if not specified values will be based on Company.FiscalCalendarID"  */  
   vBookID:string,
      /**  Fiscal Year  */  
   ipFiscalYear:number,
}

export interface ValidateFiscalYear_output{
}

