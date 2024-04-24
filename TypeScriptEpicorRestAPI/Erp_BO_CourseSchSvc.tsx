import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CourseSchSvc
// Description: Course Schedule Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/$metadata", {
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
   Description: Get CourseSches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchRow
   */  
export function get_CourseSches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches", {
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
   Summary: Calls GetByID to retrieve the CourseSch item
   Description: Calls GetByID to retrieve the CourseSch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   */  
export function get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CourseSchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CourseSchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CourseSch for the service
   Description: Calls UpdateExt to update CourseSch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")", {
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
   Summary: Call UpdateExt to delete CourseSch item
   Description: Call UpdateExt to delete CourseSch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")", {
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
   Description: Get CourseSchAttds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseSchAttds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdRow
   */  
export function get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate_CourseSchAttds(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")/CourseSchAttds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CourseSchAttd item
   Description: Calls GetByID to retrieve the CourseSchAttd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttd1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   */  
export function get_CourseSches_Company_CourseID_RevisionCode_StartDate_EndDate_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CourseSchAttdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + ")/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CourseSchAttdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CourseSchAttds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSchAttds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdRow
   */  
export function get_CourseSchAttds(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSchAttds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchAttds(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds", {
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
   Summary: Calls GetByID to retrieve the CourseSchAttd item
   Description: Calls GetByID to retrieve the CourseSchAttd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   */  
export function get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CourseSchAttdRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CourseSchAttdRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CourseSchAttd for the service
   Description: Calls UpdateExt to update CourseSchAttd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSchAttd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")", {
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
   Summary: Call UpdateExt to delete CourseSchAttd item
   Description: Call UpdateExt to delete CourseSchAttd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSchAttd
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")", {
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
   Description: Get CourseSchAttdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CourseSchAttdAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdAttchRow
   */  
export function get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_CourseSchAttdAttches(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")/CourseSchAttdAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CourseSchAttdAttch item
   Description: Calls GetByID to retrieve the CourseSchAttdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttdAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   */  
export function get_CourseSchAttds_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CourseSchAttdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttds(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + ")/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CourseSchAttdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CourseSchAttdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CourseSchAttdAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchAttdAttchRow
   */  
export function get_CourseSchAttdAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CourseSchAttdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchAttdAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches", {
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
   Summary: Calls GetByID to retrieve the CourseSchAttdAttch item
   Description: Calls GetByID to retrieve the CourseSchAttdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CourseSchAttdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   */  
export function get_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CourseSchAttdAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CourseSchAttdAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CourseSchAttdAttch for the service
   Description: Calls UpdateExt to update CourseSchAttdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CourseSchAttdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CourseSchAttdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CourseSchAttdAttch item
   Description: Call UpdateExt to delete CourseSchAttdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CourseSchAttdAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CourseID Desc: CourseID   Required: True   Allow empty value : True
      @param RevisionCode Desc: RevisionCode   Required: True   Allow empty value : True
      @param StartDate Desc: StartDate   Required: True   Allow empty value : True
      @param EndDate Desc: EndDate   Required: True   Allow empty value : True
      @param EmpID Desc: EmpID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CourseSchAttdAttches_Company_CourseID_RevisionCode_StartDate_EndDate_EmpID_DrawingSeq(Company:string, CourseID:string, RevisionCode:string, StartDate:string, EndDate:string, EmpID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdAttches(" + Company + "," + CourseID + "," + RevisionCode + "," + StartDate + "," + EndDate + "," + EmpID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CourseSchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCourseSch:string, whereClauseCourseSchAttd:string, whereClauseCourseSchAttdAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCourseSch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCourseSch=" + whereClauseCourseSch
   }
   if(typeof whereClauseCourseSchAttd!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCourseSchAttd=" + whereClauseCourseSchAttd
   }
   if(typeof whereClauseCourseSchAttdAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCourseSchAttdAttch=" + whereClauseCourseSchAttdAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(courseID:string, revisionCode:string, startDate:string, endDate:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof courseID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "courseID=" + courseID
   }
   if(typeof revisionCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "revisionCode=" + revisionCode
   }
   if(typeof startDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "startDate=" + startDate
   }
   if(typeof endDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "endDate=" + endDate
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetList" + params, {
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
   Summary: Invoke method InstrTypeChanged
   Description: Method to call when changing the InstrType field.
   OperationID: InstrTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InstrTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InstrTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InstrTypeChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/InstrTypeChanged", {
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
   Summary: Invoke method CourseResultChanged
   Description: Method to call when changing the CourseResult field.
   OperationID: CourseResultChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseResultChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseResultChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseResultChanged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseResultChanged", {
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
   Summary: Invoke method CourseSchAttdEmpIDChanging
   Description: Method to call when changing Course Schedule Attendee employee
   OperationID: CourseSchAttdEmpIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchAttdEmpIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchAttdEmpIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchAttdEmpIDChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchAttdEmpIDChanging", {
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
   Summary: Invoke method OnStartDateChanging
   Description: Method to call when changing the StartDate field.
   OperationID: OnStartDateChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnStartDateChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnStartDateChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnStartDateChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/OnStartDateChanging", {
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
   Summary: Invoke method CourseSchEmpIDChanging
   Description: Method to call when changing Course Schedule employee
   OperationID: CourseSchEmpIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchEmpIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchEmpIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchEmpIDChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchEmpIDChanging", {
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
   Summary: Invoke method CourseSchSupplierIDChanging
   Description: Method to call when changing Course Schedule supplier
   OperationID: CourseSchSupplierIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchSupplierIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchSupplierIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchSupplierIDChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchSupplierIDChanging", {
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
   Summary: Invoke method CourseSchCustIDChanging
   Description: Method to call when changing Course Schedule customer
   OperationID: CourseSchCustIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CourseSchCustIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CourseSchCustIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CourseSchCustIDChanging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CourseSchCustIDChanging", {
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
   Summary: Invoke method GetInstrTypes
   Description: Returns instructor type list
   OperationID: GetInstrTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInstrTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInstrTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetInstrTypes", {
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
   Summary: Invoke method AddAttendees
   Description: The method for assigning employees to the scheduled course.
   OperationID: AddAttendees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddAttendees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddAttendees_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddAttendees(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/AddAttendees", {
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
   Summary: Invoke method CheckFreeSpotsForCourseAttendee
   Description: The method for assigning employees to the scheduled course.
   OperationID: CheckFreeSpotsForCourseAttendee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFreeSpotsForCourseAttendee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFreeSpotsForCourseAttendee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFreeSpotsForCourseAttendee(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/CheckFreeSpotsForCourseAttendee", {
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
   Summary: Invoke method GetNewCourseSch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCourseSch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetNewCourseSch", {
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
   Summary: Invoke method GetNewCourseSchAttd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSchAttd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSchAttd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSchAttd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCourseSchAttd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetNewCourseSchAttd", {
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
   Summary: Invoke method GetNewCourseSchAttdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCourseSchAttdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCourseSchAttdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCourseSchAttdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCourseSchAttdAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetNewCourseSchAttdAttch", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CourseSchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CourseSchAttdAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchAttdRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CourseSchAttdRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CourseSchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CourseSchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CourseSchRow[],
}

export interface Erp_Tablesets_CourseSchAttdAttchRow{
   "Company":string,
   "CourseID":string,
   "RevisionCode":string,
   "StartDate":string,
   "EndDate":string,
   "EmpID":string,
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

export interface Erp_Tablesets_CourseSchAttdRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Training Course ID.  */  
   "CourseID":string,
      /**  The Course Revision Code.  */  
   "RevisionCode":string,
      /**  The start date.  */  
   "StartDate":string,
      /**  The end date.  */  
   "EndDate":string,
      /**  The employee ID attending the course.  */  
   "EmpID":string,
      /**  The cost of the training course materials for the employee.  */  
   "MaterialCost":number,
      /**  The employee's expenses whilst attending the course.  */  
   "Expenses":number,
      /**  This flag is used to indicate if the expenses have been reimbursed. Setting this field to true does NOT automatically pay the employee expenses.  */  
   "CostReimbursed":boolean,
      /**  This will contain any Reason Code that has a Reason Code Type set to U - Course Result.  */  
   "CourseResult":string,
      /**  This will default to value defined against the selected Course Result. If no Course Result is selected then this field will be set to false.  */  
   "Passed":boolean,
      /**  The employee training course results comments.  */  
   "Comments":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "EmpIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CourseSchListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Training Course ID.  */  
   "CourseID":string,
      /**  The Course Revision Code.  */  
   "RevisionCode":string,
      /**  The date that the training course is due to start. When a new schedule is created this will default to the current date.  */  
   "StartDate":string,
      /**  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  */  
   "EndDate":string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   "ActStartDate":string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   "ActEndDate":string,
      /**  The free format text to describe where the course will take place.  */  
   "Location":string,
      /**  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  */  
   "MaxAttendees":number,
      /**  The cost of the course per employee.  */  
   "CourseCost":number,
      /**  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  */  
   "InstrType":string,
      /**  The employee ID. Must be specified if InstrType = E.  */  
   "EmpID":string,
      /**  The supplier ID. Must be specified if InstrType = S.  */  
   "VendorNum":number,
      /**  The customer ID. Must be specified if InstrType = C.  */  
   "CustNum":number,
      /**  The training course schedule comments.  */  
   "Comments":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The full name of the customer.  */  
   "CustNumName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustNumCustID":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpIDName":string,
      /**  The description of the training course revision.  */  
   "RevisionCodeDescription":string,
      /**  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  */  
   "RevisionCodeDurationType":string,
      /**  The duration of the course. When a new revision is created this will default to 1.  */  
   "RevisionCodeDuration":number,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CourseSchRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The Training Course ID.  */  
   "CourseID":string,
      /**  The Course Revision Code.  */  
   "RevisionCode":string,
      /**  The date that the training course is due to start. When a new schedule is created this will default to the current date.  */  
   "StartDate":string,
      /**  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  */  
   "EndDate":string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   "ActStartDate":string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   "ActEndDate":string,
      /**  The free format text to describe where the course will take place.  */  
   "Location":string,
      /**  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  */  
   "MaxAttendees":number,
      /**  The cost of the course per employee.  */  
   "CourseCost":number,
      /**  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  */  
   "InstrType":string,
      /**  The employee ID. Must be specified if InstrType = E.  */  
   "EmpID":string,
      /**  The supplier ID. Must be specified if InstrType = S.  */  
   "VendorNum":number,
      /**  The customer ID. Must be specified if InstrType = C.  */  
   "CustNum":number,
      /**  The training course schedule comments.  */  
   "Comments":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CustNumCustID":string,
   "CustNumName":string,
   "EmpIDName":string,
   "RevisionCodeDurationType":string,
   "RevisionCodeDuration":number,
   "RevisionCodeDescription":string,
   "VendorNumVendorID":string,
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param CourseID
      @param RevisionCode
      @param StartDate
      @param EndDate
      @param EmpCourses
      @param ds
   */  
export interface AddAttendees_input{
      /**  The Course ID  */  
   CourseID:string,
      /**  The Course Revision ID  */  
   RevisionCode:string,
      /**  The Course Start Date  */  
   StartDate:string,
      /**  The Course End Date  */  
   EndDate:string,
      /**  The list of employee records IDs from EmpCourse table  */  
   EmpCourses:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface AddAttendees_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param CourseID
      @param RevisionCode
      @param StartDate
      @param EndDate
      @param NumAttendees
   */  
export interface CheckFreeSpotsForCourseAttendee_input{
      /**  The Course ID  */  
   CourseID:string,
      /**  The Course Revision ID  */  
   RevisionCode:string,
      /**  The Course Start Date  */  
   StartDate:string,
      /**  The Course End Date  */  
   EndDate:string,
      /**  The number of attendees to be added to the Scheduled Course  */  
   NumAttendees:number,
}

export interface CheckFreeSpotsForCourseAttendee_output{
parameters : {
      /**  output parameters  */  
   roomOK:boolean,
}
}

   /** Required : 
      @param proposedCourseResult
      @param ds
   */  
export interface CourseResultChanged_input{
      /**  The proposed Course Result  */  
   proposedCourseResult:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface CourseResultChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param proposedEmpID
      @param ds
   */  
export interface CourseSchAttdEmpIDChanging_input{
   proposedEmpID:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface CourseSchAttdEmpIDChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param proposedCustID
      @param ds
   */  
export interface CourseSchCustIDChanging_input{
   proposedCustID:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface CourseSchCustIDChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param proposedEmpID
      @param ds
   */  
export interface CourseSchEmpIDChanging_input{
   proposedEmpID:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface CourseSchEmpIDChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param proposedSupplierID
      @param ds
   */  
export interface CourseSchSupplierIDChanging_input{
   proposedSupplierID:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface CourseSchSupplierIDChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param courseID
      @param revisionCode
      @param startDate
      @param endDate
   */  
export interface DeleteByID_input{
   courseID:string,
   revisionCode:string,
   startDate:string,
   endDate:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CourseSchAttdAttchRow{
   Company:string,
   CourseID:string,
   RevisionCode:string,
   StartDate:string,
   EndDate:string,
   EmpID:string,
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

export interface Erp_Tablesets_CourseSchAttdRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Training Course ID.  */  
   CourseID:string,
      /**  The Course Revision Code.  */  
   RevisionCode:string,
      /**  The start date.  */  
   StartDate:string,
      /**  The end date.  */  
   EndDate:string,
      /**  The employee ID attending the course.  */  
   EmpID:string,
      /**  The cost of the training course materials for the employee.  */  
   MaterialCost:number,
      /**  The employee's expenses whilst attending the course.  */  
   Expenses:number,
      /**  This flag is used to indicate if the expenses have been reimbursed. Setting this field to true does NOT automatically pay the employee expenses.  */  
   CostReimbursed:boolean,
      /**  This will contain any Reason Code that has a Reason Code Type set to U - Course Result.  */  
   CourseResult:string,
      /**  This will default to value defined against the selected Course Result. If no Course Result is selected then this field will be set to false.  */  
   Passed:boolean,
      /**  The employee training course results comments.  */  
   Comments:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   EmpIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CourseSchListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Training Course ID.  */  
   CourseID:string,
      /**  The Course Revision Code.  */  
   RevisionCode:string,
      /**  The date that the training course is due to start. When a new schedule is created this will default to the current date.  */  
   StartDate:string,
      /**  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  */  
   EndDate:string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   ActStartDate:string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   ActEndDate:string,
      /**  The free format text to describe where the course will take place.  */  
   Location:string,
      /**  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  */  
   MaxAttendees:number,
      /**  The cost of the course per employee.  */  
   CourseCost:number,
      /**  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  */  
   InstrType:string,
      /**  The employee ID. Must be specified if InstrType = E.  */  
   EmpID:string,
      /**  The supplier ID. Must be specified if InstrType = S.  */  
   VendorNum:number,
      /**  The customer ID. Must be specified if InstrType = C.  */  
   CustNum:number,
      /**  The training course schedule comments.  */  
   Comments:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The full name of the customer.  */  
   CustNumName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustNumCustID:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpIDName:string,
      /**  The description of the training course revision.  */  
   RevisionCodeDescription:string,
      /**  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  */  
   RevisionCodeDurationType:string,
      /**  The duration of the course. When a new revision is created this will default to 1.  */  
   RevisionCodeDuration:number,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CourseSchListTableset{
   CourseSchList:Erp_Tablesets_CourseSchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CourseSchRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Training Course ID.  */  
   CourseID:string,
      /**  The Course Revision Code.  */  
   RevisionCode:string,
      /**  The date that the training course is due to start. When a new schedule is created this will default to the current date.  */  
   StartDate:string,
      /**  The date that the training course will end. This will default to a date that is calculated using the Duration and the Duration Type from the CourseRevision.  */  
   EndDate:string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   ActStartDate:string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   ActEndDate:string,
      /**  The free format text to describe where the course will take place.  */  
   Location:string,
      /**  The number that specifies the maximum number of attendees. If it is 0 then there is no limit to the number of attendees.  */  
   MaxAttendees:number,
      /**  The cost of the course per employee.  */  
   CourseCost:number,
      /**  The instructor type. Default = E. Possible values: E = Employee, S = Supplier, C = Customer.  */  
   InstrType:string,
      /**  The employee ID. Must be specified if InstrType = E.  */  
   EmpID:string,
      /**  The supplier ID. Must be specified if InstrType = S.  */  
   VendorNum:number,
      /**  The customer ID. Must be specified if InstrType = C.  */  
   CustNum:number,
      /**  The training course schedule comments.  */  
   Comments:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   EmpIDName:string,
   RevisionCodeDurationType:string,
   RevisionCodeDuration:number,
   RevisionCodeDescription:string,
   VendorNumVendorID:string,
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CourseSchTableset{
   CourseSch:Erp_Tablesets_CourseSchRow[],
   CourseSchAttd:Erp_Tablesets_CourseSchAttdRow[],
   CourseSchAttdAttch:Erp_Tablesets_CourseSchAttdAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCourseSchTableset{
   CourseSch:Erp_Tablesets_CourseSchRow[],
   CourseSchAttd:Erp_Tablesets_CourseSchAttdRow[],
   CourseSchAttdAttch:Erp_Tablesets_CourseSchAttdAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param courseID
      @param revisionCode
      @param startDate
      @param endDate
   */  
export interface GetByID_input{
   courseID:string,
   revisionCode:string,
   startDate:string,
   endDate:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CourseSchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CourseSchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CourseSchTableset[],
}

export interface GetInstrTypes_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_CourseSchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param courseID
      @param revisionCode
      @param startDate
      @param endDate
      @param empID
   */  
export interface GetNewCourseSchAttdAttch_input{
   ds:Erp_Tablesets_CourseSchTableset[],
   courseID:string,
   revisionCode:string,
   startDate:string,
   endDate:string,
   empID:string,
}

export interface GetNewCourseSchAttdAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param ds
      @param courseID
      @param revisionCode
      @param startDate
      @param endDate
   */  
export interface GetNewCourseSchAttd_input{
   ds:Erp_Tablesets_CourseSchTableset[],
   courseID:string,
   revisionCode:string,
   startDate:string,
   endDate:string,
}

export interface GetNewCourseSchAttd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param ds
      @param courseID
      @param revisionCode
      @param startDate
   */  
export interface GetNewCourseSch_input{
   ds:Erp_Tablesets_CourseSchTableset[],
   courseID:string,
   revisionCode:string,
   startDate:string,
}

export interface GetNewCourseSch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param whereClauseCourseSch
      @param whereClauseCourseSchAttd
      @param whereClauseCourseSchAttdAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCourseSch:string,
   whereClauseCourseSchAttd:string,
   whereClauseCourseSchAttdAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CourseSchTableset[],
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
      @param proposedInstrType
      @param ds
   */  
export interface InstrTypeChanged_input{
      /**  The proposed Instructor Type  */  
   proposedInstrType:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface InstrTypeChanged_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param proposedStartDate
      @param ds
   */  
export interface OnStartDateChanging_input{
      /**  The proposed Start Date  */  
   proposedStartDate:string,
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface OnStartDateChanging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCourseSchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCourseSchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CourseSchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CourseSchTableset[],
}
}

