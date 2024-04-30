import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.RPT.CurrencyRevalueSvc
// Description: CurrencyRevalueSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", {
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
   Summary: Invoke method CheckAP
   Description: Provides a warning message if Accounts Payable is not set up to interface to
the General Ledger.
            
Example output:
"WARNING: A/P is NOT interfaced with General Ledger.  G/L transactions will NOT be created.  Do you wish to continue?"
   OperationID: CheckAP
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAP_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAP(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAP_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/CheckAP", {
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
         resolve(data as CheckAP_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAR
   Description: Provides a warning message if Accounts Receivable is not set up to interface to
the General Ledger.
            
Example output:
"WARNING: A/R is NOT interfaced with General Ledger.  G/L transactions will NOT be created.  Do you wish to continue?"
   OperationID: CheckAR
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAR_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAR(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAR_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/CheckAR", {
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
         resolve(data as CheckAR_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetApplyDate
   Description: Update Apply Date information based on the UseApplyDate changing.
   OperationID: GetApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetApplyDate(requestBody:GetApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetApplyDate", {
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
         resolve(data as GetApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAPSortByList
   Description: Call this method to get the delimited list of valid values available for the
APSortyBy parameter.
   OperationID: GetAPSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAPSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAPSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetAPSortByList", {
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
         resolve(data as GetAPSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARSortByList
   Description: Call this method to get the delimited list of valid values available for the
ARSortyBy parameter.
   OperationID: GetARSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetARSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetARSortByList", {
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
         resolve(data as GetARSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBASortByList
   Description: Call this method to get the delimited list of valid values available for the
BASortyBy parameter.
   OperationID: GetBASortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBASortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBASortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBASortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetBASortByList", {
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
         resolve(data as GetBASortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTopLevelSortByList
   Description: Call this method to get the delimited list of valid values available for the
sorting top level parameter.
   OperationID: GetTopLevelSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTopLevelSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTopLevelSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTopLevelSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetTopLevelSortByList", {
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
         resolve(data as GetTopLevelSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExchangeDate
   Description: Update Exchange Date information based on the UseExchangeDate changing.
   OperationID: GetExchangeDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExchangeDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExchangeDate(requestBody:GetExchangeDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExchangeDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetExchangeDate", {
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
         resolve(data as GetExchangeDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPCDSordByList
   Description: Call this method to get the delimited list of valid values available for the
PCDSortyBy parameter.
   OperationID: GetPCDSordByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCDSordByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCDSordByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPCDSordByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetPCDSordByList", {
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
         resolve(data as GetPCDSordByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPOSortByList
   Description: Call this method to get the delimited list of valid values available for the
POSortyBy parameter.
   OperationID: GetPOSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPOSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPOSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetPOSortByList", {
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
         resolve(data as GetPOSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevaluationOption
   Description: Update the revaluation value based on the Override option changing.
   OperationID: GetRevaluationOption
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevaluationOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevaluationOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevaluationOption(requestBody:GetRevaluationOption_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevaluationOption_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetRevaluationOption", {
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
         resolve(data as GetRevaluationOption_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReverseDate
   Description: Update Reverse Date based on Revalue Date, Apply Date, or UseApplyDate changing
   OperationID: GetReverseDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReverseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReverseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReverseDate(requestBody:GetReverseDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReverseDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetReverseDate", {
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
         resolve(data as GetReverseDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSOSortByList
   Description: Call this method to get the delimited list of valid values available for the
SOSortyBy parameter.
   OperationID: GetSOSortByList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSOSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSOSortByList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSOSortByList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetSOSortByList", {
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
         resolve(data as GetSOSortByList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method inOpenFiscalPeriod
   OperationID: inOpenFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/inOpenFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/inOpenFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_inOpenFiscalPeriod(requestBody:inOpenFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<inOpenFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/inOpenFiscalPeriod", {
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
         resolve(data as inOpenFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRateTypeGrpSubs
   Description: Call this method to check if RateTypeGrpSubs is valid
   OperationID: ValidateRateTypeGrpSubs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRateTypeGrpSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateTypeGrpSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRateTypeGrpSubs(requestBody:ValidateRateTypeGrpSubs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRateTypeGrpSubs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/ValidateRateTypeGrpSubs", {
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
         resolve(data as ValidateRateTypeGrpSubs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCAllCurrenciesList
   Description: Call this method from Kinetic UI to load all Currencies
   OperationID: GetCAllCurrenciesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCAllCurrenciesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCAllCurrenciesList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCAllCurrenciesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetCAllCurrenciesList", {
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
         resolve(data as GetCAllCurrenciesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetTokenList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetTokenValue" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetRptArchiveList", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/SubmitToAgent", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetDefaults", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetNewParameters", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetParamsFromAgent" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/GetParamTaskDef", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/RemoveDefaults", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/RunDirect", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/SaveDefaults", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/SaveProcessTask", {
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
export interface CheckAP_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

export interface CheckAR_output{
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

export interface Erp_Tablesets_CurrencyRevalueParamRow{
      /**  The currency revaluation process will perform revaluations up to and including the revalue date, but not after.  */  
   RevalueDate:string,
      /**  The currency revaluation process will perform revaluations up to and including the revalue date, but not after.  */  
   RevalueDateToken:string,
      /**  Sort options for Accounts Receivable invoices  */  
   ARSortBy:string,
      /**  Sort options for Accounts Payable invoices  */  
   APSortBy:string,
      /**  Sort options for Bank Accounts  */  
   BASortBy:string,
      /**  Sort options for Sales Orders  */  
   SOSortBy:string,
      /**  Sort options for Purchase Orders  */  
   POSortBy:string,
      /**  Indicates whether each area of the report should start on its own page. If this is the case, check this box.  */  
   NewPage:boolean,
      /**  A delimited list of CurrencyCodes to process.  The corresponding exchange rate for each currency is in the ExchangeRateList.  */  
   CurrencyCodeList:string,
      /**  When TRUE, this will only print a report, no database updates will take place.  */  
   ReportOnly:boolean,
   Reverse:boolean,
   JournalCode:string,
      /**  If checked AR Invoice filter tab will be enabled  */  
   ARInvoice:boolean,
      /**  If checked AP Invoice filter tab will be enabled  */  
   APInvoice:boolean,
      /**  If checked Bank Acct filter tab will be enabled  */  
   BankAcct:boolean,
      /**  If checked Sales Orders will be revaluated  */  
   SO:boolean,
      /**  If checked Purchase Orders will be revaluated  */  
   PO:boolean,
      /**  Defaults to Revaluate Date  */  
   ExchangeDate:string,
      /**  Defaults to RevalueDate  */  
   ApplyDate:string,
   ApplyDateToken:string,
   ReverseDate:string,
      /**  List of selected AR Accounts  */  
   ARAcctList:string,
      /**  List of AP Accounts selected  */  
   APAcctList:string,
      /**  List of selected Bank Accounts  */  
   BankAcctList:string,
   ExchangeDateToken:string,
   UseExchangeDate:boolean,
   UseApplyDate:boolean,
   JrnlDescription:string,
   APGLCntrlType:string,
   ARGLCntrlType:string,
   APGLDesc:string,
   ARGLDesc:string,
      /**  Sort options for Payment Instrument Payable  */  
   PIPSortBy:string,
      /**  Sort options for Payment Instrument Receivable  */  
   PIRSortBy:string,
      /**  If checked Payment Instrument Payable filter tab will be enabled  */  
   PIP:boolean,
      /**  If checked Payment Instrument Receivable filter tab will be enabled  */  
   PIR:boolean,
      /**  List of Payment Instrument Payable Accounts selected  */  
   PIPAcctList:string,
      /**  List of Payment Instrument Receivable Accounts selected  */  
   PIRAcctList:string,
   PIPGLDesc:string,
   PIRGLDesc:string,
   PIPGLCntrlType:string,
   PIRGLCntrlType:string,
   APPrepayments:boolean,
   ARPrepayments:boolean,
   PeriodEnd:boolean,
      /**  If checked Petty Cash Desks filter tab will be enabled  */  
   PCashDesk:boolean,
      /**  List of selected Petty Cash Desks  */  
   PCashDeskList:string,
      /**  Sort options for Petty Cash Desks  */  
   PCDSortBy:string,
      /**   Flag to define if change of Reverse Option is available for the users.
If Reverse is false only  AR Invoice and AP Invoice check boxes could  be checked.  */  
   ReverseChange:boolean,
   OverrideRevalueAR:boolean,
   RevaluationAR:string,
   OverrideRevalueAP:boolean,
   RevaluationAP:string,
   OverrideRevalueBA:boolean,
   RevaluationBA:string,
   OverrideRevaluePCD:boolean,
   RevaluationPCD:string,
   RevaluationPIP:string,
   RevaluationPIR:string,
   BankAveRates:boolean,
      /**  Top-Level Sort By:  */  
   TopLevelSortBy:string,
      /**  A delimited list of CurrencyCodes to include in the report.Corresponding to base/ reporting currrencies.  */  
   CurrencyIncludeList:string,
   PrintSelCriteria:boolean,
   RateTypeGrpSubs:string,
   RateTypeGrpSubsDesc:string,
   RevaluationBAUnrealized:boolean,
   RevaluationPCDUnrealized:boolean,
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

export interface Erp_Tablesets_CurrencyRevalueTableset{
   CurrencyRevalueParam:Erp_Tablesets_CurrencyRevalueParamRow[],
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

export interface GetAPSortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
}

export interface GetARSortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
}

   /** Required : 
      @param ds
      @param lUseApplyDateOn
   */  
export interface GetApplyDate_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
      /**  Flag to indicate if ApplyDate will be cleared or set  */  
   lUseApplyDateOn:boolean,
}

export interface GetApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
}
}

export interface GetBASortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
}

export interface GetCAllCurrenciesList_output{
parameters : {
      /**  output parameters  */  
   currCodeList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
}
}

   /** Required : 
      @param ds
      @param lUseExchangeDateOn
   */  
export interface GetExchangeDate_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
      /**  Flag to indicate if ExchangeDate will be cleared or set  */  
   lUseExchangeDateOn:boolean,
}

export interface GetExchangeDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface GetPCDSordByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
}

export interface GetPOSortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
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
   returnObj:Erp_Tablesets_CurrencyRevalueTableset[],
}

   /** Required : 
      @param ds
      @param lOverride
      @param cOption
   */  
export interface GetRevaluationOption_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
      /**  Flag to indicate if the revaluation option is overridden  */  
   lOverride:boolean,
      /**  Indicates which option the override was changed for  */  
   cOption:string,
}

export interface GetRevaluationOption_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetReverseDate_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface GetReverseDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrencyRevalueTableset,
}
}

export interface GetRptArchiveList_output{
   returnObj:string,
}

export interface GetSOSortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
}
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

export interface GetTopLevelSortByList_output{
parameters : {
      /**  output parameters  */  
   pcList:string,
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
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
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
   ds:Erp_Tablesets_CurrencyRevalueTableset[],
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

   /** Required : 
      @param RateTypeGrpSubs
   */  
export interface ValidateRateTypeGrpSubs_input{
      /**  RateTypeGrpSubs parameter  */  
   RateTypeGrpSubs:string,
}

export interface ValidateRateTypeGrpSubs_output{
}

   /** Required : 
      @param id_RevalueDate
   */  
export interface inOpenFiscalPeriod_input{
   id_RevalueDate:string,
}

export interface inOpenFiscalPeriod_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   pcMsg:string,
}
}

