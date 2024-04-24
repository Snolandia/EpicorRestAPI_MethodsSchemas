import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.SerialMatchingSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/$metadata", {
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
   Summary: Invoke method AutoMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipPartNum">Part.PartNum</param><param name="ipRevNum">PartRev.RevisionNum</param><param name="ipCrtHdr">ipCrtHdr</param><param name="opRevMsg">revision</param><param name="ds">The Serial Matching data set </param>
   OperationID: AutoMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoMatch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/AutoMatch", {
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
   Summary: Invoke method ChangeSerialNum
   Description: Purpose:
Parameters:  none
Notes:type="Epicor.Mfg.BO.SerialMatchingDataSet"
<param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipPartNum">SerialNo.PartNum</param><param name="ipRevNum">PartRev.RevisionNum</param><param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opRevMsg">revision</param><param name="opnoBOMMsg">bommessage</param><return name="ds">The Serial Matching data set </return>
   OperationID: ChangeSerialNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSerialNum(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/ChangeSerialNum", {
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
   Summary: Invoke method ChangeFullyMatched
   Description: Purpose:
Parameters:  none
Notes:type="Epicor.Mfg.BO.SerialMatchingDataSet"
<param name="ipFullyMatched">ttSerialMatchHdr.FullyMatched</param><param name="ds">The Serial Matching data set </param>
   OperationID: ChangeFullyMatched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFullyMatched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFullyMatched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFullyMatched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/ChangeFullyMatched", {
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
   Summary: Invoke method GetAvailableToMatch
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipType"></param><param name="ds">The Serial Matching data set </param>
   OperationID: GetAvailableToMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableToMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableToMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableToMatch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/GetAvailableToMatch", {
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
   Summary: Invoke method GetNewSerialMatchAsmbl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipParAsmblSeqNum">parent assembly AsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: GetNewSerialMatchAsmbl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMatchAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMatchAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialMatchAsmbl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/GetNewSerialMatchAsmbl", {
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
   Summary: Invoke method GetNewSerialMatchMtl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipAsmblSeqNum">ipAsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: GetNewSerialMatchMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMatchMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMatchMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialMatchMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/GetNewSerialMatchMtl", {
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
   Summary: Invoke method OnChangeAsmblSerialNo
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode"></param><param name="ipSerialNum">SerialNo.SerialNumber</param><param name="ipInt"></param><param name="ds">The Serial Matching data set </param>
   OperationID: OnChangeAsmblSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAsmblSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAsmblSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAsmblSerialNo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/OnChangeAsmblSerialNo", {
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
   Summary: Invoke method UpdateSMAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode"></param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipAsmSeqNum"></param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSMAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/UpdateSMAssembly", {
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
   Summary: Invoke method UpdateONSaveAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerilaNum">ipSerilaNum</param><param name="ipAsmblSeqNum">ipAsmblSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateONSaveAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateONSaveAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateONSaveAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateONSaveAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/UpdateONSaveAssembly", {
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
   Summary: Invoke method OnChangeMtlSerialNo
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">revision</param><param name="ipSerialNum">Serial Number</param><param name="ipMtlSeqNum">ipMtlSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: OnChangeMtlSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMtlSerialNo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/OnChangeMtlSerialNo", {
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
   Summary: Invoke method UpdateSMMtl
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">Part.PartNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSMMtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/UpdateSMMtl", {
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
   Summary: Invoke method UpdateSMMaterial
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipMode">Part.PartNum</param><param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipMtlSeqNum">ipMtlSeqNum</param><param name="ds">The Serial Matching data set </param>
   OperationID: UpdateSMMaterial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSMMaterial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSMMaterial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSMMaterial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/UpdateSMMaterial", {
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
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">Part.PartNum</param><param name="ds">The Serial Matching data set </param>
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/OnChangePartNum", {
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
   Summary: Invoke method SetFullyMatched
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipAssmblSeq">JobAsmbl.AssemblySeq</param><param name="ds">The Serial Matching data set </param>
   OperationID: SetFullyMatched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetFullyMatched_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetFullyMatched_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetFullyMatched(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/SetFullyMatched", {
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
   Summary: Invoke method ValidateAssembly
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opQuestion"></param><param name="ds">The Serial Matching data set </param>
   OperationID: ValidateAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAssembly(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/ValidateAssembly", {
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
   Summary: Invoke method ValidateJob
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipJobNum">JobHead.JobNum</param><param name="opQuestion"></param>
   OperationID: ValidateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateJob(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/ValidateJob", {
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
   Summary: Invoke method ValidateTopSerialNumber
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipSerialNo">SerialNo.SerialNumber</param><param name="ipJobNum">JobHead.JobNum</param><param name="ipAssemblySeq">JobAsmbl.AssemblySeq</param><param name="opErrMsg"></param>
   OperationID: ValidateTopSerialNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTopSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTopSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTopSerialNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/ValidateTopSerialNumber", {
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
   Summary: Invoke method GetPlantLLSerTrk
   Description: Purpose:
Parameters:  none
Notes:
<return name="opLLSerTrk">PlantConfCtrl.LowLvlSerialTrk</return>
   OperationID: GetPlantLLSerTrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantLLSerTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantLLSerTrk(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/GetPlantLLSerTrk", {
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
   Summary: Invoke method GetMatchToParentAsmblSerialNo
   OperationID: GetMatchToParentAsmblSerialNo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatchToParentAsmblSerialNo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatchToParentAsmblSerialNo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMatchToParentAsmblSerialNo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchingSvc/GetMatchToParentAsmblSerialNo", {
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
      @param ipJobNum
      @param ipAssemblySeq
      @param ipSerialNo
      @param ipPartNum
      @param ipRevNum
      @param ipCrtHdr
      @param ds
   */  
export interface AutoMatch_input{
   ipJobNum:string,
   ipAssemblySeq:number,
   ipSerialNo:string,
   ipPartNum:string,
   ipRevNum:string,
   ipCrtHdr:boolean,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface AutoMatch_output{
parameters : {
      /**  output parameters  */  
   opRevMsg:string,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipFullyMatched
      @param ds
   */  
export interface ChangeFullyMatched_input{
   ipFullyMatched:boolean,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface ChangeFullyMatched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipSerialNo
      @param ipPartNum
      @param ipRevNum
      @param ipJobNum
      @param ipAssemblySeq
   */  
export interface ChangeSerialNum_input{
   ipSerialNo:string,
   ipPartNum:string,
   ipRevNum:string,
   ipJobNum:string,
   ipAssemblySeq:number,
}

export interface ChangeSerialNum_output{
   returnObj:Erp_Tablesets_SerialMatchingTableset[],
parameters : {
      /**  output parameters  */  
   opRevMsg:string,
   opnoBOMMsg:string,
}
}

export interface Erp_Tablesets_AvailToMatchRow{
   Company:string,
      /**  Part Number  */  
   PartNum:string,
      /**  Serial Number  */  
   SerialNumber:string,
      /**  Job Number assigned to the SerialNo  */  
   JobNum:string,
      /**  Job Assembly Seq the SerialNo should be defined as a child of  */  
   IssueToAssembly:number,
      /**  MtlSeq the serial number was issued to.  */  
   MtlSeq:number,
      /**  Indicates whether the serial number has been matched to a parent in SerialMatch.  */  
   Matched:boolean,
      /**  Indicates if the serial number has been selected to be matched  */  
   Selected:boolean,
   AttributeSetID:number,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialMatchAsmblRow{
      /**  Sequence counter for this SerialMatchAsmbl record; required to keep the record unique because when the BOM is exploded to create the rows for the dataset, multiple records may be generated with the same assembly number (assembly SN will be null for all unmatched assembly qty).  */  
   Company:string,
   AsmblSeqNum:number,
      /**  AssemblySeq number of this assemby for the BOM  */  
   BOMAssemblySeq:number,
      /**  Indicates whether this assembly is serial tracked. Non tracked assemblies are included because they may have serial tracked requirements.  */  
   IsSerialTracked:boolean,
      /**  Top SN part number. Used to relate SerialMatchAsmbl to SerialMatchHdr  */  
   TopPartNum:string,
      /**  Top SN serial number. Used to relate SerialMatchAsmbl to SerialMatchHdr  */  
   TopSerialNum:string,
      /**  This will be the SeqNum from the SeiralMatchAsmbl record of the SerialMatchAsmbl record this material is required by. In the case where SerialMatchAsmbl part is not serial tracked, this will not be the same assembly sequence counter as in the ParentAsmblSeqNum.  */  
   ReqByAsmblSeqNum:number,
      /**  Part number for the assembly parent serial number  */  
   ParentPartNum:string,
      /**  Assembly Parent serial number  */  
   ParentSerialNo:string,
      /**  AssemblySeq for the assembly parent serial number.  */  
   ParentAssemblySeq:number,
      /**  Parent part number description from Part.PartDescription.  */  
   ParentPartDesc:string,
      /**  This will be the AsmblSeqNum from the SeiralMatchAsmbl record of the serial tracked parent assembly this material serial numberl will be matched to. In the case where the subassembly this subassembly is required by is not serial tracked, this will not be the same assembly sequence counter as in the ReqByAsmblSeqNum field. This relates the SerialMatchAsmbl record to its parent serial number SerialMatchAsmbl  */  
   ParentAsmblSeqNum:number,
      /**  Part number for the assembly serial number  */  
   AsmblPartNum:string,
      /**  Assembly serial number  */  
   AsmblSerialNo:string,
   AsmblPartDesc:string,
      /**  Qty of this assembly required per parent assembly  */  
   QtyPer:number,
      /**  PullQty for this assembly  */  
   PullQty:number,
      /**  OverRunQty for this assembly  */  
   OverRunQty:number,
      /**  RequiredQty for this assembly  */  
   RequiredQty:number,
      /**  Indicates whether this record was manually added using the Add Subassembly option in the Serial Matching UI. Set to true when a new entry is added in the UI.  */  
   AddedByMatching:boolean,
      /**  Indicates if this assembly serial number has  all child serial numbers (material and subassembly) matched  */  
   FullyMatched:boolean,
   ReqByAssemblySeq:number,
   RecNum:number,
   BOMSeq:number,
   BOMLevel:number,
   ParRowIDent:string,
   FromReassignSNAsm:boolean,
   AsmblAttributeSetID:number,
   AsmblAttributeSetIDDesc:string,
   AsmblAttributeSetIDShortDesc:string,
   AsmblRevisionNum:string,
   ParentAttributeSetID:number,
   ParentAttributeSetIDDesc:string,
   ParentAttributeSetIDShortDesc:string,
   ParentRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialMatchHdrRow{
      /**  Company  */  
   Company:string,
      /**  Job Number for the Serial Number if this serial was created for the top level assembly of a job.  */  
   JobNum:string,
      /**  Part number for the parent serial number, from SerialNo.PartNum  */  
   TopPartNum:string,
      /**  When Serial Matching is in Job mode this is from JobHead RevisionNum; when in Serial mode with no job it will be for the part revision being used for matching.  */  
   RevisionNum:string,
      /**  In Job Mode this is from JobHead PartDescription; in Serial Mode this is from Part.PartDescription  */  
   PartDescription:string,
      /**  Parent serial number  */  
   TopSerialNum:string,
      /**  Serial Number status from SerialNo.SNStatus  */  
   SNStatus:string,
      /**  In Job Mode: The quantity of the part on the job. This will be the same for all entries for the same part/job in this table so that it can be displayed correctly in the UI, although each record in this table only represents a qty of 1 of the part; in Serial Mode the qty will always be 1.  */  
   Quantity:number,
      /**  The SerialNo CreateDate for the parent serial  */  
   CreateDate:string,
      /**  Indicates whether the UI form should enable the New Child Part menu option.  */  
   EnableNewChildPart:boolean,
      /**  AssemblySeq of the parent part if related to a job  */  
   AssemblySeq:number,
      /**  Indicates if this assembly serial number has  all child serial numbers (material and subassembly) matched  */  
   FullyMatched:boolean,
   SourceIsJob:boolean,
   AttributeSetID:number,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialMatchMtlRow{
   Company:string,
      /**  Sequence counter required to keep the record unique because when the BOM is exploded to create the rows for the dataset, multiple records may be generated with the same part number number (part SN will be null for all unmatched material qty).  */  
   SeqNum:number,
      /**  Top SN part number. Used to relate SerialMatchMtl to SerialMatchHdr  */  
   TopPartNum:string,
      /**  Top SN serial number. Used to relate SerialMatchMtl to SerialMatchHdr  */  
   TopSerialNum:string,
      /**  Part number for the assembly parent serial number  */  
   ParentPartNum:string,
      /**  Assembly Parent serial number  */  
   ParentSerialNo:string,
      /**  AssemblySeq for the assembly parent serial number.  */  
   ParentAssemblySeq:number,
      /**  Parent part number description from Part.PartDescription.  */  
   ParentPartDesc:string,
      /**  This will be the AsmblSeqNum from the SeiralMatchAsmbl record of the SerialMatchAsmbl record this material is required by. In the case where SerialMatchAsmbl part is not serial tracked, this will not be the same assembly sequence as in the ParentAsmblSeqNum field.  */  
   ReqByAsmblSeqNum:number,
      /**  This will be the SeqNum from the SeiralMatchAsmbl record of the serial tracked parent assembly this material serial numberl will be matched to. In the case where the subassembly this material is required by is not serial tracked, this will not be the same assembly sequence counter as in the AsmblSeqNum field. This relates the SerialMatchMtl record to its parent serial number SerialMatchAsmbl  */  
   ParentAsmblSeqNum:number,
      /**  Part number for the material serial number  */  
   MtlPartNum:string,
      /**  Material  serial number  */  
   MtlSerialNo:string,
      /**  Material part number description from Part.PartDescription  */  
   MtlPartDesc:string,
      /**  MtlSeq number of this material requirement for the BOM  */  
   BOMMtlSeq:number,
      /**  AssemblySeq number of this material requirement for the BOM  */  
   BOMAssemblySeq:number,
      /**  Qty of this assembly required per parent assembly  */  
   QtyPer:number,
      /**  Indicates whether this record was manually added using the Add Material option in the Serial Matching UI. Set to true when a new entry is added in the UI.  */  
   AddedByMatching:boolean,
   ParRowIDent:string,
      /**  Sequence counter for material serial numbers  */  
   BOMMtlSeqNum:number,
   FromReassignSNAsm:boolean,
   MtlAttributeSetID:number,
   MtlAttributeSetIDDesc:string,
   MtlAttributeSetIDShortDesc:string,
   MtlRevisionNum:string,
   ParentAttributeSetID:number,
   ParentAttributeSetIDDesc:string,
   ParentAttributeSetIDShortDesc:string,
   ParentRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialMatchingTableset{
   SerialMatchHdr:Erp_Tablesets_SerialMatchHdrRow[],
   SerialMatchAsmbl:Erp_Tablesets_SerialMatchAsmblRow[],
   SerialMatchMtl:Erp_Tablesets_SerialMatchMtlRow[],
   AvailToMatch:Erp_Tablesets_AvailToMatchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ipType
      @param ds
   */  
export interface GetAvailableToMatch_input{
   ipType:string,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface GetAvailableToMatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipAsmSeq
   */  
export interface GetMatchToParentAsmblSerialNo_input{
   ipAsmSeq:number,
}

export interface GetMatchToParentAsmblSerialNo_output{
   returnObj:string,
}

   /** Required : 
      @param ipParAsmblSeqNum
      @param ds
   */  
export interface GetNewSerialMatchAsmbl_input{
   ipParAsmblSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface GetNewSerialMatchAsmbl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipAsmblSeqNum
      @param ds
   */  
export interface GetNewSerialMatchMtl_input{
   ipAsmblSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface GetNewSerialMatchMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

export interface GetPlantLLSerTrk_output{
parameters : {
      /**  output parameters  */  
   opLLSerTrk:number,
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
      @param ipMode
      @param ipSerialNum
      @param ipInt
      @param ds
   */  
export interface OnChangeAsmblSerialNo_input{
   ipMode:string,
   ipSerialNum:string,
   ipInt:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface OnChangeAsmblSerialNo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipMode
      @param ipSerialNum
      @param ipMtlSeqNum
      @param ds
   */  
export interface OnChangeMtlSerialNo_input{
   ipMode:string,
   ipSerialNum:string,
   ipMtlSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface OnChangeMtlSerialNo_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipPartNum
      @param ds
   */  
export interface OnChangePartNum_input{
   ipPartNum:string,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipAssmblSeq
      @param ds
   */  
export interface SetFullyMatched_input{
   ipAssmblSeq:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface SetFullyMatched_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipSerilaNum
      @param ipAsmblSeqNum
      @param ds
   */  
export interface UpdateONSaveAssembly_input{
   ipSerilaNum:string,
   ipAsmblSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface UpdateONSaveAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipMode
      @param ipSerialNo
      @param ipAsmSeqNum
      @param ds
   */  
export interface UpdateSMAssembly_input{
   ipMode:string,
   ipSerialNo:string,
   ipAsmSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface UpdateSMAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipMode
      @param ipSerialNo
      @param ipMtlSeqNum
      @param ds
   */  
export interface UpdateSMMaterial_input{
   ipMode:string,
   ipSerialNo:string,
   ipMtlSeqNum:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface UpdateSMMaterial_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipMode
      @param ds
   */  
export interface UpdateSMMtl_input{
   ipMode:string,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface UpdateSMMtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipJobNum
      @param ipAssemblySeq
      @param ds
   */  
export interface ValidateAssembly_input{
   ipJobNum:string,
   ipAssemblySeq:number,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}

export interface ValidateAssembly_output{
parameters : {
      /**  output parameters  */  
   opQuestion:string,
   ds:Erp_Tablesets_SerialMatchingTableset[],
}
}

   /** Required : 
      @param ipJobNum
   */  
export interface ValidateJob_input{
   ipJobNum:string,
}

export interface ValidateJob_output{
parameters : {
      /**  output parameters  */  
   opQuestion:string,
}
}

   /** Required : 
      @param ipSerialNo
      @param ipJobNum
      @param ipAssemblySeq
   */  
export interface ValidateTopSerialNumber_input{
   ipSerialNo:string,
   ipJobNum:string,
   ipAssemblySeq:number,
}

export interface ValidateTopSerialNumber_output{
parameters : {
      /**  output parameters  */  
   opErrMsg:string,
}
}

