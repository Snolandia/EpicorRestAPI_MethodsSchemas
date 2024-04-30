import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ReceiptsFromMfgSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/$metadata", {
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

   /**  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReceiptsFromMfgJobAsmblRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReceiptsFromMfgJobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReceiptsFromMfgJobAsmblRow)
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
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetRows
      @param whereClauseJobHead Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param whereClauseJobAsmbl Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJobHead:string, whereClauseJobAsmbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
   }
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetRows" + params, {
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
   Summary: Invoke method GetList
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetList
      @param whereClauseJobHead Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param whereClauseJobAsmbl Desc: Where condition without the where word   Required: True   Allow empty value : True
      @param pageSize Desc: # of records returned.  0 means all   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClauseJobHead:string, whereClauseJobAsmbl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
   }
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
   }
   if(typeof pageSize!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "pageSize=" + pageSize
   }
   if(typeof absolutePage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "absolutePage=" + absolutePage
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   Description: Check Package Code Allocated negative quantity.
   OperationID: CheckPackageCodeAllocNegQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPackageCodeAllocNegQty(requestBody:CheckPackageCodeAllocNegQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPackageCodeAllocNegQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/CheckPackageCodeAllocNegQty", {
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
         resolve(data as CheckPackageCodeAllocNegQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get Available Transaction Doc Types.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultTranDocTypeID
   Description: Get default trandoctypeid.
   OperationID: GetDefaultTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultTranDocTypeID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetDefaultTranDocTypeID", {
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
         resolve(data as GetDefaultTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultWhseBin
   Description: Get Warehouse Code for PCID.
   OperationID: GetDefaultWhseBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultWhseBin(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultWhseBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetDefaultWhseBin", {
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
         resolve(data as GetDefaultWhseBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCIDParamsRow
   Description: Creates a new PCID Parameter row used to contain the PCID receipt to inventory default information.
   OperationID: GetNewPCIDParamsRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCIDParamsRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDParamsRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCIDParamsRow(requestBody:GetNewPCIDParamsRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCIDParamsRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewPCIDParamsRow", {
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
         resolve(data as GetNewPCIDParamsRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsValidAssembly
   Description: Returns logical true if the assembly is valid and false otherwise.
   OperationID: IsValidAssembly
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsValidAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsValidAssembly(requestBody:IsValidAssembly_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsValidAssembly_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/IsValidAssembly", {
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
         resolve(data as IsValidAssembly_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: <param name="pcPartNum"></param>
<param name="pcWhseCode"></param>
<param name="pcBinNum"></param>
<param name="pcLotNum"></param>
<param name="pcAttributeSetID"></param>
<param name="pcPCID"></param>
<param name="pcDimCode"></param>
<param name="pdDimConvFactor"></param>
<param name="ipSellingQuantity"></param>
<param name="pcNeqQtyAction"></param>
<param name="pcMessage"></param>
   OperationID: NegativeInventoryTest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:NegativeInventoryTest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NegativeInventoryTest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/NegativeInventoryTest", {
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
         resolve(data as NegativeInventoryTest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWhsePCID
   Description: Validates warehouse for PCID
   OperationID: ValidateWhsePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhsePCID(requestBody:ValidateWhsePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWhsePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidateWhsePCID", {
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
         resolve(data as ValidateWhsePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWhsePCIDAndGetDefaultBin
   Description: Validates warehouse for PCID and returns a bin if there is only one available.
   OperationID: ValidateWhsePCIDAndGetDefaultBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhsePCIDAndGetDefaultBin(requestBody:ValidateWhsePCIDAndGetDefaultBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWhsePCIDAndGetDefaultBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidateWhsePCIDAndGetDefaultBin", {
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
         resolve(data as ValidateWhsePCIDAndGetDefaultBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWhseBinPCID
   Description: Validates BinNum for PCID
   OperationID: ValidateWhseBinPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWhseBinPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhseBinPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhseBinPCID(requestBody:ValidateWhseBinPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWhseBinPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidateWhseBinPCID", {
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
         resolve(data as ValidateWhseBinPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePCIDExists
   Description: Validate PCID Exists
   OperationID: ValidatePCIDExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePCIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePCIDExists(requestBody:ValidatePCIDExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePCIDExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidatePCIDExists", {
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
         resolve(data as ValidatePCIDExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPCID
   Description: Get PCID
   OperationID: GetPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCID(requestBody:GetPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetPCID", {
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
         resolve(data as GetPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExecuteProcessPCID
   Description: Execute Process a PCID
   OperationID: ExecuteProcessPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExecuteProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteProcessPCID(requestBody:ExecuteProcessPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExecuteProcessPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ExecuteProcessPCID", {
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
         resolve(data as ExecuteProcessPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePCID
   Description: Validates PCID
   OperationID: ValidatePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePCID(requestBody:ValidatePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidatePCID", {
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
         resolve(data as ValidatePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobAsmblMultiple
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewJobAsmblMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmblMultiple(requestBody:GetNewJobAsmblMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobAsmblMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewJobAsmblMultiple", {
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
         resolve(data as GetNewJobAsmblMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobAsmblSearch
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewJobAsmblSearch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmblSearch(requestBody:GetNewJobAsmblSearch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobAsmblSearch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewJobAsmblSearch", {
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
         resolve(data as GetNewJobAsmblSearch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromMfg
   Description: This method creates a new ttPartTran row entry.
   OperationID: GetNewReceiptsFromMfg
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromMfg(requestBody:GetNewReceiptsFromMfg_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromMfg_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromMfg", {
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
         resolve(data as GetNewReceiptsFromMfg_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFromJob
   Description: validate from job
   OperationID: ValidateFromJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFromJob(requestBody:ValidateFromJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFromJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidateFromJob", {
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
         resolve(data as ValidateFromJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromMfgJobAsm
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewReceiptsFromMfgJobAsm
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfgJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfgJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromMfgJobAsm(requestBody:GetNewReceiptsFromMfgJobAsm_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromMfgJobAsm_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromMfgJobAsm", {
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
         resolve(data as GetNewReceiptsFromMfgJobAsm_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromMfgMtlQueue
   Description: This method creates a new ReceiptsFromMfgDataSet using MtlQueue RowIdent.
   OperationID: GetNewReceiptsFromMfgMtlQueue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfgMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfgMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromMfgMtlQueue(requestBody:GetNewReceiptsFromMfgMtlQueue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromMfgMtlQueue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromMfgMtlQueue", {
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
         resolve(data as GetNewReceiptsFromMfgMtlQueue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromPCID
   Description: creates job receipt to inventory transactions for the selected PCID.
   OperationID: GetNewReceiptsFromPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromPCID(requestBody:GetNewReceiptsFromPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromPCID", {
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
         resolve(data as GetNewReceiptsFromPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromPCIDMultiple
   Description: Creates job receipt to inventory transactions for the selected PCIDs.
   OperationID: GetNewReceiptsFromPCIDMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCIDMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCIDMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromPCIDMultiple(requestBody:GetNewReceiptsFromPCIDMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromPCIDMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromPCIDMultiple", {
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
         resolve(data as GetNewReceiptsFromPCIDMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReceiptsFromPCIDSupplyJobNum
   Description: Creates job receipt to inventory transactions for PCIDs associated with a JobNumber.
   OperationID: GetNewReceiptsFromPCIDSupplyJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCIDSupplyJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCIDSupplyJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReceiptsFromPCIDSupplyJobNum(requestBody:GetNewReceiptsFromPCIDSupplyJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReceiptsFromPCIDSupplyJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetNewReceiptsFromPCIDSupplyJobNum", {
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
         resolve(data as GetNewReceiptsFromPCIDSupplyJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUpdate(requestBody:PreUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/PreUpdate", {
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
         resolve(data as PreUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreProcessPCID
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreProcessPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcessPCID(requestBody:PreProcessPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreProcessPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/PreProcessPCID", {
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
         resolve(data as PreProcessPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessPCID
   Description: Process a PCID
   OperationID: ProcessPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessPCID(requestBody:ProcessPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ProcessPCID", {
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
         resolve(data as ProcessPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveMfgPartToInventory
   Description: Update the Receipts from Manufacturing to Inventory.
   OperationID: ReceiveMfgPartToInventory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPartToInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPartToInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveMfgPartToInventory(requestBody:ReceiveMfgPartToInventory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveMfgPartToInventory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ReceiveMfgPartToInventory", {
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
         resolve(data as ReceiveMfgPartToInventory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveMfgPartToJob
   Description: Update the Receipts from Manufacturing to Job.
   OperationID: ReceiveMfgPartToJob
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPartToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPartToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveMfgPartToJob(requestBody:ReceiveMfgPartToJob_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveMfgPartToJob_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ReceiveMfgPartToJob", {
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
         resolve(data as ReceiveMfgPartToJob_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveMfgPCIDtoInventory
   Description: Receives a PCID at WIPFG status into Inventory.
   OperationID: ReceiveMfgPCIDtoInventory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPCIDtoInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPCIDtoInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveMfgPCIDtoInventory(requestBody:ReceiveMfgPCIDtoInventory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveMfgPCIDtoInventory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ReceiveMfgPCIDtoInventory", {
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
         resolve(data as ReceiveMfgPCIDtoInventory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveMfgPCIDtoInventoryMultiple
   Description: Receives multiple PCIDs which are at status WIPFG into inventory.
   OperationID: ReceiveMfgPCIDtoInventoryMultiple
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPCIDtoInventoryMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPCIDtoInventoryMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveMfgPCIDtoInventoryMultiple(requestBody:ReceiveMfgPCIDtoInventoryMultiple_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveMfgPCIDtoInventoryMultiple_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ReceiveMfgPCIDtoInventoryMultiple", {
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
         resolve(data as ReceiveMfgPCIDtoInventoryMultiple_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReceiveSalvagedPartToInventory
   Description: Update Salvaged Material to Inventory.
   OperationID: ReceiveSalvagedPartToInventory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReceiveSalvagedPartToInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveSalvagedPartToInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReceiveSalvagedPartToInventory(requestBody:ReceiveSalvagedPartToInventory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReceiveSalvagedPartToInventory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ReceiveSalvagedPartToInventory", {
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
         resolve(data as ReceiveSalvagedPartToInventory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeActTranQty
   Description: Change the PartTran values based on the new value of PartTran.ActTranQty.
   OperationID: OnChangeActTranQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeActTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeActTranQty(requestBody:OnChangeActTranQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeActTranQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeActTranQty", {
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
         resolve(data as OnChangeActTranQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCalculateExtCost
   Description: Calculate Extend unit Cost
   OperationID: OnChangeCalculateExtCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCalculateExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalculateExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCalculateExtCost(requestBody:OnChangeCalculateExtCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCalculateExtCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeCalculateExtCost", {
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
         resolve(data as OnChangeCalculateExtCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeActTransUOM
   Description: Call this method when the value of Epicor.Mfg.BO.PartTran.ActTransUOM changes.
   OperationID: OnChangeActTransUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeActTransUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActTransUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeActTransUOM(requestBody:OnChangeActTransUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeActTransUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeActTransUOM", {
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
         resolve(data as OnChangeActTransUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssemblySeq
   Description: Change the PartTran values based on the new PartTran.AssemblySeq.
   OperationID: OnChangeAssemblySeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssemblySeq(requestBody:OnChangeAssemblySeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssemblySeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeAssemblySeq", {
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
         resolve(data as OnChangeAssemblySeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssemblySeq2
   Description: Change the PartTran values based on the new value of PartTran.AssemblySeq2.
   OperationID: OnChangeAssemblySeq2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssemblySeq2(requestBody:OnChangeAssemblySeq2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssemblySeq2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeAssemblySeq2", {
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
         resolve(data as OnChangeAssemblySeq2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.ReceiptsFromMfgDataSet.BinNum changes.
   OperationID: OnChangeBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:OnChangeBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeBinNum", {
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
         resolve(data as OnChangeBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: When the user enters the Job# in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:OnChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeJobNum", {
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
         resolve(data as OnChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeExtCost
   Description: Calculate extended cost
   OperationID: OnChangeExtCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeExtCost(requestBody:OnChangeExtCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeExtCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeExtCost", {
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
         resolve(data as OnChangeExtCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum2
   Description: Change the PartTran values based on the new value of PartTran.JobNum2.
   OperationID: OnChangeJobNum2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum2(requestBody:OnChangeJobNum2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobNum2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeJobNum2", {
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
         resolve(data as OnChangeJobNum2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobSeq2
   Description: Change the PartTran values based on the new value of PartTran.JobSeq2.
   OperationID: OnChangeJobSeq2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobSeq2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobSeq2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobSeq2(requestBody:OnChangeJobSeq2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobSeq2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeJobSeq2", {
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
         resolve(data as OnChangeJobSeq2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLotNum
   Description: Change the PartTran values based on the new value of PartTran.LotNum.
   OperationID: OnChangeLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNum(requestBody:OnChangeLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeLotNum", {
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
         resolve(data as OnChangeLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOverrideCost
   Description: Recalculate the PartTran unit cost values when the user unchecks the Override Cost toggle box.
   OperationID: OnChangeOverrideCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOverrideCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOverrideCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOverrideCost(requestBody:OnChangeOverrideCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOverrideCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeOverrideCost", {
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
         resolve(data as OnChangeOverrideCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: When the user changes the PartNum in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangingAttributeSet", {
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
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamsPlant
   Description: Validate PCID defaults to site and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamsPlant(requestBody:OnChangePCIDParamsPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamsPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamsPlant", {
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
         resolve(data as OnChangePCIDParamsPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamWarehouseCode
   Description: Validate PCID defaults to Warehouse code and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamWarehouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamWarehouseCode(requestBody:OnChangePCIDParamWarehouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamWarehouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamWarehouseCode", {
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
         resolve(data as OnChangePCIDParamWarehouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeToPCID
   Description: Call this method when the value of To PCID changes.
   OperationID: OnChangeToPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToPCID(requestBody:OnChangeToPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeToPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeToPCID", {
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
         resolve(data as OnChangeToPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFromPCID
   Description: Call this method when the value of From PCID changes.
   OperationID: OnChangeFromPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromPCID(requestBody:OnChangeFromPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFromPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeFromPCID", {
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
         resolve(data as OnChangeFromPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamsBinNum
   Description: Validate PCID defaults To Bin and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamsBinNum(requestBody:OnChangePCIDParamsBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamsBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamsBinNum", {
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
         resolve(data as OnChangePCIDParamsBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamsTranDate
   Description: Change the PCID defaults Transaction date and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamsTranDate(requestBody:OnChangePCIDParamsTranDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamsTranDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamsTranDate", {
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
         resolve(data as OnChangePCIDParamsTranDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamsTranReference
   Description: Called when changing the PCID defaults transaction reference and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranReference
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamsTranReference(requestBody:OnChangePCIDParamsTranReference_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamsTranReference_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamsTranReference", {
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
         resolve(data as OnChangePCIDParamsTranReference_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCIDParamsTranDocTypeID
   Description: Validate the PCID defaults transaction document type and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranDocTypeID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCIDParamsTranDocTypeID(requestBody:OnChangePCIDParamsTranDocTypeID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCIDParamsTranDocTypeID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePCIDParamsTranDocTypeID", {
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
         resolve(data as OnChangePCIDParamsTranDocTypeID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePlant
   Description: When the user changes the Plant2 in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangePlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePlant(requestBody:OnChangePlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangePlant", {
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
         resolve(data as OnChangePlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWareHouseCode
   Description: When the user changes the WareHouseCode in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangeWareHouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWareHouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWareHouseCode(requestBody:OnChangeWareHouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWareHouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeWareHouseCode", {
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
         resolve(data as OnChangeWareHouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSalvageJobSeq
   Description: Change the PartTran values based on the new PartTran.JobSeq.
This method is used while receiving Salvaged material to Inventory.
   OperationID: OnChangeSalvageJobSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSalvageJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalvageJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSalvageJobSeq(requestBody:OnChangeSalvageJobSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSalvageJobSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeSalvageJobSeq", {
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
         resolve(data as OnChangeSalvageJobSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSalvagePartNum
   Description: Change the PartTran values based on the new PartTran.PartNum.
This method is used while receiving Salvaged material to Inventory.
   OperationID: OnChangeSalvagePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSalvagePartNum(requestBody:OnChangeSalvagePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSalvagePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeSalvagePartNum", {
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
         resolve(data as OnChangeSalvagePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranQty
   Description: Change the PartTran values based on the new value of PartTran.TranQty.
   OperationID: OnChangeTranQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranQty(requestBody:OnChangeTranQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTranQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangeTranQty", {
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
         resolve(data as OnChangeTranQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangingRevisionNum", {
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
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNumMS
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNumMS
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumMS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumMS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNumMS(requestBody:OnChangingRevisionNumMS_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNumMS_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/OnChangingRevisionNumMS", {
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
         resolve(data as OnChangingRevisionNumMS_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method EnableSerialMatching
   Description: Validates if the option Serial Matching should be enabled.
   OperationID: EnableSerialMatching
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/EnableSerialMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSerialMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableSerialMatching(requestBody:EnableSerialMatching_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnableSerialMatching_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/EnableSerialMatching", {
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
         resolve(data as EnableSerialMatching_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:GetSelectSerialNumbersParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectSerialNumbersParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/GetSelectSerialNumbersParams", {
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
         resolve(data as GetSelectSerialNumbersParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:ValidateSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/ValidateSN", {
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
         resolve(data as ValidateSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifySerialMatchAndPlanContract
   Description: Verifies if the user should enter child serial numbers for the serial numbers
being received depending on the setting of the Serial Number Matching before save.
   OperationID: VerifySerialMatchAndPlanContract
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifySerialMatchAndPlanContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySerialMatchAndPlanContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifySerialMatchAndPlanContract(requestBody:VerifySerialMatchAndPlanContract_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifySerialMatchAndPlanContract_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/VerifySerialMatchAndPlanContract", {
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
         resolve(data as VerifySerialMatchAndPlanContract_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReceiptsFromMfgJobAsmblRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ReceiptsFromMfgJobAsmblRow,
}

export interface Erp_Tablesets_ReceiptsFromMfgJobAsmblRow{
   "Company":string,
   "JobNum":string,
   "AssemblySeq":number,
   "PartNum":string,
   "Description":string,
   "QtyCompleted":number,
   "JobHeadPartNum":string,
   "JobHeadPartDescription":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipcalledFrom
      @param ipPackageCode
      @param ipQty
   */  
export interface CheckPackageCodeAllocNegQty_input{
   ipcalledFrom:string,
   ipPackageCode:string,
   ipQty:number,
}

export interface CheckPackageCodeAllocNegQty_output{
parameters : {
      /**  output parameters  */  
   opWarning:string,
   opAction:string,
   opAllocWarning:string,
   opAllocAction:string,
}
}

   /** Required : 
      @param ds
   */  
export interface EnableSerialMatching_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface EnableSerialMatching_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   plEnable:boolean,
}
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDReceiptsParamsRow{
   BinNum:string,
   Plant2:string,
   Plant2Name:string,
   PreviousPCID:string,
   TranDate:string,
   TranDocTypeID:string,
   TranReference:string,
   WareHouseCode:string,
   WarehouseDescription:string,
   BinNumDescription:string,
      /**  Set to True if multiple PCIDs have been selected for processing  */  
   EnableReceiveAllPCIDs:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDReceiptsSelectedRow{
   PCID:string,
   Company:string,
   ActTranQty:number,
   ActTransUOM:string,
   PartNum:string,
   SupplyJobNum:string,
   TrackLots:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  */  
   TranClass:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  */  
   CostMethod:string,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Assembly Sequence #  */  
   AssemblySeq:number,
      /**   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  */  
   JobSeqType:string,
      /**  Seq # of specific material or subcontract operation record.  */  
   JobSeq:number,
      /**  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  */  
   PackType:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  */  
   PackLine:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**  The line # of detail record on the purchase order.  */  
   POLine:number,
      /**  Purchase Order Release # of the POSched record that this transaction is for.  */  
   PORelNum:number,
      /**  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  */  
   WareHouse2:string,
      /**  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  */  
   BinNum2:string,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**  The sales order line that this transaction is associated with.  */  
   OrderLine:number,
      /**  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  */  
   OrderRelNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  */  
   PartDescription:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  */  
   VendorNum:number,
      /**  Vendor purchase point ID. (see VendorNum)  */  
   PurPoint:string,
      /**  Quantity received against a purchase order in the vendors unit of measure.  */  
   POReceiptQty:number,
      /**  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  */  
   POUnitCost:number,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  */  
   InvoiceNum:string,
      /**  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  */  
   InvoiceLine:number,
      /**  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  */  
   InvAdjSrc:string,
      /**  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  */  
   InvAdjReason:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  Transfer "From/To" lot number.  */  
   LotNum2:string,
      /**  Transfer "From/To" Part Dimension  */  
   DimCode2:string,
      /**  Transfer "From/To" Dimension unit of measure.  */  
   DUM2:string,
      /**  Transfer "From/To" Dimension conversion factor.  */  
   DimConvFactor2:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  */  
   GLTrans:boolean,
      /**  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  */  
   Costed:boolean,
      /**  DMR number used to identify the related DMR record.  */  
   DMRNum:number,
      /**  DMR action number  */  
   ActionNum:number,
      /**  RMA Number  */  
   RMANum:number,
      /**   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  */  
   COSPostingReqd:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Site Identifier.  */  
   Plant2:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Reference to the service call line  that the material is being issued for.  */  
   CallLine:number,
      /**  Reference to the service call line Material sequence that the material is being issued for.  */  
   MatNum:number,
      /**  Job Number of transfer source/target.  */  
   JobNum2:string,
      /**  Assembly Sequence  of transfer source/target.  */  
   AssemblySeq2:number,
      /**  Seq # of transfer source/target.  */  
   JobSeq2:number,
      /**   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  */  
   CustNum:number,
      /**  Line number of the related RMADtl record.  */  
   RMALine:number,
      /**  RMA Receipt  */  
   RMAReceipt:number,
      /**  RMA Disposition  */  
   RMADisp:number,
      /**  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  */  
   OtherDivValue:number,
      /**  Site Transaction Number  */  
   PlantTranNum:number,
      /**  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  */  
   NonConfID:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  Link to the related GLRefTyp.RefType.  */  
   RefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   RefCode:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  On Hand Quantity before the part costing calculations were run.  */  
   BeginQty:number,
      /**  On Hand Quantity after part costing calculation were run.  */  
   AfterQty:number,
      /**  Burden Unit cost before the part costing calculation was run  */  
   BegBurUnitCost:number,
      /**  Labor Unit cost before the costing calculation was run  */  
   BegLbrUnitCost:number,
      /**  Material Burden Unit Cost before the costing calculation was run  */  
   BegMtlBurUnitCost:number,
      /**  Material Unit Cost before the costing calculation was run  */  
   BegMtlUnitCost:number,
      /**  Sub Contract Unit Cost before the costing calculation was run  */  
   BegSubUnitCost:number,
      /**  Burden Unit cost after the part costing calculation was run  */  
   AfterBurUnitCost:number,
      /**  Labor Unit Cost after the costing calculation was run  */  
   AfterLbrUnitCost:number,
      /**  Material Burden Unit Cost after the costing calculation was run  */  
   AfterMtlBurUnitCost:number,
      /**  Material Unit Cost after the costing calculation was run  */  
   AfterMtlUnitCost:number,
      /**  Sub Contract Unit Cost after the costing calculation was run  */  
   AfterSubUnitCost:number,
      /**  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  */  
   PlantCostValue:number,
      /**  The Shop Employee ID of the user that created this transaction.  */  
   EmpID:string,
      /**  The unique identifier of the DemandReconcile that created this PartTran record.  */  
   ReconcileNum:number,
      /**  Id to the Cost Set Group that is used as the default CostGrp.  */  
   CostID:string,
      /**  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  */  
   FIFODate:string,
      /**  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  */  
   FIFOSeq:number,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM:string,
      /**  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  */  
   InvtyUOM2:string,
      /**   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  */  
   FIFOAction:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CCYear:number,
      /**  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  */  
   CCMonth:number,
      /**  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  */  
   CycleSeq:number,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  */  
   BaseCostMethod:string,
      /**   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  */  
   RevertStatus:number,
      /**  Reference on revert line  by SySRowID.  */  
   RevertID:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  */  
   VarTarget:string,
      /**  The FIFO subsequence number of the related PartFIFOCost record.  */  
   FIFOSubSeq:number,
      /**  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlUnitCost:number,
      /**  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltLbrUnitCost:number,
      /**  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltBurUnitCost:number,
      /**  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltSubUnitCost:number,
      /**  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltMtlBurUnitCost:number,
      /**  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  */  
   AltExtCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlMtlUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlLabUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlSubUnitCost:number,
      /**  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  */  
   AltMtlBurdenUnitCost:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Invoice Number from Progress Billing Invoice preparation  */  
   PBInvNum:number,
      /**   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  */  
   LoanFlag:string,
      /**  Unique identifier of the Asset.  */  
   AssetNum:string,
      /**  Unique number to identify the Addition activity of an asset.  */  
   AdditionNum:number,
      /**  Unique number to identify the Disposal activity of an asset.  */  
   DisposalNum:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used by Project Analysis process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process  */  
   AsOfSeq:number,
      /**  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  */  
   MscNum:number,
      /**  ODC Unit Cost  */  
   ODCUnitCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  TranRefType  */  
   TranRefType:number,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  ExtMtlCost  */  
   ExtMtlCost:number,
      /**  ExtLbrCost  */  
   ExtLbrCost:number,
      /**  ExtBurCost  */  
   ExtBurCost:number,
      /**  ExtSubCost  */  
   ExtSubCost:number,
      /**  ExtMtlBurCost  */  
   ExtMtlBurCost:number,
      /**  ExtMtlMtlCost  */  
   ExtMtlMtlCost:number,
      /**  ExtMtlLabCost  */  
   ExtMtlLabCost:number,
      /**  ExtMtlSubCost  */  
   ExtMtlSubCost:number,
      /**  ExtMtlBurdenCost  */  
   ExtMtlBurdenCost:number,
      /**  MYImportNum  */  
   MYImportNum:string,
      /**  AutoReverse  */  
   AutoReverse:boolean,
      /**  RevTranNum  */  
   RevTranNum:number,
      /**  RevSysDate  */  
   RevSysDate:string,
      /**  RevSysTime  */  
   RevSysTime:number,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  WIPPCID  */  
   WIPPCID:string,
      /**  WIPPCID2  */  
   WIPPCID2:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
   DIMDescription:string,
      /**  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  */  
   DisableFieldPart:boolean,
      /**  Display format of System Time in Hrs:Min.  */  
   DispSysTime:string,
   DispUOM:string,
   dummyKeyField:string,
   EnableSerialNumbers:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
      /**  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  */  
   FullPhysical:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Inventory subcontract unit cost  */  
   InvBurUnitCost:number,
      /**  Inventory Labor unit cost.  */  
   InvLbrUnitCost:number,
      /**  Inventory burden unit cost  */  
   InvMtlBurUnitCost:number,
      /**  Inventory material unit cost  */  
   InvMtlUnitCost:number,
      /**  Inventory subcontract unit cost.  */  
   InvSubUnitCost:number,
   IssuedComplete:boolean,
   JobBurUnitCost:number,
   JobLbrUnitCost:number,
   JobMtlBurUnitCost:number,
   JobMtlUnitCost:number,
   JobSubUnitCost:number,
   LegalNumberNumber:string,
   LegalNumberPrefix:string,
   LegalNumberPrefixList:string,
   LegalNumberReadOnlyFields:string,
   LegalNumberYear:number,
   MtlLbrUnitCost:number,
   MtlQueueRowId:string,
      /**  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  */  
   MultiEndParts:boolean,
   OnHandQty:number,
      /**  Override Costs.  Set to yes if the user chooses to override the cost.  */  
   OverRideCosts:boolean,
   PartDescriptionAsm:string,
   PartDescriptionJH:string,
   PartDescriptionMS:string,
   PartDescriptionSP:string,
   PartNumAsm:string,
   PartNumJH:string,
   PartNumMS:string,
   PartNumSP:string,
   QtyAvailToComplete:number,
   QtyBearing:boolean,
      /**  Quantity Completed  */  
   QtyCompleted:number,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   SalvageQtyToDate:number,
   SerialNoTempTranID:number,
   ThisTranQty:number,
      /**  Transaction Amount  */  
   TranAmount:number,
   TreeDisplay:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
      /**  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
   CostMethodDisplay:string,
      /**  Number of pieces for inventory attribute tracked parts  */  
   DispNumberOfPieces:number,
   RevisionNumAsm:string,
   RevisionNumMS:string,
   RevisionNumSP:string,
   PlantConfCtrlEnablePackageControl:boolean,
      /**  Description for AttributeSetID associated with PartNumMS  */  
   AttributeSetDescriptionMS:string,
      /**  AttributeSetID associated with PartNumMS  */  
   AttributeSetIDMS:number,
      /**  AttributeSetShortDescription associated with PartNumMS  */  
   AttributeSetShortDescriptionMS:string,
   BitFlag:number,
   AssemblySeqDescription:string,
   BinNumDescription:string,
   CallLineLineDesc:string,
   CustNumCustID:string,
   CustNumBTName:string,
   CustNumName:string,
   DimCodeDimCodeDescription:string,
   DMRNumPartDescription:string,
   FromBinDescription:string,
   FromPlantName:string,
   FromWareHouseDescription:string,
   InvoiceNumDescription:string,
   JobNumPartDescription:string,
   MatNumLineDesc:string,
   OrderLineLineDesc:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PackLineLineDesc:string,
   PackNumName:string,
   PartLotPartLotDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   POLineVenPartNum:string,
   POLinePartNum:string,
   POLineLineDesc:string,
   RMALineLineDesc:string,
   VendorNumName:string,
   VendorNumAddress3:string,
   VendorNumDefaultFOB:string,
   VendorNumCurrencyCode:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumAddress2:string,
   VendorNumVendorID:string,
   VendorNumCountry:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumTermsCode:string,
   VendorPPNumAddress1:string,
   VendorPPNumAddress2:string,
   VendorPPNumPrimPCon:number,
   VendorPPNumAddress3:string,
   VendorPPNumCountry:string,
   VendorPPNumState:string,
   VendorPPNumZip:string,
   VendorPPNumCity:string,
   VendorPPNumName:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlHeaderRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Site where the PCID is currently located.  */  
   Plant:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  Warehouse where the PCID return stock needs to be returned to.  */  
   ReturnToWarehouseCode:string,
      /**  Warehouse Bin where the PCID return stock needs to be returned to.  */  
   ReturnToBinNum:string,
      /**  PCID current status.  */  
   PkgControlStatus:string,
      /**  PCID prior status.  */  
   PkgControlPriorStatus:string,
      /**  Label Print Control status.  */  
   LabelPrintControlStatus:string,
      /**  Label Print Control prior status.  */  
   LabelPrintControlPriorStatus:string,
      /**  If false then PCID is a single-level PCID that cannot be associated with a Parent.  */  
   AllowParentPCID:boolean,
      /**  If false then PCID must contain only one PartNum.  */  
   AllowMixedParts:boolean,
      /**  If false then PCID must contain only one LotNum for each Part on the PCID.  */  
   AllowMixedLots:boolean,
      /**  If false then PCID must contain only one UOM per Part on the PCID.  */  
   AllowMixedUOMs:boolean,
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  */  
   AllowMixedChildPCIDs:boolean,
      /**  If false then PCID must contain only one Serial Number per PCID.  */  
   AllowMultipleSerialNumPerPCID:boolean,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   LabelPrintControlled:boolean,
      /**  If false then the number of PCID label prints will not be tracked.  */  
   LabelPrintCounter:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  */  
   AllowVoids:boolean,
      /**  If false then PkgControlHeader and PkgControlItem cannot be deleted.  */  
   AllowDeletes:boolean,
      /**  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  */  
   ArchivePCIDHistory:boolean,
      /**  Unique packaging code assigned by the user.  */  
   PkgCode:string,
      /**  User defined code which uniquely identifies the UOM for length, width, and height.  */  
   LWHDimensionUOM:string,
      /**  Length dimension.  */  
   Length:number,
      /**  Width dimension.  */  
   Width:number,
      /**  Height dimension.  */  
   Height:number,
      /**  User defined code which uniquely identifies the UOM for volume.  */  
   VolumeUOM:string,
      /**  Volume.  */  
   Volume:number,
      /**  User defined code which uniquely identifies the UOM for weight.  */  
   WeightUOM:string,
      /**  Maximum Weight.  */  
   MaximumWeight:number,
      /**  Calculated Weight.  */  
   CalculatedWeight:number,
      /**  The total weight of the parts and the container combined.  */  
   TotalWeight:number,
      /**  Maximum number of PCIDs allowed if vertically stacked.  */  
   MaximumStack:number,
      /**  Position Sequence within a parent PCID.  */  
   PositionSeq:number,
      /**  Trailer ID.  */  
   TrailerID:string,
      /**  Bond or Security Seal ID.  */  
   SecuritySealID:string,
      /**  Raw PCID as scanned or generated.  */  
   RawPCIDLicensePlate:string,
      /**  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  */  
   GS1128:string,
      /**  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  */  
   PkgControlCollapseCounter:number,
      /**  System date and time when the row was created.  */  
   CreatedDate:string,
      /**  The user ID that created this row.  */  
   CreatedBy:string,
      /**  System date and time when the row was last updated.  */  
   UpdatedDate:string,
      /**  The user ID that last updated this row.  */  
   UpdatedBy:string,
      /**  Last PCID Scanned.  */  
   LastPCIDScanned:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
      /**  Flag used to fire the auto print rule that will print the labels.  */  
   AutoPrint:boolean,
      /**  System date and time when the row was created.  */  
   LPCCreatedDate:string,
      /**  The user ID that created this record.  */  
   LPCCreatedBy:string,
      /**  Printer ID that printed the label.  */  
   LPCPrinterID:string,
      /**  User that printed the label.  */  
   LPCPrintedBy:string,
      /**  Label feature. Displays what transaction the label was printed from.  */  
   LPCPrintedFromTx:string,
      /**  Ad Hoc feature. Displays what transaction type the label was printed from.  */  
   LPCPrintedFromTxType:string,
      /**  The job for which the label was printed.  */  
   LPCJobNum:string,
      /**  The operation sequence for which the label was printed.  */  
   LPCOprSeq:number,
      /**  The assembly sequence for which the label was printed.  */  
   LPCAssemblySeq:number,
      /**  Shift that the label was created on or shift entered in Ad Hoc print program.  */  
   LPCShift:number,
      /**  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  */  
   LPCOperatorEmpID:string,
      /**  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  */  
   OriginalSourcePCID:string,
      /**  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  */  
   OverlaidByPCID:string,
      /**  Set to True when PCID has been overlaid using the overlay feature.  */  
   Overlaid:boolean,
      /**  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  */  
   ContainerPartial:boolean,
      /**  If true the container was repacked.  */  
   ContainerRepacked:boolean,
      /**  If true the container used is a returnable container.  */  
   ContainerReturnable:boolean,
      /**  Our Vendor ID for the Customer being Shipped To.  */  
   OurSupplierCode:string,
      /**  Site Name.  */  
   PlantName:string,
      /**  Site Address line 1.  */  
   PlantAddress1:string,
      /**  Site Address line 2.  */  
   PlantAddress2:string,
      /**  Site Address line 3.  */  
   PlantAddress3:string,
      /**  Site City.  */  
   PlantCity:string,
      /**  Site State.  */  
   PlantState:string,
      /**  Site Zip.  */  
   PlantZip:string,
      /**  Site Country Number.  */  
   PlantCountryNum:number,
      /**  Site Country Description.  */  
   PlantCountryDesc:string,
      /**  Site Phone.  */  
   PlantPhone:string,
      /**  Pack Number if applicable.  */  
   PackNum:number,
      /**  Ship To Customer Container Part Number.  */  
   CustContainerPartNum:string,
      /**  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  */  
   EDIShipToNum:string,
      /**  Ship To Number.  */  
   ShipToNum:string,
      /**  Name of the Ship To that the PCID is going to.  */  
   ShipToName:string,
      /**  Address line 1 of the Ship To that the PCID is going to.  */  
   ShipToAddress1:string,
      /**  Address line 2 of the Ship To that the PCID is going to.  */  
   ShipToAddress2:string,
      /**  Address line 3 of the Ship To that the PCID is going to.  */  
   ShipToAddress3:string,
      /**  City of the Ship To that the PCID is going to.  */  
   ShipToCity:string,
      /**  State of the Ship To that the PCID is going to.  */  
   ShipToState:string,
      /**  Zip of the Ship To that the PCID is going to.  */  
   ShipToZip:string,
      /**  Country number of the Ship To that the PCID is going to.  */  
   ShipToCountryNum:number,
      /**  Country of the Ship To that the PCID is going to.  */  
   ShipToCountryDesc:string,
      /**  The dock that the parts should be shipped to.  */  
   ShipToDock:string,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  Vendor Number.  */  
   VendorNum:number,
      /**  Vendor ID.  */  
   VendorID:string,
      /**  Vendor Purchase Point.  */  
   VendorPurPoint:string,
      /**  Vendor Address line 1.  */  
   VendorAddress1:string,
      /**  Vendor Address line 2.  */  
   VendorAddress2:string,
      /**  Vendor Address line 3.  */  
   VendorAddress3:string,
      /**  Vendor City.  */  
   VendorCity:string,
      /**  Vendor State.  */  
   VendorState:string,
      /**  Vendor Zip.  */  
   VendorZip:string,
      /**  Vendor Country Number.  */  
   VendorCountryNum:number,
      /**  Vendor Country Description.  */  
   VendorCountryDesc:string,
      /**  Our Dock ID.  */  
   OurDock:string,
      /**  Value to display on package control label.  */  
   LabelValue01:string,
      /**  Value to display on package control label.  */  
   LabelValue02:string,
      /**  Value to display on package control label.  */  
   LabelValue03:string,
      /**  Value to display on package control label.  */  
   LabelValue04:string,
      /**  Value to display on package control label.  */  
   LabelValue05:string,
      /**  Value to display on package control label.  */  
   LabelValue06:string,
      /**  Value to display on package control label.  */  
   LabelValue07:string,
      /**  Value to display on package control label.  */  
   LabelValue08:string,
      /**  Value to display on package control label.  */  
   LabelValue09:string,
      /**  Value to display on package control label.  */  
   LabelValue10:string,
      /**  Value to display on package control label.  */  
   LabelValue11:string,
      /**  Value to display on package control label.  */  
   LabelValue12:string,
      /**  Value to display on package control label.  */  
   LabelValue13:string,
      /**  Value to display on package control label.  */  
   LabelValue14:string,
      /**  Value to display on package control label.  */  
   LabelValue15:string,
      /**  Value to display on package control label.  */  
   LabelValue16:string,
      /**  Value to display on package control label.  */  
   LabelValue17:string,
      /**  Value to display on package control label.  */  
   LabelValue18:string,
      /**  Value to display on package control label.  */  
   LabelValue19:string,
      /**  Value to display on package control label.  */  
   LabelValue20:string,
      /**  Value to display on package control label.  */  
   LabelValue21:string,
      /**  Value to display on package control label.  */  
   LabelValue22:string,
      /**  Value to display on package control label.  */  
   LabelValue23:string,
      /**  Value to display on package control label.  */  
   LabelValue24:string,
      /**  Value to display on package control label.  */  
   LabelValue25:string,
      /**  Value to display on package control label.  */  
   LabelValue26:string,
      /**  Value to display on package control label.  */  
   LabelValue27:string,
      /**  Value to display on package control label.  */  
   LabelValue28:string,
      /**  Value to display on package control label.  */  
   LabelValue29:string,
      /**  Value to display on package control label.  */  
   LabelValue30:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter03:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter04:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter05:string,
      /**  Reserved for development use.  */  
   PkgControlDate01:string,
      /**  Reserved for development use.  */  
   PkgControlDate02:string,
      /**  Reserved for development use.  */  
   PkgControlBoolean01:boolean,
      /**  Reserved for development use.  */  
   PkgControlBoolean02:boolean,
      /**  Reserved for development use.  */  
   PkgControlInteger01:number,
      /**  Reserved for development use.  */  
   PkgControlInteger02:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal01:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal02:number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   PkgControlType:string,
      /**  Package Control ID Code.  */  
   PkgControlIDCode:string,
      /**  External Length dimension.  */  
   ExternalLength:number,
      /**  External Width dimension.  */  
   ExternalWidth:number,
      /**  External Height dimension.  */  
   ExternalHeight:number,
      /**  External Volume.  */  
   ExternalVolume:number,
      /**  Tare Weight.  */  
   TareWeight:number,
      /**  Incremental tally of number of times PCID label has been printed.  */  
   LabelPrintCount:number,
      /**  Indicates if the expendable PCID will be tracked.  */  
   TrackExpendable:boolean,
      /**  Indicates if the returnable PCID will be tracked.  */  
   TrackReturnable:boolean,
      /**  Label Type.  */  
   LabelType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Ship To Customer Number.  */  
   CustNum:number,
      /**  Indicates if the PCID is expendable.  */  
   ContainerExpendable:boolean,
      /**  Ship To Customer ID.  */  
   CustID:string,
      /**  Ship To Customer Name.  */  
   CustName:string,
      /**  Vendor Name.  */  
   VendorName:string,
      /**  Vendor Purchase Point Name.  */  
   VendorPPName:string,
      /**  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  */  
   AdhocStagedInventory:boolean,
      /**  UpdatedByEmpID  */  
   UpdatedByEmpID:string,
      /**  Raw Barcode Scan prior to execution of any extract logic.  */  
   RawBarcodeScan:string,
      /**  OutboundContainer  */  
   OutboundContainer:boolean,
      /**  PkgControlStatus value prior to being added to a pack.  */  
   BeforePackPkgControlStatus:string,
      /**  LabelPrintControlStatus value prior to being added to a pack.  */  
   BeforePackLabelPrintControlStatus:string,
      /**  To indicate the source process when a PCID was added to a pack.  */  
   PackedFromSource:string,
      /**  Date last counted.  Updated during the cycle count Posting Process.  */  
   LastCountedDate:string,
      /**  TFPackNum  */  
   TFPackNum:number,
      /**  Child PCID count  */  
   ChildPCIDCount:number,
      /**  Indicates if EnableCboReasonCode control should be Enabled.  */  
   EnableCboReasonCode:boolean,
      /**  if the PkgControlID is expendable  */  
   Expendable:boolean,
   ExtensionDigit:number,
      /**  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  */  
   HHASN:boolean,
   HHItemIUM:string,
   HHItemPartNum:string,
      /**  Used for Handheld.  */  
   HHItemQuantity:number,
   HHItemRevisionNum:string,
      /**  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  */  
   HHLabelStatus:string,
      /**   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  */  
   HHPackSlip:number,
      /**  Used for HandHeld, It could contains a list of PackNum from the children  */  
   HHPackSlipList:string,
   LWHDimUOM:string,
      /**  Warehouse Bin where the Parent PCID is currently located.  */  
   ParentBinNum:string,
      /**  System date and time when the row was created.  */  
   ParentCreatedDate:string,
      /**  Ship To Customer Container Part Number.  */  
   ParentCustContainerPartNum:string,
      /**  Parent Ship To Customer ID.  */  
   ParentCustID:string,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   ParentLabelPrintControlled:boolean,
      /**  Label Print Control status.  */  
   ParentLabelPrintControlStatus:string,
      /**  Label Type.  */  
   ParentLabelType:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   ParentNumberOfPCIDs:number,
      /**  Pack Number if applicable.  */  
   ParentPackNum:number,
      /**  Parent Package Control Identification Number  */  
   ParentPCID:string,
      /**  Unique packaging code assigned by the user.  */  
   ParentPkgCode:string,
      /**  The Internal PartNum for the Package Code.  */  
   ParentPkgCodePartNum:string,
      /**  PCID current status.  */  
   ParentPkgControlStatus:string,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   ParentPkgControlType:string,
      /**  Site where the Parent PCID is currently located.  */  
   ParentPlant:string,
      /**  Site Name.  */  
   ParentPlantName:string,
      /**  Parent Ship To Number.  */  
   ParentShipToNum:string,
      /**  Warehouse where the Parent PCID is currently located.  */  
   ParentWarehouseCode:string,
   ParentWhseDesc:string,
   PartDesc:string,
   PkgCodeDesc:string,
   PkgType:string,
      /**  Reason Code  */  
   ReasonCode:string,
   ResCodeIn:string,
   ResCodeOut:string,
   RTWhseDesc:string,
      /**  Ship To Container Part ID  */  
   ShipToContainerPartID:string,
      /**  Transaction document type  */  
   TranDocTypeID:string,
   WhseDesc:string,
      /**  Adjust Inventory  */  
   AdjustInventory:boolean,
      /**  Container UOM  */  
   ContainerUOM:string,
   DisableReasonCode:boolean,
      /**  Indicates if BtnVoidPCIDInv control should be Enabled.  */  
   EnableBtnVoidPCIDInv:boolean,
   BitFlag:number,
   BinDescription:string,
   WarehouseDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlItemRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  PCID Item Sequence  */  
   PCIDItemSeq:number,
      /**  The PCID of the item in this PCID.  */  
   ItemPCID:string,
      /**  The Part Number of the item in this PCID.  */  
   ItemPartNum:string,
      /**  The Revision Number of the item in this PCID.  */  
   ItemRevisionNum:string,
      /**  The Part Description of the item in this PCID.  */  
   ItemPartDesc:string,
      /**  The Lot Number of the item in this PCID.  */  
   ItemLotNum:string,
      /**  The Inventory UOM of the item in this PCID.  */  
   ItemIUM:string,
      /**  The Quantity of the item in this PCID.  */  
   ItemQuantity:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Demand Type.  */  
   DemandType:string,
      /**  Order Number of the demand.  */  
   OrderNum:number,
      /**  Order Line Number of the demand.  */  
   OrderLine:number,
      /**  Order Release Number of the demand.  */  
   OrderRelNum:number,
      /**  Job Number of the demand.  */  
   JobNum:string,
      /**  Assembly Sequence Number of the demand.  */  
   AssemblySeq:number,
      /**  Material Sequence Number of the demand.  */  
   MtlSeq:number,
      /**  Transfer Order Number of the demand.  */  
   TFOrdNum:string,
      /**  Transfer Order Line of the demand.  */  
   TFOrdLine:number,
      /**  Pack Number if applicable.  */  
   PackNum:number,
      /**  Pack Line Number if applicable.  */  
   PackLine:number,
      /**  Ship To Customer Part Number.  */  
   CustPartNum:string,
      /**  Ship To Customer Part Revision.  */  
   CustPartRev:string,
      /**  The PO number that these parts were created against.  */  
   CustPONum:string,
      /**  Engineering Alert to display on the label.  */  
   CustShipToEngineerAlert:string,
      /**  Safety Indicator to display on the label.  */  
   SafetyIndicator:boolean,
      /**  The Internal PartNum for the Package Code.  */  
   PkgCodePartNum:string,
      /**  Purchase Order Type.  */  
   VendorPOType:string,
      /**  Purchase Order Number.  */  
   VendorPONum:number,
      /**  Purchase Order Line Number.  */  
   VendorPOLine:number,
      /**  Purchase Order Release Number.  */  
   VendorPORelNum:number,
      /**  Supplier Part Number.  */  
   VendorPartNum:string,
      /**  Supplier Unit of Measure.  */  
   VendorUOM:string,
      /**  Supplier Quantity.  */  
   VendorQty:number,
      /**  Receipt Packing Slip.  */  
   ReceiptPackSlip:string,
      /**  Receipt Type.  */  
   ReceiptType:string,
      /**  Receipt Date.  */  
   ReceiptDate:string,
      /**  Receipt UOM.  */  
   ReceiptUOM:string,
      /**  Receipt Quantity.  */  
   ReceiptQty:number,
      /**  RMA Number.  */  
   RMANum:number,
      /**  RMA Line.  */  
   RMALine:number,
      /**  Reserved for development use.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter03:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter04:string,
      /**  Reserved for development use.  */  
   PkgControlCharacter05:string,
      /**  Reserved for development use.  */  
   PkgControlDate01:string,
      /**  Reserved for development use.  */  
   PkgControlDate02:string,
      /**  Reserved for development  */  
   PkgControlBoolean01:boolean,
      /**  Reserved for development use.  */  
   PkgControlBoolean02:boolean,
      /**  Reserved for development use.  */  
   PkgControlDecimal01:number,
      /**  Reserved for development use.  */  
   PkgControlDecimal02:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  */  
   ShipmentInvoicedPosted:string,
      /**  The job number on which the quantity on this record were produced  */  
   SupplyJobNum:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
      /**  TFPackNum  */  
   TFPackNum:number,
      /**  TFPackLine  */  
   TFPackLine:number,
      /**  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  */  
   ItemPicked:boolean,
      /**  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  */  
   ItemPartWipSysRowID:string,
      /**  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  */  
   TrackType:string,
      /**  Job operation sequence number that part is related to.  */  
   OprSeq:number,
      /**  Indicates if the WIP has been sent to Non-Conformance.  */  
   InNonConformance:boolean,
      /**  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  */  
   InDMRProcessing:boolean,
   ChildPCIDOrPart:string,
   CustID:string,
   CustName:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
   PackageCode:string,
      /**  Site Name.  */  
   PlantName:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
   WhseDesc:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  The Full Description of the Attribute Set.  */  
   ItemAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   ItemAttributeSetShortDescription:string,
   ItemPartAttrClassID:string,
   ItemType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReceiptsFromMfgJobAsmblRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   PartNum:string,
   Description:string,
   QtyCompleted:number,
   JobHeadPartNum:string,
   JobHeadPartDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset{
   ReceiptsFromMfgJobAsmbl:Erp_Tablesets_ReceiptsFromMfgJobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ReceiptsFromMfgTableset{
   PartTran:Erp_Tablesets_PartTranRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PkgControlHeader:Erp_Tablesets_PkgControlHeaderRow[],
   PkgControlItem:Erp_Tablesets_PkgControlItemRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedJobAsmblRow{
   Company:string,
   JobNum:string,
   AssemblySeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectedReceiptsJobAsmblTableset{
   SelectedJobAsmbl:Erp_Tablesets_SelectedJobAsmblRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedReceiptsPCIDTableset{
   PCIDReceiptsParams:Erp_Tablesets_PCIDReceiptsParamsRow[],
   PCIDReceiptsSelected:Erp_Tablesets_PCIDReceiptsSelectedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param pcid
      @param whse
      @param binNum
      @param pcProcessID
      @param ds
   */  
export interface ExecuteProcessPCID_input{
      /**  pcid  */  
   pcid:string,
      /**  whse  */  
   whse:string,
      /**  binNum  */  
   binNum:string,
      /**  Process ID that calls this method  */  
   pcProcessID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface ExecuteProcessPCID_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   pcMessage:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetDefaultTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   defaultTranDocTypeID:string,
}
}

export interface GetDefaultWhseBin_output{
parameters : {
      /**  output parameters  */  
   defaultWhse:string,
   defaultWhseDesc:string,
   defaultBinNum:string,
   defaultBinDescription:string,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param whereClauseJobAsmbl
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  Where condition without the where word  */  
   whereClauseJobHead:string,
      /**  Where condition without the where word  */  
   whereClauseJobAsmbl:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pcTranType
      @param pcProcessID
   */  
export interface GetNewJobAsmblMultiple_input{
   ds:Erp_Tablesets_SelectedReceiptsJobAsmblTableset[],
      /**  Tran Type.  Determines the nature of Receipts  */  
   pcTranType:string,
      /**  Process ID that calls this method  */  
   pcProcessID:string,
}

export interface GetNewJobAsmblMultiple_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedReceiptsJobAsmblTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobAsmblSearch_input{
   ds:Erp_Tablesets_SelectedReceiptsJobAsmblTableset[],
}

export interface GetNewJobAsmblSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedReceiptsJobAsmblTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
   */  
export interface GetNewPCIDParamsRow_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
}

export interface GetNewPCIDParamsRow_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
}
}

   /** Required : 
      @param pcJobNum
      @param piAssemblySeq
      @param pcTranType
      @param pcProcessID
      @param ds
   */  
export interface GetNewReceiptsFromMfgJobAsm_input{
      /**  Job Number  */  
   pcJobNum:string,
      /**  Assembly Sequence  */  
   piAssemblySeq:number,
      /**  Tran Type.  Determines the nature of Receipts  */  
   pcTranType:string,
      /**  Process ID that calls this method  */  
   pcProcessID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface GetNewReceiptsFromMfgJobAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param pcMtlQueueRowIdent
      @param ds
      @param dsSelectedPCID
   */  
export interface GetNewReceiptsFromMfgMtlQueue_input{
      /**  RowIdent of MtlQueue record  */  
   pcMtlQueueRowIdent:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
}

export interface GetNewReceiptsFromMfgMtlQueue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
}
}

   /** Required : 
      @param pcTranType
      @param ds
   */  
export interface GetNewReceiptsFromMfg_input{
      /**  Tran Type. Determines the nature of Receipts  */  
   pcTranType:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface GetNewReceiptsFromMfg_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param tranType
      @param processID
   */  
export interface GetNewReceiptsFromPCIDMultiple_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
      /**  The transaction type.  */  
   tranType:string,
      /**  The process identifier.  */  
   processID:string,
}

export interface GetNewReceiptsFromPCIDMultiple_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param supplyJobNum
      @param tranType
      @param processID
   */  
export interface GetNewReceiptsFromPCIDSupplyJobNum_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
      /**  The job number used to retrieve all the PCIDs associated.  */  
   supplyJobNum:string,
      /**  The transaction type.  */  
   tranType:string,
      /**  The process identifier.  */  
   processID:string,
}

export interface GetNewReceiptsFromPCIDSupplyJobNum_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param pcid
      @param tranType
      @param processID
   */  
export interface GetNewReceiptsFromPCID_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
      /**  The package control ID.  */  
   pcid:string,
      /**  The transaction type.  */  
   tranType:string,
      /**  The process identifier.  */  
   processID:string,
}

export interface GetNewReceiptsFromPCID_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
}
}

   /** Required : 
      @param pcid
      @param ds
   */  
export interface GetPCID_input{
      /**  pcid  */  
   pcid:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface GetPCID_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   isJobClosed:boolean,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param whereClauseJobAsmbl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
      /**  Where condition without the where word  */  
   whereClauseJobHead:string,
      /**  Where condition without the where word  */  
   whereClauseJobAsmbl:string,
      /**  # of records returned.  0 means all  */  
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param pcProcessID
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The name of the calling process (UI Application).  */  
   pcProcessID:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
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
      @param pcJobNum
      @param piAssemblySeq
   */  
export interface IsValidAssembly_input{
      /**  The job number  */  
   pcJobNum:string,
      /**  The assembly sequence number.  */  
   piAssemblySeq:number,
}

export interface IsValidAssembly_output{
parameters : {
      /**  output parameters  */  
   plFound:boolean,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface NegativeInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeActTranQty_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeActTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param pUOM
      @param ds
   */  
export interface OnChangeActTransUOM_input{
      /**  Transaction UOM  */  
   pUOM:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeActTransUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeAssemblySeq2_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeAssemblySeq2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeAssemblySeq_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeAssemblySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeBinNum_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeCalculateExtCost_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeCalculateExtCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeExtCost_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeExtCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ipPCID
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromPCID_input{
      /**  Proposed PCID value  */  
   ipPCID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeJobNum2_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeJobNum2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeJobNum_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeJobSeq2_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeJobSeq2_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
      @param messageasked
      @param ProposedLotNumber
   */  
export interface OnChangeLotNum_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  Set by the UI. If set to true then lot messages will not be returned. If false, either pcMessage or errormsg will be set if there is an error.  */  
   messageasked:boolean,
      /**  Lot number the user entered.  */  
   ProposedLotNumber:string,
}

export interface OnChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
   errormsg:string,
}
}

   /** Required : 
      @param ds
      @param ProposedOverride
   */  
export interface OnChangeOverrideCost_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  Override Cost value that the user selected.  */  
   ProposedOverride:boolean,
}

export interface OnChangeOverrideCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param pcProcessID
      @param warehouseCode
   */  
export interface OnChangePCIDParamWarehouseCode_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The calling process identifier.  */  
   pcProcessID:string,
      /**  The to warehouse code.  */  
   warehouseCode:string,
}

export interface OnChangePCIDParamWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param binNum
   */  
export interface OnChangePCIDParamsBinNum_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The to bin number.  */  
   binNum:string,
}

export interface OnChangePCIDParamsBinNum_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param pcProcessID
      @param plant2
   */  
export interface OnChangePCIDParamsPlant_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The calling process identifier.  */  
   pcProcessID:string,
      /**  The To Site.  */  
   plant2:string,
}

export interface OnChangePCIDParamsPlant_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param tranDate
   */  
export interface OnChangePCIDParamsTranDate_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The transaction date.  */  
   tranDate:string,
}

export interface OnChangePCIDParamsTranDate_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param tranDocTypeID
   */  
export interface OnChangePCIDParamsTranDocTypeID_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The transaction document type identifier.  */  
   tranDocTypeID:string,
}

export interface OnChangePCIDParamsTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param dsSelectedPCID
      @param ds
      @param tranReference
   */  
export interface OnChangePCIDParamsTranReference_input{
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The transaction reference.  */  
   tranReference:string,
}

export interface OnChangePCIDParamsTranReference_output{
parameters : {
      /**  output parameters  */  
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
      @param ProposedPartNum
      @param ipContinue
   */  
export interface OnChangePartNum_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The proposed PartNum  */  
   ProposedPartNum:string,
      /**  The action from user in response to the question sent in opMessage  */  
   ipContinue:boolean,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   opMessage:string,
}
}

   /** Required : 
      @param pcProcessID
      @param ds
   */  
export interface OnChangePlant_input{
      /**  Process ID where this method is called From  */  
   pcProcessID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangePlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeSalvageJobSeq_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeSalvageJobSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeSalvagePartNum_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeSalvagePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param ipPCID
      @param pCallProcess
      @param ds
   */  
export interface OnChangeToPCID_input{
      /**  Proposed To PCID value  */  
   ipPCID:string,
      /**  Calling Process value  */  
   pCallProcess:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeToPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeTranQty_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeTranQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
}
}

   /** Required : 
      @param pcProcessID
      @param ds
   */  
export interface OnChangeWareHouseCode_input{
      /**  Process ID where this method is called From  */  
   pcProcessID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangeWareHouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   outMsg:string,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNumMS_input{
   revisionNum:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangingRevisionNumMS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreProcessPCID_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface PreProcessPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface PreUpdate_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface PreUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param pcid
      @param whse
      @param binNum
      @param pcProcessID
      @param ds
   */  
export interface ProcessPCID_input{
      /**  pcid  */  
   pcid:string,
      /**  whse  */  
   whse:string,
      /**  binNum  */  
   binNum:string,
      /**  Process ID that calls this method  */  
   pcProcessID:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface ProcessPCID_output{
   returnObj:Erp_Tablesets_ReceiptsFromMfgTableset[],
parameters : {
      /**  output parameters  */  
   pcMessage:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
}
}

   /** Required : 
      @param ds
      @param dsSelectedPCID
      @param pcProcessID
   */  
export interface ReceiveMfgPCIDtoInventoryMultiple_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
      /**  The process calling this method.  */  
   pcProcessID:string,
}

export interface ReceiveMfgPCIDtoInventoryMultiple_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
   pcPartTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param dsSelectedPCID
      @param pcid
      @param pcProcessID
   */  
export interface ReceiveMfgPCIDtoInventory_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset[],
      /**  The pcid that is to be received into inventory.  */  
   pcid:string,
      /**  The process calling this method.  */  
   pcProcessID:string,
}

export interface ReceiveMfgPCIDtoInventory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   dsSelectedPCID:Erp_Tablesets_SelectedReceiptsPCIDTableset,
   pcMessage:string,
   pcPartTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param pdSerialNoQty
      @param plNegQtyAction
      @param pcProcessID
   */  
export interface ReceiveMfgPartToInventory_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   pdSerialNoQty:number,
      /**  When TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  */  
   plNegQtyAction:boolean,
      /**  The name ID of the UI process that's calling this procedure.  */  
   pcProcessID:string,
}

export interface ReceiveMfgPartToInventory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
   pcPartTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param pdSerialNoQty
      @param plNegQtyAction
      @param plIssuedComplete
      @param pcProcessID
   */  
export interface ReceiveMfgPartToJob_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   pdSerialNoQty:number,
      /**  When TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  */  
   plNegQtyAction:boolean,
      /**  Issue Complete  */  
   plIssuedComplete:boolean,
      /**  The name ID of the UI process that's calling this procedure.  */  
   pcProcessID:string,
}

export interface ReceiveMfgPartToJob_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
   pcPartTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param pcProcessID
   */  
export interface ReceiveSalvagedPartToInventory_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  The name ID of the UI process that's calling this procedure.  */  
   pcProcessID:string,
}

export interface ReceiveSalvagedPartToInventory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMessage:string,
   pcPartTranPKs:string,
}
}

   /** Required : 
      @param pcJobNum
   */  
export interface ValidateFromJob_input{
   pcJobNum:string,
}

export interface ValidateFromJob_output{
}

   /** Required : 
      @param pcid
   */  
export interface ValidatePCIDExists_input{
      /**  pcid  */  
   pcid:string,
}

export interface ValidatePCIDExists_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   isJobClosed:boolean,
}
}

   /** Required : 
      @param pcid
      @param ds
   */  
export interface ValidatePCID_input{
      /**  pcid  */  
   pcid:string,
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface ValidatePCID_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   isJobClosed:boolean,
}
}

   /** Required : 
      @param ds
      @param serialNumber
      @param pcProcessID
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
      /**  The ID of the calling process in UI  */  
   pcProcessID:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   isVoided:boolean,
}
}

   /** Required : 
      @param ToWhse
      @param ToBinNum
   */  
export interface ValidateWhseBinPCID_input{
      /**  Warehouse  */  
   ToWhse:string,
      /**  Bin Num to validate  */  
   ToBinNum:string,
}

export interface ValidateWhseBinPCID_output{
   returnObj:boolean,
}

   /** Required : 
      @param ToWhse
   */  
export interface ValidateWhsePCIDAndGetDefaultBin_input{
      /**  Warehouse to validate.  */  
   ToWhse:string,
}

export interface ValidateWhsePCIDAndGetDefaultBin_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   defaultBinNum:string,
   defaultBinDescription:string,
}
}

   /** Required : 
      @param ToWhse
   */  
export interface ValidateWhsePCID_input{
      /**  Warehouse to validate.  */  
   ToWhse:string,
}

export interface ValidateWhsePCID_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface VerifySerialMatchAndPlanContract_input{
   ds:Erp_Tablesets_ReceiptsFromMfgTableset[],
}

export interface VerifySerialMatchAndPlanContract_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReceiptsFromMfgTableset,
   pcMsg:string,
   piMsgType:number,
   pcPCBinAction:string,
   pcPCBinMessage:string,
}
}

