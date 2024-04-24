import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.APPromNoteGrpSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/$metadata", {
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
   Description: Get APPromNoteGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPromNoteGrps
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpRow
   */  
export function get_APPromNoteGrps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPromNoteGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APPromNoteGrps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps", {
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
   Summary: Calls GetByID to retrieve the APPromNoteGrp item
   Description: Calls GetByID to retrieve the APPromNoteGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPromNoteGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   */  
export function get_APPromNoteGrps_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APChkGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APPromNoteGrp for the service
   Description: Calls UpdateExt to update APPromNoteGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPromNoteGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APPromNoteGrps_Company_GroupID(Company:string, GroupID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete APPromNoteGrp item
   Description: Call UpdateExt to delete APPromNoteGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPromNoteGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APPromNoteGrps_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get APChkGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APChkGrpAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpAttchRow
   */  
export function get_APPromNoteGrps_Company_GroupID_APChkGrpAttches(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")/APChkGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APChkGrpAttch item
   Description: Calls GetByID to retrieve the APChkGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   */  
export function get_APPromNoteGrps_Company_GroupID_APChkGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APPromNoteGrps(" + Company + "," + GroupID + ")/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APChkGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get APChkGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APChkGrpAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpAttchRow
   */  
export function get_APChkGrpAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APChkGrpAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APChkGrpAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches", {
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
   Summary: Calls GetByID to retrieve the APChkGrpAttch item
   Description: Calls GetByID to retrieve the APChkGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APChkGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   */  
export function get_APChkGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APChkGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_APChkGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APChkGrpAttch for the service
   Description: Calls UpdateExt to update APChkGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APChkGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APChkGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APChkGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete APChkGrpAttch item
   Description: Call UpdateExt to delete APChkGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APChkGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APChkGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/APChkGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APChkGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpListRow)
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
export function get_GetRows(whereClauseAPChkGrp:string, whereClauseAPChkGrpAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseAPChkGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPChkGrp=" + whereClauseAPChkGrp
   }
   if(typeof whereClauseAPChkGrpAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPChkGrpAttch=" + whereClauseAPChkGrpAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetRows" + params, {
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
export function get_GetByID(groupID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetList" + params, {
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
   Summary: Invoke method GetNewAPChkGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated. Active user locking disabled.
   OperationID: GetNewAPChkGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPChkGrpNoLock(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetNewAPChkGrpNoLock", {
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
   Summary: Invoke method CheckForEditList
   Description: This method informs the user if any of PI of this Group will not be included in Edit List
because of their First GL Stage Update status
   OperationID: CheckForEditList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForEditList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForEditList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckForEditList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/CheckForEditList", {
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
   Summary: Invoke method DeleteZeroAmtTaxRec
   Description: This method deletes TaxDtl records which have zero amounts
Since  TAx logic calculates tax conditionally only for the first tax line the invoice could have multiple zero tax records.
   OperationID: DeleteZeroAmtTaxRec
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteZeroAmtTaxRec_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZeroAmtTaxRec_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteZeroAmtTaxRec(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/DeleteZeroAmtTaxRec", {
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
   Summary: Invoke method LockGroup
   Description: This procedure is GetById + Lock the Group.  This procedure can be run
instead of GetById if you want to lock along with doing a GetByID.
If the lock is acquired successfully, plSuccess is returned as true.
   OperationID: LockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/LockGroup", {
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
   Summary: Invoke method OnChangeBankAcctID
   Description: Call this method when the user changes the Bank Account.
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/OnChangeBankAcctID", {
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
   Summary: Invoke method PrePostGrp
   Description: Method to call before posting invoices for a specific group..  This method will check if there are
records with zero tax amounts and return
message text asking the user if they would like to continue with posting or delete these tax records.
   OperationID: PrePostGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePostGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/PrePostGrp", {
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
   Summary: Invoke method SetBankAcctID
   Description: Purpose:     Set Bank Account ID before updating a just created ApChkGrp record.
Parameters:  APPromNoteGrp DataSet
Notes:
   OperationID: SetBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetBankAcctID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/SetBankAcctID", {
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
   Summary: Invoke method UnLockGroup
   Description: Unlock the group.  The user who locked the group can only unlock it.
   OperationID: UnLockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnLockGroup(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/UnLockGroup", {
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
   Summary: Invoke method GetNewAPChkGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPChkGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetNewAPChkGrp", {
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
   Summary: Invoke method GetNewAPChkGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPChkGrpAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPChkGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPChkGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPChkGrpAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetNewAPChkGrpAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.APPromNoteGrpSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APChkGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APChkGrpRow[],
}

export interface Erp_Tablesets_APChkGrpAttchRow{
   "Company":string,
   "GroupID":string,
   "DrawingSeq":number,
   "XFileRefNum":number,
   "SysRevID":number,
   "SysRowID":string,
   "ForeignSysRowID":string,
   "DrawDesc":string,
   "FileName":string,
   "PDMDocID":string,
   "DocTypeID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APChkGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  */  
   "BankAcctID":string,
      /**  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  */  
   "CheckDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   "Cashbook":boolean,
      /**  Contains error messages returned by the Post process.  */  
   "PostErrorLog":string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   "PostInProcess":boolean,
      /**  Rate Group Code  */  
   "RateGrpCode":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Payment Instrument  */  
   "PromissoryNote":boolean,
      /**  Yes if group having payment method with type ?Electronic Interface? was successfully processed  */  
   "EIPaymSent":boolean,
      /**   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  */  
   "GrpCreationVia":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "APInterfaced":boolean,
   "TotalCheckAmt":number,
   "TotalDocCheckAmt":number,
   "TotalMiscCheckAmt":number,
   "TotalAmountToAP":number,
   "TotalDiscAmt":number,
   "TotalDocDiscAmt":number,
   "BaseCurrSymbol":string,
   "TotalDocMiscCheckAmt":number,
   "BankAcctIDEnabled":boolean,
   "Rpt1TotalCheckAmt":number,
   "Rpt2TotalCheckAmt":number,
   "Rpt3TotalCheckAmt":number,
   "Rpt1TotalDiscAmt":number,
   "Rpt2TotalDiscAmt":number,
   "Rpt3TotalDiscAmt":number,
   "Rpt1TotalMiscCheckAmt":number,
   "Rpt2TotalMiscCheckAmt":number,
   "Rpt3TotalMiscCheckAmt":number,
   "TotalWithHoldTax":number,
   "TotalDocWithHoldTax":number,
   "Rpt1TotalWithHoldTax":number,
   "Rpt3TotalWithHoldTax":number,
   "Rpt2TotalWithHoldTax":number,
   "EnableCurrency":boolean,
   "BaseCurrencyID":string,
   "DispCurrencyCode":string,
   "PymtProposal":boolean,
   "BankTotalCheckAmt":number,
   "BankTotalMiscCheckAmt":number,
   "BankCurrencyCode":string,
   "BankTotalDiscAmt":number,
   "BankTotalWithholdTax":number,
   "BankTotalAmountToAP":number,
   "TotalDocAmountToAP":number,
   "BankCurrDesc":string,
   "CurrencyList":string,
      /**  The flag to indicate if this Payment Group is created by processing Bank Import File.  */  
   "FromImportPmt":boolean,
      /**  The Bank's full name.  */  
   "BankAcctIDBankName":string,
      /**  Full description of the bank account.  */  
   "BankAcctIDDescription":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrSymbolDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrSymbolCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrSymbolCurrName":string,
      /**  Description of the currency  */  
   "BaseCurrSymbolCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrSymbolCurrSymbol":string,
      /**  Description of the currency  */  
   "CurrencyCodeCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCodeCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCodeCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyCodeDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCodeCurrName":string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   "PayMethodOnlyBankCurr":boolean,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  Description  */  
   "RateGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APChkGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  */  
   "BankAcctID":string,
      /**  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  */  
   "CheckDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   "Cashbook":boolean,
      /**  Contains error messages returned by the Post process.  */  
   "PostErrorLog":string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   "PostInProcess":boolean,
      /**  Rate Group Code  */  
   "RateGrpCode":string,
      /**  Unique identifier of the payment method  */  
   "PMUID":number,
      /**  Payment Instrument  */  
   "PromissoryNote":boolean,
      /**  Yes if group having payment method with type ?Electronic Interface? was successfully processed  */  
   "EIPaymSent":boolean,
      /**   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  */  
   "GrpCreationVia":string,
      /**  Auto Generated  */  
   "AutoGenerated":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CHOrderNum  */  
   "CHOrderNum":number,
      /**  NOPaymentList  */  
   "NOPaymentList":boolean,
      /**  BankBatchSysRowID  */  
   "BankBatchSysRowID":string,
      /**  Plant  */  
   "Plant":string,
      /**  CentralizedPayment  */  
   "CentralizedPayment":boolean,
   "APInterfaced":boolean,
   "BankCurrencyCode":string,
   "BankTotalAmountToAP":number,
   "BankTotalCheckAmt":number,
   "BankTotalDiscAmt":number,
   "BankTotalMiscCheckAmt":number,
   "BankTotalWithholdTax":number,
   "BaseCurrencyID":string,
   "BaseCurrSymbol":string,
   "CurrencyList":string,
      /**  Displays the currency or currencies of payments in the group. If more than one payment currency is used in the group, user is able to switch between currencies to see total cash and total AP for the group, specific to the payments in that selected currency.  */  
   "DispCurrencyCode":string,
   "DocBankTotalCheckAmt":number,
      /**  Displays the generated batch reference for the group when batches are being used for the selected payment method.  */  
   "DspBankBatchID":string,
      /**  Yes if group having payment method with type ?Electronic Interface? allows for zero balance payments  */  
   "EFTAllowZeroNet":boolean,
      /**  Debit Memo due date on credits for Type 2 payments.  */  
   "EFTDebitMemoDueDate":string,
      /**  Special code to handle EFT payments, this is defined by the CSF as needed.  */  
   "EFTDebitMemoHandlingCode":string,
   "EIGrouping":boolean,
   "EnableCurrency":boolean,
      /**  The flag to indicate if this Payment Group is created by processing Bank Import File.  */  
   "FromImportPmt":boolean,
      /**  Norway CSF: is Nordea payment  */  
   "NOTelepayPayment":boolean,
      /**  Norway CSF: Telepay Reply  */  
   "NOTelepayReply":boolean,
   "PymtProposal":boolean,
   "Rpt1BankTotalCheckAmt":number,
   "Rpt1TotalCheckAmt":number,
   "Rpt1TotalDiscAmt":number,
   "Rpt1TotalMiscCheckAmt":number,
   "Rpt1TotalWithHoldTax":number,
   "Rpt2BankTotalCheckAmt":number,
   "Rpt2TotalCheckAmt":number,
   "Rpt2TotalDiscAmt":number,
   "Rpt2TotalMiscCheckAmt":number,
   "Rpt2TotalWithHoldTax":number,
   "Rpt3BankTotalCheckAmt":number,
   "Rpt3TotalCheckAmt":number,
   "Rpt3TotalDiscAmt":number,
   "Rpt3TotalMiscCheckAmt":number,
   "Rpt3TotalWithHoldTax":number,
   "SEEFTPO3Payment":boolean,
      /**  Total AP amount for the payment entry group.  */  
   "TotalAmountToAP":number,
      /**  Total Cash amount for the payment entry group.  */  
   "TotalCheckAmt":number,
      /**  Total discount amount for the payment entry group.  */  
   "TotalDiscAmt":number,
      /**  Total AP amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   "TotalDocAmountToAP":number,
      /**  Total Cash amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   "TotalDocCheckAmt":number,
      /**  Total discount amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   "TotalDocDiscAmt":number,
      /**  Total miscellaneous amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   "TotalDocMiscCheckAmt":number,
      /**  Total withholding tax amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   "TotalDocWithHoldTax":number,
      /**  Total miscellaneous amount for the payment entry group.  */  
   "TotalMiscCheckAmt":number,
      /**  Total withholding tax amount for the payment entry group.  */  
   "TotalWithHoldTax":number,
   "UIGrouping":boolean,
   "BankAcctIDEnabled":boolean,
   "BankCurrDesc":string,
      /**  Indicates if the selected bank account uses average rates on payments.  */  
   "APPaymentUseBankAvg":boolean,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   "HasDetails":boolean,
      /**  Indicates that the group is locked and currently in journal review.  */  
   "IsDocumentLocked":boolean,
      /**  Locked means can not be posted: a payment is already in review journal or in posting process.  */  
   "LockStatus":string,
   "RvJrnUID":number,
   "BitFlag":number,
   "BankAcctIDDescription":string,
   "BankAcctIDBankName":string,
   "BaseCurrSymbolCurrSymbol":string,
   "BaseCurrSymbolCurrencyID":string,
   "BaseCurrSymbolDocumentDesc":string,
   "BaseCurrSymbolCurrDesc":string,
   "BaseCurrSymbolCurrName":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrDesc":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeCurrName":string,
   "PayMethodOnlyBankCurr":boolean,
   "PayMethodName":string,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodType":number,
   "RateGrpDescription":string,
   "XbSystSiteIsLegalEntity":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param postGroupID
   */  
export interface CheckForEditList_input{
      /**  The Group ID of the Group for Edit List  */  
   postGroupID:string,
}

export interface CheckForEditList_output{
parameters : {
      /**  output parameters  */  
   noPI:boolean,
   noPIList:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param postGroupID
   */  
export interface DeleteZeroAmtTaxRec_input{
      /**  The Group ID of the Group to post  */  
   postGroupID:string,
}

export interface DeleteZeroAmtTaxRec_output{
}

export interface Erp_Tablesets_APChkGrpAttchRow{
   Company:string,
   GroupID:string,
   DrawingSeq:number,
   XFileRefNum:number,
   SysRevID:number,
   SysRowID:string,
   ForeignSysRowID:string,
   DrawDesc:string,
   FileName:string,
   PDMDocID:string,
   DocTypeID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APChkGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  */  
   BankAcctID:string,
      /**  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  */  
   CheckDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   Cashbook:boolean,
      /**  Contains error messages returned by the Post process.  */  
   PostErrorLog:string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   PostInProcess:boolean,
      /**  Rate Group Code  */  
   RateGrpCode:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Payment Instrument  */  
   PromissoryNote:boolean,
      /**  Yes if group having payment method with type ?Electronic Interface? was successfully processed  */  
   EIPaymSent:boolean,
      /**   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  */  
   GrpCreationVia:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   APInterfaced:boolean,
   TotalCheckAmt:number,
   TotalDocCheckAmt:number,
   TotalMiscCheckAmt:number,
   TotalAmountToAP:number,
   TotalDiscAmt:number,
   TotalDocDiscAmt:number,
   BaseCurrSymbol:string,
   TotalDocMiscCheckAmt:number,
   BankAcctIDEnabled:boolean,
   Rpt1TotalCheckAmt:number,
   Rpt2TotalCheckAmt:number,
   Rpt3TotalCheckAmt:number,
   Rpt1TotalDiscAmt:number,
   Rpt2TotalDiscAmt:number,
   Rpt3TotalDiscAmt:number,
   Rpt1TotalMiscCheckAmt:number,
   Rpt2TotalMiscCheckAmt:number,
   Rpt3TotalMiscCheckAmt:number,
   TotalWithHoldTax:number,
   TotalDocWithHoldTax:number,
   Rpt1TotalWithHoldTax:number,
   Rpt3TotalWithHoldTax:number,
   Rpt2TotalWithHoldTax:number,
   EnableCurrency:boolean,
   BaseCurrencyID:string,
   DispCurrencyCode:string,
   PymtProposal:boolean,
   BankTotalCheckAmt:number,
   BankTotalMiscCheckAmt:number,
   BankCurrencyCode:string,
   BankTotalDiscAmt:number,
   BankTotalWithholdTax:number,
   BankTotalAmountToAP:number,
   TotalDocAmountToAP:number,
   BankCurrDesc:string,
   CurrencyList:string,
      /**  The flag to indicate if this Payment Group is created by processing Bank Import File.  */  
   FromImportPmt:boolean,
      /**  The Bank's full name.  */  
   BankAcctIDBankName:string,
      /**  Full description of the bank account.  */  
   BankAcctIDDescription:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrSymbolDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrSymbolCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrSymbolCurrName:string,
      /**  Description of the currency  */  
   BaseCurrSymbolCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrSymbolCurrSymbol:string,
      /**  Description of the currency  */  
   CurrencyCodeCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCodeCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCodeCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyCodeDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCodeCurrName:string,
      /**  Indicates if this interface will only support payments in the currency of the bank. This will affect selection of invoices in the AP payment function.  */  
   PayMethodOnlyBankCurr:boolean,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  Description  */  
   RateGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APChkGrpListTableset{
   APChkGrpList:Erp_Tablesets_APChkGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_APChkGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**  The ID of the BankAcct master which for the bank account from which the transactions in this group will be paid. This is a mandatory entry and must be valid.  It can be changed at check print time. Check printing uses this as a default account to pay from.  */  
   BankAcctID:string,
      /**  Default Check date to be used when printing checks for this group. Default to current system date.  During the check print process the check date is overridable; this is date is used as a default. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on this date.  */  
   CheckDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  if this group is created by the Cashbook then other programs can not select this group.  */  
   Cashbook:boolean,
      /**  Contains error messages returned by the Post process.  */  
   PostErrorLog:string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   PostInProcess:boolean,
      /**  Rate Group Code  */  
   RateGrpCode:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  Payment Instrument  */  
   PromissoryNote:boolean,
      /**  Yes if group having payment method with type ?Electronic Interface? was successfully processed  */  
   EIPaymSent:boolean,
      /**   Indicates if the group was created by AP Payment Instrument Entry or AP Invoice Entry.

Possible values are:
"PrN" - Created by AP Payment Instrument Entry
"API" - Created by AP Invoice Entry  */  
   GrpCreationVia:string,
      /**  Auto Generated  */  
   AutoGenerated:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHOrderNum  */  
   CHOrderNum:number,
      /**  NOPaymentList  */  
   NOPaymentList:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  Plant  */  
   Plant:string,
      /**  CentralizedPayment  */  
   CentralizedPayment:boolean,
   APInterfaced:boolean,
   BankCurrencyCode:string,
   BankTotalAmountToAP:number,
   BankTotalCheckAmt:number,
   BankTotalDiscAmt:number,
   BankTotalMiscCheckAmt:number,
   BankTotalWithholdTax:number,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
   CurrencyList:string,
      /**  Displays the currency or currencies of payments in the group. If more than one payment currency is used in the group, user is able to switch between currencies to see total cash and total AP for the group, specific to the payments in that selected currency.  */  
   DispCurrencyCode:string,
   DocBankTotalCheckAmt:number,
      /**  Displays the generated batch reference for the group when batches are being used for the selected payment method.  */  
   DspBankBatchID:string,
      /**  Yes if group having payment method with type ?Electronic Interface? allows for zero balance payments  */  
   EFTAllowZeroNet:boolean,
      /**  Debit Memo due date on credits for Type 2 payments.  */  
   EFTDebitMemoDueDate:string,
      /**  Special code to handle EFT payments, this is defined by the CSF as needed.  */  
   EFTDebitMemoHandlingCode:string,
   EIGrouping:boolean,
   EnableCurrency:boolean,
      /**  The flag to indicate if this Payment Group is created by processing Bank Import File.  */  
   FromImportPmt:boolean,
      /**  Norway CSF: is Nordea payment  */  
   NOTelepayPayment:boolean,
      /**  Norway CSF: Telepay Reply  */  
   NOTelepayReply:boolean,
   PymtProposal:boolean,
   Rpt1BankTotalCheckAmt:number,
   Rpt1TotalCheckAmt:number,
   Rpt1TotalDiscAmt:number,
   Rpt1TotalMiscCheckAmt:number,
   Rpt1TotalWithHoldTax:number,
   Rpt2BankTotalCheckAmt:number,
   Rpt2TotalCheckAmt:number,
   Rpt2TotalDiscAmt:number,
   Rpt2TotalMiscCheckAmt:number,
   Rpt2TotalWithHoldTax:number,
   Rpt3BankTotalCheckAmt:number,
   Rpt3TotalCheckAmt:number,
   Rpt3TotalDiscAmt:number,
   Rpt3TotalMiscCheckAmt:number,
   Rpt3TotalWithHoldTax:number,
   SEEFTPO3Payment:boolean,
      /**  Total AP amount for the payment entry group.  */  
   TotalAmountToAP:number,
      /**  Total Cash amount for the payment entry group.  */  
   TotalCheckAmt:number,
      /**  Total discount amount for the payment entry group.  */  
   TotalDiscAmt:number,
      /**  Total AP amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   TotalDocAmountToAP:number,
      /**  Total Cash amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   TotalDocCheckAmt:number,
      /**  Total discount amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   TotalDocDiscAmt:number,
      /**  Total miscellaneous amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   TotalDocMiscCheckAmt:number,
      /**  Total withholding tax amount for the payment entry group. This total is specific to the Payments made in the currency selected in the group display Currency field.  */  
   TotalDocWithHoldTax:number,
      /**  Total miscellaneous amount for the payment entry group.  */  
   TotalMiscCheckAmt:number,
      /**  Total withholding tax amount for the payment entry group.  */  
   TotalWithHoldTax:number,
   UIGrouping:boolean,
   BankAcctIDEnabled:boolean,
   BankCurrDesc:string,
      /**  Indicates if the selected bank account uses average rates on payments.  */  
   APPaymentUseBankAvg:boolean,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   HasDetails:boolean,
      /**  Indicates that the group is locked and currently in journal review.  */  
   IsDocumentLocked:boolean,
      /**  Locked means can not be posted: a payment is already in review journal or in posting process.  */  
   LockStatus:string,
   RvJrnUID:number,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   BaseCurrSymbolCurrSymbol:string,
   BaseCurrSymbolCurrencyID:string,
   BaseCurrSymbolDocumentDesc:string,
   BaseCurrSymbolCurrDesc:string,
   BaseCurrSymbolCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   PayMethodOnlyBankCurr:boolean,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodType:number,
   RateGrpDescription:string,
   XbSystSiteIsLegalEntity:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APPromNoteGrpTableset{
   APChkGrp:Erp_Tablesets_APChkGrpRow[],
   APChkGrpAttch:Erp_Tablesets_APChkGrpAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtAPPromNoteGrpTableset{
   APChkGrp:Erp_Tablesets_APChkGrpRow[],
   APChkGrpAttch:Erp_Tablesets_APChkGrpAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_APPromNoteGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_APPromNoteGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_APPromNoteGrpTableset[],
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
   returnObj:Erp_Tablesets_APChkGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewAPChkGrpAttch_input{
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
   groupID:string,
}

export interface GetNewAPChkGrpAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPChkGrpNoLock_input{
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}

export interface GetNewAPChkGrpNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPChkGrp_input{
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}

export interface GetNewAPChkGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

   /** Required : 
      @param whereClauseAPChkGrp
      @param whereClauseAPChkGrpAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseAPChkGrp:string,
   whereClauseAPChkGrpAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_APPromNoteGrpTableset[],
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
      @param pcGroupID
   */  
export interface LockGroup_input{
      /**  The Group ID selected by the user.  */  
   pcGroupID:string,
}

export interface LockGroup_output{
   returnObj:Erp_Tablesets_APPromNoteGrpTableset[],
parameters : {
      /**  output parameters  */  
   plSuccess:boolean,
}
}

   /** Required : 
      @param pcBankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
      /**  The proposed value of BankAcctID.  */  
   pcBankAcctID:string,
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

   /** Required : 
      @param postGroupID
   */  
export interface PrePostGrp_input{
      /**  The Group ID of the Group to post  */  
   postGroupID:string,
}

export interface PrePostGrp_output{
parameters : {
      /**  output parameters  */  
   taxRecMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface SetBankAcctID_input{
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}

export interface SetBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

   /** Required : 
      @param pcGroupID
   */  
export interface UnLockGroup_input{
      /**  The Group ID selected by the user.  */  
   pcGroupID:string,
}

export interface UnLockGroup_output{
parameters : {
      /**  output parameters  */  
   plSuccess:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAPPromNoteGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAPPromNoteGrpTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_APPromNoteGrpTableset[],
}
}

