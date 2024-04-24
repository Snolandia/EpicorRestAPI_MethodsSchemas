import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ReturnRequestSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", {
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
   Summary: Invoke method CheckEmployee
   Description: This method needs to be called from the main menu only.  if the object
is being called from the shop floor menu then the employee id has already been determined
and validated and is passed in
   OperationID: CheckEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEmployee(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/CheckEmployee", {
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
   Summary: Invoke method GetNewAssyMtlInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Job#
   OperationID: GetNewAssyMtlInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAssyMtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAssyMtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAssyMtlInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/GetNewAssyMtlInfo", {
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
   Summary: Invoke method GetNewMiscInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Part#
   OperationID: GetNewMiscInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMiscInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMiscInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMiscInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/GetNewMiscInfo", {
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
   Summary: Invoke method GetNewSalvageInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Job#
   OperationID: GetNewSalvageInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalvageInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalvageInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSalvageInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/GetNewSalvageInfo", {
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
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangingAttributeSet", {
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
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangeAssembly
   Description: Call this method to update the dataset when the ReturnRequest.AssemblySeq is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeAssembly", {
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
   Summary: Invoke method OnChangeFromBin
   Description: Call this method to update the dataset when the RequestLines.FromBinNum is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeFromBin", {
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
   Summary: Invoke method OnChangeFromWhse
   Description: Call this method to update the dataset when the RequestLines.FromWhse is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromWhse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeFromWhse", {
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
   Summary: Invoke method OnChangeIUM
   Description: Call this method when the value of Epicor.Mfg.BO.ReturnRequest.IUM changes.
   OperationID: OnChangeIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeIUM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeIUM", {
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
   Summary: Invoke method OnChangeJobNum
   Description: Call this method to update the dataset when the ReturnRequest.JobNum is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeMtlSeq
   Description: Call this method to update the dataset when the ReturnRequest.MtlSeq is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMtlSeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeMtlSeq", {
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
   Summary: Invoke method OnChangePartNum
   Description: Call this method to update the dataset when the ReturnRequest.PartNum is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangePartNum", {
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
   Summary: Invoke method OnChangeFromPCID
   Description: Call this method when the value of From PCID changes.
   OperationID: OnChangeFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromPCID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeFromPCID", {
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
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.ReturnRequest.RequestQty changes.
   OperationID: OnChangeRequestQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRequestQty(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeRequestQty", {
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
   Summary: Invoke method OnChangeToBin
   Description: Call this method to update the dataset when the RequestLines.ToBinNum is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToBin(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeToBin", {
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
   Summary: Invoke method OnChangeToWhse
   Description: Call this method to update the dataset when the RequestLines.ToWhse is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToWhse(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangeToWhse", {
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
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new request qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/OnChangingNumberOfPieces", {
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
   Summary: Invoke method ProcessLines
   Description: Run this method when done updating all the detail lines (currently OK button in 6.1)
clear screen when done
Must set the ReturnRequest RowMod to "U" for this method to work
   OperationID: ProcessLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessLines(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/ProcessLines", {
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
   Summary: Invoke method GetCodeDescList
   Description: Returns code description as string
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/GetCodeDescList", {
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
      @param empID
   */  
export interface CheckEmployee_input{
      /**  Employee ID  */  
   empID:string,
}

export interface CheckEmployee_output{
parameters : {
      /**  output parameters  */  
   empName:string,
}
}

export interface Erp_Tablesets_RequestLinesRow{
   JobNum:string,
   AssemblySeq:number,
   JobSeq:number,
   JobSeqType:string,
   PartNum:string,
   Description:string,
   RequiredQty:number,
   QtyIssued:number,
   QtyStaged:number,
      /**  Unit of Measure used for the transaction  */  
   IUM:string,
   TranType:string,
   MtlQueueQty:number,
   RequestQty:number,
   NextJobSeq:number,
   FromBinNum:string,
   FromWhse:string,
   ToBinNum:string,
   ToWhse:string,
   DummyKeyField:string,
   DummyLineField:string,
   FromWhseDesc:string,
   FromBinDesc:string,
   ToWhseDesc:string,
   ToBinDesc:string,
      /**  UOM for the Quantity Issued  */  
   IssuedUM:string,
      /**  The quantity value converted from Request UOM to Issued UOM.  */  
   ThisTranQty:number,
   RequiredQtyUOM:string,
   RequestQtyUOM:string,
   QtyStagedUOM:string,
      /**  Requested UOM  */  
   MtlQueueQtyUOM:string,
   QtyIssuedUOM:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   EnableAttributeSetSearch:boolean,
      /**  Site Identifier  */  
   Plant:string,
   FromPCID:string,
   ToPCID:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReturnRequestRow{
   JobNum:string,
   JobPartNum:string,
   JobPartDesc:string,
   AssemblySeq:number,
   AsmPartNum:string,
   AsmPartDesc:string,
   MtlSeq:number,
   MtlPartNum:string,
   MtlPartDesc:string,
   PartNum:string,
   PartDesc:string,
   ReturnType:string,
      /**  Dummy Unique Key  */  
   DummyKeyField:string,
   EmpID:string,
   EmpName:string,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   EnableAttributeSetSearch:boolean,
   Plant:string,
   PlantConfCtrlEnablePackageControl:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   MtlRevisionNum:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   AsmRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReturnRequestTableset{
   ReturnRequest:Erp_Tablesets_ReturnRequestRow[],
   RequestLines:Erp_Tablesets_RequestLinesRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  table name  */  
   tableName:string,
      /**  field name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface GetNewAssyMtlInfo_input{
      /**  Job Number  */  
   jobNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface GetNewAssyMtlInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface GetNewMiscInfo_input{
      /**  Part Number  */  
   partNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface GetNewMiscInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface GetNewSalvageInfo_input{
      /**  Job Number  */  
   jobNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface GetNewSalvageInfo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
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
      @param assemblySeq
      @param ds
   */  
export interface OnChangeAssembly_input{
      /**  AssemblySeq  */  
   assemblySeq:number,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param binNum
      @param cRowIdent
      @param ds
   */  
export interface OnChangeFromBin_input{
      /**  BinNum  */  
   binNum:string,
      /**  RequestLines RowIDent  */  
   cRowIdent:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeFromBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param pcid
      @param ds
      @param pCallProcess
   */  
export interface OnChangeFromPCID_input{
      /**  Proposed PCID value  */  
   pcid:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
      /**  Calling Process value  */  
   pCallProcess:string,
}

export interface OnChangeFromPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param whseCode
      @param cRowIdent
      @param ds
   */  
export interface OnChangeFromWhse_input{
      /**  From Warehose  */  
   whseCode:string,
      /**  RequestLines RowIDent  */  
   cRowIdent:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeFromWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param pUM
      @param ds
   */  
export interface OnChangeIUM_input{
      /**  Transaction UOM  */  
   pUM:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeIUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  JobNum  */  
   jobNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param mtlSeq
      @param ds
   */  
export interface OnChangeMtlSeq_input{
      /**  MtlSeq  */  
   mtlSeq:number,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  PartNum  */  
   partNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param requestQty
      @param cRowIdent
      @param ds
   */  
export interface OnChangeRequestQty_input{
      /**  Request Quantity  */  
   requestQty:number,
      /**  SysRowID  */  
   cRowIdent:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeRequestQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param binNum
      @param cRowIdent
      @param ds
   */  
export interface OnChangeToBin_input{
      /**  BinNum  */  
   binNum:string,
      /**  RequestLines RowIDent  */  
   cRowIdent:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeToBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param whseCode
      @param cRowIdent
      @param ds
   */  
export interface OnChangeToWhse_input{
      /**  To Warehose  */  
   whseCode:string,
      /**  RequestLines RowIDent  */  
   cRowIdent:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangeToWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
      /**  attributeSetID  */  
   attributeSetID:number,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessLines_input{
   ds:Erp_Tablesets_ReturnRequestTableset[],
}

export interface ProcessLines_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReturnRequestTableset[],
}
}

