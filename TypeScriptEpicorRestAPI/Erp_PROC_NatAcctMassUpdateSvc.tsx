import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.PROC.NatAcctMassUpdateSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", {
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
   Summary: Invoke method EditListValidateParam
   Description: Validates parameters prior to opening the Print Edit List
   OperationID: EditListValidateParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EditListValidateParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditListValidateParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EditListValidateParam(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/EditListValidateParam", {
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
   Summary: Invoke method checkForNaturalAccountControl
   Description: checkForNaturalAccountControl
   OperationID: checkForNaturalAccountControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkForNaturalAccountControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkForNaturalAccountControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_checkForNaturalAccountControl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/checkForNaturalAccountControl", {
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
   Summary: Invoke method ChangeCOA_Type
   Description: Assign values to COACat
   OperationID: ChangeCOA_Type
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOA_Type_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOA_Type_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCOA_Type(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ChangeCOA_Type", {
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
   Summary: Invoke method OnCOACodeChanging
   Description: Validate COACode
   OperationID: OnCOACodeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCOACodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCOACodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnCOACodeChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/OnCOACodeChanging", {
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
   Summary: Invoke method OnCOASegValuesChanging
   Description: Validate Segment Values
   OperationID: OnCOASegValuesChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCOASegValuesChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCOASegValuesChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnCOASegValuesChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/OnCOASegValuesChanging", {
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
   Summary: Invoke method OnAnalysisCodeChange
   Description: Validate Analysis Code
   OperationID: OnAnalysisCodeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnAnalysisCodeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnAnalysisCodeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnAnalysisCodeChange(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/OnAnalysisCodeChange", {
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
   Summary: Invoke method OnCategoryChanging
   Description: This method convert the document currency to the journal currency.
   OperationID: OnCategoryChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCategoryChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCategoryChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnCategoryChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/OnCategoryChanging", {
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
   Summary: Invoke method ValidateDefaultSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: ValidateDefaultSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDefaultSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDefaultSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateDefaultSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ValidateDefaultSegment", {
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
   Summary: Invoke method ValidateSubSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Code to search for </param>
Notes:
   OperationID: ValidateSubSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSubSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSubSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSubSegment(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ValidateSubSegment", {
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
   Summary: Invoke method COACatofSegValues
   Description: Return category type of segments
   OperationID: COACatofSegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COACatofSegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COACatofSegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COACatofSegValues(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/COACatofSegValues", {
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
   Summary: Invoke method ChangeCurrencyAccount
   Description: On currency account change all related currencies should be updated to allowed/not allowed
   OperationID: ChangeCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCurrencyAccount(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ChangeCurrencyAccount", {
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
   Summary: Invoke method ChangeRevalueOpt
   Description: On Revalue Option change
   OperationID: ChangeRevalueOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalueOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalueOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevalueOpt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ChangeRevalueOpt", {
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
   Summary: Invoke method ChangeRateType
   Description: On Rate Type changing
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ChangeRateType", {
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
   Summary: Invoke method ChangeAccountContext
   Description: On Account context changing
   OperationID: ChangeAccountContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAccountContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAccountContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAccountContext(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ChangeAccountContext", {
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
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultsOnAdd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/DefaultsOnAdd", {
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
   Summary: Invoke method ValidateCurrencyAccountType
   Description: Validate Currency Account Type
   OperationID: ValidateCurrencyAccountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencyAccountType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ValidateCurrencyAccountType", {
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
   Summary: Invoke method ValidateCurrencyAccounts
   Description: Validate Currency Accounts book default data.
   OperationID: ValidateCurrencyAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCurrencyAccounts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/ValidateCurrencyAccounts", {
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
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given datatype.
   OperationID: Get_GetTokenList
      @param tokenDataType Desc: Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetTokenList" + params, {
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

   /**  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of values based on a type that is passed in.
   OperationID: Get_GetTokenValue
      @param pcValue Desc: Type of token   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetTokenValue" + params, {
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

   /**  
   Summary: Invoke method SubmitToAgent
   Description: Submits this report to a System Agent. The system agent will run the task based on the defined schedule.
   OperationID: SubmitToAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SubmitToAgent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/SubmitToAgent", {
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
   Summary: Invoke method GetDefaults
   Description: Use to get the current parameter defaults that the user has established for this report.
Note: This is automatically run as part of the GetNewParameters method.
In cases where the ParamSetID would be blank (this is most cases) you would not need to call this method.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
As is the case in GLFinancial Reports the GLFinancialParam.GLReportID is used as the ParamSetID field.
Another possible use would be to Reset the screen to default values.
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetDefaults", {
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
   Summary: Invoke method GetNewParameters
   Description: Creates a new (parameter record) in the dataset.
Note: A parameter dataset should never contain more than one record.
   OperationID: Get_GetNewParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetNewParameters", {
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

   /**  
   Summary: Invoke method GetParamsFromAgent
   Description: Gets existing parameter values from the Task Agent and returns them in the in the dataset.
Note: Parameters are stored as individual fields in the database. This method is
used to retrieve those values and return them in the specific dataset.
   OperationID: Get_GetParamsFromAgent
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetParamsFromAgent" + params, {
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

   /**  
   Summary: Invoke method GetParamTaskDef
   Description: Use to get the specified ProcessSet Task defaults that the user has established for this report.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
   OperationID: GetParamTaskDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetParamTaskDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/GetParamTaskDef", {
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
   Summary: Invoke method RemoveDefaults
   Description: Use to remove the current parameter defaults that the user has established for this report.
   OperationID: RemoveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/RemoveDefaults", {
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
   Summary: Invoke method RunDirect
   Description: Use to run the process directly from the client instead of submitting to a System Agent.
   OperationID: RunDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunDirect(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/RunDirect", {
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
   Summary: Invoke method SaveDefaults
   Description: Use to save the current parameters as the users defaults for this report
   OperationID: SaveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/SaveDefaults", {
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
   Summary: Invoke method SaveProcessTask
   Description: Use to save the current parameters as the users defaults for this report
<param name="maintProgram">UI Maintenance program </param><param name="ds" />
   OperationID: SaveProcessTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SaveProcessTask(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/SaveProcessTask", {
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
      @param ipCOACode
      @param ipSegmentNbr
      @param ipSegmentRange
      @param refType
   */  
export interface COACatofSegValues_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment number  */  
   ipSegmentNbr:number,
      /**  Segment Value list  */  
   ipSegmentRange:string,
      /**  Category Type  */  
   refType:string,
}

export interface COACatofSegValues_output{
parameters : {
      /**  output parameters  */  
   refType:string,
}
}

   /** Required : 
      @param context
   */  
export interface ChangeAccountContext_input{
      /**  GL Account Context  */  
   context:string,
}

export interface ChangeAccountContext_output{
}

   /** Required : 
      @param ipCOACode
      @param ipType
      @param ds
   */  
export interface ChangeCOA_Type_input{
      /**  The COACode  */  
   ipCOACode:string,
      /**  The Type  */  
   ipType:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface ChangeCOA_Type_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ipValue
      @param ds
   */  
export interface ChangeCurrencyAccount_input{
      /**  Currency Account flag  */  
   ipValue:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface ChangeCurrencyAccount_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param rateType
      @param isCredit
   */  
export interface ChangeRateType_input{
      /**  Rate Type to change.  */  
   rateType:string,
      /**  Flag to use Credit Rate Type instead of Debit.  */  
   isCredit:boolean,
}

export interface ChangeRateType_output{
}

   /** Required : 
      @param proposedRevalue
      @param ds
   */  
export interface ChangeRevalueOpt_input{
      /**  Proposed Revalue option  */  
   proposedRevalue:number,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface ChangeRevalueOpt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ipGLAccount
      @param ipAccountField
      @param ds
   */  
export interface DefaultsOnAdd_input{
      /**  GL Account being added  */  
   ipGLAccount:string,
      /**  GL Account being added  */  
   ipAccountField:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface DefaultsOnAdd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface EditListValidateParam_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface EditListValidateParam_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

export interface Erp_Tablesets_NatAcctMassUpdateRow{
      /**  Chart of Accounts header table  */  
   COACode:string,
      /**   COA category Types -                
Values:
A - All
B - Balance Sheet
I - Income Statement  */  
   AcctType:string,
      /**  COA Categories  */  
   COACat:string,
      /**  Natural Account Segment Ranges  */  
   SegRanges:string,
      /**  COA Description  */  
   COADescription:string,
      /**  COA is Master  */  
   COAMaster:boolean,
      /**  Indicates if the segment is active. Transactions cannot be posted to inactive segments  */  
   ActiveFlag:boolean,
      /**  Override Active flag.  */  
   ActiveFlagOrd:boolean,
      /**  Category description  */  
   CategoryDesc:string,
      /**  Override Category flag.  */  
   CategoryOrd:boolean,
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
      /**   0)      Summarize (default)   
1)      Summarize debit and credits separately
2)      No summarization  */  
   Summarization:number,
      /**  Summarization description  */  
   SummarizationDesc:string,
      /**  Override summarization flag.  */  
   SummarizationOrd:boolean,
      /**  Override external analysis code flag.  */  
   ExtAnalysisCodeOrd:boolean,
      /**  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  */  
   Category:string,
      /**   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  */  
   ValOption:string,
      /**  CurrencyAcctType  */  
   CurrencyAcctType:string,
      /**  RevalueOpt  */  
   RevalueOpt:number,
      /**  Rate type used for credit balances  */  
   CreditRateType:string,
      /**  Rate type used for debit balances.  */  
   DebitRateType:string,
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
      /**  Chart of Accounts Segment Values Currency Accounts List.  */  
   COASegAcct:string,
      /**  GLGainAcctContext  */  
   GLGainAcctContext:string,
      /**  GLLossAcctContext  */  
   GLLossAcctContext:string,
   NewCurrency:boolean,
   OverrideCurrency:boolean,
   OverrideRT:boolean,
   ReplaceCurrency:boolean,
      /**   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  */  
   Statistical:number,
      /**  Override statistical flag.  */  
   StatisticalOrd:boolean,
      /**  StatUOMCode  */  
   StatUOMCode:string,
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

export interface Erp_Tablesets_NatAcctMassUpdateTableset{
   NatAcctMassUpdate:Erp_Tablesets_NatAcctMassUpdateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GetDefaults_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface GetDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

export interface GetNewParameters_output{
   returnObj:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

   /** Required : 
      @param ds
   */  
export interface GetParamTaskDef_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface GetParamTaskDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
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
   returnObj:Erp_Tablesets_NatAcctMassUpdateTableset[],
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
      @param AnalysisCd
      @param ds
   */  
export interface OnAnalysisCodeChange_input{
      /**  Analysis Code  */  
   AnalysisCd:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface OnAnalysisCodeChange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ds
   */  
export interface OnCOACodeChanging_input{
      /**  Proposed COACode  */  
   ipCOACode:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface OnCOACodeChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSegmentNbr
      @param ipSegmentCode
   */  
export interface OnCOASegValuesChanging_input{
      /**  COA Code  */  
   ipCOACode:string,
      /**  Segment number  */  
   ipSegmentNbr:number,
      /**  Proposed Segment Value  */  
   ipSegmentCode:string,
}

export interface OnCOASegValuesChanging_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedCategory
      @param isReverse
      @param ds
   */  
export interface OnCategoryChanging_input{
      /**  The proposed Category  */  
   proposedCategory:string,
      /**  Is true if the Category combo is for the reverse category  */  
   isReverse:boolean,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface OnCategoryChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
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
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface RunDirect_output{
}

   /** Required : 
      @param ds
   */  
export interface SaveDefaults_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface SaveDefaults_output{
}

   /** Required : 
      @param maintProgram
      @param ds
   */  
export interface SaveProcessTask_input{
   maintProgram:string,
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
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
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
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
      @param ipCurrencyAcct
      @param CurrencyAcctType
   */  
export interface ValidateCurrencyAccountType_input{
      /**  Flag identifying the segment as a currency account  */  
   ipCurrencyAcct:boolean,
      /**  Currency Account Type  */  
   CurrencyAcctType:string,
}

export interface ValidateCurrencyAccountType_output{
}

   /** Required : 
      @param ds
   */  
export interface ValidateCurrencyAccounts_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface ValidateCurrencyAccounts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

   /** Required : 
      @param ipCOACode
      @param ipSubSegmentNbr
      @param ipSegmentCode
   */  
export interface ValidateDefaultSegment_input{
   ipCOACode:string,
   ipSubSegmentNbr:number,
   ipSegmentCode:string,
}

export interface ValidateDefaultSegment_output{
}

   /** Required : 
      @param ipCOACode
      @param ipSubSegmentNbr
   */  
export interface ValidateSubSegment_input{
   ipCOACode:string,
   ipSubSegmentNbr:number,
}

export interface ValidateSubSegment_output{
}

   /** Required : 
      @param ds
   */  
export interface checkForNaturalAccountControl_input{
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}

export interface checkForNaturalAccountControl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_NatAcctMassUpdateTableset[],
}
}

