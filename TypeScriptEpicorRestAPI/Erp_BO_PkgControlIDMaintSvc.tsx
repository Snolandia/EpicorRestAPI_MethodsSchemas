import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PkgControlIDMaintSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", {
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
   Summary: Invoke method GetPkgControlHdrByIDInvTrans
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
   OperationID: GetPkgControlHdrByIDInvTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByIDInvTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByIDInvTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlHdrByIDInvTrans(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlHdrByIDInvTrans", {
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
   Summary: Invoke method GetPkgControlHdrByID
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
   OperationID: GetPkgControlHdrByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlHdrByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlHdrByID", {
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
   Summary: Invoke method GetPkgControlHdrByID2
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
Created for Kinetic so the LabelValue records all have a unique GUID
   OperationID: GetPkgControlHdrByID2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByID2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByID2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlHdrByID2(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlHdrByID2", {
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
   Summary: Invoke method GetPkgControlHdrByGUID
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by SysRowID
   OperationID: GetPkgControlHdrByGUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByGUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByGUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlHdrByGUID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlHdrByGUID", {
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
   Summary: Invoke method GetHeaderRows
   Description: Gets PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records into the Erp.BO.PkgControlIDMergedTableset
Based on the whereClauses provided and other parameters selected
   OperationID: GetHeaderRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeaderRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHeaderRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetHeaderRows", {
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
   Summary: Invoke method GetHeaderList
   Description: Gets PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records into the Erp.BO.PkgControlIDMergedTableset
Based on the whereClauses provided and other parameters selected
   OperationID: GetHeaderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeaderList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetHeaderList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetHeaderList", {
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
   Summary: Invoke method UpdatePkgControl
   Description: Updates PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records
   OperationID: UpdatePkgControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePkgControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePkgControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePkgControl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/UpdatePkgControl", {
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
   Summary: Invoke method CommitPCIDTransfer
   Description: This method will commit the inventory transfer.
   OperationID: CommitPCIDTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitPCIDTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitPCIDTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitPCIDTransfer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/CommitPCIDTransfer", {
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
   Summary: Invoke method GetDefaultWhseBin
   Description: Get Warehouse Code for PCID.
   OperationID: GetDefaultWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetDefaultWhseBin", {
          method: 'post',
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
   Summary: Invoke method GetValidPCIDRow
   Description: This method verifies if a PCID entered is valid. If so, returns PkgControlIDMergedTableset with the PCID row value.
   OperationID: GetValidPCIDRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidPCIDRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidPCIDRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetValidPCIDRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetValidPCIDRow", {
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
   Summary: Invoke method VoidPCIDProcess
   Description: This method updates PkgControlStatus to VOID for a PCID.
   OperationID: VoidPCIDProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPCIDProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPCIDProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidPCIDProcess(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/VoidPCIDProcess", {
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
   Summary: Invoke method PreSetLegalNumPkgControlVoidPCID
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction. The RequiresUserInput
flag will indicate if this legal number requires input from the user. If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information. This method should be called when the user
inputs the target PCID or clicks the print button and the source qty > 0,
and before calling any update method that could generate PartTran.
   OperationID: PreSetLegalNumPkgControlVoidPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetLegalNumPkgControlVoidPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetLegalNumPkgControlVoidPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSetLegalNumPkgControlVoidPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/PreSetLegalNumPkgControlVoidPCID", {
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
   Summary: Invoke method PCIDExists
   Description: Purpose:  Test if a given PCID already exists in the PkgControlHeader table.
   OperationID: PCIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PCIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PCIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCIDExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/PCIDExists", {
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
   Summary: Invoke method WarehseEnforcePkgControlRulesExists
   Description: This method is udes to verify if a Warehouse with EnforcePkgControlRules exists
   OperationID: WarehseEnforcePkgControlRulesExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WarehseEnforcePkgControlRulesExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/WarehseEnforcePkgControlRulesExists", {
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
   Summary: Invoke method ValidateWhsePCIDAndGetDefaultBin
   Description: Validates warehouse for PCID and returns a bin if there is only one available.
   OperationID: ValidateWhsePCIDAndGetDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWhsePCIDAndGetDefaultBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/ValidateWhsePCIDAndGetDefaultBin", {
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
   Summary: Invoke method WhseBinExists
   Description: This method is udes to verify if a WhseBin exists
   OperationID: WhseBinExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WhseBinExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhseBinExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WhseBinExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/WhseBinExists", {
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
   Summary: Invoke method isWhseBinManaged
   Description: This method is used to verify if a WhseBin is Supplier or Customer Managed
   OperationID: isWhseBinManaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isWhseBinManaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isWhseBinManaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_isWhseBinManaged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/isWhseBinManaged", {
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
   Summary: Invoke method isWhseBinActive
   Description: This method is used to verify if a WhseBin is Active or Inactive
   OperationID: isWhseBinActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isWhseBinActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isWhseBinActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_isWhseBinActive(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/isWhseBinActive", {
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
   Summary: Invoke method ConfirmSupervisorPassword
   Description: This method is used to confirm if the User/Supervisor Password provided is correct.
This is called from PackageControlLib.
   OperationID: ConfirmSupervisorPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmSupervisorPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmSupervisorPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfirmSupervisorPassword(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/ConfirmSupervisorPassword", {
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
   Summary: Invoke method PrintLabel
   OperationID: PrintLabel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintLabel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintLabel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrintLabel(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/PrintLabel", {
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
   Summary: Invoke method GetSplitMergeData
   Description: Purpose: Get splitMerge target or source data for a PCID
Parameters:  none
Notes:
<param name="ipPCID">The PCID the data is being retrieved for</param><param name="ipSourceOrTarget">Retrieve Split Merge for the source or target (S or T) PCIDs for the input PCID</param><param name="ds">The PkgControlSplitMerge data set</param>
   OperationID: GetSplitMergeData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSplitMergeData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSplitMergeData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSplitMergeData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetSplitMergeData", {
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
   Summary: Invoke method GetDefaultTranDocTypeID
   Description: Returns the default Transaction Document Type ID for a given System Transaction.
   OperationID: GetDefaultTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetDefaultTranDocTypeID", {
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
   Summary: Invoke method ProcessAdhocRecipt
   Description: Moves inventory from STAGE to INVENTORY
   OperationID: ProcessAdhocRecipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessAdhocRecipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessAdhocRecipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessAdhocRecipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/ProcessAdhocRecipt", {
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
   Summary: Invoke method PreProcessAdhocRecipt
   Description: Validates PCID for Adhoc Receipt and performs NegInvTest
   OperationID: PreProcessAdhocRecipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessAdhocRecipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessAdhocRecipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcessAdhocRecipt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/PreProcessAdhocRecipt", {
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
   Summary: Invoke method GetDefaultAdhocMoveLocation
   Description: Gets the default to warehouse and bin for Adhoc Receipt
   OperationID: GetDefaultAdhocMoveLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultAdhocMoveLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultAdhocMoveLocation(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetDefaultAdhocMoveLocation", {
          method: 'post',
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
   Summary: Invoke method GetPkgControlIDMergedList
   Description: Retrieves PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records and their associated item records and merges into PkgControlIDMergedListTableset.
   OperationID: GetPkgControlIDMergedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDMergedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDMergedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlIDMergedList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlIDMergedList", {
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
   Summary: Invoke method GetPkgControlIDMergedListAll
   Description: Copy of GetPkgControlIDMergedList that sets pageSize to 0 to avoid a paging issue in kinetic.
   OperationID: GetPkgControlIDMergedListAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDMergedListAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDMergedListAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPkgControlIDMergedListAll(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/GetPkgControlIDMergedListAll", {
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
      @param toWhse
      @param toBin
      @param ds
   */  
export interface CommitPCIDTransfer_input{
   toWhse:string,
   toBin:string,
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}

export interface CommitPCIDTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}
}

   /** Required : 
      @param password
   */  
export interface ConfirmSupervisorPassword_input{
   password:string,
}

export interface ConfirmSupervisorPassword_output{
   returnObj:boolean,
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

export interface Erp_Tablesets_PCLabelValuesRow{
   Company:string,
   LabelSeq:number,
   LabelValues:string,
   PCID:string,
   ValueField:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlCustPartNumRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Package Control Identification Number.  */  
   PCID:string,
      /**  PCID Customer Part Sequence.  */  
   PCIDCustPartSeq:number,
      /**  Used for MixedMaster parent PCIDs.  Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustPartNum:string,
      /**  Used for MixedMaster parent PCIDs. Number of parts per parent PCID for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustQtyPerContainer:number,
      /**  Used for MixedMaster parent PCIDs.  Number of PCIDs for the Customer Part Number associated to the MixedMaster parent PCID.  */  
   CustNumContainers:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlHeaderMergedListRow{
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
      /**  Reserved for development use for PkgControlStatus value prior to being added to a pack.  */  
   PkgControlCharacter01:string,
      /**  Reserved for development use for LabelPrintControlStatus value prior to being added to a pack  */  
   PkgControlCharacter02:string,
      /**  Reserved for development use to indicate the source process when a PCID was added to a pack.  */  
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
   OutboundContainer:boolean,
   BeforePackPkgControlStatus:string,
   BeforePackLabelPrintControlStatus:string,
   PackedFromSource:string,
      /**  Record Type Description, can be Inventory, History or Stage  */  
   RecordTypeDesc:string,
      /**  PCID Item Sequence  */  
   PCIDItemSeq:number,
      /**  The Part Number of the item in this PCID.  */  
   ItemPartNum:string,
      /**  The Part Description of the item in this PCID.  */  
   ItemPartDesc:string,
      /**  The Lot Number of the item in this PCID.  */  
   ItemLotNum:string,
      /**  The Inventory UOM of the item in this PCID.  */  
   ItemIUM:string,
      /**  The Quantity of the item in this PCID.  */  
   ItemQuantity:number,
      /**  Job that is supplying the allocated quantity  */  
   SupplyJobNum:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlHeaderMergedRow{
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
      /**  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a Mixed PCID.  */  
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
      /**  if the PkgControlID is expendable  */  
   Expendable:boolean,
   ExtensionDigit:number,
      /**   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  */  
   HHPackSlip:number,
      /**  Used for HandHeld, It could contains a list of PackNum from the children  */  
   HHPackSlipList:string,
   PartDesc:string,
   PkgCodeDesc:string,
   ResCodeIn:string,
   ResCodeOut:string,
   RTWhseDesc:string,
   WhseDesc:string,
      /**  Child PCID count  */  
   ChildPCIDCount:number,
      /**  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  */  
   HHASN:boolean,
      /**  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  */  
   HHLabelStatus:string,
   LWHDimUOM:string,
      /**  Parent Package Control Identification Number  */  
   ParentPCID:string,
      /**  Site where the Parent PCID is currently located.  */  
   ParentPlant:string,
      /**  Warehouse where the Parent PCID is currently located.  */  
   ParentWarehouseCode:string,
      /**  Warehouse Bin where the Parent PCID is currently located.  */  
   ParentBinNum:string,
      /**  Parent Ship To Customer ID.  */  
   ParentCustID:string,
      /**  Parent Ship To Number.  */  
   ParentShipToNum:string,
      /**  Unique packaging code assigned by the user.  */  
   ParentPkgCode:string,
      /**  Pack Number if applicable.  */  
   ParentPackNum:number,
      /**  The Internal PartNum for the Package Code.  */  
   ParentPkgCodePartNum:string,
      /**  Ship To Customer Container Part Number.  */  
   ParentCustContainerPartNum:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   ParentNumberOfPCIDs:number,
      /**  Package Control Type.  Valid values are “Static” or “Dynamic”.  */  
   ParentPkgControlType:string,
      /**  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  */  
   ParentLabelPrintControlled:boolean,
      /**  Label Type.  */  
   ParentLabelType:string,
      /**  Label Print Control status.  */  
   ParentLabelPrintControlStatus:string,
      /**  System date and time when the row was created.  */  
   ParentCreatedDate:string,
      /**  PCID current status.  */  
   ParentPkgControlStatus:string,
   PkgType:string,
      /**  Site Name.  */  
   ParentPlantName:string,
   ParentWhseDesc:string,
      /**  Used for Handheld.  */  
   HHItemQuantity:number,
   HHItemIUM:string,
   HHItemPartNum:string,
   HHItemRevisionNum:string,
   DisableReasonCode:boolean,
      /**  Reason Code  */  
   ReasonCode:string,
      /**  Ship To Container Part ID  */  
   ShipToContainerPartID:string,
      /**  Container UOM  */  
   ContainerUOM:string,
      /**  Adjust Inventory  */  
   AdjustInventory:boolean,
      /**  Indicates if BtnVoidPCIDInv control should be Enabled.  */  
   EnableBtnVoidPCIDInv:boolean,
      /**  Indicates if EnableCboReasonCode control should be Enabled.  */  
   EnableCboReasonCode:boolean,
   RecordType:string,
   RecordTypeDesc:string,
   BitFlag:number,
   AdhocStagedInventory:boolean,
   Ext_PrevPCID:string,
   ResCodeInDesc:string,
   ResCodeOutDesc:string,
      /**  Used for the PkgControl ID Maint form Activities  tab. It will display the PkgControlHeaderMerged.OriginalSourcePCID if there is only one, or "Multiple" if this PCID has PkgControlSplitMerger where it is specified as the Target.  */  
   OriginalSourcePCIDDisp:string,
      /**  Used for the PkgControl ID Maint form Activities  tab. It will display the PkgControlHeaderMerged.OverlaidByPCID if there is only one, or "Multiple" if this PCID has PkgControlSplitMerger where it is specified as the Source.  */  
   OverlaidByPCIDDisp:string,
      /**  Holds any message returned from the legal number generation.  */  
   LegalNumberMessage:string,
      /**  The employee that last updated this row.  */  
   UpdatedByEmpID:string,
   RawBarcodeScan:string,
      /**  Transaction Document Type  */  
   TranDocTypeID:string,
      /**  Temporal Transaction Document Type. This is used to be able to have TranDocTypeIDs for different System Transactions in different tabs of the same form.  */  
   TranDocTypeIDPCID:string,
      /**  Temporal Transaction Document Type. This is used to be able to have TranDocTypeIDs for different System Transactions in different tabs of the same form.  */  
   TranDocTypeIDPCIDInv:string,
   OutboundContainer:boolean,
   BeforePackPkgControlStatus:string,
   BeforePackLabelPrintControlStatus:string,
   PackedFromSource:string,
      /**  Transfer Shipment Pack Number if applicable.  */  
   TFPackNum:number,
      /**  Item Quantity for a PCID  */  
   ItemQuantity:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlIDMergedListTableset{
   PkgControlHeaderMergedList:Erp_Tablesets_PkgControlHeaderMergedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlIDMergedTableset{
   PkgControlHeaderMerged:Erp_Tablesets_PkgControlHeaderMergedRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   PCLabelValues:Erp_Tablesets_PCLabelValuesRow[],
   PkgControlCustPartNum:Erp_Tablesets_PkgControlCustPartNumRow[],
   PkgControlItemMerged:Erp_Tablesets_PkgControlItemMergedRow[],
   PkgControlSplitMerge:Erp_Tablesets_PkgControlSplitMergeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PkgControlItemMergedRow{
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
      /**  Site.  */  
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
      /**  The internal Part for the Package Code.  */  
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
      /**  Reserved for development use.  */  
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
   ChildPCIDOrPart:string,
   PackageCode:string,
   CustID:string,
   CustName:string,
      /**  Warehouse where the PCID is currently located.  */  
   WarehouseCode:string,
      /**  Warehouse Bin where the PCID is currently located.  */  
   BinNum:string,
      /**  Number of next level down child PCIDs associated to this PCID.  */  
   NumberOfPCIDs:number,
      /**  Site Name.  */  
   PlantName:string,
   WhseDesc:string,
   ShipmentInvoicedPosted:string,
   RecordTypeDesc:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
      /**  Transfer Shipment Pack Number if applicable.  */  
   TFPackNum:number,
      /**  Transfer Shipment Line Num if applicable.  */  
   TFPackLine:number,
      /**  The Full Description of the Attribute Set.  */  
   ItemAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   ItemAttributeSetShortDescription:string,
   ItemPartAttrClassID:string,
      /**  Display (decimal) number of pieces for inventory tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Indicates the order info comes from picking/picked, used to determine whether to retain the demand data if the PCID is packed then unpacked.  */  
   ItemPicked:boolean,
      /**  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  */  
   ItemPartWipSysRowID:string,
      /**  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  */  
   TrackType:string,
      /**  Job operation sequence number that part is related to.  */  
   OprSeq:number,
   ItemType:string,
   InNonConformance:boolean,
   InDMRProcessing:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PkgControlSplitMergeRow{
      /**  Company  */  
   Company:string,
      /**  TranNum  */  
   TranNum:number,
      /**  TranType  */  
   TranType:string,
      /**  Plant  */  
   Plant:string,
      /**  SourcePCID  */  
   SourcePCID:string,
      /**  SourcePkgControlStatus  */  
   SourcePkgControlStatus:string,
      /**  SourceWarehouseCode  */  
   SourceWarehouseCode:string,
      /**  SourceBinNum  */  
   SourceBinNum:string,
      /**  SourceLabelPrintControlStatus  */  
   SourceLabelPrintControlStatus:string,
      /**  TargetPCID  */  
   TargetPCID:string,
      /**  TargetPkgControlStatus  */  
   TargetPkgControlStatus:string,
      /**  TargetWarehouseCode  */  
   TargetWarehouseCode:string,
      /**  TargetBinNum  */  
   TargetBinNum:string,
      /**  ItemPartNum  */  
   ItemPartNum:string,
      /**  ItemRevisionNum  */  
   ItemRevisionNum:string,
      /**  TargetLabelPrintControlStatus  */  
   TargetLabelPrintControlStatus:string,
      /**  ItemLotNum  */  
   ItemLotNum:string,
      /**  ItemIUM  */  
   ItemIUM:string,
      /**  ItemQuantity  */  
   ItemQuantity:number,
      /**  CreatedDate  */  
   CreatedDate:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetDefaultAdhocMoveLocation_output{
parameters : {
      /**  output parameters  */  
   whse:string,
   binNum:string,
}
}

   /** Required : 
      @param sysTranID
   */  
export interface GetDefaultTranDocTypeID_input{
      /**  The System Transaction ID as stored in the TranDocType table.  */  
   sysTranID:string,
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
      @param whereClausePkgControlHeader
      @param whereClauseHXPkgControlHeader
      @param whereClausePkgControlStageHeader
      @param whereClauseChild
      @param onlyTopParentPCID
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param searchByPart
      @param pageSize
   */  
export interface GetHeaderList_input{
      /**  Filter to be used on the PkgControlHeader Table  */  
   whereClausePkgControlHeader:string,
      /**  Filter to be used on the HXPkgControlHeader Table  */  
   whereClauseHXPkgControlHeader:string,
      /**  Filter to be used on the PkgControlStageHeader Table  */  
   whereClausePkgControlStageHeader:string,
      /**  Filter to be used on the ChildTable for all the whereClause: whereClausePkgControlHeader, whereClauseHXPkgControlHeader, whereClausePkgControlStageHeader  */  
   whereClauseChild:string,
      /**  When true the search will retrieve only PCIDs that are not listed,as children, on other PCIDs  */  
   onlyTopParentPCID:boolean,
      /**  When true will exclude PkgControlHeader table its whereClause from the search.  */  
   excludeInventory:boolean,
      /**  When true will exclude HXPkgControlHeader table its whereClause from the search.  */  
   excludeHistory:boolean,
      /**  When true will exclude PkgControlStageHeader table its whereClause from the search.  */  
   excludeStaged:boolean,
      /**  When selected the search will retrieve one line for each of the child records for each PCID that meets the filter whereClause  */  
   searchByPart:boolean,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
}

export interface GetHeaderList_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePkgControlHeader
      @param whereClauseHXPkgControlHeader
      @param whereClausePkgControlStageHeader
      @param onlyTopParentPCID
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
   */  
export interface GetHeaderRows_input{
      /**  Filter to be used on the PkgControlHeader Table  */  
   whereClausePkgControlHeader:string,
      /**  Filter to be used on the HXPkgControlHeader Table  */  
   whereClauseHXPkgControlHeader:string,
      /**  Filter to be used on the PkgControlStageHeader Table  */  
   whereClausePkgControlStageHeader:string,
      /**  When true the search will retrieve only PCIDs that are not listed,as children, on other PCIDs  */  
   onlyTopParentPCID:boolean,
      /**  When true will exclude PkgControlHeader table its whereClause from the search.  */  
   excludeInventory:boolean,
      /**  When true will exclude HXPkgControlHeader table its whereClause from the search.  */  
   excludeHistory:boolean,
      /**  When true will exclude PkgControlStageHeader table its whereClause from the search.  */  
   excludeStaged:boolean,
}

export interface GetHeaderRows_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param sysRowID
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param combineWhenInventoryAndStaged
   */  
export interface GetPkgControlHdrByGUID_input{
      /**  SysRowID of header to retrieve  */  
   sysRowID:string,
      /**  Flag to exclude Inventory PCIDs  */  
   excludeInventory:boolean,
      /**  Flag to exclude History PCIDs  */  
   excludeHistory:boolean,
      /**  Flag to exclude Staged PCIDs  */  
   excludeStaged:boolean,
      /**  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  */  
   combineWhenInventoryAndStaged:boolean,
}

export interface GetPkgControlHdrByGUID_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param pcid
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param combineWhenInventoryAndStaged
   */  
export interface GetPkgControlHdrByID2_input{
      /**  SysRowID of header to retrieve  */  
   pcid:string,
      /**  Flag to exclude Inventory PCIDs  */  
   excludeInventory:boolean,
      /**  Flag to exclude History PCIDs  */  
   excludeHistory:boolean,
      /**  Flag to exclude Staged PCIDs  */  
   excludeStaged:boolean,
      /**  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  */  
   combineWhenInventoryAndStaged:boolean,
}

export interface GetPkgControlHdrByID2_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param pcid
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param calledFrom
   */  
export interface GetPkgControlHdrByIDInvTrans_input{
   pcid:string,
   excludeInventory:boolean,
   excludeHistory:boolean,
   excludeStaged:boolean,
   calledFrom:string,
}

export interface GetPkgControlHdrByIDInvTrans_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param pcid
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param combineWhenInventoryAndStaged
   */  
export interface GetPkgControlHdrByID_input{
      /**  SysRowID of header to retrieve  */  
   pcid:string,
      /**  Flag to exclude Inventory PCIDs  */  
   excludeInventory:boolean,
      /**  Flag to exclude History PCIDs  */  
   excludeHistory:boolean,
      /**  Flag to exclude Staged PCIDs  */  
   excludeStaged:boolean,
      /**  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  */  
   combineWhenInventoryAndStaged:boolean,
}

export interface GetPkgControlHdrByID_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param whoLaunched
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetPkgControlIDMergedListAll_input{
   whoLaunched:string,
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPkgControlIDMergedListAll_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whoLaunched
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetPkgControlIDMergedList_input{
   whoLaunched:string,
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPkgControlIDMergedList_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPCID
      @param ipSourceOrTarget
      @param ds
   */  
export interface GetSplitMergeData_input{
   ipPCID:string,
   ipSourceOrTarget:string,
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}

export interface GetSplitMergeData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}
}

   /** Required : 
      @param pcid
      @param excludeInventory
      @param excludeHistory
      @param excludeStaged
      @param calledFromHH
   */  
export interface GetValidPCIDRow_input{
      /**  pcid  */  
   pcid:string,
      /**  excludeInventory  */  
   excludeInventory:boolean,
      /**  excludeHistory  */  
   excludeHistory:boolean,
      /**  excludeStaged  */  
   excludeStaged:boolean,
      /**  calledFromHH  */  
   calledFromHH:boolean,
}

export interface GetValidPCIDRow_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
parameters : {
      /**  output parameters  */  
   errorMessage:string,
   supervisorRequired:boolean,
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
      @param ipPCID
   */  
export interface PCIDExists_input{
      /**  PCID  */  
   ipPCID:string,
}

export interface PCIDExists_output{
      /**  bool  */  
   returnObj:boolean,
}

   /** Required : 
      @param pcid
      @param whse
      @param binNum
   */  
export interface PreProcessAdhocRecipt_input{
      /**  PCID to move from staged  */  
   pcid:string,
      /**  Warehouse to move to  */  
   whse:string,
      /**  Bin to move to  */  
   binNum:string,
}

export interface PreProcessAdhocRecipt_output{
parameters : {
      /**  output parameters  */  
   negQtyAction:string,
   negQtyMsg:string,
}
}

   /** Required : 
      @param ds
      @param adjustInventory
   */  
export interface PreSetLegalNumPkgControlVoidPCID_input{
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
      /**  Helps to define the System Transaction that will be handled  */  
   adjustInventory:boolean,
}

export interface PreSetLegalNumPkgControlVoidPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ipPCID
   */  
export interface PrintLabel_input{
   ipPCID:string,
}

export interface PrintLabel_output{
parameters : {
      /**  output parameters  */  
   printerID:string,
   lpcPrintedFromTx:string,
   lpcPrintedFromTxType:string,
   numberOfLabels:number,
   styleNum:number,
   promptUser:boolean,
}
}

   /** Required : 
      @param pcid
      @param whse
      @param binNum
   */  
export interface ProcessAdhocRecipt_input{
      /**  PCID to move from staged  */  
   pcid:string,
      /**  Warehouse to move to  */  
   whse:string,
      /**  Bin to move to  */  
   binNum:string,
}

export interface ProcessAdhocRecipt_output{
   returnObj:Erp_Tablesets_PkgControlIDMergedTableset[],
}

   /** Required : 
      @param ds
   */  
export interface UpdatePkgControl_input{
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}

export interface UpdatePkgControl_output{
}

   /** Required : 
      @param ToWhse
      @param PlantID
   */  
export interface ValidateWhsePCIDAndGetDefaultBin_input{
      /**  Warehouse to validate.  */  
   ToWhse:string,
      /**  current PlantID  */  
   PlantID:string,
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
      @param pcid
      @param reasonCode
      @param adjustInventory
      @param ds
   */  
export interface VoidPCIDProcess_input{
      /**  pcid  */  
   pcid:string,
      /**  Reason Code required as part of the Void of Inventory  */  
   reasonCode:string,
      /**  Set this to true when it is desired that the Inventory and/or WIP inside the PCID should be removed as part of the Void  */  
   adjustInventory:boolean,
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}

export interface VoidPCIDProcess_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PkgControlIDMergedTableset[],
}
}

   /** Required : 
      @param WarehouseCode
      @param PlantID
   */  
export interface WarehseEnforcePkgControlRulesExists_input{
      /**  WarehouseCode to search for  */  
   WarehouseCode:string,
      /**  Current PlantID  */  
   PlantID:string,
}

export interface WarehseEnforcePkgControlRulesExists_output{
      /**  True if Warehouse exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param WarehouseCode
      @param BinNum
   */  
export interface WhseBinExists_input{
      /**  Current WarehouseCode  */  
   WarehouseCode:string,
      /**  BinNum to search for  */  
   BinNum:string,
}

export interface WhseBinExists_output{
      /**  True if WhseBin exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param WarehouseCode
      @param BinNum
   */  
export interface isWhseBinActive_input{
      /**  Current WarehouseCode  */  
   WarehouseCode:string,
      /**  BinNum to search for  */  
   BinNum:string,
}

export interface isWhseBinActive_output{
      /**  True if WhseBin is Active  */  
   returnObj:boolean,
}

   /** Required : 
      @param WarehouseCode
      @param BinNum
   */  
export interface isWhseBinManaged_input{
      /**  Current WarehouseCode  */  
   WarehouseCode:string,
      /**  BinNum to search for  */  
   BinNum:string,
}

export interface isWhseBinManaged_output{
      /**  True if WhseBin is Supplier or Customer Managed  */  
   returnObj:boolean,
}

