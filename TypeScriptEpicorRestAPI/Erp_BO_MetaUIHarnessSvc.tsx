import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MetaUIHarnessSvc
// Description: Meta UI Harness related functionality
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/$metadata", {
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
   Summary: Invoke method GetListSpecial
   Description: GetListSpecial - returns random list data w/scalars - whereClause has no effect
   OperationID: GetListSpecial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListSpecial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListSpecial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListSpecial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetListSpecial", {
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
   Summary: Invoke method GetSampleRows
   Description: GetSampleRows - returns random row data
   OperationID: GetSampleRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSampleRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetSampleRows", {
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
   Summary: Invoke method GetSampleRowsAdded
   Description: GetSampleRowsAdded - returns random row data
   OperationID: GetSampleRowsAdded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRowsAdded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRowsAdded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSampleRowsAdded(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetSampleRowsAdded", {
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
   Summary: Invoke method GetSampleRowsAddedNoSysRowID
   Description: GetSampleRowsAdded - returns random row data with blank SysRowID
   OperationID: GetSampleRowsAddedNoSysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleRowsAddedNoSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleRowsAddedNoSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSampleRowsAddedNoSysRowID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetSampleRowsAddedNoSysRowID", {
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
   Summary: Invoke method GetDynamicData
   Description: GetDynamicData - returns an untyped dynamic dataset
   OperationID: GetDynamicData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynamicData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynamicData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDynamicData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetDynamicData", {
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
   Summary: Invoke method UpdateSpecial
   Description: Updates all the modified rows
   OperationID: UpdateSpecial
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSpecial_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSpecial_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSpecial(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/UpdateSpecial", {
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
   Summary: Invoke method Update
   Description: Updates all the modified / Added rows
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/Update", {
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
   Summary: Invoke method ModifyRows
   Description: Set Approved to true for all modified rows
   OperationID: ModifyRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifyRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/ModifyRows", {
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
   Summary: Invoke method OnChangeQuantity1
   Description: Invoked on change of Quantity1.  Approve set true if quantity is greater than 50, false if less than.
   OperationID: OnChangeQuantity1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity1_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQuantity1(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/OnChangeQuantity1", {
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
   Summary: Invoke method ModifyRowsReturnUnChanged
   Description: Set Approved to true for all modified rows and return them as unchanged
   OperationID: ModifyRowsReturnUnChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyRowsReturnUnChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyRowsReturnUnChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifyRowsReturnUnChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/ModifyRowsReturnUnChanged", {
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
   Summary: Invoke method DeleteRows
   Description: Delete all modified rows
   OperationID: DeleteRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/DeleteRows", {
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
   Summary: Invoke method ModifyAddDeleteRows
   Description: This will expect three rows and then delete the first row / leave 2nd row unchanged / Modify the third row
It will then add one 'unchanged' row and one with rowMod = 'A'
   OperationID: ModifyAddDeleteRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifyAddDeleteRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifyAddDeleteRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ModifyAddDeleteRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/ModifyAddDeleteRows", {
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
   Summary: Invoke method ReturnMultipleUnModifiedRows
   Description: This will expect a row and change it but return two unmodified rows which are different and we need to ensure that the 'last' row is the one that is shown in the Harness
   OperationID: ReturnMultipleUnModifiedRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReturnMultipleUnModifiedRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnMultipleUnModifiedRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReturnMultipleUnModifiedRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/ReturnMultipleUnModifiedRows", {
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
   Summary: Invoke method GetDefaultEvents
   Description: Returns sample rows for epScheduler control in Misc harness
   OperationID: GetDefaultEvents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEvents_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultEvents(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetDefaultEvents", {
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
   Summary: Invoke method GetNewEvent
   Description: Get a new event for the ep-scheduler control
   OperationID: GetNewEvent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEvent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEvent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEvent(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetNewEvent", {
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
   Summary: Invoke method GetSampleDataTreeStructure
   Description: GetSampleDataTreeStructure
   OperationID: GetSampleDataTreeStructure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSampleDataTreeStructure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSampleDataTreeStructure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSampleDataTreeStructure(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetSampleDataTreeStructure", {
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
   Summary: Invoke method GetSomeDatasetsOneType
   Description: Returns two datasets with the same type.
   OperationID: GetSomeDatasetsOneType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSomeDatasetsOneType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSomeDatasetsOneType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSomeDatasetsOneType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/GetSomeDatasetsOneType", {
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
   Summary: Invoke method NullStringTestNonEmptyResult
   Description: Returns non-empty string
   OperationID: NullStringTestNonEmptyResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NullStringTestNonEmptyResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NullStringTestNonEmptyResult(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/NullStringTestNonEmptyResult", {
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
   Summary: Invoke method NullStringTestNullResult
   Description: Returns null result
   OperationID: NullStringTestNullResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NullStringTestNullResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NullStringTestNullResult(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MetaUIHarnessSvc/NullStringTestNullResult", {
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



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ds
   */  
export interface DeleteRows_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface DeleteRows_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

export interface Erp_Tablesets_DynFieldAttributesRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   DataType:string,
   Required:boolean,
   ReadOnly:boolean,
   FieldFormat:string,
   FieldLabel:string,
   LikeDataFieldSystemCode:string,
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
   CurrencyCodeColumn:string,
   CurrencyType:string,
   CurrencySource:string,
   BizType:string,
   CGCCode:string,
   UomColumn:string,
   CodeDescriptionList:string,
   Seq:number,
   IsHidden:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynFieldHelpRow{
   SystemCode:string,
   DataTableID:string,
   FieldName:string,
   Description:string,
   DBTableName:string,
   DBFieldName:string,
   External:boolean,
   InitialValue:string,
   IsDescriptionField:boolean,
   SystemFlag:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynTableAttributesRow{
   SystemCode:string,
      /**  The actual generic table name used by the BL  */  
   DataTableID:string,
      /**  Unique identifier for the virtual schema  */  
   UniqueTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DynamicMetadataTableset{
   DynTableAttributes:Erp_Tablesets_DynTableAttributesRow[],
   DynFieldAttributes:Erp_Tablesets_DynFieldAttributesRow[],
   DynFieldHelp:Erp_Tablesets_DynFieldHelpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MetaUIHarnessListTableset{
   ParentList:Erp_Tablesets_ParentListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MetaUIHarnessTableset{
   Parent:Erp_Tablesets_ParentRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ParentListRow{
   ID:string,
   FirstName:string,
   LastName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ParentRow{
   ID:string,
   FirstName:string,
   LastName:string,
   Approved:boolean,
   Photo:string,
   DOB:string,
   LastUpdated:string,
   Amount:number,
   IntNum:number,
   GenAmount:number,
   DocGenAmount:number,
   Rpt1GenAmount:number,
   Rpt2GenAmount:number,
   Rtp3GenAmount:number,
   CostAmount:number,
   DocCostAmount:number,
   Rpt1CostAmount:number,
   Rpt2CostAmount:number,
   Rpt3CostAmount:number,
   PriceAmount:number,
   DocPriceAmount:number,
   CurrentyCode:string,
   UOM1:string,
   UOM2:string,
   Quantity1:number,
   Quantity2:number,
   EmailAddress:string,
   EventStart:string,
   EventEnd:string,
   EventTitle:string,
   EventDescription:string,
   EventIsAllDay:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface GetDefaultEvents_output{
   returnObj:Erp_Tablesets_MetaUIHarnessTableset[],
}

   /** Required : 
      @param formatNum
   */  
export interface GetDynamicData_input{
   formatNum:number,
}

export interface GetDynamicData_output{
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DynamicMetadataTableset[],
}
}

   /** Required : 
      @param whereClause
      @param firstName
      @param onlyLastNamesThatStartWith
      @param seed
   */  
export interface GetListSpecial_input{
   whereClause:string,
   firstName:string,
   onlyLastNamesThatStartWith:string,
   seed:number,
}

export interface GetListSpecial_output{
   returnObj:Erp_Tablesets_MetaUIHarnessListTableset[],
}

   /** Required : 
      @param startDateTime
      @param endDateTime
      @param ds
   */  
export interface GetNewEvent_input{
      /**  Event start time  */  
   startDateTime:string,
      /**  Event end time  */  
   endDateTime:string,
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface GetNewEvent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param treeSelection
   */  
export interface GetSampleDataTreeStructure_input{
      /**  The string identifier that corresponds to the tree you want  */  
   treeSelection:string,
}

export interface GetSampleDataTreeStructure_output{
      /**  The requested JSON as a string  */  
   returnObj:string,
}

   /** Required : 
      @param rowCount
      @param seed
      @param rowMod
      @param ds
   */  
export interface GetSampleRowsAddedNoSysRowID_input{
   rowCount:number,
   seed:number,
   rowMod:string,
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface GetSampleRowsAddedNoSysRowID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param rowCount
      @param seed
      @param rowMod
      @param ds
   */  
export interface GetSampleRowsAdded_input{
   rowCount:number,
   seed:number,
   rowMod:string,
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface GetSampleRowsAdded_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param rowCount
      @param seed
      @param rowMod
   */  
export interface GetSampleRows_input{
   rowCount:number,
   seed:number,
   rowMod:string,
}

export interface GetSampleRows_output{
   returnObj:Erp_Tablesets_MetaUIHarnessTableset[],
}

   /** Required : 
      @param firstDSParam
      @param ds
   */  
export interface GetSomeDatasetsOneType_input{
   firstDSParam:Erp_Tablesets_MetaUIHarnessTableset[],
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface GetSomeDatasetsOneType_output{
parameters : {
      /**  output parameters  */  
   firstDSParam:Erp_Tablesets_MetaUIHarnessTableset[],
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
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
      @param ds
   */  
export interface ModifyAddDeleteRows_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface ModifyAddDeleteRows_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ModifyRowsReturnUnChanged_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface ModifyRowsReturnUnChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ModifyRows_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface ModifyRows_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

export interface NullStringTestNonEmptyResult_output{
   returnObj:string,
}

export interface NullStringTestNullResult_output{
   returnObj:string,
}

   /** Required : 
      @param id
      @param proposedQuantity1
      @param ds
   */  
export interface OnChangeQuantity1_input{
   id:string,
   proposedQuantity1:number,
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface OnChangeQuantity1_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface ReturnMultipleUnModifiedRows_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface ReturnMultipleUnModifiedRows_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateSpecial_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface UpdateSpecial_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MetaUIHarnessTableset[],
}
}

