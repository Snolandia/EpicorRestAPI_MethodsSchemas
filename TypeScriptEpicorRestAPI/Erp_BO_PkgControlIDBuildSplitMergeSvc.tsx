import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PkgControlIDBuildSplitMergeSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", {
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
   Summary: Invoke method AddPartToPCID
   Description: Add Part to PCID
   OperationID: AddPartToPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddPartToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPartToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPartToPCID(requestBody:AddPartToPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddPartToPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/AddPartToPCID", {
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
         resolve(data as AddPartToPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddPartToPCIDAndRefreshDest
   Description: Add Part to PCID
   OperationID: AddPartToPCIDAndRefreshDest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddPartToPCIDAndRefreshDest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPartToPCIDAndRefreshDest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPartToPCIDAndRefreshDest(requestBody:AddPartToPCIDAndRefreshDest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddPartToPCIDAndRefreshDest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/AddPartToPCIDAndRefreshDest", {
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
         resolve(data as AddPartToPCIDAndRefreshDest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AddPCIDToPCID
   Description: Add PCID to PCID
   OperationID: AddPCIDToPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddPCIDToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPCIDToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddPCIDToPCID(requestBody:AddPCIDToPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddPCIDToPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/AddPCIDToPCID", {
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
         resolve(data as AddPCIDToPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveFromSourcePCIDToDestPCIDAndRefresh
   Description: Move from Source PCID to Destination PCID
   OperationID: MoveFromSourcePCIDToDestPCIDAndRefresh
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveFromSourcePCIDToDestPCIDAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromSourcePCIDToDestPCIDAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveFromSourcePCIDToDestPCIDAndRefresh(requestBody:MoveFromSourcePCIDToDestPCIDAndRefresh_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveFromSourcePCIDToDestPCIDAndRefresh_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/MoveFromSourcePCIDToDestPCIDAndRefresh", {
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
         resolve(data as MoveFromSourcePCIDToDestPCIDAndRefresh_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveFromDestPCIDToSourcePCID
   Description: Move from Destination PCID to Source PCID
   OperationID: MoveFromDestPCIDToSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveFromDestPCIDToSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromDestPCIDToSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveFromDestPCIDToSourcePCID(requestBody:MoveFromDestPCIDToSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveFromDestPCIDToSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/MoveFromDestPCIDToSourcePCID", {
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
         resolve(data as MoveFromDestPCIDToSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveFromSourcePCIDToDestPCID
   Description: Move from Source PCID to Destination PCID
   OperationID: MoveFromSourcePCIDToDestPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveFromSourcePCIDToDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromSourcePCIDToDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveFromSourcePCIDToDestPCID(requestBody:MoveFromSourcePCIDToDestPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveFromSourcePCIDToDestPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/MoveFromSourcePCIDToDestPCID", {
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
         resolve(data as MoveFromSourcePCIDToDestPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveFromDestPCID
   Description: Remove from Dest PCID
   OperationID: RemoveFromDestPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveFromDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveFromDestPCID(requestBody:RemoveFromDestPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveFromDestPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/RemoveFromDestPCID", {
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
         resolve(data as RemoveFromDestPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveFromSourcePCID
   Description: Remove from Source PCID
   OperationID: RemoveFromSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RemoveFromSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveFromSourcePCID(requestBody:RemoveFromSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveFromSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/RemoveFromSourcePCID", {
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
         resolve(data as RemoveFromSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSourcePCID
   Description: Returns the Source PCID dataset.
   OperationID: GetSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourcePCID(requestBody:GetSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetSourcePCID", {
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
         resolve(data as GetSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDestPCID
   Description: Returns the Destination PCID dataset.
   OperationID: GetDestPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDestPCID(requestBody:GetDestPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDestPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetDestPCID", {
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
         resolve(data as GetDestPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDestPCID
   Description: OnChangeDestPCID
   OperationID: OnChangeDestPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDestPCID(requestBody:OnChangeDestPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDestPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeDestPCID", {
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
         resolve(data as OnChangeDestPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDestBinNum
   Description: OnChangeDestBinNum
   OperationID: OnChangeDestBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDestBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDestBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDestBinNum(requestBody:OnChangeDestBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDestBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeDestBinNum", {
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
         resolve(data as OnChangeDestBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeItemPartNum
   Description: OnChangeItemPartNum
   OperationID: OnChangeItemPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeItemPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeItemPartNum(requestBody:OnChangeItemPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeItemPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeItemPartNum", {
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
         resolve(data as OnChangeItemPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeItemPCID
   Description: OnChangeItemPCID
   OperationID: OnChangeItemPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeItemPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeItemPCID(requestBody:OnChangeItemPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeItemPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeItemPCID", {
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
         resolve(data as OnChangeItemPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeItemLotNum
   Description: Method to call when the source item lot number changes.
   OperationID: OnChangeItemLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeItemLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeItemLotNum(requestBody:OnChangeItemLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeItemLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeItemLotNum", {
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
         resolve(data as OnChangeItemLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourcePartNum
   Description: OnChangeSourcePartNum
   OperationID: OnChangeSourcePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePartNum(requestBody:OnChangeSourcePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePartNum", {
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
         resolve(data as OnChangeSourcePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourceAttributeSetID
   Description: OnChangeSourceAttributeSetID
   OperationID: OnChangeSourceAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourceAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourceAttributeSetID(requestBody:OnChangeSourceAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourceAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourceAttributeSetID", {
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
         resolve(data as OnChangeSourceAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourcePartBinNum
   Description: OnChangeSourcePartBinNum
   OperationID: OnChangeSourcePartBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePartBinNum(requestBody:OnChangeSourcePartBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePartBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePartBinNum", {
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
         resolve(data as OnChangeSourcePartBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourcePartLotNum
   Description: OnChangeSourcePartLotNum
   OperationID: OnChangeSourcePartLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePartLotNum(requestBody:OnChangeSourcePartLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePartLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePartLotNum", {
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
         resolve(data as OnChangeSourcePartLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourceQty
   Description: OnChangeSourcePartQuantity
   OperationID: OnChangeSourceQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourceQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourceQty(requestBody:OnChangeSourceQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourceQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourceQty", {
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
         resolve(data as OnChangeSourceQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new request qty
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangingNumberOfPieces", {
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
   Summary: Invoke method OnChangeSourcePartUOM
   Description: OnChangeSourcePartIUM
   OperationID: OnChangeSourcePartUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePartUOM(requestBody:OnChangeSourcePartUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePartUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePartUOM", {
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
         resolve(data as OnChangeSourcePartUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourcePCID
   Description: OnChangeSourcePCID
   OperationID: OnChangeSourcePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePCID(requestBody:OnChangeSourcePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePCID", {
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
         resolve(data as OnChangeSourcePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourcePCIDHandheld
   Description: OnChangeSourcePCIDHandheld
   OperationID: OnChangeSourcePCIDHandheld
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePCIDHandheld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePCIDHandheld_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourcePCIDHandheld(requestBody:OnChangeSourcePCIDHandheld_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourcePCIDHandheld_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourcePCIDHandheld", {
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
         resolve(data as OnChangeSourcePCIDHandheld_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSourceRevisionNum
   Description: OnChangeSourceRevisionNum
   OperationID: OnChangeSourceRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSourceRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourceRevisionNum(requestBody:OnChangeSourceRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSourceRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/OnChangeSourceRevisionNum", {
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
         resolve(data as OnChangeSourceRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultWarehouse
   Description: Returns the Default Warehouse for the current session company and site
   OperationID: GetDefaultWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultWarehouse(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetDefaultWarehouse", {
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
         resolve(data as GetDefaultWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCIDDestination
   OperationID: GetNewPCIDDestination
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCIDDestination_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDDestination_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCIDDestination(requestBody:GetNewPCIDDestination_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCIDDestination_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetNewPCIDDestination", {
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
         resolve(data as GetNewPCIDDestination_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCIDSource
   OperationID: GetNewPCIDSource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCIDSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCIDSource(requestBody:GetNewPCIDSource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCIDSource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetNewPCIDSource", {
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
         resolve(data as GetNewPCIDSource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPCIDPart
   OperationID: GetNewPCIDPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPCIDPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCIDPart(requestBody:GetNewPCIDPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPCIDPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetNewPCIDPart", {
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
         resolve(data as GetNewPCIDPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: Checks if the quantity will move the inventory quantity negative
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/NegativeInventoryTest", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/GetSelectSerialNumbersParams", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/ValidateSN", {
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



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param sourceDS
      @param destDS
   */  
export interface AddPCIDToPCID_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface AddPCIDToPCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param sourceDS
      @param destDS
      @param destPCID
      @param warehouseCode
   */  
export interface AddPartToPCIDAndRefreshDest_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
      /**  Destination PCID  */  
   destPCID:string,
      /**  Selected Warehouse  */  
   warehouseCode:string,
}

export interface AddPartToPCIDAndRefreshDest_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param sourceDS
      @param destDS
   */  
export interface AddPartToPCID_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface AddPartToPCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

export interface Erp_Tablesets_PCIDBuildSplitMergeDestItemRow{
   Company:string,
   PCID:string,
   PCIDItemSeq:number,
   ItemPCID:string,
   ItemPartNum:string,
   ItemPartDesc:string,
   ItemLotNum:string,
   ItemIUM:string,
   ItemQuantity:number,
   SerialTrackedPart:boolean,
   PrevItemPCID:string,
   SelectedForAction:boolean,
   MoveQuantity:number,
   LotTrackedPart:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   ItemAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   ItemAttributeSetShortDescription:string,
   ItemPartAttrClassID:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   ItemRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDBuildSplitMergeDestRow{
   Company:string,
   PCID:string,
   PkgControlStatus:string,
   PkgControlIDCode:string,
   PkgCode:string,
   PkgControlIDDesc:string,
   WarehouseCode:string,
   PreviousPCID:string,
   Plant:string,
   PkgCodeDescription:string,
   BinNum:string,
   BinDescription:string,
   WarehouseDescription:string,
   PCIDContainsChildParts:boolean,
   PCIDContainsChildPCIDs:boolean,
   BinNumEnabled:boolean,
      /**  Indicates if serial number tracking is available.  Is set to true when the warehouse plant does full serial tracking, or the warehouse plant does outbound serial tracking and the PCID is an outbound container.  */  
   SerialNumberTracking:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDBuildSplitMergeDestTableset{
   PCIDBuildSplitMergeDest:Erp_Tablesets_PCIDBuildSplitMergeDestRow[],
   PCIDBuildSplitMergeDestItem:Erp_Tablesets_PCIDBuildSplitMergeDestItemRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCIDBuildSplitMergeSourceItemRow{
   Company:string,
   PCID:string,
   PCIDItemSeq:number,
   ItemPCID:string,
   ItemPartNum:string,
   ItemPartDesc:string,
   ItemLotNum:string,
   ItemIUM:string,
   ItemQuantity:number,
   MoveQuantity:number,
   PrevItemPCID:string,
   SerialTrackedPart:boolean,
   SelectedForAction:boolean,
   LotTrackedPart:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   ItemAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   ItemAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   ItemAttributeSetShortDescription:string,
   ItemPartAttrClassID:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   ItemRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDBuildSplitMergeSourcePartRow{
   Company:string,
   Plant:string,
   PartNum:string,
   PartDescription:string,
   BinNum:string,
   BinDescription:string,
   LotNum:string,
   LotTrackedPart:boolean,
   SerialTrackedPart:boolean,
   OnHandQuantity:number,
   SourceQuantity:number,
   AvailableQuantity:number,
   WarehouseCode:string,
   WarehouseDescription:string,
   SourceUOM:string,
   AvailableUOM:string,
   OnHandUOM:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   EnableAttributeSetSearch:boolean,
   PartAttrClassID:string,
   PartTrackInventoryAttributes:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   PartTrackInventoryByRevision:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset{
   PCIDBuildSplitMergeSourcePart:Erp_Tablesets_PCIDBuildSplitMergeSourcePartRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCIDBuildSplitMergeSourceRow{
   Company:string,
   WarehouseCode:string,
   PCID:string,
   PkgControlStatus:string,
   PkgControlIDCode:string,
   PkgCode:string,
   WarehouseDescription:string,
   PkgControlIDDesc:string,
   PkgCodeDescription:string,
   PreviousPCID:string,
   Plant:string,
   PCIDContainsChildPCIDs:boolean,
   PCIDContainsChildParts:boolean,
   BinNum:string,
   BinDescription:string,
   BinNumEnabled:boolean,
      /**  Indicates if serial number tracking is available.  Is set to true when the warehouse plant does full serial tracking, or the warehouse plant does outbound serial tracking and the PCID is an outbound container.  */  
   SerialNumberTracking:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCIDBuildSplitMergeSourceTableset{
   PCIDBuildSplitMergeSource:Erp_Tablesets_PCIDBuildSplitMergeSourceRow[],
   PCIDBuildSplitMergeSourceItem:Erp_Tablesets_PCIDBuildSplitMergeSourceItemRow[],
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

export interface GetDefaultWarehouse_output{
parameters : {
      /**  output parameters  */  
   warehouseCode:string,
   warehouseDesc:string,
}
}

   /** Required : 
      @param destPCID
      @param getPCIDContents
      @param destDS
   */  
export interface GetDestPCID_input{
      /**  Destination PCID  */  
   destPCID:string,
      /**  Get PCID Contents  */  
   getPCIDContents:boolean,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface GetDestPCID_output{
parameters : {
      /**  output parameters  */  
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPCIDDestination_input{
   ds:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface GetNewPCIDDestination_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPCIDPart_input{
   ds:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface GetNewPCIDPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param ds
      @param clearWarehouse
   */  
export interface GetNewPCIDSource_input{
   ds:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
   clearWarehouse:boolean,
}

export interface GetNewPCIDSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param quantity
      @param unitOfMeasure
      @param warehouseCode
      @param binNum
      @param lotNum
      @param pcid
      @param dataSource
      @param voidedOnly
      @param sysRowID
   */  
export interface GetSelectSerialNumbersParams_input{
      /**  The source part number  */  
   partNum:string,
      /**  The part's attribute set  */  
   attributeSetID:number,
      /**  The source quantity  */  
   quantity:number,
      /**  The source unit of measure  */  
   unitOfMeasure:string,
      /**  The warehouse code  */  
   warehouseCode:string,
      /**  The source bin number  */  
   binNum:string,
      /**  The source lot number  */  
   lotNum:string,
      /**  The source pcid number  */  
   pcid:string,
      /**  Indicates the source of the data: SourcePart = from part, SourceItem = from source control item, DestItem = from destination control item  */  
   dataSource:string,
      /**  Indicates if only voided serial numbers should be returned  */  
   voidedOnly:boolean,
      /**  The source SysRowID  */  
   sysRowID:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
}

   /** Required : 
      @param sourcePCID
      @param getPCIDContents
      @param sourceDS
   */  
export interface GetSourcePCID_input{
      /**  Source PCID  */  
   sourcePCID:string,
      /**  Get PCID Contents  */  
   getPCIDContents:boolean,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface GetSourcePCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
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
      @param destDS
      @param sourceDS
   */  
export interface MoveFromDestPCIDToSourcePCID_input{
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface MoveFromDestPCIDToSourcePCID_output{
parameters : {
      /**  output parameters  */  
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
   pcidNotMovedMessage:string,
   serialTrackPartsNotMovedMessage:string,
}
}

   /** Required : 
      @param sourceDS
      @param destDS
   */  
export interface MoveFromSourcePCIDToDestPCIDAndRefresh_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface MoveFromSourcePCIDToDestPCIDAndRefresh_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
   pcidNotMovedMessage:string,
   serialTrackPartsNotMovedMessage:string,
}
}

   /** Required : 
      @param sourceDS
      @param destDS
      @param fromHandHeld
      @param validateSNForOutbound
   */  
export interface MoveFromSourcePCIDToDestPCID_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
      /**  Indicates if the method was called from handheld  */  
   fromHandHeld:boolean,
      /**  Indicates the validation for serial number selection should be validated when moving from a non-outbound container to an outbound container  */  
   validateSNForOutbound:boolean,
}

export interface MoveFromSourcePCIDToDestPCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
   pcidNotMovedMessage:string,
   serialTrackPartsNotMovedMessage:string,
}
}

   /** Required : 
      @param partNum
      @param warehouseCode
      @param binNum
      @param lotNum
      @param attributeSetID
      @param pcid
      @param dimCode
      @param dimConvFactor
      @param quantity
   */  
export interface NegativeInventoryTest_input{
   partNum:string,
   warehouseCode:string,
   binNum:string,
   lotNum:string,
   attributeSetID:number,
   pcid:string,
   dimCode:string,
   dimConvFactor:number,
   quantity:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   negativeQuantityAction:string,
   message:string,
}
}

   /** Required : 
      @param newDestBinNum
      @param destDS
   */  
export interface OnChangeDestBinNum_input{
      /**  Dest BinNum  */  
   newDestBinNum:string,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface OnChangeDestBinNum_output{
parameters : {
      /**  output parameters  */  
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param newDestPCID
      @param getPCIDContents
      @param destDS
   */  
export interface OnChangeDestPCID_input{
      /**  Dest PCID  */  
   newDestPCID:string,
      /**  Get PCID Contents  */  
   getPCIDContents:boolean,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface OnChangeDestPCID_output{
parameters : {
      /**  output parameters  */  
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param newItemLotNum
      @param sourceDS
   */  
export interface OnChangeItemLotNum_input{
      /**  Item Lot Number  */  
   newItemLotNum:string,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface OnChangeItemLotNum_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param newItemPCID
      @param sourceDS
   */  
export interface OnChangeItemPCID_input{
      /**  Item PCID  */  
   newItemPCID:string,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface OnChangeItemPCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param newItemPartNum
      @param sourceDS
   */  
export interface OnChangeItemPartNum_input{
      /**  Item PartNum  */  
   newItemPartNum:string,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface OnChangeItemPartNum_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param newSourceAttributeSetID
      @param sourcePartDS
   */  
export interface OnChangeSourceAttributeSetID_input{
      /**  Attribute Set  */  
   newSourceAttributeSetID:number,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourceAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param newSourcePCID
      @param getPCIDContents
      @param sourceDS
   */  
export interface OnChangeSourcePCIDHandheld_input{
      /**  Source PCID  */  
   newSourcePCID:string,
      /**  Get PCID Contents  */  
   getPCIDContents:boolean,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface OnChangeSourcePCIDHandheld_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param newSourcePCID
      @param getPCIDContents
      @param sourceDS
   */  
export interface OnChangeSourcePCID_input{
      /**  Source PCID  */  
   newSourcePCID:string,
      /**  Get PCID Contents  */  
   getPCIDContents:boolean,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface OnChangeSourcePCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param newSourceBinNum
      @param sourcePartDS
   */  
export interface OnChangeSourcePartBinNum_input{
      /**  Bin Number  */  
   newSourceBinNum:string,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourcePartBinNum_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param newSourceLotNum
      @param sourcePartDS
   */  
export interface OnChangeSourcePartLotNum_input{
      /**  Lot Number  */  
   newSourceLotNum:string,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourcePartLotNum_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param newSourcePartNum
      @param newSourceWarehouseCode
      @param sourcePartDS
   */  
export interface OnChangeSourcePartNum_input{
      /**  Part Number  */  
   newSourcePartNum:string,
      /**  Warehouse Code can be specified if the Source PCID is empty and does not currently have a Warehouse assigned  */  
   newSourceWarehouseCode:string,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourcePartNum_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param newSourceUOM
      @param sourcePartDS
   */  
export interface OnChangeSourcePartUOM_input{
      /**  Unit of Measure  */  
   newSourceUOM:string,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourcePartUOM_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param sourceQuantity
      @param sourcePartDS
   */  
export interface OnChangeSourceQty_input{
      /**  Source Quantity  */  
   sourceQuantity:number,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourceQty_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param newRevisionNum
      @param sourcePartDS
   */  
export interface OnChangeSourceRevisionNum_input{
      /**  Revision num  */  
   newRevisionNum:string,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangeSourceRevisionNum_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param sourcePartDS
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   sourcePartDS:Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset,
}
}

   /** Required : 
      @param destDS
      @param sourceDS
   */  
export interface RemoveFromDestPCID_input{
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
}

export interface RemoveFromDestPCID_output{
parameters : {
      /**  output parameters  */  
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
}
}

   /** Required : 
      @param sourceDS
      @param destDS
   */  
export interface RemoveFromSourcePCID_input{
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset[],
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset[],
}

export interface RemoveFromSourcePCID_output{
parameters : {
      /**  output parameters  */  
   sourceDS:Erp_Tablesets_PCIDBuildSplitMergeSourceTableset,
   destDS:Erp_Tablesets_PCIDBuildSplitMergeDestTableset,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param warehouseCode
      @param serialNumber
   */  
export interface ValidateSN_input{
      /**  Part number to validate.  */  
   partNum:string,
      /**  The part's attribute set  */  
   attributeSetID:number,
      /**  Warehouse to validate.  */  
   warehouseCode:string,
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   isVoided:boolean,
}
}

