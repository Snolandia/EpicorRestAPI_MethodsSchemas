import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.AttachmentSvc
// Description: Class for handling of attachments.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/$metadata", {
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
   Description: Get Attachments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Attachments
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XFileAttchRow
   */  
export function get_Attachments(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Attachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Attachments(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments", {
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
   Summary: Calls GetByID to retrieve the Attachment item
   Description: Calls GetByID to retrieve the Attachment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Attachment
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param AttachNum Desc: AttachNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   */  
export function get_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName:string, RelatedToFile:string, ForeignSysRowID:string, AttachNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_XFileAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_XFileAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Attachment for the service
   Description: Calls UpdateExt to update Attachment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Attachment
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param AttachNum Desc: AttachNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.XFileAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName:string, RelatedToFile:string, ForeignSysRowID:string, AttachNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")", {
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
   Summary: Call UpdateExt to delete Attachment item
   Description: Call UpdateExt to delete Attachment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Attachment
      @param RelatedToSchemaName Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param ForeignSysRowID Desc: ForeignSysRowID   Required: True   Allow empty value : True
      @param AttachNum Desc: AttachNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Attachments_RelatedToSchemaName_RelatedToFile_ForeignSysRowID_AttachNum(RelatedToSchemaName:string, RelatedToFile:string, ForeignSysRowID:string, AttachNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Attachments(" + RelatedToSchemaName + "," + RelatedToFile + "," + ForeignSysRowID + "," + AttachNum + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get AttachmentCredentials items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AttachmentCredentials
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AttachmentCredentialsRow
   */  
export function get_AttachmentCredentials(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AttachmentCredentialsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AttachmentCredentialsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AttachmentCredentials
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AttachmentCredentials(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials", {
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
   Summary: Calls GetByID to retrieve the AttachmentCredential item
   Description: Calls GetByID to retrieve the AttachmentCredential item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AttachmentCredential
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   */  
export function get_AttachmentCredentials_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_AttachmentCredentialsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_AttachmentCredentialsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AttachmentCredential for the service
   Description: Calls UpdateExt to update AttachmentCredential. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AttachmentCredential
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AttachmentCredentialsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AttachmentCredentials_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete AttachmentCredential item
   Description: Call UpdateExt to delete AttachmentCredential item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AttachmentCredential
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AttachmentCredentials_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/AttachmentCredentials(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XFileAttchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseXFileAttch:string, whereClauseAttachmentCredentials:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseXFileAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseXFileAttch=" + whereClauseXFileAttch
   }
   if(typeof whereClauseAttachmentCredentials!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAttachmentCredentials=" + whereClauseAttachmentCredentials
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(relatedToSchemaName:string, relatedToFile:string, foreignSysRowID:string, attachNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof relatedToSchemaName!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "relatedToSchemaName=" + relatedToSchemaName
   }
   if(typeof relatedToFile!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "relatedToFile=" + relatedToFile
   }
   if(typeof foreignSysRowID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "foreignSysRowID=" + foreignSysRowID
   }
   if(typeof attachNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "attachNum=" + attachNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetList" + params, {
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
   Summary: Invoke method GetPathReferences
   Description: Returns a list of rows that reference the same path.
   OperationID: GetPathReferences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPathReferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPathReferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPathReferences(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetPathReferences", {
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
   Summary: Invoke method OnChangeOfFileName
   Description: Call when FileName is changed.
The purpose of this method is to find out if a given FileName is already
known in the database. That is, does a XFileRef record exist.
Client program should pass the current values from the dataset for the given parameters.
The returned parameter values should unconditionally moved to the corresponding fields in the dataset.
   OperationID: OnChangeOfFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfFileName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/OnChangeOfFileName", {
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
   Summary: Invoke method OnChangeOfDocType
   Description: Call when DocTypeID is changed.
Will reset the path portion of the file name with the BaseURL of the DocType.
Note: It will not overlay a fully qualified filename.
   OperationID: OnChangeOfDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/OnChangeOfDocType", {
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
   Summary: Invoke method ServerDirectoryExists
   Description: Determines whether the given path refers to an existing directory on the server.
   OperationID: ServerDirectoryExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ServerDirectoryExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ServerDirectoryExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ServerDirectoryExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/ServerDirectoryExists", {
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
   Summary: Invoke method DownloadFile
   Description: Get a file's content from the server
   OperationID: DownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DownloadFile", {
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
   Summary: Invoke method UploadFile
   Description: Set a file's content on the server
   OperationID: UploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/UploadFile", {
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
   Summary: Invoke method FileExists
   Description: Check if file exists on the server
   OperationID: FileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/FileExists", {
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
   Summary: Invoke method DeleteFile
   Description: Deletes the specified file.
   OperationID: DeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DeleteFile", {
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
   Summary: Invoke method DetermineTransferModeByStorageType
   Description: Determines whether the storage type for the given doctype uses client or service
document transfer.  If no storage type is specified then will return the company default
storage type transfer mode if a company default is specified. Returns the literal 'NONE' if
no storage type found.
   OperationID: DetermineTransferModeByStorageType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DetermineTransferModeByStorageType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DetermineTransferModeByStorageType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DetermineTransferModeByStorageType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DetermineTransferModeByStorageType", {
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
   Summary: Invoke method UploadFileToDocTypeStorage
   Description: Upload file to the storage defined by document type (or default company storage)
   OperationID: UploadFileToDocTypeStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadFileToDocTypeStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadFileToDocTypeStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadFileToDocTypeStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/UploadFileToDocTypeStorage", {
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
   Summary: Invoke method UploadNonERPFileToDocTypeStorage
   Description: Upload a NON ERP file to the storage defined by document type (or default company storage)
   OperationID: UploadNonERPFileToDocTypeStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadNonERPFileToDocTypeStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadNonERPFileToDocTypeStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UploadNonERPFileToDocTypeStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/UploadNonERPFileToDocTypeStorage", {
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
   Summary: Invoke method DownloadFileFromDocumentStorage
   OperationID: DownloadFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadFileFromDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DownloadFileFromDocumentStorage", {
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
   Summary: Invoke method DownloadNonERPFileFromDocumentStorage
   OperationID: DownloadNonERPFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadNonERPFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadNonERPFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DownloadNonERPFileFromDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DownloadNonERPFileFromDocumentStorage", {
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
   Summary: Invoke method DeleteFileFromDocumentStorage
   Description: Delete a file from its associated storage system.
   OperationID: DeleteFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteFileFromDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DeleteFileFromDocumentStorage", {
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
   Summary: Invoke method DeleteNonERPFileFromDocumentStorage
   Description: Delete a file from its associated storage system.
   OperationID: DeleteNonERPFileFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteNonERPFileFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteNonERPFileFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteNonERPFileFromDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DeleteNonERPFileFromDocumentStorage", {
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
   Summary: Invoke method GetFileMetaDataFromDocumentStorage
   OperationID: GetFileMetaDataFromDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFileMetaDataFromDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFileMetaDataFromDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFileMetaDataFromDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetFileMetaDataFromDocumentStorage", {
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
   Summary: Invoke method UpdateMetadataOnDocumentStorage
   Description: Updates the files metadata on the storage system.
   OperationID: UpdateMetadataOnDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateMetadataOnDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateMetadataOnDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateMetadataOnDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/UpdateMetadataOnDocumentStorage", {
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
   Summary: Invoke method FileExistsOnDocumentStorage
   Description: Determines if the document already exists in storage.
   OperationID: FileExistsOnDocumentStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FileExistsOnDocumentStorage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FileExistsOnDocumentStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FileExistsOnDocumentStorage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/FileExistsOnDocumentStorage", {
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
   Summary: Invoke method GetCredentialsForServer
   Description: Get external attachment system credentials (username, domain and authentication type) for this company or document type.
   OperationID: GetCredentialsForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCredentialsForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCredentialsForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCredentialsForServer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetCredentialsForServer", {
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
   Summary: Invoke method GetAccountForServer
   Description: Get external attachment system account user name for this company or doc type.
   OperationID: GetAccountForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccountForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccountForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAccountForServer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetAccountForServer", {
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
   Summary: Invoke method SetAccountForServer
   Description: Set external attachment system account info for the company or doc type. Security Manager access right is requried.
   OperationID: SetAccountForServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAccountForServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAccountForServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAccountForServer(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SetAccountForServer", {
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
   Summary: Invoke method GetAccountForUser
   Description: Get external attachment system account info for this company or doc type for logged in user
   OperationID: GetAccountForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccountForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccountForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAccountForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetAccountForUser", {
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
   Summary: Invoke method SetAccountForUser
   Description: Set SP account info for the company or doc type for loggedin user
   OperationID: SetAccountForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAccountForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAccountForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetAccountForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SetAccountForUser", {
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
   Summary: Invoke method ClearAccountsForUser
   Description: Clear stored external attachment system user accounts for current company and any document type
   OperationID: ClearAccountsForUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAccountsForUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAccountsForUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearAccountsForUser(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/ClearAccountsForUser", {
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
   Summary: Invoke method GetNewXFileAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXFileAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXFileAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXFileAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewXFileAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetNewXFileAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/UpdateExt", {
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
   Summary: Invoke method DocStarTestConnection
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarTestConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarTestConnection", {
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
   Summary: Invoke method DocStarTestConnectionCompany
   Description: Test connection to DocStar system.
   OperationID: DocStarTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarTestConnectionCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarTestConnectionCompany", {
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
   Summary: Invoke method DocStarCreateCompanyFolder
   Description: Create folder for company in the DocStar system
   OperationID: DocStarCreateCompanyFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateCompanyFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateCompanyFolder(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarCreateCompanyFolder", {
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
   Summary: Invoke method DocStarCreateDocumentTypeFolder
   Description: Create folder for document type in the DocStar system
   OperationID: DocStarCreateDocumentTypeFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateDocumentTypeFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateDocumentTypeFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateDocumentTypeFolder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarCreateDocumentTypeFolder", {
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
   Summary: Invoke method DocStarCreateDocumentFolder
   Description: Create folder for table inside document type folder in the DocStar system
   OperationID: DocStarCreateDocumentFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateDocumentFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateDocumentFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateDocumentFolder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarCreateDocumentFolder", {
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
   Summary: Invoke method DocStarCreateCustomFields
   Description: Create custom fields in DocStar system
   OperationID: DocStarCreateCustomFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateCustomFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateCustomFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateCustomFields(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarCreateCustomFields", {
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
   Summary: Invoke method DocStarUploadFile
   Description: Upload file to DocStar system and store metadata
   OperationID: DocStarUploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarUploadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarUploadFile", {
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
   Summary: Invoke method DocStarUploadFileAsVersion
   Description: Upload file to DocStar system and store metadata
   OperationID: DocStarUploadFileAsVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUploadFileAsVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUploadFileAsVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarUploadFileAsVersion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarUploadFileAsVersion", {
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
   Summary: Invoke method DocStarDownloadFile
   OperationID: DocStarDownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarDownloadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarDownloadFile", {
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
   Summary: Invoke method DocStarDownloadNonERPFile
   OperationID: DocStarDownloadNonERPFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDownloadNonERPFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDownloadNonERPFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarDownloadNonERPFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarDownloadNonERPFile", {
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
   Summary: Invoke method DocStarUpdateMetadata
   Description: Update metadata for the file
   OperationID: DocStarUpdateMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarUpdateMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarUpdateMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarUpdateMetadata(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarUpdateMetadata", {
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
   Summary: Invoke method DocStarGetMetadata
   OperationID: DocStarGetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarGetMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarGetMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarGetMetadata(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarGetMetadata", {
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
   Summary: Invoke method DocStarDeleteNonERPFile
   Description: Delete file to Recycle Bin
   OperationID: DocStarDeleteNonERPFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDeleteNonERPFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDeleteNonERPFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarDeleteNonERPFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarDeleteNonERPFile", {
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
   Summary: Invoke method DocStarDeleteFile
   Description: Delete file to Recycle Bin
   OperationID: DocStarDeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarDeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarDeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarDeleteFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarDeleteFile", {
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
   Summary: Invoke method DocStarFileExistsForTableRow
   Description: Check if docStar file with the same name already exists in the XFileRef attachment table for this Epicor table record
   OperationID: DocStarFileExistsForTableRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarFileExistsForTableRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarFileExistsForTableRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarFileExistsForTableRow(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarFileExistsForTableRow", {
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
   Summary: Invoke method DocStarCreateBrowserUrl
   Description: Builds a URL in DocStar which will be used to open the attachment within DocStar.
   OperationID: DocStarCreateBrowserUrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DocStarCreateBrowserUrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DocStarCreateBrowserUrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DocStarCreateBrowserUrl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DocStarCreateBrowserUrl", {
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
   Summary: Invoke method DropboxFileExists
   Description: Determines if the file exists on Dropbox using the given path.
   OperationID: DropboxFileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DropboxFileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DropboxFileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DropboxFileExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/DropboxFileExists", {
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
   Summary: Invoke method GoogleUpdateMetaData
   Description: Updates the file metadata.
   OperationID: GoogleUpdateMetaData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GoogleUpdateMetaData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GoogleUpdateMetaData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GoogleUpdateMetaData(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/GoogleUpdateMetaData", {
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
   Summary: Invoke method SpUploadFile
   Description: Upload file to Sharepoint and store metadata
   OperationID: SpUploadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpUploadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpUploadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpUploadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpUploadFile", {
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
   Summary: Invoke method SpDownloadFile
   Description: Download file and its metadata from SharePoint
   OperationID: SpDownloadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpDownloadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpDownloadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpDownloadFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpDownloadFile", {
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
   Summary: Invoke method SpGetMetadata
   OperationID: SpGetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpGetMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpGetMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpGetMetadata(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpGetMetadata", {
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
   Summary: Invoke method SpUpdateMetadata
   Description: Update metadata for Sharepoint file
   OperationID: SpUpdateMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpUpdateMetadata_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpUpdateMetadata_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpUpdateMetadata(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpUpdateMetadata", {
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
   Summary: Invoke method SpDeleteFile
   Description: Delete file from SharePoint
   OperationID: SpDeleteFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpDeleteFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpDeleteFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpDeleteFile(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpDeleteFile", {
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
   Summary: Invoke method SpFileExists
   Description: Check if file exists on the sharepoint site
   OperationID: SpFileExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpFileExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpFileExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpFileExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpFileExists", {
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
   Summary: Invoke method SpCreateDocumentLibrary
   Description: Create Sharepoint Document library.
   OperationID: SpCreateDocumentLibrary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateDocumentLibrary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateDocumentLibrary_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpCreateDocumentLibrary(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpCreateDocumentLibrary", {
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
   Summary: Invoke method SpCreateDocumentFolder
   Description: Create Sharepoint document folder for table.
   OperationID: SpCreateDocumentFolder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateDocumentFolder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateDocumentFolder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpCreateDocumentFolder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpCreateDocumentFolder", {
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
   Summary: Invoke method SpCreateContentType
   Description: Create Sharepoint Content type.
   OperationID: SpCreateContentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpCreateContentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpCreateContentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpCreateContentType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpCreateContentType", {
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
   Summary: Invoke method SpAddFieldToContentType
   Description: Add field to the Sharepoint content type. Security Manager access right is requried.
   OperationID: SpAddFieldToContentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpAddFieldToContentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpAddFieldToContentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpAddFieldToContentType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpAddFieldToContentType", {
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
   Summary: Invoke method SpTestConnection
   Description: Test connection to SharePoint
   OperationID: SpTestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpTestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpTestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpTestConnection(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpTestConnection", {
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
   Summary: Invoke method SpTestConnectionCompany
   Description: Test connection to SharePoint
   OperationID: SpTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpTestConnectionCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpTestConnectionCompany", {
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
   Summary: Invoke method SpOnlineTestConnectionCompany
   Description: Test connection to SharePoint Online.
   OperationID: SpOnlineTestConnectionCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SpOnlineTestConnectionCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SpOnlineTestConnectionCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SpOnlineTestConnectionCompany(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.AttachmentSvc/SpOnlineTestConnectionCompany", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AttachmentCredentialsRow{
   "odatametadata":string,
   "value":Ice_Tablesets_AttachmentCredentialsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_XFileAttchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XFileAttchRow{
   "odatametadata":string,
   "value":Ice_Tablesets_XFileAttchRow[],
}

export interface Ice_Tablesets_AttachmentCredentialsRow{
   "UserName":string,
   "Domain":string,
   "AuthType":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_XFileAttchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  */  
   "AttachNum":number,
      /**   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  */  
   "Key5":string,
      /**  Foreign Key to XFileRef record.  */  
   "XFileRefNum":number,
      /**  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  */  
   "DoTrigger":boolean,
      /**  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  */  
   "DupToRelatedToFile":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey1":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey2":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey3":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey4":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey5":string,
      /**  See DupToRelatedToFile  */  
   "DupToAttachNum":number,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   "SharePointID":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_XFileAttchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  RelatedToSchemaName  */  
   "RelatedToSchemaName":string,
      /**   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  */  
   "AttachNum":number,
      /**   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  */  
   "Key5":string,
      /**  Foreign Key to XFileRef record.  */  
   "XFileRefNum":number,
      /**  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  */  
   "DoTrigger":boolean,
      /**  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  */  
   "DupToRelatedToFile":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey1":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey2":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey3":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey4":string,
      /**  See DupToRelatedToFile  */  
   "DupToKey5":string,
      /**  See DupToRelatedToFile  */  
   "DupToAttachNum":number,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   "SharePointID":string,
      /**  ForeignSysRowID  */  
   "ForeignSysRowID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "XFileRefDocTypeID":string,
   "XFileRefPDMDocID":string,
   "XFileRefXFileName":string,
   "XFileRefXFileDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param storageType
   */  
export interface ClearAccountsForUser_input{
      /**  Storage type this account is created for  */  
   storageType:number,
}

export interface ClearAccountsForUser_output{
}

   /** Required : 
      @param relatedToSchemaName
      @param relatedToFile
      @param foreignSysRowID
      @param attachNum
   */  
export interface DeleteByID_input{
   relatedToSchemaName:string,
   relatedToFile:string,
   foreignSysRowID:string,
   attachNum:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param xFileRefNum
   */  
export interface DeleteFileFromDocumentStorage_input{
      /**  The xFileRef file ID associated with the document.  */  
   xFileRefNum:number,
}

export interface DeleteFileFromDocumentStorage_output{
}

   /** Required : 
      @param xFileRefNum
      @param makeBackup
   */  
export interface DeleteFile_input{
      /**  id of the attachment  */  
   xFileRefNum:number,
      /**  copy backup to 'deleted' directory  */  
   makeBackup:boolean,
}

export interface DeleteFile_output{
}

   /** Required : 
      @param xFileRefNum
      @param companyId
   */  
export interface DeleteNonERPFileFromDocumentStorage_input{
      /**  The xFileRef file ID associated with the document.  */  
   xFileRefNum:number,
   companyId:string,
}

export interface DeleteNonERPFileFromDocumentStorage_output{
}

   /** Required : 
      @param docTypeID
   */  
export interface DetermineTransferModeByStorageType_input{
   docTypeID:string,
}

export interface DetermineTransferModeByStorageType_output{
      /**  'S' for service transfer, 'C' for client transfer and 'NONE' if no storage type can be determined.  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param documentId
      @param userName
      @param userPwd
      @param domain
      @param authType
      @param saveLogin
   */  
export interface DocStarCreateBrowserUrl_input{
      /**  Document type for the attachment  */  
   docTypeID:string,
      /**  Document identifier  */  
   documentId:string,
      /**  User Identifier  */  
   userName:string,
      /**  Encrypted user password  */  
   userPwd:string,
      /**  Domain for Windows authentication  */  
   domain:string,
      /**  Authentication type  */  
   authType:string,
      /**  If true saves the user account information  */  
   saveLogin:boolean,
}

export interface DocStarCreateBrowserUrl_output{
      /**  Url for the attachment document within DocStar  */  
   returnObj:string,
}

export interface DocStarCreateCompanyFolder_output{
}

   /** Required : 
      @param docTypeID
      @param customFieldNames
   */  
export interface DocStarCreateCustomFields_input{
   docTypeID:string,
   customFieldNames:string,
}

export interface DocStarCreateCustomFields_output{
}

   /** Required : 
      @param docTypeID
      @param tableName
   */  
export interface DocStarCreateDocumentFolder_input{
      /**  Document type  */  
   docTypeID:string,
      /**  Table name  */  
   tableName:string,
}

export interface DocStarCreateDocumentFolder_output{
}

   /** Required : 
      @param docTypeID
   */  
export interface DocStarCreateDocumentTypeFolder_input{
      /**  Document type  */  
   docTypeID:string,
}

export interface DocStarCreateDocumentTypeFolder_output{
}

   /** Required : 
      @param xFileRefNum
   */  
export interface DocStarDeleteFile_input{
      /**  File ID from xFileRef table  */  
   xFileRefNum:number,
}

export interface DocStarDeleteFile_output{
}

   /** Required : 
      @param xFileRefNum
      @param companyId
   */  
export interface DocStarDeleteNonERPFile_input{
      /**  File ID from xFileRef table  */  
   xFileRefNum:number,
   companyId:string,
}

export interface DocStarDeleteNonERPFile_output{
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface DocStarDownloadFile_input{
   xFileRefNum:number,
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarDownloadFile_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param xFileRefNum
      @param companyId
      @param metadata
   */  
export interface DocStarDownloadNonERPFile_input{
   xFileRefNum:number,
   companyId:string,
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarDownloadNonERPFile_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
      @param foreignSysRowID
   */  
export interface DocStarFileExistsForTableRow_input{
      /**  document type or empty, if default  */  
   docTypeID:string,
      /**  table where attacment belongs  */  
   parentTable:string,
      /**  file name  */  
   fileName:string,
   foreignSysRowID:string,
}

export interface DocStarFileExistsForTableRow_output{
      /**  returns xFileRefNum or 0  */  
   returnObj:number,
parameters : {
      /**  output parameters  */  
   xFileName:string,
   AttachNum:number,
}
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface DocStarGetMetadata_input{
   xFileRefNum:number,
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarGetMetadata_output{
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param docTypeID
      @param userName
      @param userPwd
      @param domain
      @param authType
      @param hostName
   */  
export interface DocStarTestConnectionCompany_input{
      /**  Document type ID, or empty string to test company access  */  
   docTypeID:string,
      /**  suggested username  */  
   userName:string,
      /**  suggested password  */  
   userPwd:string,
      /**  domain for Windows authentication  */  
   domain:string,
      /**  Authentication type - NTLM or USERNAME  */  
   authType:string,
      /**  Host Name  */  
   hostName:string,
}

export interface DocStarTestConnectionCompany_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param userName
      @param userPwd
      @param domain
      @param authType
   */  
export interface DocStarTestConnection_input{
      /**  Document type ID, or empty string to test company access  */  
   docTypeID:string,
      /**  suggested username  */  
   userName:string,
      /**  suggested password  */  
   userPwd:string,
      /**  domain for Windows authentication  */  
   domain:string,
      /**  Authentication type - NTLM or USERNAME  */  
   authType:string,
}

export interface DocStarTestConnection_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown  */  
   returnObj:string,
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface DocStarUpdateMetadata_input{
      /**  File ID from xFileRef table  */  
   xFileRefNum:number,
      /**  metadata to update  */  
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarUpdateMetadata_output{
}

   /** Required : 
      @param xFileRefNum
      @param fileName
      @param data
      @param docTypeID
      @param parentTable
      @param metadata
   */  
export interface DocStarUploadFileAsVersion_input{
   xFileRefNum:number,
      /**  file name without path  */  
   fileName:string,
      /**  file binary data  */  
   data:string,
      /**  Document type for the attachment  */  
   docTypeID:string,
      /**  Table where file is attached  */  
   parentTable:string,
      /**  Metadata values to store with file  */  
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarUploadFileAsVersion_output{
   returnObj:string,
}

   /** Required : 
      @param fileName
      @param data
      @param docTypeID
      @param parentTable
      @param metadata
   */  
export interface DocStarUploadFile_input{
      /**  file name without path  */  
   fileName:string,
      /**  file binary data  */  
   data:string,
      /**  Document type for the attachment  */  
   docTypeID:string,
      /**  Table where file is attached  */  
   parentTable:string,
      /**  Metadata values to store with file  */  
   metadata:any,      //schema had no properties on an object.
}

export interface DocStarUploadFile_output{
   returnObj:string,
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface DownloadFileFromDocumentStorage_input{
   xFileRefNum:number,
   metadata:any,      //schema had no properties on an object.
}

export interface DownloadFileFromDocumentStorage_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param xFileRefNum
   */  
export interface DownloadFile_input{
      /**  id of the attachment  */  
   xFileRefNum:number,
}

export interface DownloadFile_output{
      /**  File data  */  
   returnObj:string,
}

   /** Required : 
      @param xFileRefNum
      @param companyId
      @param metadata
   */  
export interface DownloadNonERPFileFromDocumentStorage_input{
   xFileRefNum:number,
   companyId:string,
   metadata:any,      //schema had no properties on an object.
}

export interface DownloadNonERPFileFromDocumentStorage_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param dropboxFilePath
   */  
export interface DropboxFileExists_input{
      /**  The dropbox file path.  */  
   dropboxFilePath:string,
}

export interface DropboxFileExists_output{
      /**  True if the file exists, otherwise false.  */  
   returnObj:boolean,
}

   /** Required : 
      @param xFileRefNum
   */  
export interface FileExistsOnDocumentStorage_input{
      /**  The xFileRef file ID associated with the document.  */  
   xFileRefNum:number,
}

export interface FileExistsOnDocumentStorage_output{
   returnObj:boolean,
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
   */  
export interface FileExists_input{
      /**  document type or empty, if default  */  
   docTypeID:string,
      /**  table where attacment belongs  */  
   parentTable:string,
      /**  Path to the file on the server  */  
   fileName:string,
}

export interface FileExists_output{
      /**  True if exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param docTypeID
      @param storageType
   */  
export interface GetAccountForServer_input{
      /**  Document type ID, or empty string for company level.  */  
   docTypeID:string,
      /**  Storage type this accound is created for.  */  
   storageType:number,
}

export interface GetAccountForServer_output{
      /**  User name used on server side.  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   authType:string,
}
}

   /** Required : 
      @param docTypeID
      @param storageType
   */  
export interface GetAccountForUser_input{
      /**  Document type ID, or empty string for company level  */  
   docTypeID:string,
      /**  Storage type this accound is created for  */  
   storageType:number,
}

export interface GetAccountForUser_output{
      /**  true if record is found  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   spUserName:string,
   spUserPwd:string,
   spDomain:string,
   authType:string,
}
}

   /** Required : 
      @param relatedToSchemaName
      @param relatedToFile
      @param foreignSysRowID
      @param attachNum
   */  
export interface GetByID_input{
   relatedToSchemaName:string,
   relatedToFile:string,
   foreignSysRowID:string,
   attachNum:number,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_AttachmentTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_AttachmentTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_AttachmentTableset[],
}

   /** Required : 
      @param docTypeID
      @param storageType
   */  
export interface GetCredentialsForServer_input{
      /**  Document type ID, or empty string for company level.  */  
   docTypeID:string,
      /**  Storage type this accound is created for.  */  
   storageType:number,
}

export interface GetCredentialsForServer_output{
      /**  Credentials used on server side.  */  
   returnObj:Ice_Tablesets_AttachmentCredentialsRow[],
}

   /** Required : 
      @param xFileRefNum
      @param metaData
   */  
export interface GetFileMetaDataFromDocumentStorage_input{
   xFileRefNum:number,
   metaData:any,      //schema had no properties on an object.
}

export interface GetFileMetaDataFromDocumentStorage_output{
parameters : {
      /**  output parameters  */  
   metaData: UNKNOW TYPE(error 2338),
}
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
   returnObj:Ice_Tablesets_XFileAttchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToSchemaName
      @param relatedToFile
      @param foreignSysRowID
   */  
export interface GetNewXFileAttch_input{
   ds:Ice_Tablesets_AttachmentTableset[],
   relatedToSchemaName:string,
   relatedToFile:string,
   foreignSysRowID:string,
}

export interface GetNewXFileAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AttachmentTableset[],
}
}

   /** Required : 
      @param path
   */  
export interface GetPathReferences_input{
      /**  The path to match.  */  
   path:string,
}

export interface GetPathReferences_output{
   returnObj:Ice_Tablesets_XFileAttchListTableset[],
}

   /** Required : 
      @param whereClauseXFileAttch
      @param whereClauseAttachmentCredentials
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseXFileAttch:string,
   whereClauseAttachmentCredentials:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_AttachmentTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param xFileRefNum
      @param metadata
      @param addProps
   */  
export interface GoogleUpdateMetaData_input{
      /**  The xFileRef file ID associated with the document.  */  
   xFileRefNum:number,
      /**  Dictionary containing the file metadata to update.  */  
   metadata:any,      //schema had no properties on an object.
      /**  Indicates whether or not to add custom properties.  */  
   addProps:boolean,
}

export interface GoogleUpdateMetaData_output{
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

export interface Ice_Tablesets_AttachmentCredentialsRow{
   UserName:string,
   Domain:string,
   AuthType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_AttachmentTableset{
   XFileAttch:Ice_Tablesets_XFileAttchRow[],
   AttachmentCredentials:Ice_Tablesets_AttachmentCredentialsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtAttachmentTableset{
   XFileAttch:Ice_Tablesets_XFileAttchRow[],
   AttachmentCredentials:Ice_Tablesets_AttachmentCredentialsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_XFileAttchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  */  
   Key4:string,
      /**   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  */  
   AttachNum:number,
      /**   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  */  
   Key5:string,
      /**  Foreign Key to XFileRef record.  */  
   XFileRefNum:number,
      /**  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  */  
   DoTrigger:boolean,
      /**  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  */  
   DupToRelatedToFile:string,
      /**  See DupToRelatedToFile  */  
   DupToKey1:string,
      /**  See DupToRelatedToFile  */  
   DupToKey2:string,
      /**  See DupToRelatedToFile  */  
   DupToKey3:string,
      /**  See DupToRelatedToFile  */  
   DupToKey4:string,
      /**  See DupToRelatedToFile  */  
   DupToKey5:string,
      /**  See DupToRelatedToFile  */  
   DupToAttachNum:number,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   SharePointID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_XFileAttchListTableset{
   XFileAttchList:Ice_Tablesets_XFileAttchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_XFileAttchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  RelatedToSchemaName  */  
   RelatedToSchemaName:string,
      /**   Identifies the master file to which the drawing related to.  This field is used to properly  isolate drawings to the masters they are related to.
For example; Part, QuoteAsm, JobAsmbl identifies drawings that are related to Parts, Quote Assemblies and Job Assemblies.  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  drawing this field would contain the related Part Number,  for a "QuoteAsm"  it contains the QuoteAsm.QuoteNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
For example: For a "QuoteAsm"  drawing this field would contain the QuoteAsm.LineNum of the related QuoteAsm record.  The usage of this field is dependent on the type of record.  For example "Part" drawings do not use this field while JobAsmbl drawings would.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
For example: For a "QuoteAsm" drawing this field would contain the QuoteAsm.AssemblySeq # of the related QuoteAsm record.  The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
For example: For a "QuoteOpr" drawing this field would contain the QuoteOpr.OprSeq # of the related QuoteOpr record.  The usage of this field is dependent record type.  */  
   Key4:string,
      /**   An integer which uniquely identifies a attachment to the related master document.  Ex: If a specific job assembly has two attachements then the DrawingSeq = 1 and 2 respectively. This value is assigned by the system.
Note: Prior to 8.03 this field was named DrawingSeq.  */  
   AttachNum:number,
      /**   5th component of the foreign key to the related master record.
For example: For a "ECORev" drawing this field would contain the ECORev.AltMethod of the related ECORev record.  The usage of this field is dependent record type.  */  
   Key5:string,
      /**  Foreign Key to XFileRef record.  */  
   XFileRefNum:number,
      /**  A flag used to force a write trigger event even though none of the other fields are changing. FYI: Originally created to handle the automatic duplication of RcvDtl attachments to the PartLot. If Part or LotNum is changed in RcvDtl or the DocType is changed the related XFileAttch.DoTrigger will be set to Yes. Which will then invoke the logic which automatically syncs up PartLot Attachments. Note DocType change sets this flag only the single specific XFileAttch record. It does not invoke the triggers for other XFileAttch records that are be related to the same XFileRef  */  
   DoTrigger:boolean,
      /**  In some cases the system will duplicate a XFileAttch attaching it to a different table. Ex: RcvDtl attachments may be replicated to PartLot.  When this duplication occurs the source XFileAttch record ?DupTo? fields are updated and provide a link between the two. If the source XFileAttch is changed or deleted so will the record that was duplicated.  */  
   DupToRelatedToFile:string,
      /**  See DupToRelatedToFile  */  
   DupToKey1:string,
      /**  See DupToRelatedToFile  */  
   DupToKey2:string,
      /**  See DupToRelatedToFile  */  
   DupToKey3:string,
      /**  See DupToRelatedToFile  */  
   DupToKey4:string,
      /**  See DupToRelatedToFile  */  
   DupToKey5:string,
      /**  See DupToRelatedToFile  */  
   DupToAttachNum:number,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  The unique ID assigned by the Sharepoint system to attachments.  Field not required  */  
   SharePointID:string,
      /**  ForeignSysRowID  */  
   ForeignSysRowID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   XFileRefDocTypeID:string,
   XFileRefPDMDocID:string,
   XFileRefXFileName:string,
   XFileRefXFileDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param docTypeID
      @param fileName
   */  
export interface OnChangeOfDocType_input{
      /**  The Document Type ID (tablenameAttch.DocTypeID) that has been entered.  */  
   docTypeID:string,
      /**  The fully qualified file name that the user is referencing for this attachment.  */  
   fileName:string,
}

export interface OnChangeOfDocType_output{
parameters : {
      /**  output parameters  */  
   fileName:string,
}
}

   /** Required : 
      @param fileName
      @param xFileRefNum
      @param xFileDesc
      @param docTypeID
      @param pdmDocID
   */  
export interface OnChangeOfFileName_input{
      /**  The fully qualified file name (tablenameAttch.FileName) that the user is referencing for this attachment.  */  
   fileName:string,
      /**  External File Reference Number (tablenameAttch.XFileRefNum).  */  
   xFileRefNum:number,
      /**  File description (tablenameAttch.DrawDesc).  */  
   xFileDesc:string,
      /**  Document Type ID (tablenameAttch.DocTypeID).  */  
   docTypeID:string,
      /**  PDM Document ID (tablenameAttch.PDMDocID).  */  
   pdmDocID:string,
}

export interface OnChangeOfFileName_output{
parameters : {
      /**  output parameters  */  
   xFileRefNum:number,
   xFileDesc:string,
   docTypeID:string,
   pdmDocID:string,
}
}

   /** Required : 
      @param path
   */  
export interface ServerDirectoryExists_input{
      /**  The path to test  */  
   path:string,
}

export interface ServerDirectoryExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param docTypeID
      @param storageType
      @param spUserName
      @param spUserPwd
      @param spDomain
      @param authType
   */  
export interface SetAccountForServer_input{
      /**  Document type ID, or empty string for company level  */  
   docTypeID:string,
      /**  Storage type this accound is created for  */  
   storageType:number,
      /**  User name  */  
   spUserName:string,
      /**  Password  */  
   spUserPwd:string,
      /**  Domain for Windows authentication  */  
   spDomain:string,
      /**  Authentication type - NTLM for Windows or SPO for SharePoint Online  */  
   authType:string,
}

export interface SetAccountForServer_output{
}

   /** Required : 
      @param docTypeID
      @param storageType
      @param spUserName
      @param spUserPwd
      @param spDomain
      @param authType
   */  
export interface SetAccountForUser_input{
      /**  Document type ID, or empty string to change access to company  */  
   docTypeID:string,
      /**  Storage type this accound is created for  */  
   storageType:number,
      /**  suggested username  */  
   spUserName:string,
      /**  suggested password  */  
   spUserPwd:string,
      /**  domain for Windows authentication  */  
   spDomain:string,
      /**  Authentication type - NTLM for Windows or SPO for SharePoint Online  */  
   authType:string,
}

export interface SetAccountForUser_output{
}

   /** Required : 
      @param docTypeID
      @param contentTypeName
      @param columnName
      @param displayName
      @param dataType
   */  
export interface SpAddFieldToContentType_input{
      /**  Document type  */  
   docTypeID:string,
   contentTypeName:string,
   columnName:string,
   displayName:string,
   dataType:string,
}

export interface SpAddFieldToContentType_output{
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param contentTypeName
      @param contentTypeDescription
   */  
export interface SpCreateContentType_input{
      /**  Document type  */  
   docTypeID:string,
   contentTypeName:string,
   contentTypeDescription:string,
}

export interface SpCreateContentType_output{
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param tableName
   */  
export interface SpCreateDocumentFolder_input{
      /**  Document type  */  
   docTypeID:string,
      /**  Table to use for attachments  */  
   tableName:string,
}

export interface SpCreateDocumentFolder_output{
   returnObj:boolean,
}

   /** Required : 
      @param docTypeID
   */  
export interface SpCreateDocumentLibrary_input{
      /**  Document type  */  
   docTypeID:string,
}

export interface SpCreateDocumentLibrary_output{
   returnObj:boolean,
}

   /** Required : 
      @param xFileRefNum
   */  
export interface SpDeleteFile_input{
      /**  File ID  */  
   xFileRefNum:number,
}

export interface SpDeleteFile_output{
}

   /** Required : 
      @param xFileRefNum
   */  
export interface SpDownloadFile_input{
      /**  file ID  */  
   xFileRefNum:number,
}

export interface SpDownloadFile_output{
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
   */  
export interface SpFileExists_input{
      /**  document type or empty, if default  */  
   docTypeID:string,
      /**  table where attacment belongs  */  
   parentTable:string,
      /**  Path to the file on the server  */  
   fileName:string,
}

export interface SpFileExists_output{
      /**  True if exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface SpGetMetadata_input{
   xFileRefNum:number,
   metadata:any,      //schema had no properties on an object.
}

export interface SpGetMetadata_output{
parameters : {
      /**  output parameters  */  
   metadata: UNKNOW TYPE(error 2338),
}
}

   /** Required : 
      @param docTypeID
      @param directoryID
      @param applicationID
      @param certificateThumbPrint
      @param sharePointRoot
      @param authorityEndpoint
   */  
export interface SpOnlineTestConnectionCompany_input{
      /**  Document type ID, or empty string to test company access.  */  
   docTypeID:string,
      /**  Azure Active Directory ID.  */  
   directoryID:string,
      /**  Azure Active Directory WEb application ID.  */  
   applicationID:string,
   certificateThumbPrint:string,
      /**  Share Point Root  */  
   sharePointRoot:string,
      /**  Authority endpoint. Default will be used if nothing specified.  */  
   authorityEndpoint:string,
}

export interface SpOnlineTestConnectionCompany_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown.  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param spUserName
      @param spUserPwd
      @param spDomain
      @param authType
      @param sharePointRoot
   */  
export interface SpTestConnectionCompany_input{
      /**  Document type ID, or empty string to test company access  */  
   docTypeID:string,
      /**  suggested username  */  
   spUserName:string,
      /**  suggested password  */  
   spUserPwd:string,
      /**  domain for Windows authentication  */  
   spDomain:string,
      /**  Authentication type - should be NTLM.  */  
   authType:string,
      /**  Share Point Root  */  
   sharePointRoot:string,
}

export interface SpTestConnectionCompany_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param spUserName
      @param spUserPwd
      @param spDomain
      @param authType
   */  
export interface SpTestConnection_input{
      /**  Document type ID, or empty string to test company access  */  
   docTypeID:string,
      /**  suggested username  */  
   spUserName:string,
      /**  suggested password  */  
   spUserPwd:string,
      /**  domain for Windows authentication  */  
   spDomain:string,
      /**  Authentication type - NTLM for Windows or SPO for SharePoint Online  */  
   authType:string,
}

export interface SpTestConnection_output{
      /**  Message that connection succeeded. In case of failure exception will be thrown  */  
   returnObj:string,
}

   /** Required : 
      @param xFileRefNum
      @param addSpPropsFields
      @param metadata
   */  
export interface SpUpdateMetadata_input{
      /**  File ID from xFileRef table  */  
   xFileRefNum:number,
      /**  set to false to update only description, true - to update comment and status  */  
   addSpPropsFields:boolean,
      /**  metadata to update  */  
   metadata:any,      //schema had no properties on an object.
}

export interface SpUpdateMetadata_output{
}

   /** Required : 
      @param fileName
      @param data
      @param docTypeID
      @param parentTable
      @param metadata
   */  
export interface SpUploadFile_input{
      /**  file name without path  */  
   fileName:string,
      /**  file binary data  */  
   data:string,
      /**  Document type for the attachment  */  
   docTypeID:string,
      /**  Table where file is attached  */  
   parentTable:string,
      /**  SharePoint metadata  */  
   metadata:any,      //schema had no properties on an object.
}

export interface SpUploadFile_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtAttachmentTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtAttachmentTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param xFileRefNum
      @param metadata
   */  
export interface UpdateMetadataOnDocumentStorage_input{
      /**  The xFileRef file ID associated with the document.  */  
   xFileRefNum:number,
      /**  Dictionary containing the file metadata to update.  */  
   metadata:any,      //schema had no properties on an object.
}

export interface UpdateMetadataOnDocumentStorage_output{
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_AttachmentTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_AttachmentTableset[],
}
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
      @param data
      @param metadata
   */  
export interface UploadFileToDocTypeStorage_input{
   docTypeID:string,
   parentTable:string,
   fileName:string,
   data:string,
   metadata:any,      //schema had no properties on an object.
}

export interface UploadFileToDocTypeStorage_output{
      /**  server file path  */  
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
      @param data
   */  
export interface UploadFile_input{
      /**  document type or empty, if default  */  
   docTypeID:string,
      /**  table where attacment belongs  */  
   parentTable:string,
      /**  filename, without path  */  
   fileName:string,
      /**  file content  */  
   data:string,
}

export interface UploadFile_output{
   returnObj:string,
}

   /** Required : 
      @param docTypeID
      @param parentTable
      @param fileName
      @param data
      @param metadata
   */  
export interface UploadNonERPFileToDocTypeStorage_input{
   docTypeID:string,
   parentTable:string,
   fileName:string,
   data:string,
   metadata:any,      //schema had no properties on an object.
}

export interface UploadNonERPFileToDocTypeStorage_output{
      /**  server file path  */  
   returnObj:string,
}

