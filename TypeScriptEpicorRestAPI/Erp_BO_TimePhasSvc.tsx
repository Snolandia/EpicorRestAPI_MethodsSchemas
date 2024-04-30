import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.TimePhasSvc
// Description: Time Phase Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", {
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
   Summary: Invoke method EnableDisableWhatIfAndTFSugTogs
   Description: SET Enable or Disable WhatIf And TFSugTogs
   OperationID: EnableDisableWhatIfAndTFSugTogs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableDisableWhatIfAndTFSugTogs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EnableDisableWhatIfAndTFSugTogs(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<EnableDisableWhatIfAndTFSugTogs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/EnableDisableWhatIfAndTFSugTogs", {
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
         resolve(data as EnableDisableWhatIfAndTFSugTogs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFrameTitle
   OperationID: GetFrameTitle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFrameTitle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFrameTitle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFrameTitle(requestBody:GetFrameTitle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFrameTitle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetFrameTitle", {
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
         resolve(data as GetFrameTitle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFrameTitleWithTime
   Description: Geting of FrameTitle by Plant. It called from Kinetic UI to get time portion separately
   OperationID: GetFrameTitleWithTime
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFrameTitleWithTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFrameTitleWithTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFrameTitleWithTime(requestBody:GetFrameTitleWithTime_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFrameTitleWithTime_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetFrameTitleWithTime", {
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
         resolve(data as GetFrameTitleWithTime_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLastRunDateTimes
   Description: Gets the last mrp run date and time and the last scheduled date
   OperationID: GetLastRunDateTimes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLastRunDateTimes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLastRunDateTimes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLastRunDateTimes(requestBody:GetLastRunDateTimes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLastRunDateTimes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetLastRunDateTimes", {
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
         resolve(data as GetLastRunDateTimes_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetPartXRefInfo", {
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
   Summary: Invoke method GetContractByID
   Description: This method retrieve an active and approved planning contract
   OperationID: GetContractByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContractByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContractByID(requestBody:GetContractByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContractByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetContractByID", {
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
         resolve(data as GetContractByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GoProcessTimePhase
   Description: Creating the TimePhase by PartNum and Plant
   OperationID: GoProcessTimePhase
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GoProcessTimePhase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GoProcessTimePhase_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GoProcessTimePhase(requestBody:GoProcessTimePhase_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GoProcessTimePhase_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GoProcessTimePhase", {
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
         resolve(data as GoProcessTimePhase_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPlanningAttributeSetID
   Description: Get the AttributeSetID of the Planning Attribute Set of any Attribute Set
by passing in its AttributeSetID.
   OperationID: GetPlanningAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPlanningAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlanningAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlanningAttributeSetID(requestBody:GetPlanningAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPlanningAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetPlanningAttributeSetID", {
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
         resolve(data as GetPlanningAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   Description: Find part.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/FindPart", {
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
   Description: GetPartFromRowID.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/GetPartFromRowID", {
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
   Summary: Invoke method FindPlanningAttributeSet
   Description: Resolve Attribute ID passed into form
   OperationID: FindPlanningAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPlanningAttributeSet(requestBody:FindPlanningAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPlanningAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/FindPlanningAttributeSet", {
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
         resolve(data as FindPlanningAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindAttributeSet
   Description: Find attribute short description and attributeSetDesc
   OperationID: FindAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindAttributeSet(requestBody:FindAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/FindAttributeSet", {
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
         resolve(data as FindAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAttributeSetIDFromRevisionNum(requestBody:UpdateAttributeSetIDFromRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAttributeSetIDFromRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/UpdateAttributeSetIDFromRevisionNum", {
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
         resolve(data as UpdateAttributeSetIDFromRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateRevisionNumFromAttributeSetID
   Description: This method updates the revision number from an attributeSetID when new attributeSetID is selected.
   OperationID: UpdateRevisionNumFromAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateRevisionNumFromAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateRevisionNumFromAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateRevisionNumFromAttributeSetID(requestBody:UpdateRevisionNumFromAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateRevisionNumFromAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/UpdateRevisionNumFromAttributeSetID", {
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
         resolve(data as UpdateRevisionNumFromAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method determines whether revision is Used in Planning.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody:PartsAttributeClassHasRevisionAndIsMRPTracked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PartsAttributeClassHasRevisionAndIsMRPTracked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/PartsAttributeClassHasRevisionAndIsMRPTracked", {
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
         resolve(data as PartsAttributeClassHasRevisionAndIsMRPTracked_output)
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
export interface EnableDisableWhatIfAndTFSugTogs_output{
parameters : {
      /**  output parameters  */  
   EnableBoth:boolean,
}
}

export interface Erp_Tablesets_PartPlanningAttributeRow{
      /**  AttributeSetDescription  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Description of the Planning Attribute Set  */  
   PlanningAttributeSet:string,
   PlanningAttributeSetSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartPlanningAttributeTableset{
   PartPlanningAttribute:Erp_Tablesets_PartPlanningAttributeRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_TimePhasRow{
   PartNum:string,
   SortByDate:boolean,
   DueDate:string,
   RequirementFlag:boolean,
   ReceiptQty:number,
   RequiredQty:number,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   PONum:number,
   POLine:number,
   PORelNum:number,
   LeadTime:number,
   BalanceQty:number,
   ExceptionReason:string,
   SugOrderDate:string,
   SourceName:string,
   PartDescription:string,
   IUM:string,
   BuyForJob:boolean,
   PrintMe:boolean,
   SourceFile:string,
   Plant:string,
   JobStatus:string,
   Suggestions:boolean,
   TOSuggestions:boolean,
   TFOrder:string,
      /**  Container ID the PO release is tied to.  This is used for display purposes only.  */  
   ContainerID:number,
      /**  Promise Date for the Part Release given by the PO Vendor  */  
   PromiseDate:string,
   ContractID:string,
   LinkToContract:boolean,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   DispNumberOfPieces:number,
   NumberOfPieces:number,
      /**  Revision Number associated with part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TimePhasTableset{
   TimePhas:Erp_Tablesets_TimePhasRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param attributeSetID
   */  
export interface FindAttributeSet_input{
   attributeSetID:number,
}

export interface FindAttributeSet_output{
parameters : {
      /**  output parameters  */  
   attributeSetShortDesc:string,
   attributeSetDesc:string,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface FindPart_input{
      /**  PartNum  */  
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
      @param partNum
      @param attributeSetID
      @param trackInventoryAttributes
      @param hasMRPPlanningAttribute
   */  
export interface FindPlanningAttributeSet_input{
   partNum:string,
   attributeSetID:number,
   trackInventoryAttributes:boolean,
   hasMRPPlanningAttribute:boolean,
}

export interface FindPlanningAttributeSet_output{
parameters : {
      /**  output parameters  */  
   attributeSetShortDesc:string,
   attributeSetDesc:string,
   newAttributeSetID:number,
}
}

   /** Required : 
      @param contractID
   */  
export interface GetContractByID_input{
      /**  ContractID changed  */  
   contractID:string,
}

export interface GetContractByID_output{
parameters : {
      /**  output parameters  */  
   description:string,
}
}

   /** Required : 
      @param inPlant
      @param inPart
   */  
export interface GetFrameTitleWithTime_input{
      /**  The Plant  */  
   inPlant:string,
      /**  The Partt  */  
   inPart:string,
}

export interface GetFrameTitleWithTime_output{
parameters : {
      /**  output parameters  */  
   mRPLastRun:string,
   mRPLastScheduled:string,
}
}

   /** Required : 
      @param inPlant
      @param inPart
   */  
export interface GetFrameTitle_input{
   inPlant:string,
   inPart:string,
}

export interface GetFrameTitle_output{
parameters : {
      /**  output parameters  */  
   frameTitle:string,
   mRPLastRunDate:string,
   FrameLastSchedTitle:string,
   mRPLastScheduledDate:string,
}
}

   /** Required : 
      @param inPlant
      @param inPart
   */  
export interface GetLastRunDateTimes_input{
      /**  The Plant  */  
   inPlant:string,
      /**  The Part  */  
   inPart:string,
}

export interface GetLastRunDateTimes_output{
parameters : {
      /**  output parameters  */  
   mrpLastRun:string,
   mrpLastRunTime:string,
   mrpLastScheduled:string,
}
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
      /**  Row Type  */  
   ipRowType:string,
      /**  Row ID  */  
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
      @param plantID
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  Plant ID  */  
   plantID:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
   returnObj:Erp_Tablesets_PartPlanningAttributeTableset[],
parameters : {
      /**  output parameters  */  
   partNum:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
   partFound:boolean,
   partDesc:string,
}
}

   /** Required : 
      @param attributeSetID
   */  
export interface GetPlanningAttributeSetID_input{
   attributeSetID:number,
}

export interface GetPlanningAttributeSetID_output{
   returnObj:number,
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param plant
      @param whatIfTog
      @param tFSug
      @param plnCtInfo
      @param contractID
   */  
export interface GoProcessTimePhase_input{
      /**  Part Number  */  
   partNum:string,
   attributeSetID:number,
      /**  Plant  */  
   plant:string,
      /**  Suggestions  */  
   whatIfTog:boolean,
      /**  Transfer Order Suggestions  */  
   tFSug:boolean,
      /**  Planning Contract Info  */  
   plnCtInfo:boolean,
      /**  ContractID  */  
   contractID:string,
}

export interface GoProcessTimePhase_output{
   returnObj:Erp_Tablesets_TimePhasTableset[],
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
      @param attrClassID
   */  
export interface PartsAttributeClassHasRevisionAndIsMRPTracked_input{
      /**  current Attribute Class ID  */  
   attrClassID:string,
}

export interface PartsAttributeClassHasRevisionAndIsMRPTracked_output{
   returnObj:boolean,
}

   /** Required : 
      @param partNum
      @param revisionNum
   */  
export interface UpdateAttributeSetIDFromRevisionNum_input{
      /**  current part number  */  
   partNum:string,
      /**  new revision selected  */  
   revisionNum:string,
}

export interface UpdateAttributeSetIDFromRevisionNum_output{
parameters : {
      /**  output parameters  */  
   attributeSetID:number,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
   */  
export interface UpdateRevisionNumFromAttributeSetID_input{
      /**  current part number  */  
   partNum:string,
      /**  new AttributeSetID selected  */  
   attributeSetID:number,
}

export interface UpdateRevisionNumFromAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   revisionNum:string,
}
}

