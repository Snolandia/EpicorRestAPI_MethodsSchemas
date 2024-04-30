import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.EmpCourseSvc
// Description: Business object for Employee Training Course Maintenance.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/$metadata", {
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

   /**  
   Summary: Calls GetRows for the service
   Description: Get EmpCourses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCourses
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseRow
   */  
export function get_EmpCourses(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCourses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EmpCourseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpCourses(requestBody:Erp_Tablesets_EmpCourseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpCourse item
   Description: Calls GetByID to retrieve the EmpCourse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EmpCourseRow
   */  
export function get_EmpCourses_Company_EmpCourseID(Company:string, EmpCourseID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpCourseRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")", {
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
         resolve(data as Erp_Tablesets_EmpCourseRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpCourse for the service
   Description: Calls UpdateExt to update EmpCourse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCourse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCourseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpCourses_Company_EmpCourseID(Company:string, EmpCourseID:string, requestBody:Erp_Tablesets_EmpCourseRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete EmpCourse item
   Description: Call UpdateExt to delete EmpCourse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCourse
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpCourses_Company_EmpCourseID(Company:string, EmpCourseID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")", {
          method: 'delete',
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

   /**  
   Summary: Calls GetByID for the service
   Description: Get EmpCourseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpCourseAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseAttchRow
   */  
export function get_EmpCourses_Company_EmpCourseID_EmpCourseAttches(Company:string, EmpCourseID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")/EmpCourseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpCourseAttch item
   Description: Calls GetByID to retrieve the EmpCourseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourseAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   */  
export function get_EmpCourses_Company_EmpCourseID_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company:string, EmpCourseID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpCourseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourses(" + Company + "," + EmpCourseID + ")/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EmpCourseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EmpCourseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpCourseAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseAttchRow
   */  
export function get_EmpCourseAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpCourseAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EmpCourseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EmpCourseAttches(requestBody:Erp_Tablesets_EmpCourseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches", {
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EmpCourseAttch item
   Description: Calls GetByID to retrieve the EmpCourseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpCourseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   */  
export function get_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company:string, EmpCourseID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EmpCourseAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_EmpCourseAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EmpCourseAttch for the service
   Description: Calls UpdateExt to update EmpCourseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpCourseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpCourseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company:string, EmpCourseID:string, DrawingSeq:string, requestBody:Erp_Tablesets_EmpCourseAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")", {
          method: 'patch',
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
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Call UpdateExt to delete EmpCourseAttch item
   Description: Call UpdateExt to delete EmpCourseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpCourseAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param EmpCourseID Desc: EmpCourseID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EmpCourseAttches_Company_EmpCourseID_DrawingSeq(Company:string, EmpCourseID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/EmpCourseAttches(" + Company + "," + EmpCourseID + "," + DrawingSeq + ")", {
          method: 'delete',
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpCourseListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseListRow)
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
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseEmpCourse:string, whereClauseEmpCourseAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseEmpCourse!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpCourse=" + whereClauseEmpCourse
   }
   if(typeof whereClauseEmpCourseAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEmpCourseAttch=" + whereClauseEmpCourseAttch
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

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetRows" + params, {
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
         resolve(data as GetRows_output)
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(empCourseID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof empCourseID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "empCourseID=" + empCourseID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetByID" + params, {
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
         resolve(data as GetByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetList" + params, {
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
         resolve(data as GetList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateMultiRequest
   Description: Creates an Employee Course Request for multiple employees.
   OperationID: CreateMultiRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateMultiRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMultiRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateMultiRequest(requestBody:CreateMultiRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateMultiRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/CreateMultiRequest", {
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
         resolve(data as CreateMultiRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangedEmpCourseCourseStatus
   Description: Invoked after CourseStatus has been changed to update Dates/Costs etc
   OperationID: OnChangedEmpCourseCourseStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangedEmpCourseCourseStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedEmpCourseCourseStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedEmpCourseCourseStatus(requestBody:OnChangedEmpCourseCourseStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangedEmpCourseCourseStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/OnChangedEmpCourseCourseStatus", {
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
         resolve(data as OnChangedEmpCourseCourseStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingEmpCourseCourseIDRevisionCode
   Description: Invoked on changing of CourseID or RevisionCode
   OperationID: OnChangingEmpCourseCourseIDRevisionCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingEmpCourseCourseIDRevisionCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEmpCourseCourseIDRevisionCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingEmpCourseCourseIDRevisionCode(requestBody:OnChangingEmpCourseCourseIDRevisionCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingEmpCourseCourseIDRevisionCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/OnChangingEmpCourseCourseIDRevisionCode", {
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
         resolve(data as OnChangingEmpCourseCourseIDRevisionCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingEmpCourseCourseResult
   Description: Invoked on change on CourseResult
   OperationID: OnChangingEmpCourseCourseResult
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingEmpCourseCourseResult_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEmpCourseCourseResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingEmpCourseCourseResult(requestBody:OnChangingEmpCourseCourseResult_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingEmpCourseCourseResult_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/OnChangingEmpCourseCourseResult", {
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
         resolve(data as OnChangingEmpCourseCourseResult_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnCourseStatusChanging
   OperationID: OnCourseStatusChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnCourseStatusChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCourseStatusChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnCourseStatusChanging(requestBody:OnCourseStatusChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnCourseStatusChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/OnCourseStatusChanging", {
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
         resolve(data as OnCourseStatusChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateEmpID
   Description: ValidateEmpID
   OperationID: ValidateEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateEmpID(requestBody:ValidateEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/ValidateEmpID", {
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
         resolve(data as ValidateEmpID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCourseStatuses
   OperationID: GetCourseStatuses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCourseStatuses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCourseStatuses(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCourseStatuses_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetCourseStatuses", {
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
         resolve(data as GetCourseStatuses_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExpiresOn
   OperationID: GetExpiresOn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExpiresOn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExpiresOn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExpiresOn(requestBody:GetExpiresOn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExpiresOn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetExpiresOn", {
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
         resolve(data as GetExpiresOn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRevisionData
   Description: Gets the Description and Duration data for a given course.
   OperationID: GetRevisionData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRevisionData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevisionData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRevisionData(requestBody:GetRevisionData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRevisionData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetRevisionData", {
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
         resolve(data as GetRevisionData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEmpCourse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCourse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEmpCourse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCourse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpCourse(requestBody:GetNewEmpCourse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEmpCourse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetNewEmpCourse", {
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
         resolve(data as GetNewEmpCourse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEmpCourseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpCourseAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEmpCourseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpCourseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEmpCourseAttch(requestBody:GetNewEmpCourseAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEmpCourseAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetNewEmpCourseAttch", {
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
         resolve(data as GetNewEmpCourseAttch_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:DeleteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/DeleteByID", {
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
         resolve(data as DeleteByID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetBySysRowID" + params, {
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
         resolve(data as GetBySysRowID_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
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

   return (new Promise<GetBySysRowIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/GetBySysRowIDs" + params, {
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
         resolve(data as GetBySysRowIDs_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:Update_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Update_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/Update", {
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
         resolve(data as Update_output)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:UpdateExt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateExt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.EmpCourseSvc/UpdateExt", {
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
         resolve(data as UpdateExt_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpCourseAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpCourseListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpCourseRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EmpCourseRow,
}

export interface Erp_Tablesets_EmpCourseAttchRow{
   "Company":string,
   "EmpCourseID":number,
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

export interface Erp_Tablesets_EmpCourseListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The technical identifier.  */  
   "EmpCourseID":number,
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
      /**  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  */  
   "CourseStatus":string,
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
      /**  Shows when course expires for employee.  */  
   "ExpiresOn":string,
      /**  The description of the Training Course.  */  
   "CourseIDDescription":string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   "CourseSchActEndDate":string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   "CourseSchActStartDate":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpIDName":string,
      /**  Home phone number  */  
   "EmpIDPhone":string,
      /**  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  */  
   "RevisionCodeExpiresIn":number,
      /**  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  */  
   "RevisionCodeDurationType":string,
      /**  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  */  
   "RevisionCodeExpirationType":string,
      /**  The description of the training course revision.  */  
   "RevisionCodeDescription":string,
      /**  The duration of the course. When a new revision is created this will default to 1.  */  
   "RevisionCodeDuration":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EmpCourseRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The technical identifier.  */  
   "EmpCourseID":number,
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
      /**  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  */  
   "CourseStatus":string,
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
      /**  Shows when course expires for employee.  */  
   "ExpiresOn":string,
      /**  Flag to indicate if the course has expired  */  
   "Expired":boolean,
   "BitFlag":number,
   "CourseIDDescription":string,
   "CourseSchActStartDate":string,
   "CourseSchActEndDate":string,
   "EmpIDSupervisorID":string,
   "EmpIDPhone":string,
   "EmpIDName":string,
   "ReasonDescription":string,
   "RevisionCodeExpiresIn":number,
   "RevisionCodeDurationType":string,
   "RevisionCodeDescription":string,
   "RevisionCodeExpirationType":string,
   "RevisionCodeDuration":number,
      /**  RowMod  */  
   "RowMod":string,
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
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param courseID
      @param revisionCode
      @param empIDs
   */  
export interface CreateMultiRequest_input{
      /**  The course for which the employees are requesting.  */  
   courseID:string,
      /**  The course's revision.  */  
   revisionCode:string,
      /**  A list of EmpIDs that represent the employees requesting the course.  */  
   empIDs:string,
}

export interface CreateMultiRequest_output{
}

   /** Required : 
      @param empCourseID
   */  
export interface DeleteByID_input{
   empCourseID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_EmpCourseAttchRow{
   Company:string,
   EmpCourseID:number,
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

export interface Erp_Tablesets_EmpCourseListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The technical identifier.  */  
   EmpCourseID:number,
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
      /**  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  */  
   CourseStatus:string,
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
      /**  Shows when course expires for employee.  */  
   ExpiresOn:string,
      /**  The description of the Training Course.  */  
   CourseIDDescription:string,
      /**  The date that the training course actually ended. This will default to the End Date.  */  
   CourseSchActEndDate:string,
      /**  The date that the training course actually started. This will default to the Start Date.  */  
   CourseSchActStartDate:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpIDName:string,
      /**  Home phone number  */  
   EmpIDPhone:string,
      /**  The number which indicates the expiration period. This will default to 0 which indicates that the training course never expires.  */  
   RevisionCodeExpiresIn:number,
      /**  The duration type. Default = D. Possible values: H = Hours, D = Days, W = Weeks, M = Months.  */  
   RevisionCodeDurationType:string,
      /**  The expiration type. Default = Y. Possible values: M = Months, Y = Years.  */  
   RevisionCodeExpirationType:string,
      /**  The description of the training course revision.  */  
   RevisionCodeDescription:string,
      /**  The duration of the course. When a new revision is created this will default to 1.  */  
   RevisionCodeDuration:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpCourseListTableset{
   EmpCourseList:Erp_Tablesets_EmpCourseListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EmpCourseRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The technical identifier.  */  
   EmpCourseID:number,
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
      /**  The employee course status. Default = R. Possible values: R = Requested, P = Planned, F = Firm, A = Attended.  */  
   CourseStatus:string,
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
      /**  Shows when course expires for employee.  */  
   ExpiresOn:string,
      /**  Flag to indicate if the course has expired  */  
   Expired:boolean,
   BitFlag:number,
   CourseIDDescription:string,
   CourseSchActStartDate:string,
   CourseSchActEndDate:string,
   EmpIDSupervisorID:string,
   EmpIDPhone:string,
   EmpIDName:string,
   ReasonDescription:string,
   RevisionCodeExpiresIn:number,
   RevisionCodeDurationType:string,
   RevisionCodeDescription:string,
   RevisionCodeExpirationType:string,
   RevisionCodeDuration:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EmpCourseTableset{
   EmpCourse:Erp_Tablesets_EmpCourseRow[],
   EmpCourseAttch:Erp_Tablesets_EmpCourseAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtEmpCourseTableset{
   EmpCourse:Erp_Tablesets_EmpCourseRow[],
   EmpCourseAttch:Erp_Tablesets_EmpCourseAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param empCourseID
   */  
export interface GetByID_input{
   empCourseID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_EmpCourseTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_EmpCourseTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_EmpCourseTableset[],
}

export interface GetCourseStatuses_output{
   returnObj:string,
}

   /** Required : 
      @param CourseStatus
      @param CourseID
      @param RevisionCode
      @param StartDate
      @param EndDate
   */  
export interface GetExpiresOn_input{
   CourseStatus:string,
   CourseID:string,
   RevisionCode:string,
   StartDate:string,
   EndDate:string,
}

export interface GetExpiresOn_output{
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
   returnObj:Erp_Tablesets_EmpCourseListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param empCourseID
   */  
export interface GetNewEmpCourseAttch_input{
   ds:Erp_Tablesets_EmpCourseTableset[],
   empCourseID:number,
}

export interface GetNewEmpCourseAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewEmpCourse_input{
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface GetNewEmpCourse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param CourseID
      @param RevisionCode
      @param ds
   */  
export interface GetRevisionData_input{
   CourseID:string,
   RevisionCode:string,
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface GetRevisionData_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param whereClauseEmpCourse
      @param whereClauseEmpCourseAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseEmpCourse:string,
   whereClauseEmpCourseAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_EmpCourseTableset[],
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
   */  
export interface OnChangedEmpCourseCourseStatus_input{
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface OnChangedEmpCourseCourseStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param courseID
      @param revisionCode
      @param ds
   */  
export interface OnChangingEmpCourseCourseIDRevisionCode_input{
   courseID:string,
   revisionCode:string,
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface OnChangingEmpCourseCourseIDRevisionCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param reasonCode
      @param ds
   */  
export interface OnChangingEmpCourseCourseResult_input{
   reasonCode:string,
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface OnChangingEmpCourseCourseResult_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param pcCompany
      @param pcEmpCourseID
      @param pcCourseStatus
      @param pcDeleteCourseSchAttdResponse
   */  
export interface OnCourseStatusChanging_input{
   pcCompany:string,
   pcEmpCourseID:number,
   pcCourseStatus:string,
   pcDeleteCourseSchAttdResponse:string,
}

export interface OnCourseStatusChanging_output{
parameters : {
      /**  output parameters  */  
   pcQuestion:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtEmpCourseTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtEmpCourseTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_EmpCourseTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_EmpCourseTableset,
}
}

   /** Required : 
      @param EmpID
   */  
export interface ValidateEmpID_input{
   EmpID:string,
}

export interface ValidateEmpID_output{
}

