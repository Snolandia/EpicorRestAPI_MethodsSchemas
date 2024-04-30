import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.RPT.NatAcctMassUpdRptSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/$metadata", {
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
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given datatype.
   OperationID: Get_GetTokenList
      @param tokenDataType Desc: Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenList(tokenDataType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof tokenDataType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tokenDataType=" + tokenDataType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetTokenList" + params, {
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
         resolve(data as GetTokenList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of values based on a type that is passed in.
   OperationID: Get_GetTokenValue
      @param pcValue Desc: Type of token   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetTokenValue(pcValue:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof pcValue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pcValue=" + pcValue
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetTokenValue" + params, {
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
         resolve(data as GetTokenValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRptArchiveList
   Description: Returns a sub-delimited list of valid archive codes/descriptions.
   OperationID: GetRptArchiveList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRptArchiveList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRptArchiveList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRptArchiveList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetRptArchiveList", {
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
         resolve(data as GetRptArchiveList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SubmitToAgent
   Description: Submits this report to a System Agent. The system agent will run the task based on the defined schedule.
   OperationID: SubmitToAgent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitToAgent(requestBody:SubmitToAgent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SubmitToAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/SubmitToAgent", {
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
         resolve(data as SubmitToAgent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaults
   Description: Use to get the current parameter defaults that the user has established for this report.
Note: This is automatically run as part of the GetNewParameters method.
In cases where the ParamSetID would be blank (this is most cases) you would not need to call this method.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
As is the case in GLFinancial Reports the GLFinancialParam.GLReportID is used as the ParamSetID field.
Another possible use would be to Reset the screen to default values.
   OperationID: GetDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:GetDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetDefaults", {
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
         resolve(data as GetDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewParameters
   Description: Creates a new (parameter record) in the dataset.
Note: A parameter dataset should never contain more than one record.
   OperationID: Get_GetNewParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetNewParameters(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetNewParameters", {
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
         resolve(data as GetNewParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamsFromAgent
   Description: Gets existing parameter values from the Task Agent and returns them in the in the dataset.
Note: Parameters are stored as individual fields in the database. This method is
used to retrieve those values and return them in the specific dataset.
   OperationID: Get_GetParamsFromAgent
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamsFromAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetParamsFromAgent(agentID:string, agentSchedNum:string, agentTaskNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof agentID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentID=" + agentID
   }
   if(typeof agentSchedNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentSchedNum=" + agentSchedNum
   }
   if(typeof agentTaskNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "agentTaskNum=" + agentTaskNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParamsFromAgent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetParamsFromAgent" + params, {
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
         resolve(data as GetParamsFromAgent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetParamTaskDef
   Description: Use to get the specified ProcessSet Task defaults that the user has established for this report.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
   OperationID: GetParamTaskDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamTaskDef(requestBody:GetParamTaskDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetParamTaskDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/GetParamTaskDef", {
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
         resolve(data as GetParamTaskDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveDefaults
   Description: Use to remove the current parameter defaults that the user has established for this report.
   OperationID: RemoveDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveDefaults(requestBody:RemoveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/RemoveDefaults", {
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
         resolve(data as RemoveDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunDirect
   Description: Use to run the process directly from the client instead of submitting to a System Agent.
   OperationID: RunDirect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunDirect(requestBody:RunDirect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RunDirect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/RunDirect", {
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
         resolve(data as RunDirect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveDefaults
   Description: Use to save the current parameters as the users defaults for this report
   OperationID: SaveDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDefaults(requestBody:SaveDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/SaveDefaults", {
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
         resolve(data as SaveDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SaveProcessTask
   Description: Use to save the current parameters as the users defaults for this report
<param name="maintProgram">UI Maintenance program </param><param name="ds" />
   OperationID: SaveProcessTask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveProcessTask(requestBody:SaveProcessTask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SaveProcessTask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.NatAcctMassUpdRptSvc/SaveProcessTask", {
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
         resolve(data as SaveProcessTask_output)
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
export interface Erp_Tablesets_NatAcctMassUpdRptParamRow{
      /**  AccrualAccount  */  
   AccrualAccount:string,
      /**  Accrual Account Description  */  
   AccrualAcctDesc:string,
      /**  AccrualSegVal1  */  
   AccrualSegVal1:string,
      /**  AccrualSegVal10  */  
   AccrualSegVal10:string,
      /**  AccrualSegVal11  */  
   AccrualSegVal11:string,
      /**  AccrualSegVal12  */  
   AccrualSegVal12:string,
      /**  AccrualSegVal13  */  
   AccrualSegVal13:string,
      /**  AccrualSegVal14  */  
   AccrualSegVal14:string,
      /**  AccrualSegVal15  */  
   AccrualSegVal15:string,
      /**  AccrualSegVal16  */  
   AccrualSegVal16:string,
      /**  AccrualSegVal17  */  
   AccrualSegVal17:string,
      /**  AccrualSegVal18  */  
   AccrualSegVal18:string,
      /**  AccrualSegVal19  */  
   AccrualSegVal19:string,
      /**  AccrualSegVal2  */  
   AccrualSegVal2:string,
      /**  AccrualSegVal20  */  
   AccrualSegVal20:string,
      /**  AccrualSegVal3  */  
   AccrualSegVal3:string,
      /**  AccrualSegVal4  */  
   AccrualSegVal4:string,
      /**  AccrualSegVal5  */  
   AccrualSegVal5:string,
      /**  AccrualSegVal6  */  
   AccrualSegVal6:string,
      /**  AccrualSegVal7  */  
   AccrualSegVal7:string,
      /**  AccrualSegVal8  */  
   AccrualSegVal8:string,
      /**  AccrualSegVal9  */  
   AccrualSegVal9:string,
      /**   COA category Types -                
Values:
A - All
B - Balance Sheet
I - Income Statement  */  
   AcctType:string,
      /**  Indicates if the segment is active. Transactions cannot be posted to inactive segments  */  
   ActiveFlag:boolean,
      /**  Override Active flag.  */  
   ActiveFlagOrd:boolean,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**  Category description  */  
   CategoryDesc:string,
      /**  Override Category flag.  */  
   CategoryOrd:boolean,
      /**  COA Categories  */  
   COACat:string,
      /**  Chart of Accounts header table  */  
   COACode:string,
      /**  COA Description  */  
   COADescription:string,
      /**  COA is Master  */  
   COAMaster:boolean,
      /**  Chart of Accounts Segment Values Currency Accounts List.  */  
   COASegAcct:string,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  CurrencyAcctType  */  
   CurrencyAcctType:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
      /**  Option selected to display the selected natural accounts in the report.  */  
   DisplayOpt:boolean,
      /**  Date the segment begins to be used. It must be less than or equal to the Effective To Date  */  
   EffectiveFrom:string,
      /**  Override Effective From date flag  */  
   EffectiveFromOrd:boolean,
      /**  Date the segment is no longer used. It must be greater than or equal to the Effective From date, if a value was entered in that field  */  
   EffectiveTo:string,
      /**  Override Effective To flag.  */  
   EffectiveToOrd:boolean,
      /**  External financial analysis code linked to the natural account  */  
   ExtAnalysisCode:string,
      /**  Analysis code description  */  
   ExtAnalysisCodeDesc:string,
      /**  Override external analysis code flag.  */  
   ExtAnalysisCodeOrd:boolean,
      /**  GainAccount  */  
   GainAccount:string,
      /**  Gain Account Description  */  
   GainAcctDesc:string,
      /**  GainSegVal1  */  
   GainSegVal1:string,
      /**  GainSegVal10  */  
   GainSegVal10:string,
      /**  GainSegVal11  */  
   GainSegVal11:string,
      /**  GainSegVal12  */  
   GainSegVal12:string,
      /**  GainSegVal13  */  
   GainSegVal13:string,
      /**  GainSegVal14  */  
   GainSegVal14:string,
      /**  GainSegVal15  */  
   GainSegVal15:string,
      /**  GainSegVal16  */  
   GainSegVal16:string,
      /**  GainSegVal17  */  
   GainSegVal17:string,
      /**  GainSegVal18  */  
   GainSegVal18:string,
      /**  GainSegVal19  */  
   GainSegVal19:string,
      /**  GainSegVal2  */  
   GainSegVal2:string,
      /**  GainSegVal20  */  
   GainSegVal20:string,
      /**  GainSegVal3  */  
   GainSegVal3:string,
      /**  GainSegVal4  */  
   GainSegVal4:string,
      /**  GainSegVal5  */  
   GainSegVal5:string,
      /**  GainSegVal6  */  
   GainSegVal6:string,
      /**  GainSegVal7  */  
   GainSegVal7:string,
      /**  GainSegVal8  */  
   GainSegVal8:string,
      /**  GainSegVal9  */  
   GainSegVal9:string,
      /**  GLGainAcctContext  */  
   GLGainAcctContext:string,
      /**  GLLossAcctContext  */  
   GLLossAcctContext:string,
      /**  LossAccount  */  
   LossAccount:string,
      /**  Loss Account Description  */  
   LossAcctDesc:string,
      /**  LossSegVal1  */  
   LossSegVal1:string,
      /**  LossSegVal10  */  
   LossSegVal10:string,
      /**  LossSegVal11  */  
   LossSegVal11:string,
      /**  LossSegVal12  */  
   LossSegVal12:string,
      /**  LossSegVal13  */  
   LossSegVal13:string,
      /**  LossSegVal14  */  
   LossSegVal14:string,
      /**  LossSegVal15  */  
   LossSegVal15:string,
      /**  LossSegVal16  */  
   LossSegVal16:string,
      /**  LossSegVal17  */  
   LossSegVal17:string,
      /**  LossSegVal18  */  
   LossSegVal18:string,
      /**  LossSegVal19  */  
   LossSegVal19:string,
      /**  LossSegVal2  */  
   LossSegVal2:string,
      /**  LossSegVal20  */  
   LossSegVal20:string,
      /**  LossSegVal3  */  
   LossSegVal3:string,
      /**  LossSegVal4  */  
   LossSegVal4:string,
      /**  LossSegVal5  */  
   LossSegVal5:string,
      /**  LossSegVal6  */  
   LossSegVal6:string,
      /**  LossSegVal7  */  
   LossSegVal7:string,
      /**  LossSegVal8  */  
   LossSegVal8:string,
      /**  LossSegVal9  */  
   LossSegVal9:string,
      /**  This flag determines if journal detail records with this natural account are allowed to be matched  */  
   MatchingEnabled:boolean,
      /**  Override Matching Enabled flag.  */  
   MatchingEnabledOrd:boolean,
      /**  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  */  
   NormalBalance:string,
      /**  Normal balance description  */  
   NormalBalanceDesc:string,
      /**  Override Normal Balance flag.  */  
   NormalBalanceOrd:boolean,
      /**  Executing dll name.  */  
   RestrictID:string,
      /**   Modify restrictions:          
A - Add
O - Override
R - Replace  */  
   RestrictionMod:string,
      /**  Lists of restrictions to add/override  */  
   RestrictionsList:string,
      /**  RevalueOpt  */  
   RevalueOpt:number,
      /**  Identifies the account category this is used to determine characteristics when the segment value is reversed.  */  
   ReverseCategory:string,
      /**  Reverse category description.  */  
   ReverseCategoryDesc:string,
      /**  Override reverse category.  */  
   ReverseCategoryOrd:boolean,
      /**  List of segment options to add/override  */  
   SegmentOptsList:string,
      /**   Modify segment options          
A - Add
O - Override
R - Replace  */  
   SegmentOptsMod:string,
      /**  Enable segment options  */  
   SegOptsEnabled:boolean,
      /**  Natural Account Segment Ranges  */  
   SegRanges:string,
      /**   0)      Summarize (default)   
1)      Summarize debit and credits separately
2)      No summarization  */  
   Summarization:number,
      /**  Summarization description  */  
   SummarizationDesc:string,
      /**  Override summarization flag.  */  
   SummarizationOrd:boolean,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   ValOption:string,
   NewCurrency:boolean,
   OverrideCurrency:boolean,
   OverrideRT:boolean,
   ReplaceCurrency:boolean,
   CurrencyAcctTypeDesc:string,
   RevalueOptDesc:string,
   GainAccountDisp:string,
   LossAccountDisp:string,
   AccrualAccountDisp:string,
   DebitRateTypeDesc:string,
   CreditRateTypeDesc:string,
   StatisticalDesc:string,
   StatUOMCode:string,
   StatUOMDesc:string,
   Statistical:number,
      /**  Override Statistical  */  
   StatisticalOrd:boolean,
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

export interface Erp_Tablesets_NatAcctMassUpdRptTableset{
   NatAcctMassUpdRptParam:Erp_Tablesets_NatAcctMassUpdRptParamRow[],
   ReportStyle:Erp_Tablesets_ReportStyleRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReportStyleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  Report Style Description  */  
   StyleDescription:string,
      /**  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  */  
   RptTypeID:string,
      /**  Program which performs the actual printing  */  
   PrintProgram:string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   PrintProgramOptions:string,
      /**  Foreign Key to RptDef table.  */  
   RptDefID:string,
      /**   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  */  
   CompanyList:string,
      /**  This is a Crystal Server Num that is defined in CrystalServer table.  */  
   ServerNum:number,
      /**   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  */  
   OutputLocation:string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   OutputEDI:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  StructuredOutputEnabled  */  
   StructuredOutputEnabled:boolean,
      /**  RequireSubmissionID  */  
   RequireSubmissionID:boolean,
      /**  AllowResetAfterSubmit  */  
   AllowResetAfterSubmit:boolean,
      /**  CertificateID  */  
   CertificateID:string,
      /**  Language  */  
   LangNameID:string,
      /**  Culture Format  */  
   FormatCulture:string,
      /**  StructuredOutputCertificateID  */  
   StructuredOutputCertificateID:string,
      /**  StructuredOutputAlgorithm  */  
   StructuredOutputAlgorithm:string,
      /**  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  */  
   HasBAQOrEI:boolean,
      /**  Flag to indicate if this report style record has an enabled routing rule.  */  
   RoutingRuleEnabled:boolean,
      /**  Digital cert for signing is an All Company cert.  */  
   CertificateIsAllComp:boolean,
      /**  Indicates the certificate is a system cert.  */  
   CertificateIsSystem:boolean,
      /**  Certificate expiration date.  */  
   CertExpiration:string,
      /**  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  */  
   Status:number,
      /**  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  */  
   StatusMessage:string,
   RptDefSystemFlag:boolean,
   LangNameIDDescription:string,
   IsBAQReport:boolean,
   StructuredOutputCertificateIsAllComp:boolean,
   StructuredOutputCertificateIsSystem:boolean,
   StructuredOutputCertificateExpirationDate:string,
   AllowGenerateEDI:boolean,
   BitFlag:number,
   ReportRptDescription:string,
   RptDefRptDescription:string,
   RptTypeRptTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset,
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset,
}
}

   /** Required : 
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
   */  
export interface GetParamsFromAgent_input{
   agentID:string,
   agentSchedNum:number,
   agentTaskNum:number,
}

export interface GetParamsFromAgent_output{
   returnObj:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface GetRptArchiveList_output{
   returnObj:string,
}

   /** Required : 
      @param tokenDataType
   */  
export interface GetTokenList_input{
      /**  Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear  */  
   tokenDataType:string,
}

export interface GetTokenList_output{
   returnObj:string,
}

   /** Required : 
      @param pcValue
   */  
export interface GetTokenValue_input{
      /**  Type of token  */  
   pcValue:string,
}

export interface GetTokenValue_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   pcTokenValue:string,
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
      @param paramSetID
   */  
export interface RemoveDefaults_input{
      /**  The defaults are stored with a key of Company,UserID,ProgramID,ParamSetID and FieldName
            The values of all of these, except ParamSetID are controlled by the backend logic.
            In most cases the ParamSetID is blank. Usually for a single program the user can only have one set of defaults.
            This parameter provides multi parameters sets to be associated with a single report.
            As is the case of GL Financial Reports. The user picks from a list of reports to be run.
            In this case you would pass the GLFinancialParam.GLReportID as the ParamSetID  */  
   paramSetID:string,
}

export interface RemoveDefaults_output{
}

   /** Required : 
      @param ds
   */  
export interface RunDirect_input{
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
}

export interface SaveProcessTask_output{
}

   /** Required : 
      @param ds
      @param agentID
      @param agentSchedNum
      @param agentTaskNum
      @param maintProgram
   */  
export interface SubmitToAgent_input{
   ds:Erp_Tablesets_NatAcctMassUpdRptTableset[],
      /**  Agent ID that will run this task  */  
   agentID:string,
      /**  Identifies the agent schedule of when this task should be run.
           Set to zero if you want to run this immediately.  */  
   agentSchedNum:number,
      /**  Identifies the agent task number within the schedule that is to be updated.
           Set to zero if you want to create a new task.  */  
   agentTaskNum:number,
      /**  Identifies the Maintenance program to run  */  
   maintProgram:string,
}

export interface SubmitToAgent_output{
}

