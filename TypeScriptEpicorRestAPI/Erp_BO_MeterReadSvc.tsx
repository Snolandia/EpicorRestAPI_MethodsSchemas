import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MeterReadSvc
// Description: Created for Equipment Meter Reading Entry
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/$metadata", {
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
   Summary: Calls GetRows for the service
   Description: Get MeterReads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MeterReads
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MeterReadRow
   */  
export function get_MeterReads(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MeterReads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MeterReads(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads", {
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
   Summary: Calls GetByID to retrieve the MeterRead item
   Description: Calls GetByID to retrieve the MeterRead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MeterRead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   */  
export function get_MeterReads_Company_EquipID(Company:string, EquipID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MeterReadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MeterReadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MeterRead for the service
   Description: Calls UpdateExt to update MeterRead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MeterRead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MeterReadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MeterReads_Company_EquipID(Company:string, EquipID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")", {
          method: 'patch',
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
   Summary: Call UpdateExt to delete MeterRead item
   Description: Call UpdateExt to delete MeterRead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MeterRead
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EquipID Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MeterReads_Company_EquipID(Company:string, EquipID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/MeterReads(" + Company + "," + EquipID + ")", {
          method: 'delete',
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
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MeterReadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMeterRead:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMeterRead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMeterRead=" + whereClauseMeterRead
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetRows" + params, {
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
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(equipID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof equipID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "equipID=" + equipID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetByID" + params, {
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
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      @param whereClause Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      @param pageSize Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      @param absolutePage Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClause!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClause=" + whereClause
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetList" + params, {
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
   Summary: Invoke method GetNewMeterRead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMeterRead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMeterRead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMeterRead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMeterRead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetNewMeterRead", {
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
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/DeleteByID", {
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
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowID(id:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof id!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "id=" + id
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetBySysRowID" + params, {
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
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetBySysRowIDs(ids:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof ids!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "ids=" + ids
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/GetBySysRowIDs" + params, {
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
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/Update", {
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
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MeterReadSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MeterReadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MeterReadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MeterReadRow[],
}

export interface Erp_Tablesets_MeterReadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   "EquipID":string,
      /**  Site in which the equipment is currently located.  */  
   "Plant":string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   "InActive":boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   "Description":string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   "StatusID":string,
      /**  OEM Number  */  
   "OEM":string,
      /**  Serial Number of equipment  */  
   "SerialNum":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  Model Number  */  
   "Model":string,
      /**  Date that equipment was first put into service. Required field.  */  
   "InServiceDate":string,
      /**  Warrenty Expiration Date  */  
   "WarrantyExpDate":string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   "TypeID":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "SellingVendorNum":number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "SellingPurPoint":string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "ServiceVendorNum":number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "ServicePurPoint":string,
      /**  Foreign Component key to the FAsset table.  */  
   "AssetNum":string,
      /**  Comments about the Equipment.  */  
   "Comments":string,
      /**  Allows entry of freeform equipment specifications.  */  
   "Specs":string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   "MeterUOM":string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   "CurrentMeter":number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   "ReadingComment":string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   "LocID":string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   "ParentEquipID":string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   "LaborMeterOpt":string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   "ReadingDate":string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   "ReadingTime":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   "ProjectID":string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   "UOMClassID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
   "AvgDailyUsage":number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   "GlobalEquip":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  */  
   "NewMeter":number,
      /**  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  */  
   "NewReadingComment":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MeterReadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   "EquipID":string,
      /**  Site in which the equipment is currently located.  */  
   "Plant":string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   "InActive":boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   "Description":string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   "StatusID":string,
      /**  OEM Number  */  
   "OEM":string,
      /**  Serial Number of equipment  */  
   "SerialNum":string,
      /**  Brand of equipment  */  
   "Brand":string,
      /**  Model Number  */  
   "Model":string,
      /**  Date that equipment was first put into service. Required field.  */  
   "InServiceDate":string,
      /**  Warrenty Expiration Date  */  
   "WarrantyExpDate":string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   "TypeID":string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   "ResourceGrpID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   "ResourceID":string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "SellingVendorNum":number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "SellingPurPoint":string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   "ServiceVendorNum":number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   "ServicePurPoint":string,
      /**  Foreign Component key to the FAsset table.  */  
   "AssetNum":string,
      /**  Comments about the Equipment.  */  
   "Comments":string,
      /**  Allows entry of freeform equipment specifications.  */  
   "Specs":string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   "MeterUOM":string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   "CurrentMeter":number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   "ReadingComment":string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   "LocID":string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   "ParentEquipID":string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   "LaborMeterOpt":string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   "ReadingDate":string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   "ReadingTime":number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   "InspPlanPartNum":string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   "SpecID":string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   "LastCalDate":string,
      /**  The inspection plan revision number (configurator revision number).  */  
   "InspPlanRevNum":string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   "SpecRevNum":string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   "ProjectID":string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   "UOMClassID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   "Lineage":string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
   "AvgDailyUsage":number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   "GlobalEquip":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  */  
   "NewMeter":number,
      /**  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  */  
   "NewReadingComment":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param equipID
   */  
export interface DeleteByID_input{
   equipID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MeterReadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   EquipID:string,
      /**  Site in which the equipment is currently located.  */  
   Plant:string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   InActive:boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   Description:string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   StatusID:string,
      /**  OEM Number  */  
   OEM:string,
      /**  Serial Number of equipment  */  
   SerialNum:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  Model Number  */  
   Model:string,
      /**  Date that equipment was first put into service. Required field.  */  
   InServiceDate:string,
      /**  Warrenty Expiration Date  */  
   WarrantyExpDate:string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   TypeID:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   SellingVendorNum:number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   SellingPurPoint:string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   ServiceVendorNum:number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   ServicePurPoint:string,
      /**  Foreign Component key to the FAsset table.  */  
   AssetNum:string,
      /**  Comments about the Equipment.  */  
   Comments:string,
      /**  Allows entry of freeform equipment specifications.  */  
   Specs:string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   MeterUOM:string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   CurrentMeter:number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   ReadingComment:string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   LocID:string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   ParentEquipID:string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   LaborMeterOpt:string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   ReadingDate:string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   ReadingTime:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   ProjectID:string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   UOMClassID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
   AvgDailyUsage:number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   GlobalEquip:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  */  
   NewMeter:number,
      /**  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  */  
   NewReadingComment:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MeterReadListTableset{
   MeterReadList:Erp_Tablesets_MeterReadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MeterReadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  */  
   EquipID:string,
      /**  Site in which the equipment is currently located.  */  
   Plant:string,
      /**  Flag which indicates if Equipment is considered as "Inactive".  */  
   InActive:boolean,
      /**  Full description of Equipment. Cannot be blank.  */  
   Description:string,
      /**  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  */  
   StatusID:string,
      /**  OEM Number  */  
   OEM:string,
      /**  Serial Number of equipment  */  
   SerialNum:string,
      /**  Brand of equipment  */  
   Brand:string,
      /**  Model Number  */  
   Model:string,
      /**  Date that equipment was first put into service. Required field.  */  
   InServiceDate:string,
      /**  Warrenty Expiration Date  */  
   WarrantyExpDate:string,
      /**  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  */  
   TypeID:string,
      /**  A code that identifies the Resource Group that the resource belongs to.  */  
   ResourceGrpID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Resource.  */  
   ResourceID:string,
      /**  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   SellingVendorNum:number,
      /**  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   SellingPurPoint:string,
      /**  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  */  
   ServiceVendorNum:number,
      /**  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  */  
   ServicePurPoint:string,
      /**  Foreign Component key to the FAsset table.  */  
   AssetNum:string,
      /**  Comments about the Equipment.  */  
   Comments:string,
      /**  Allows entry of freeform equipment specifications.  */  
   Specs:string,
      /**  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  */  
   MeterUOM:string,
      /**  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  */  
   CurrentMeter:number,
      /**  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  */  
   ReadingComment:string,
      /**  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  */  
   LocID:string,
      /**  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  */  
   ParentEquipID:string,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   LaborMeterOpt:string,
      /**  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  */  
   ReadingDate:string,
      /**  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  */  
   ReadingTime:number,
      /**  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  */  
   InspPlanPartNum:string,
      /**  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  */  
   SpecID:string,
      /**  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  */  
   LastCalDate:string,
      /**  The inspection plan revision number (configurator revision number).  */  
   InspPlanRevNum:string,
      /**  The specification revision number.  Must be valid in the SpecRev table.  */  
   SpecRevNum:string,
      /**  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  */  
   ProjectID:string,
      /**   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  */  
   UOMClassID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  */  
   Lineage:string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
   AvgDailyUsage:number,
      /**  Marks this Equip as global, available to be sent out to other companies.  */  
   GlobalEquip:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  External field used to enter a NEW meter reading valule.  When saved, it will update Equip.CurrentMeter, and them be set to zero for the next transaction.  */  
   NewMeter:number,
      /**  Used to enter a comment related to the NEW meter reading.  When saved, this value updates current reading comment (Equip.ReadingComment) and is then blanked out.  */  
   NewReadingComment:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MeterReadTableset{
   MeterRead:Erp_Tablesets_MeterReadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMeterReadTableset{
   MeterRead:Erp_Tablesets_MeterReadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param equipID
   */  
export interface GetByID_input{
   equipID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MeterReadTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MeterReadTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MeterReadTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
      /**  An expression used to filter the rows. Can be left blank for all rows.  */  
   whereClause:string,
      /**  The maximum number of rows to return. Leave as zero for no maximum.  */  
   pageSize:number,
      /**  Page of rows to return.  */  
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_MeterReadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMeterRead_input{
   ds:Erp_Tablesets_MeterReadTableset[],
}

export interface GetNewMeterRead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MeterReadTableset[],
}
}

   /** Required : 
      @param whereClauseMeterRead
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMeterRead:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MeterReadTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BOUpdErrorRow{
   TableName:string,
   ErrorLevel:string,
   ErrorType:string,
   ErrorText:string,
   ErrorSysRowID:string,
   SysRowID:string,
   RowMod:string,
}

export interface Ice_BOUpdErrorTableset{
   BOUpdError:Ice_BOUpdErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMeterReadTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMeterReadTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MeterReadTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MeterReadTableset[],
}
}

