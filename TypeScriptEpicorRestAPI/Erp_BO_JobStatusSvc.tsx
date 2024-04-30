import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.JobStatusSvc
// Description: The JobStatus main object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/$metadata", {
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
   Description: Get JobStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobStatus
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadRow
   */  
export function get_JobStatus(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobStatus(requestBody:Erp_Tablesets_JobHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus", {
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
   Summary: Calls GetByID to retrieve the JobStatu item
   Description: Calls GetByID to retrieve the JobStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobHeadRow
   */  
export function get_JobStatus_Company_JobNum(Company:string, JobNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")", {
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
         resolve(data as Erp_Tablesets_JobHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobStatu for the service
   Description: Calls UpdateExt to update JobStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobStatus_Company_JobNum(Company:string, JobNum:string, requestBody:Erp_Tablesets_JobHeadRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")", {
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
   Summary: Call UpdateExt to delete JobStatu item
   Description: Call UpdateExt to delete JobStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobStatu
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobStatus_Company_JobNum(Company:string, JobNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")", {
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
   Description: Get JobAsmbls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JobAsmbls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   */  
export function get_JobStatus_Company_JobNum_JobAsmbls(Company:string, JobNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobAsmbls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JobAsmbl item
   Description: Calls GetByID to retrieve the JobAsmbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmbl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobAsmblRow
   */  
export function get_JobStatus_Company_JobNum_JobAsmbls_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
         resolve(data as Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get JobMtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JobMtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   */  
export function get_JobStatus_Company_JobNum_JobMtls(Company:string, JobNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobMtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JobMtl item
   Description: Calls GetByID to retrieve the JobMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobMtlRow
   */  
export function get_JobStatus_Company_JobNum_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobStatus(" + Company + "," + JobNum + ")/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get JobAsmbls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobAsmbls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobAsmblRow
   */  
export function get_JobAsmbls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobAsmbls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobAsmblRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobAsmbls(requestBody:Erp_Tablesets_JobAsmblRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls", {
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
   Summary: Calls GetByID to retrieve the JobAsmbl item
   Description: Calls GetByID to retrieve the JobAsmbl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobAsmbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobAsmblRow
   */  
export function get_JobAsmbls_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobAsmblRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
         resolve(data as Erp_Tablesets_JobAsmblRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobAsmbl for the service
   Description: Calls UpdateExt to update JobAsmbl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobAsmbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobAsmblRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobAsmbls_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, requestBody:Erp_Tablesets_JobAsmblRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
   Summary: Call UpdateExt to delete JobAsmbl item
   Description: Call UpdateExt to delete JobAsmbl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobAsmbl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobAsmbls_Company_JobNum_AssemblySeq(Company:string, JobNum:string, AssemblySeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobAsmbls(" + Company + "," + JobNum + "," + AssemblySeq + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get JobMtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JobMtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobMtlRow
   */  
export function get_JobMtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JobMtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JobMtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JobMtls(requestBody:Erp_Tablesets_JobMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls", {
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
   Summary: Calls GetByID to retrieve the JobMtl item
   Description: Calls GetByID to retrieve the JobMtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JobMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JobMtlRow
   */  
export function get_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JobMtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
         resolve(data as Erp_Tablesets_JobMtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JobMtl for the service
   Description: Calls UpdateExt to update JobMtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JobMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JobMtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, requestBody:Erp_Tablesets_JobMtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
   Summary: Call UpdateExt to delete JobMtl item
   Description: Call UpdateExt to delete JobMtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JobMtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param JobNum Desc: JobNum   Required: True   Allow empty value : True
      @param AssemblySeq Desc: AssemblySeq   Required: True
      @param MtlSeq Desc: MtlSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JobMtls_Company_JobNum_AssemblySeq_MtlSeq(Company:string, JobNum:string, AssemblySeq:string, MtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/JobMtls(" + Company + "," + JobNum + "," + AssemblySeq + "," + MtlSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JobHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseJobHead:string, whereClauseJobAsmbl:string, whereClauseJobMtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseJobHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobHead=" + whereClauseJobHead
   }
   if(typeof whereClauseJobAsmbl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
   }
   if(typeof whereClauseJobMtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJobMtl=" + whereClauseJobMtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(jobNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof jobNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "jobNum=" + jobNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetList" + params, {
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
   Summary: Invoke method AutoAllocateJobMtl
   Description: This method allocates any selected job materials
   OperationID: AutoAllocateJobMtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoAllocateJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoAllocateJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoAllocateJobMtl(requestBody:AutoAllocateJobMtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoAllocateJobMtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/AutoAllocateJobMtl", {
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
         resolve(data as AutoAllocateJobMtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AutoReserveJobMtl
   Description: This method reserves any selected job materials
   OperationID: AutoReserveJobMtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AutoReserveJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoReserveJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AutoReserveJobMtl(requestBody:AutoReserveJobMtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AutoReserveJobMtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/AutoReserveJobMtl", {
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
         resolve(data as AutoReserveJobMtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobHeadFirm
   Description: This method validates the JobHead.JobFirm and potentially changes the jobreleased
fields.
This method should run when the JobHead.JobFirm field changes.
   OperationID: ChangeJobHeadFirm
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadFirm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadFirm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobHeadFirm(requestBody:ChangeJobHeadFirm_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobHeadFirm_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/ChangeJobHeadFirm", {
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
         resolve(data as ChangeJobHeadFirm_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobHeadJobEngineered
   Description: This method validates the JobHead.JobEngineered and potentially changes the jobreleased field.
This method should run when the JobHead.JobEngineered field changes.
   OperationID: ChangeJobHeadJobEngineered
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadJobEngineered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadJobEngineered_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobHeadJobEngineered(requestBody:ChangeJobHeadJobEngineered_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobHeadJobEngineered_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/ChangeJobHeadJobEngineered", {
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
         resolve(data as ChangeJobHeadJobEngineered_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobHeadJobReleased
   Description: This method validates the JobHead.JobReleased and potentially changes the jobengineered
and/or jobfirm fields.
This method should run when the JobHead.JobReleased field changes.
   OperationID: ChangeJobHeadJobReleased
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobHeadJobReleased_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobHeadJobReleased_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobHeadJobReleased(requestBody:ChangeJobHeadJobReleased_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobHeadJobReleased_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/ChangeJobHeadJobReleased", {
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
         resolve(data as ChangeJobHeadJobReleased_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDJobMtl
   Description: Performs the standard GetByID and includes any related job materials
   OperationID: GetByIDJobMtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDJobMtl(requestBody:GetByIDJobMtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDJobMtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetByIDJobMtl", {
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
         resolve(data as GetByIDJobMtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListFromSelectedKeys
   Description: This methods will return all of the JobHeadSearch records which will be a subset
of the JobHead records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: GetListFromSelectedKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListFromSelectedKeys(requestBody:GetListFromSelectedKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListFromSelectedKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetListFromSelectedKeys", {
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
         resolve(data as GetListFromSelectedKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsFromSelectedKeys
   Description: This methods will return all of the JobHeadSearch records which will be a subset
of the JobHead records that meet the selection criteria.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: GetRowsFromSelectedKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsFromSelectedKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFromSelectedKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsFromSelectedKeys(requestBody:GetRowsFromSelectedKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsFromSelectedKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetRowsFromSelectedKeys", {
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
         resolve(data as GetRowsFromSelectedKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MassUpdate
   Description: Call this method to update multiple JobHead records.
   OperationID: MassUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MassUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MassUpdate(requestBody:MassUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MassUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/MassUpdate", {
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
         resolve(data as MassUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobHead
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobHead(requestBody:GetNewJobHead_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobHead_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetNewJobHead", {
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
         resolve(data as GetNewJobHead_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJobAsmbl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJobAsmbl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmbl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmbl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJobAsmbl(requestBody:GetNewJobAsmbl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJobAsmbl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetNewJobAsmbl", {
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
         resolve(data as GetNewJobAsmbl_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.JobStatusSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobAsmblRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobAsmblRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobHeadRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JobMtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JobMtlRow,
}

export interface Erp_Tablesets_JobAsmblRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   "JobComplete":boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   "JobNum":string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   "AssemblySeq":number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   "PartNum":string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   "Description":string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   "QtyPer":number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   "IUM":string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   "RequiredQty":number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   "PullQty":number,
      /**  This is the warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  The material burden rate for this Job Assembly.  */  
   "MtlBurRate":number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   "EstUnitCost":number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   "EstMtlBurUnitCost":number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   "OverRunQty":number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "StartHour":number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Sequence number of the Parent Assembly.  */  
   "Parent":number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   "PriorPeer":number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   "NextPeer":number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   "Child":number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   "TotalCost":number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   "MtlBurCost":number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   "IssuedQty":number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   "DrawNum":string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Editor widget for Job Assembly comments.  */  
   "CommentText":string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   "BomSequence":number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   "BomLevel":number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   "WIStartHour":number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**  This Level Actual Labor Cost.  */  
   "TLALaborCost":number,
      /**  This Level Actual Burden Cost.  */  
   "TLABurdenCost":number,
      /**  This Level Actual Material Cost.  */  
   "TLAMaterialCost":number,
      /**  This Level Actual Subcontract Cost.  */  
   "TLASubcontractCost":number,
      /**  This Level Actual Material Burden Cost.  */  
   "TLAMtlBurCost":number,
      /**  This Level Actual Setup Hours.  */  
   "TLASetupHours":number,
      /**  This Level Actual Production Hours.  */  
   "TLAProdHours":number,
      /**  This Level Estimated Labor Cost.  */  
   "TLELaborCost":number,
      /**  This Level Estimated Burden Cost.  */  
   "TLEBurdenCost":number,
      /**  This Level Estimated Material Cost.  */  
   "TLEMaterialCost":number,
      /**  This Level Estimated Subcontract Cost.  */  
   "TLESubcontractCost":number,
      /**  This Level Estimated Material Burden Cost.  */  
   "TLEMtlBurCost":number,
      /**  This Level Estimated Setup Hours.  */  
   "TLESetupHours":number,
      /**  This Level Estimated Production Hours.  */  
   "TLEProdHours":number,
      /**  Lower Level Actual Labor Cost.  */  
   "LLALaborCost":number,
      /**  Lower Level Burden Labor Cost.  */  
   "LLABurdenCost":number,
      /**  Lower Level Actual Material Cost.  */  
   "LLAMaterialCost":number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   "LLASubcontractCost":number,
      /**  Lower Level Actual Material Burden Cost.  */  
   "LLAMtlBurCost":number,
      /**  Lower Level Actual Setup Hours.  */  
   "LLASetupHours":number,
      /**  Lower Level Actual Production Hours.  */  
   "LLAProdHours":number,
      /**  Lower Level Estimated Labor Cost.  */  
   "LLELaborCost":number,
      /**  Lower Level Estimated Burden Cost.  */  
   "LLEBurdenCost":number,
      /**  Lower Level Estimated Material Cost.  */  
   "LLEMaterialCost":number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   "LLESubcontractCost":number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   "LLEMtlBurCost":number,
      /**  Lower Level Estimated Setup Hours.  */  
   "LLESetupHours":number,
      /**  Lower Level Estimated Production Hours.  */  
   "LLEProdHours":number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   "AutoRecOpr":number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   "FinalOpr":number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   "FindNum":string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   "ReceivedToStock":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   "Direct":boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   "RelatedOperation":number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialLabCost":number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialMtlCost":number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialSubCost":number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   "TLAMaterialBurCost":number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialLabCost":number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialMtlCost":number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialSubCost":number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   "LLAMaterialBurCost":number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "TotalMtlMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlSubCost":number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "TotalMtlBurCost":number,
      /**  The service call that this assembly belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this assembly relates to.  */  
   "CallLine":number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  The date when the configuration was completed for the assembly.  */  
   "LastConfigDate":string,
      /**  The system time when the configuration was completed for the assembly.  */  
   "LastConfigTime":number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   "LastConfigUserID":string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigRequiredQty":number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   "TLAMaterialMtlBurCost":number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   "LLAMaterialMtlBurCost":number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompLabCost":number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlCost":number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompSubCost":number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompBurCost":number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   "TLAMfgCompMtlBurCost":number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompLabCost":number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlCost":number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompSubCost":number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompBurCost":number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   "LLAMfgCompMtlBurCost":number,
      /**  Assembly Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Original Material Sequence. Used in the configurator.  */  
   "OrigMtlSeq":number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   "OrigRuleTag":string,
      /**  Validate Reference Designators.  */  
   "ValRefDes":boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   "PlanAsAsm":boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   "PAARef":string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   "PAAFirm":boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   "EstScrap":number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   "EstScrapType":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Reassign Serial Numbers Assembly  */  
   "ReassignSNAsm":boolean,
      /**  This Level Actual Other Direct Cost.  */  
   "TLAODCCost":number,
      /**  AssemblyMatch  */  
   "AssemblyMatch":string,
      /**  JdfStatus  */  
   "JdfStatus":string,
      /**  PressDevice  */  
   "PressDevice":string,
      /**  DigitalFileName  */  
   "DigitalFileName":string,
      /**  PrepressJobName  */  
   "PrepressJobName":string,
      /**  JdfPrepressAction  */  
   "JdfPrepressAction":string,
      /**  SendToPress  */  
   "SendToPress":boolean,
      /**  RemovedFromPlan  */  
   "RemovedFromPlan":boolean,
      /**  SendToPressInitiator  */  
   "SendToPressInitiator":number,
      /**  OperationType  */  
   "OperationType":number,
      /**  SendToPrePress  */  
   "SendToPrePress":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PartPlanInfo  */  
   "PartPlanInfo":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   "LinkToContract":boolean,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Calculated Available Quantity  */  
   "AvailableQty":number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bUseAvailQty":boolean,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   "ChildAssemblySeq":number,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   "DispIUM":string,
      /**  The order JobAsmbl records should be displayed.  */  
   "DisplayOrder":number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableAsmSplitCosts":boolean,
   "EnableMtlSalvage":boolean,
   "EnablePurDir":boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   "FirmProcess":boolean,
      /**  External field for EQSyst GetCostsFromInventory  */  
   "GetCostsFromInventory":boolean,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   "GetCostsFromTemplate":boolean,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   "ParentAssemblySeq":number,
      /**  Parent Description  */  
   "ParentDescription":string,
      /**  Parent PartNum  */  
   "ParentPartNum":string,
      /**  Parent RevisionNum  */  
   "ParentRev":string,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   "PartExists":boolean,
   "PartmasterPart":boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  Related Operation Description  */  
   "RelatedOperationDesc":string,
      /**  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  */  
   "ShowWarningBOMResequence":boolean,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   "AddAsmAs":string,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   "bAvailQty":number,
   "EnableAttributeSetSearch":boolean,
   "AttributeSetShortDescription":string,
   "AttributeSetDescription":string,
   "AttrClassID":string,
      /**  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  */  
   "TLATotalCost":number,
      /**  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  */  
   "TLETotalCost":number,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetShortDescription":string,
   "DynAttrValueSetDescription":string,
   "JobNumPartDescription":string,
   "PartNumIUM":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackLots":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PlantName":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobHeadListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   "ProductionYield":boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   "EquipID":string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   "PlanNum":number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  PersonIDName  */  
   "PersonIDName":string,
   "SOExists":boolean,
      /**  Part Description  */  
   "PartNumPartDescription":string,
      /**  Track Dimension  */  
   "PartNumTrackDimension":boolean,
      /**  Track Lots  */  
   "PartNumTrackLots":boolean,
      /**  Track Serial Num  */  
   "PartNumTrackSerialNum":boolean,
   "EquipOEM":string,
   "EquipModel":string,
   "EquipTypeID":string,
   "EquipLocID":string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   "PMJob":boolean,
   "EquipDescription":string,
   "JobTypeName":string,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
      /**  ID of related Attribute Class  */  
   "AttrClassID":string,
      /**  Description of values in set  */  
   "AttrDescription":string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   "ShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   "JobClosed":boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   "ClosedDate":string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   "JobComplete":boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   "JobCompletionDate":string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   "JobEngineered":boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff1":boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff2":boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff3":boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff4":boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   "CheckOff5":boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   "JobReleased":boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   "JobHeld":boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   "SchedStatus":string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   "JobNum":string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   "PartNum":string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   "DrawNum":string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   "PartDescription":string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   "ProdQty":number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   "IUM":string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "StartDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "StartHour":number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "DueDate":string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "DueHour":number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   "ReqDueDate":string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   "JobCode":string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   "QuoteNum":number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   "QuoteLine":number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  UserChar1  */  
   "UserChar1":string,
      /**  UserChar2  */  
   "UserChar2":string,
      /**  UserChar3  */  
   "UserChar3":string,
      /**  UserChar4  */  
   "UserChar4":string,
      /**  UserDate1  */  
   "UserDate1":string,
      /**  UserDate2  */  
   "UserDate2":string,
      /**  UserDate3  */  
   "UserDate3":string,
      /**  UserDate4  */  
   "UserDate4":string,
      /**  UserDecimal1  */  
   "UserDecimal1":number,
      /**  UserDecimal2  */  
   "UserDecimal2":number,
      /**  UserInteger1  */  
   "UserInteger1":number,
      /**  UserInteger2  */  
   "UserInteger2":number,
      /**  Editor widget for Job header comments.  */  
   "CommentText":string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   "ExpenseCode":string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   "InCopyList":boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   "WIName":string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   "WIStartDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   "WIStartHour":number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   "WIDueDate":string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   "WIDueHour":number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   "Candidate":boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   "SchedCode":string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   "SchedLocked":boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   "ProjectID":string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   "WIPCleared":boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   "JobFirm":boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   "PersonList":string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   "PersonID":string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   "ProdTeamID":string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   "QtyCompleted":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   "DatePurged":string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   "TravelerReadyToPrint":boolean,
      /**  The last date the job traveler was mass printed.  */  
   "TravelerLastPrinted":string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   "StatusReadyToPrint":boolean,
      /**  The last date the job status was mass printed.  */  
   "StatusLastPrinted":string,
      /**  The Service Call number that this Job is linked to.  */  
   "CallNum":number,
      /**  The Service Call Line that this Job is linked to.  */  
   "CallLine":number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   "JobType":string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   "RestoreFlag":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Indicates that the quantity on this job is locked  */  
   "LockQty":boolean,
      /**  The help desk case that created this job.  */  
   "HDCaseNum":number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   "ProcessMode":string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   "PlannedActionDate":string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   "PlannedKitDate":string,
      /**  The task ID that is returned from Microsoft Project.  */  
   "MSPTaskID":string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   "MSPPredecessor":string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   "UserMapData":string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   "ProductionYield":boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   "OrigProdQty":number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   "PreserveOrigQtys":boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   "NoAutoCompletion":boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   "NoAutoClosing":boolean,
      /**  The user that created this Job.  */  
   "CreatedBy":string,
      /**  The date that this Job was created.  */  
   "CreateDate":string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   "OwnershipStatus":string,
      /**  Holds the internal object id of PDM parts.  */  
   "PDMObjID":string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   "ExportRequested":string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   "SplitMfgCostElements":boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   "XRefPartNum":string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   "XRefPartType":string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   "XRefCustNum":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job was rough cut scheduled.  */  
   "RoughCutScheduled":boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   "EquipID":string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   "PlanNum":number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   "MaintPriority":string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   "SplitJob":boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   "NumberSource":boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   "CloseMeterReading":number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   "IssueTopicID1":string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   "IssueTopicID2":string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   "IssueTopicID3":string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   "IssueTopicID4":string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   "IssueTopicID5":string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   "IssueTopicID6":string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   "IssueTopicID7":string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   "IssueTopicID8":string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   "IssueTopicID9":string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   "IssueTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "IssueTopics":string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   "ResTopicID1":string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   "ResTopicID2":string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   "ResTopicID3":string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   "ResTopicID4":string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   "ResTopicID5":string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   "ResTopicID6":string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   "ResTopicID7":string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   "ResTopicID8":string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   "ResTopicID9":string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   "ResTopicID10":string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   "ResTopics":string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   "Forward":boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedSeq":number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   "PAAExists":boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   "DtlsWithinLeadTime":boolean,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   "RoughCut":boolean,
      /**  PlanGUID  */  
   "PlanGUID":string,
      /**  PlanUserID  */  
   "PlanUserID":string,
      /**  LastChangedBy  */  
   "LastChangedBy":string,
      /**  LastChangedOn  */  
   "LastChangedOn":string,
      /**  EPMExportLevel  */  
   "EPMExportLevel":number,
      /**  JobWorkflowState  */  
   "JobWorkflowState":string,
      /**  JobCSR  */  
   "JobCSR":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  LastExternalMESDate  */  
   "LastExternalMESDate":string,
      /**  LastScheduleDate  */  
   "LastScheduleDate":string,
      /**  LastScheduleProc  */  
   "LastScheduleProc":string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   "SchedPriority":number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   "DaysLate":number,
      /**  ContractID  */  
   "ContractID":string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   "ProjProcessed":boolean,
      /**  SyncReqBy  */  
   "SyncReqBy":boolean,
      /**  CustName  */  
   "CustName":string,
      /**  CustID  */  
   "CustID":string,
      /**  IsCSRSet  */  
   "IsCSRSet":boolean,
      /**  UnReadyCostProcess  */  
   "UnReadyCostProcess":boolean,
      /**  ProcSuspendedUpdates  */  
   "ProcSuspendedUpdates":string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   "ProjProcessedDate":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   "KBConfigProdID":number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   "UseAdvancedStaging":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  PersonIDName  */  
   "PersonIDName":string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  FSMSendTo  */  
   "FSMSendTo":boolean,
      /**  FSMServiceReportID  */  
   "FSMServiceReportID":string,
   "AdvanceLaborRate":boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   "dspReadyCostProcess":boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   "EnableJobEngineered":boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   "EnableJobFirm":boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   "EnableJobReleased":boolean,
   "EnableMaterialStatus":boolean,
   "EnableProject":boolean,
      /**  Is the job allowed to be engineered?  */  
   "EngineerAllowed":boolean,
   "EquipLocDesc":string,
      /**  If some fields except ToFirm have been updated  */  
   "ExtUpdated":boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   "FinalOpDueDate":string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   "FirmProcEnable":boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   "FirmProcess":boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   "HasPlanAsAsm":boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   "HeaderSensitive":boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   "IgnoreMtlConstraints":boolean,
   "JobTypeName":string,
      /**  If part is backflush the kit time is ignored.  */  
   "KitTime":number,
      /**  Locked Qty Flag  */  
   "LockedQty":boolean,
   "NewMeter":number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   "OldJobNum":string,
      /**  The order qty  */  
   "OrderQty":number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   "PartmasterPart":boolean,
   "PhaseDescription":string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   "PMJob":boolean,
      /**  Process Mode Description  */  
   "ProcessModeDescription":string,
      /**  Receive Time field for Job Part entered on Job  */  
   "ReceiveTime":number,
      /**  Original smart string passed in for configuration  */  
   "SmartString":string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   "SmartStringProcessed":boolean,
   "SOExists":boolean,
   "StockQty":number,
      /**  To be Firmed  */  
   "ToFirm":boolean,
      /**  Description for XRefPartType  */  
   "XRefPartTypeDesc":string,
      /**  The audit change description for the jobaudit record.  */  
   "ChangeDescription":string,
   "ClearDataset":boolean,
      /**  True if more than one co-part exists  */  
   "IsCoPart":boolean,
      /**  The identifier of related Process Manufacturing.  */  
   "PartRevProcessMfgID":string,
      /**  Type of Process Manufacturing.  */  
   "PartRevProcessMfgType":string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   "SendToFSA":boolean,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "EquipMeterUOM":string,
   "EquipSerialNum":string,
   "EquipLocID":string,
   "EquipPlant":string,
   "EquipDescription":string,
   "EquipBrand":string,
   "EquipModel":string,
   "EquipCurrentMeter":number,
   "EquipTypeID":string,
   "EquipOEM":string,
   "ExpenseCodeDescription":string,
   "HDCaseDescription":string,
   "IssueTopicID1Description":string,
   "IssueTopicID10Description":string,
   "IssueTopicID2Description":string,
   "IssueTopicID3Description":string,
   "IssueTopicID4Description":string,
   "IssueTopicID5Description":string,
   "IssueTopicID6Description":string,
   "IssueTopicID7Description":string,
   "IssueTopicID8Description":string,
   "IssueTopicID9Description":string,
   "PartNumSalesUM":string,
   "PartNumIUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumTrackDimension":boolean,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumLocationIDNumReq":boolean,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumAttrClassID":string,
   "PlantName":string,
   "PlantMaintPlant":string,
   "ProdCodeDescription":string,
   "ProdTeamIDDescription":string,
   "ProdTeamIDName":string,
   "ProjectIDDescription":string,
   "QuoteLineLineDesc":string,
   "QuoteNumCurrencyCode":string,
   "ResTopicID1Description":string,
   "ResTopicID10Description":string,
   "ResTopicID2Description":string,
   "ResTopicID3Description":string,
   "ResTopicID4Description":string,
   "ResTopicID5Description":string,
   "ResTopicID6Description":string,
   "ResTopicID7Description":string,
   "ResTopicID8Description":string,
   "ResTopicID9Description":string,
   "SchedCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JobMtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   "JobComplete":boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   "IssuedComplete":boolean,
      /**  Job Number.  */  
   "JobNum":string,
      /**  Assembly sequence number that this material is associated with.  */  
   "AssemblySeq":number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   "MtlSeq":number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   "PartNum":string,
      /**  A description of the material.  */  
   "Description":string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   "QtyPer":number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   "RequiredQty":number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   "IUM":string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   "LeadTime":number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   "RelatedOperation":number,
      /**  The material burden rate for this Job Material.  */  
   "MtlBurRate":number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstMtlBurUnitCost":number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   "EstUnitCost":number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   "IssuedQty":number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   "TotalCost":number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   "MtlBurCost":number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "ReqDate":string,
      /**  The warehouse that the material is allocated against.  */  
   "WarehouseCode":string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   "SalvagePartNum":string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   "SalvageDescription":string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   "SalvageQtyPer":number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   "SalvageUM":string,
      /**  The salvage material burden rate for this Job Material.  */  
   "SalvageMtlBurRate":number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageUnitCredit":number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   "SalvageEstMtlBurUnitCredit":number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   "SalvageQtyToDate":number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageCredit":number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   "SalvageMtlBurCredit":number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   "MfgComment":string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   "VendorNum":number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   "PurPoint":string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   "BuyIt":boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   "Ordered":boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   "PurComment":string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   "BackFlush":boolean,
      /**  Estimated Scrap.  */  
   "EstScrap":number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   "EstScrapType":string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   "FixedQty":boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   "FindNum":string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   "RevisionNum":string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   "SndAlrtCmpl":boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   "RcvInspectionReq":boolean,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   "Direct":boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   "MaterialMtlCost":number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialLabCost":number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialSubCost":number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   "MaterialBurCost":number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageMtlCredit":number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageLbrCredit":number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageBurCredit":number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   "SalvageSubCredit":number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   "APSAddResType":string,
      /**  The service call that this Material belongs to.  */  
   "CallNum":number,
      /**  The Service Call Line that this material relates to.  */  
   "CallLine":number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   "ProdCode":string,
      /**  FS - Unit Price for the Material in base currency.  */  
   "UnitPrice":number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   "BillableUnitPrice":number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   "DocBillableUnitPrice":number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   "PricePerCode":string,
      /**  Is this a billable material item.  */  
   "Billable":boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   "ShippedQty":number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   "DocUnitPrice":number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   "QtyStagedToDate":number,
      /**  This material was added after initial setup of the job  */  
   "AddedMtl":boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   "MiscCharge":boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   "MiscCode":string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   "SCMiscCode":string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   "RFQNeeded":boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   "RFQVendQuotes":number,
      /**  RFQ number that the item is linked to.  */  
   "RFQNum":number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   "RFQLine":number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   "RFQStat":string,
      /**  Analysis Code  */  
   "AnalysisCode":string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   "GlbRFQ":boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   "WhseAllocFlag":boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   "WIReqDate":string,
      /**  Reporting currency value of this field  */  
   "Rpt1BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3BillableUnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt1UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt2UnitPrice":number,
      /**  Reporting currency value of this field  */  
   "Rpt3UnitPrice":number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   "BaseRequiredQty":number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   "BaseUOM":string,
      /**  Material Weight defaulted from Part Master.  */  
   "Weight":number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   "WeightUOM":string,
      /**  Required number of designators  */  
   "ReqRefDes":number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   "BasePartNum":string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   "BaseRevisionNum":string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   "SelectForPicking":boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   "StagingWarehouseCode":string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   "StagingBinNum":string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   "PickError":string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstMtlUnitCost":number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstLbrUnitCost":number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstBurUnitCost":number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   "EstSubUnitCost":number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstMtlUnitCredit":number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstLbrUnitCredit":number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstBurUnitCredit":number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   "SalvageEstSubUnitCredit":number,
      /**  The material quantity that has been loaned out to another job.  */  
   "LoanedQty":number,
      /**  The material quantity that has been borrowed from another job.  */  
   "BorrowedQty":number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   "ReassignSNAsm":boolean,
      /**  GeneralPlanInfo  */  
   "GeneralPlanInfo":string,
      /**  EstStdDescription  */  
   "EstStdDescription":string,
      /**  PricingUOM  */  
   "PricingUOM":string,
      /**  RemovedFromPlan  */  
   "RemovedFromPlan":boolean,
      /**  IsPOCostingMaintained  */  
   "IsPOCostingMaintained":boolean,
      /**  EstStdType  */  
   "EstStdType":number,
      /**  POCostingFactor  */  
   "POCostingFactor":number,
      /**  PlannedQtyPerUnit  */  
   "PlannedQtyPerUnit":number,
      /**  POCostingDirection  */  
   "POCostingDirection":number,
      /**  POCostingUnitVal  */  
   "POCostingUnitVal":number,
      /**  GroupSeq  */  
   "GroupSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigStructTag":string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   "OrigGroupSeq":number,
      /**  ShowStatusIcon  */  
   "ShowStatusIcon":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   "LinkToContract":boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   "StagingLotNum":string,
      /**  PCLinkRemoved  */  
   "PCLinkRemoved":boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   "ExternalMESSyncRequired":boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   "ExternalMESLastSync":string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   "LocationView":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Planning number of pieces for this attribute set.  */  
   "PlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvageAttributeSetID":number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   "SalvagePlanningNumberOfPieces":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "SalvagePlanningAttributeSetID":number,
      /**  The identification of related StageNo.  */  
   "RelatedStage":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "SalvageRevisionNum":string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   "PartAllocQueueAction":string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   "ReadyToFulfill":boolean,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
      /**  The currency switch flag  */  
   "CurrencySwitch":boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**  The display of extended price.  */  
   "DisplayExtPrice":number,
      /**  The display unit price.  */  
   "DisplayUnitPrice":number,
      /**  The document display extended price  */  
   "DocDisplayExtPrice":number,
      /**  The document display extended price  */  
   "DocDisplayUnitPrice":number,
      /**  BuyIt field for display in the UI.  */  
   "dspBuyIt":boolean,
      /**  Display IUM (readonly)  */  
   "DspIUM":string,
      /**  Should the backflush field be enabled?  */  
   "EnableBackflush":boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   "EnableBuyIt":boolean,
      /**  flag to determine whether the Configure Option should be enabled.  */  
   "EnableConfigure":boolean,
      /**  flag to determine whether the Make Direct field should be enabled.  */  
   "EnableDirect":boolean,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   "EnableFixedQty":boolean,
   "EnableMtlSalvage":boolean,
   "EnablePurDir":boolean,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   "EnableRcvInspReq":boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   "EnableSndAlrtCmpl":boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   "EnableSplitCosts":boolean,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   "EstCost":number,
      /**  The name of the calling program  */  
   "IPCaller":string,
      /**  IsBaseCurrency  */  
   "IsBaseCurrency":boolean,
   "IsMtlConfigurationOn":boolean,
   "IsMtlConfigureOn":boolean,
   "IsMtlExtConfig":boolean,
      /**  IsMtlRevisionApproved  */  
   "IsMtlRevisionApproved":boolean,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   "PartExists":boolean,
      /**  Calculated field gets list of available Sites  */  
   "PlantList":string,
      /**  Price Per Code Description  */  
   "PricePerCodeDescription":string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   "RDEndNum":number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDPrefix":string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   "RDStartNum":number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   "RDSuffix":string,
      /**  The description of the related operation  */  
   "RelatedOperationDesc":string,
      /**  Logical used to determine if record is created from PO Entry.  */  
   "RetainValues":boolean,
   "Rpt1DisplayExtPrice":number,
   "Rpt1DisplayUnitPrice":number,
   "Rpt2DisplayExtPrice":number,
   "Rpt2DisplayUnitPrice":number,
   "Rpt3DisplayExtPrice":number,
   "Rpt3DisplayUnitPrice":number,
      /**  BaseUOM for SalvagePartNum  */  
   "SalvageBaseUOM":string,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   "ShowInspRqdImg":boolean,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   "SubContract":boolean,
      /**  Can the backflush be unchecked?  */  
   "AllowBackflushUncheck":boolean,
   "EnableAttributeSetSearch":boolean,
   "EnableSalvageAttributeSetSearch":boolean,
      /**  Number of pieces for inventory attribute tracked parts  */  
   "PlanningNumberOfPiecesDisp":number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   "SalvagePlanningNumberOfPiecesDisp":number,
      /**  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  */  
   "SkipUnitPriceCalc":boolean,
      /**  Error Status Display  */  
   "ErrorStatusDisplay":string,
      /**  True if this job material is in the fulfillment queue.  */  
   "InPartAllocQueue":boolean,
      /**  Show Fulfillment Queue Actions  */  
   "ShowFulfillmentQueueActions":boolean,
      /**  Indicates this row is selected for action.  */  
   "SelectedForAction":boolean,
      /**  The allocated quantity for this job material.  */  
   "AllocatedQty":number,
      /**  The reserved quantity for this job material.  */  
   "ReservedQty":number,
      /**  The available quantity for this job material.  */  
   "AvailableQty":number,
   "BitFlag":number,
   "AnalysisCdDescription":string,
   "AssemblySeqPartNum":string,
   "AssemblySeqDescription":string,
   "CallLineLineDesc":string,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
   "JobNumPartDescription":string,
   "JobNumPartNum":string,
   "MiscCodeDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumTrackInventoryByRevision":boolean,
   "PartNumAttrClassID":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PlantName":string,
   "ProdCodeDescription":string,
   "PurMiscCodeDescription":string,
   "PurMiscCodeLCAmount":number,
   "PurMiscCodeLCDisburseMethod":string,
   "PurMiscCodeLCCurrencyCode":string,
   "ReasonDescription":string,
   "RFQLineLineDesc":string,
   "SalvageAttributeSetIDDescription":string,
   "SalvageAttributeSetIDShortDescription":string,
   "SalvagePartNumPartDescription":string,
   "SalvagePartNumPricePerCode":string,
   "SalvagePartNumTrackInventoryByRevision":boolean,
   "SalvagePartNumTrackSerialNum":boolean,
   "SalvagePartNumTrackDimension":boolean,
   "SalvagePartNumTrackInventoryAttributes":boolean,
   "SalvagePartNumAttrClassID":string,
   "SalvagePartNumSellingFactor":number,
   "SalvagePartNumTrackLots":boolean,
   "SalvagePartNumSalesUM":string,
   "SalvagePartNumIUM":string,
   "SCMiscCodeDescription":string,
   "StageNoDescription":string,
   "VendorNumTermsCode":string,
   "VendorNumVendorID":string,
   "VendorNumZIP":string,
   "VendorNumAddress2":string,
   "VendorNumDefaultFOB":string,
   "VendorNumCountry":string,
   "VendorNumState":string,
   "VendorNumAddress3":string,
   "VendorNumCurrencyCode":string,
   "VendorNumAddress1":string,
   "VendorNumCity":string,
   "VendorNumName":string,
   "VendorPPState":string,
   "VendorPPAddress2":string,
   "VendorPPCountry":string,
   "VendorPPPrimPCon":number,
   "VendorPPZip":string,
   "VendorPPCity":string,
   "VendorPPAddress1":string,
   "VendorPPAddress3":string,
   "VendorPPName":string,
   "WarehouseCodeDescription":string,
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
      @param jobStatusTableset
      @param jobNum
   */  
export interface AutoAllocateJobMtl_input{
   jobStatusTableset:Erp_Tablesets_JobStatusTableset[],
      /**  The Job Number  */  
   jobNum:string,
}

export interface AutoAllocateJobMtl_output{
parameters : {
      /**  output parameters  */  
   jobStatusTableset:Erp_Tablesets_JobStatusTableset,
   messageText:string,
}
}

   /** Required : 
      @param jobStatusTableset
      @param jobNum
   */  
export interface AutoReserveJobMtl_input{
   jobStatusTableset:Erp_Tablesets_JobStatusTableset[],
      /**  The Job Number  */  
   jobNum:string,
}

export interface AutoReserveJobMtl_output{
parameters : {
      /**  output parameters  */  
   jobStatusTableset:Erp_Tablesets_JobStatusTableset,
   messageText:string,
}
}

   /** Required : 
      @param ipProposedJobFirm
      @param jobNum
      @param ds
   */  
export interface ChangeJobHeadFirm_input{
      /**  The new proposed JobFirm value  */  
   ipProposedJobFirm:boolean,
      /**  The job number to search appropriate record  */  
   jobNum:string,
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface ChangeJobHeadFirm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param ipProposedJobEngineered
      @param jobNum
      @param ds
   */  
export interface ChangeJobHeadJobEngineered_input{
      /**  The new proposed JobEngineered value  */  
   ipProposedJobEngineered:boolean,
      /**  The job number to search appropriate record  */  
   jobNum:string,
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface ChangeJobHeadJobEngineered_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param ipProposedJobReleased
      @param jobNum
      @param ds
   */  
export interface ChangeJobHeadJobReleased_input{
      /**  The new proposed JobReleased value  */  
   ipProposedJobReleased:boolean,
      /**  The job number to search appropriate record  */  
   jobNum:string,
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface ChangeJobHeadJobReleased_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param jobNum
   */  
export interface DeleteByID_input{
   jobNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_JobAsmblRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if the Job is complete.  This is a mirror image of JobHead.JobComplete.  Not directly maintainable.  When Job is complete, then all assembly records are also marked complete.  This is used to make database access to open assembly records more efficient.  */  
   JobComplete:boolean,
      /**  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  */  
   JobNum:string,
      /**  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  */  
   AssemblySeq:number,
      /**  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  */  
   PartNum:string,
      /**  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  */  
   Description:string,
      /**  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  The production quantity required for this assembly per one of it's parent part.  */  
   QtyPer:number,
      /**  The internal unit of measure for this assembly.  Use the Part.IUM as a default.  */  
   IUM:string,
      /**   This is how many of the assemblies are required to produce the END ITEM.  This is a calculated field.  Calculated as the (( Parents RequiredQty - Parents PullQty) X QtyPer) + OverRunQty.
This field needs to be refreshed whenever a change is made to the production quantity in any of its parents or when its QtyPer, or Overrun fields are changed. The refresh may also occur if the structure of the assemblies is changed.
The production quantity for the assembly which will drive raw material requirements and estimated production times can be determined by ( RequiredQty - PullQty).  */  
   RequiredQty:number,
      /**  This indicates a quantity that will be pulled from inventory for this assembly instead of being manufactured. This is a fixed quantity and is not affected by  QtyPer type changes. If this a valid Part, then it must update the PartWhse.AllocQty.  */  
   PullQty:number,
      /**  This is the warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  The material burden rate for this Job Assembly.  */  
   MtlBurRate:number,
      /**  The estimated unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  */  
   EstUnitCost:number,
      /**  The estimated Mtl burden unit cost for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  */  
   EstMtlBurUnitCost:number,
      /**  This value indicates a quantity that is planned to be overrun and put into inventory. This is kept as a separate field so that is does not distort the BOM requirement relationships. This increases the total production quantity for the assembly.  This is a FIXED quantity and is not affected by structure or qty/per type changes.  */  
   OverRunQty:number,
      /**  Scheduled start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process.  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   StartHour:number,
      /**  The scheduled due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the  "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Sequence number of the Parent Assembly.  */  
   Parent:number,
      /**   The  sequence number of the prior assembly that is on the same level as this assembly.  This  is known as a PriorPeer assembly.  This is automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the NextPeer is -1.  Then NextPeer of that assembly gets updated with this assemblies sequence number and this assembly gets its PriorPeer field updated with the sequence number from the assembly which was found.  */  
   PriorPeer:number,
      /**   The sequence number of the Next Assembly on the same level as this assembly.  This is known as a NextPeer assembly.  Automatically maintained by the maintenance programs.
The logic is to find an assembly where the Parent is the same and the PriorPeer is -1.  Then the PriorPeer of that assembly is updated with this assemblies sequence number and then this assemblies NextPeer gets updated with the sequence number from the assembly that was found.  */  
   NextPeer:number,
      /**  Sequence number of this assemblies very first subassembly.  This is known as the Child assembly.  Automatically maintained by the maintenance programs.  The logic is to find the Parent assembly record and if its child is -1, update it with this assemblies sequence number.  */  
   Child:number,
      /**  Total cost to date, of this component that was issued from stock.  */  
   TotalCost:number,
      /**  Total material burden cost to date, of this component that was issued from stock.  */  
   MtlBurCost:number,
      /**  This quantity is a summary of all Issue Transactions that were issued to meet this assemblies PullQty requirements.  This is not directly maintainable.  */  
   IssuedQty:number,
      /**  Optional field for Engineering Drawing Number.  Defaulted from BomHead.DrawNum during methods pull functions.  */  
   DrawNum:string,
      /**  Indicates if the pull quantity has been issued complete.  If "yes" then this record is NOT part of the PartWhse.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Editor widget for Job Assembly comments.  */  
   CommentText:string,
      /**  Indicates if this assembly is to be included in the browse of assemblies in the  "get details" function.  The user can use this option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly, it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  */  
   BomSequence:number,
      /**  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  */  
   BomLevel:number,
      /**  Scheduled "What If" start date for the assembly (including queue time).  This is not user maintainable.  It is updated by the scheduling process  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If  "Hour offset from the beginning of the work day" when this assembly is scheduled to begin (including queue time).  Scheduling uses the StartDate and StartHour of the parent assembly as the beginning Date/Hour when Backward scheduling subassemblies.  */  
   WIStartHour:number,
      /**  The scheduled "What-If" due date for the assembly (including move time).  Not user maintainable, updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this assembly is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**  This Level Actual Labor Cost.  */  
   TLALaborCost:number,
      /**  This Level Actual Burden Cost.  */  
   TLABurdenCost:number,
      /**  This Level Actual Material Cost.  */  
   TLAMaterialCost:number,
      /**  This Level Actual Subcontract Cost.  */  
   TLASubcontractCost:number,
      /**  This Level Actual Material Burden Cost.  */  
   TLAMtlBurCost:number,
      /**  This Level Actual Setup Hours.  */  
   TLASetupHours:number,
      /**  This Level Actual Production Hours.  */  
   TLAProdHours:number,
      /**  This Level Estimated Labor Cost.  */  
   TLELaborCost:number,
      /**  This Level Estimated Burden Cost.  */  
   TLEBurdenCost:number,
      /**  This Level Estimated Material Cost.  */  
   TLEMaterialCost:number,
      /**  This Level Estimated Subcontract Cost.  */  
   TLESubcontractCost:number,
      /**  This Level Estimated Material Burden Cost.  */  
   TLEMtlBurCost:number,
      /**  This Level Estimated Setup Hours.  */  
   TLESetupHours:number,
      /**  This Level Estimated Production Hours.  */  
   TLEProdHours:number,
      /**  Lower Level Actual Labor Cost.  */  
   LLALaborCost:number,
      /**  Lower Level Burden Labor Cost.  */  
   LLABurdenCost:number,
      /**  Lower Level Actual Material Cost.  */  
   LLAMaterialCost:number,
      /**  Lower Level Actual Subcontractor Cost.  */  
   LLASubcontractCost:number,
      /**  Lower Level Actual Material Burden Cost.  */  
   LLAMtlBurCost:number,
      /**  Lower Level Actual Setup Hours.  */  
   LLASetupHours:number,
      /**  Lower Level Actual Production Hours.  */  
   LLAProdHours:number,
      /**  Lower Level Estimated Labor Cost.  */  
   LLELaborCost:number,
      /**  Lower Level Estimated Burden Cost.  */  
   LLEBurdenCost:number,
      /**  Lower Level Estimated Material Cost.  */  
   LLEMaterialCost:number,
      /**  Lower Level Estimated Subcontract Cost.  */  
   LLESubcontractCost:number,
      /**  Lower Level Estimated Material Burden Cost.  */  
   LLEMtlBurCost:number,
      /**  Lower Level Estimated Setup Hours.  */  
   LLESetupHours:number,
      /**  Lower Level Estimated Production Hours.  */  
   LLEProdHours:number,
      /**   The operation number (JobOper.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable.  Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  */  
   AutoRecOpr:number,
      /**   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  */  
   FinalOpr:number,
      /**  FUTURE IMPLEMENTATION - Characters used on the parent assembly drawing to show where assembly  is used.  */  
   FindNum:string,
      /**  Total received to stock.  This pertains receiving an OverRun quantity.  Used to update the PartDtl file for expected production quantity.  PartDtl is OverRun - ReceivedToStock.  */  
   ReceivedToStock:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this assembly material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified..  */  
   Direct:boolean,
      /**   An assembly record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this assembly is required at the very beginning of the production job.  The related operation is also used to calculate scheduled start date.  */  
   RelatedOperation:number,
      /**  This Level Actual Material Labor Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialLabCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialLabCost:number,
      /**  This Level Actual Issued Material Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialMtlCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialMtlCost:number,
      /**  This Level Actual Material Subcontract Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialSubCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialSubCost:number,
      /**  This Level Actual Material Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for this level (independent of TLAMaterialCost). Otherwise, TLAMaterialBurCost is one of the component costs that makes up the TLAMaterialCost (i.e. TLAMaterialCost = TLAMaterialLabCost + TLAMaterialMtlCost + TLAMaterialSubCost + TLAMaterialBurCost).  */  
   TLAMaterialBurCost:number,
      /**  Lower Level Actual Material Labor Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialLabCost is the Total Labor costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialLabCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialLabCost:number,
      /**  Lower Level Actual Material Material Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlCost is the Total Material costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialMtlCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialMtlCost:number,
      /**  Lower Level Actual Material Subcontract Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialSubCost is the Total Subcontract costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialSubCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialSubCost:number,
      /**  Lower Level Actual Material Burden Cost. Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialBurCost is the Total Burden costs of all manufactured parts issued as material for the lower level (independent of LLAMaterialCost). Otherwise, LLAMaterialBurCost is one of the component costs that makes up the LLAMaterialCost (i.e. LLAMaterialCost = LLAMaterialLabCost + LLAMaterialMtlCost + LLAMaterialSubCost + LLAMaterialBurCost).  */  
   LLAMaterialBurCost:number,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   TotalMtlMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlSubCost:number,
      /**  Total Burden cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   TotalMtlBurCost:number,
      /**  The service call that this assembly belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this assembly relates to.  */  
   CallLine:number,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**  This field will be set to the value of the JobAsmbl.RequiredQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigRequiredQty:number,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then TLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for this level.  Otherwise, TLAMaterialMtlBurCost may be populated but is not included in the calculation of TLAMaterialCost.  */  
   TLAMaterialMtlBurCost:number,
      /**  Lower Level Actual Material Mtl Burden Cost.  Depending on the setting of JCSyst.SplitMfgCostElements, if set to true then LLAMaterialMtlBurCost is the Total Material Burden costs of all manufactured parts issued as material for the lower level.  Otherwise, LLAMaterialMtlBurCost may be populated but is not included in the calculation of LLAMaterialCost.  */  
   LLAMaterialMtlBurCost:number,
      /**  This Level Actual Component Labor Cost.  This is the Total Labor costs of all manufactured parts issued as material for this level. Unlike TLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompLabCost:number,
      /**  This Level Actual Component Material Cost.  This is the Total Material costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlCost:number,
      /**  This Level Actual Component Subcontract Cost.  This is the Total Subcontract costs of all manufactured parts issued as material for this level. Unlike TLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompSubCost:number,
      /**  This Level Actual Component Burden Cost.  This is the Total Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompBurCost:number,
      /**  This Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for this level. Unlike TLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for this assembly.  */  
   TLAMfgCompMtlBurCost:number,
      /**  Lower Level Actual Component Labor Cost. This is the Total Labor costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialLabCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompLabCost:number,
      /**  Lower Level Actual Component Material Cost. This is the Total Material costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlCost:number,
      /**  Lower Level Actual Component Subcontract Cost. This is the Total Subcontract costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialSubCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompSubCost:number,
      /**  Lower Level Actual Component Burden Cost. This is the Total Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompBurCost:number,
      /**  Lower Level Actual Component Material Burden Cost.  This is the Total Material Burden costs of all manufactured parts issued as material for the lower level. Unlike LLAMaterialMtlBurCost, this field will only store component costs that are from issued Mfg type materials used for the lower assemblies.  */  
   LLAMfgCompMtlBurCost:number,
      /**  Assembly Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Assembly Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Original Material Sequence. Used in the configurator.  */  
   OrigMtlSeq:number,
      /**  Original Rule Tag. Used in the Configurator.  */  
   OrigRuleTag:string,
      /**  Validate Reference Designators.  */  
   ValRefDes:boolean,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**   The estimated material unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   The estimated labor unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   The estimated burden unit cost component for the assembly quantity (JobAsmbl.PullQty)  that will be pulled from inventory.  Use the appropriate cost found in the Part file as a default.  That is, select the cost fields based on Part.CostMethod.  Then crossfoot the labor, burden and material into the EstUnitCost field.  This field is a subcomponent of EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurunitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**  Indicates if the sub-assemby can be spawned off to a different job.  This can occur during the firming up of a job.  */  
   PlanAsAsm:boolean,
      /**  Plan as assembly reference.  Used to link related subassemblies together when multiple assemblies are created for the same part due to PartSite lot size values.  */  
   PAARef:string,
      /**  Used only on Plan As Assembly records.  Indicates the sub assembly will be split of from the the current job and a separate job for the assembly will be created.  */  
   PAAFirm:boolean,
      /**  EstScrap =  a number representing either a scrap qty or a scrap percent depending on the value of EstScrapType field.  */  
   EstScrap:number,
      /**  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  */  
   EstScrapType:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Reassign Serial Numbers Assembly  */  
   ReassignSNAsm:boolean,
      /**  This Level Actual Other Direct Cost.  */  
   TLAODCCost:number,
      /**  AssemblyMatch  */  
   AssemblyMatch:string,
      /**  JdfStatus  */  
   JdfStatus:string,
      /**  PressDevice  */  
   PressDevice:string,
      /**  DigitalFileName  */  
   DigitalFileName:string,
      /**  PrepressJobName  */  
   PrepressJobName:string,
      /**  JdfPrepressAction  */  
   JdfPrepressAction:string,
      /**  SendToPress  */  
   SendToPress:boolean,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  SendToPressInitiator  */  
   SendToPressInitiator:number,
      /**  OperationType  */  
   OperationType:number,
      /**  SendToPrePress  */  
   SendToPrePress:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PartPlanInfo  */  
   PartPlanInfo:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Calculated Available Quantity  */  
   AvailableQty:number,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bUseAvailQty:boolean,
      /**  The child assembly sequence field.  The JobAsmbl.Child field value.  The field Child was causing a .net conflict.  */  
   ChildAssemblySeq:number,
      /**  The internal unit of measure for this assembly.  Same as IUM but readOnly  */  
   DispIUM:string,
      /**  The order JobAsmbl records should be displayed.  */  
   DisplayOrder:number,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableAsmSplitCosts:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  Is used to select stocked Job Assemblies which will be processed by Firming Process. Is available only for .FirmProcEnable = true.  */  
   FirmProcess:boolean,
      /**  External field for EQSyst GetCostsFromInventory  */  
   GetCostsFromInventory:boolean,
      /**  External field to hold JCSyst.GetCostsFromTemplate value  */  
   GetCostsFromTemplate:boolean,
      /**  The parent assembly sequence field.  The JobAsmbl.Parent field value.  The field Parent was causing a .net conflict.  */  
   ParentAssemblySeq:number,
      /**  Parent Description  */  
   ParentDescription:string,
      /**  Parent PartNum  */  
   ParentPartNum:string,
      /**  Parent RevisionNum  */  
   ParentRev:string,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   PartExists:boolean,
   PartmasterPart:boolean,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the assembly. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  Related Operation Description  */  
   RelatedOperationDesc:string,
      /**  For Internal use ONLY to set a flag calculated from BO to show a warning message to the user when there exists some inconsistences between records on JobAsml table that can cause infinite loop when BOM Resequence.  */  
   ShowWarningBOMResequence:boolean,
      /**  External field used to determine if Add assembly as "Sub"assembly or "Asm"bly  */  
   AddAsmAs:string,
      /**  external field used to calculate JobAsmbl.AvailableQty when PullQty changes.  This is needed because of a timing issue with PartQty getting updated too late.  */  
   bAvailQty:number,
   EnableAttributeSetSearch:boolean,
   AttributeSetShortDescription:string,
   AttributeSetDescription:string,
   AttrClassID:string,
      /**  This Level Total Actual Cost (TLAMaterialCost + TLALaborCost + TLABurdenCost + TLASubcontractCost + TLAMtlBurCost)  */  
   TLATotalCost:number,
      /**  The Level Estimated Total Cost (TLEMaterialCost + TLELaborCost + TLEBurdenCost + TLESubcontractCost + TLEMtlBurCost)  */  
   TLETotalCost:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   JobNumPartDescription:string,
   PartNumIUM:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackLots:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackInventoryAttributes:boolean,
   PlantName:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
   SOExists:boolean,
      /**  Part Description  */  
   PartNumPartDescription:string,
      /**  Track Dimension  */  
   PartNumTrackDimension:boolean,
      /**  Track Lots  */  
   PartNumTrackLots:boolean,
      /**  Track Serial Num  */  
   PartNumTrackSerialNum:boolean,
   EquipOEM:string,
   EquipModel:string,
   EquipTypeID:string,
   EquipLocID:string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   PMJob:boolean,
   EquipDescription:string,
   JobTypeName:string,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  ID of related Attribute Class  */  
   AttrClassID:string,
      /**  Description of values in set  */  
   AttrDescription:string,
      /**  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part  */  
   ShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobHeadListTableset{
   JobHeadList:Erp_Tablesets_JobHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_JobHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  */  
   JobClosed:boolean,
      /**  Date the Job was closed.  Defaults as the system but can be overridden.  */  
   ClosedDate:string,
      /**  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  */  
   JobComplete:boolean,
      /**  The date that production was completed for this Job.  Maintained via Job Completion Processing.  */  
   JobCompletionDate:string,
      /**  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  */  
   JobEngineered:boolean,
      /**   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff1:boolean,
      /**   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff2:boolean,
      /**   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff3:boolean,
      /**  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff4:boolean,
      /**  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  */  
   CheckOff5:boolean,
      /**  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  */  
   JobReleased:boolean,
      /**  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  */  
   JobHeld:boolean,
      /**  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  */  
   SchedStatus:string,
      /**  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  */  
   JobNum:string,
      /**   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  */  
   PartNum:string,
      /**  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  */  
   DrawNum:string,
      /**  The description of the part that is to be manufactured.  Use the Part.Description as the default.  */  
   PartDescription:string,
      /**  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  */  
   ProdQty:number,
      /**  The unit of measure for the job.  Defaulted from Part.IUM.  */  
   IUM:string,
      /**  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   StartDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   StartHour:number,
      /**  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   DueDate:string,
      /**  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   DueHour:number,
      /**  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  */  
   ReqDueDate:string,
      /**  An optional user defined code.  This will be used for report selections and views of job headers.  */  
   JobCode:string,
      /**  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  */  
   QuoteNum:number,
      /**  Contains the quote line number reference. (see QuoteNum )  */  
   QuoteLine:number,
      /**  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Editor widget for Job header comments.  */  
   CommentText:string,
      /**  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  */  
   ExpenseCode:string,
      /**  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  */  
   InCopyList:boolean,
      /**   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  */  
   WIName:string,
      /**  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  */  
   WIStartDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  */  
   WIStartHour:number,
      /**  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  */  
   WIDueDate:string,
      /**  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  */  
   WIDueHour:number,
      /**   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  */  
   Candidate:boolean,
      /**  Scheduling Code.  SchedCode references a record in the SchedPri table.  */  
   SchedCode:string,
      /**  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  */  
   SchedLocked:boolean,
      /**  Associates the JobHead with a project in the Project table.  This can be blank.  */  
   ProjectID:string,
      /**  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  */  
   WIPCleared:boolean,
      /**  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  */  
   JobFirm:boolean,
      /**  A LIST-DELIM delimited list of people.  */  
   PersonList:string,
      /**   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  */  
   PersonID:string,
      /**  Production Team for the Job.  Associates the JobHead with a ProdTeam.  */  
   ProdTeamID:string,
      /**   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  */  
   QtyCompleted:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  */  
   DatePurged:string,
      /**  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  */  
   TravelerReadyToPrint:boolean,
      /**  The last date the job traveler was mass printed.  */  
   TravelerLastPrinted:string,
      /**  Indicates if the Status can be printed. Print functions are not available if this is = No.  */  
   StatusReadyToPrint:boolean,
      /**  The last date the job status was mass printed.  */  
   StatusLastPrinted:string,
      /**  The Service Call number that this Job is linked to.  */  
   CallNum:number,
      /**  The Service Call Line that this Job is linked to.  */  
   CallLine:number,
      /**  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  */  
   JobType:string,
      /**  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  */  
   RestoreFlag:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Indicates that the quantity on this job is locked  */  
   LockQty:boolean,
      /**  The help desk case that created this job.  */  
   HDCaseNum:number,
      /**   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  */  
   ProcessMode:string,
      /**  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  */  
   PlannedActionDate:string,
      /**  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  */  
   PlannedKitDate:string,
      /**  The task ID that is returned from Microsoft Project.  */  
   MSPTaskID:string,
      /**  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  */  
   MSPPredecessor:string,
      /**  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  */  
   UserMapData:string,
      /**  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  */  
   ProductionYield:boolean,
      /**  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  */  
   OrigProdQty:number,
      /**  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  */  
   PreserveOrigQtys:boolean,
      /**  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  */  
   NoAutoCompletion:boolean,
      /**  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  */  
   NoAutoClosing:boolean,
      /**  The user that created this Job.  */  
   CreatedBy:string,
      /**  The date that this Job was created.  */  
   CreateDate:string,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  */  
   OwnershipStatus:string,
      /**  Holds the internal object id of PDM parts.  */  
   PDMObjID:string,
      /**  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  */  
   ExportRequested:string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  */  
   SplitMfgCostElements:boolean,
      /**  Cross Reference Part Num. Used for alternate serial mask support.  */  
   XRefPartNum:string,
      /**   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  */  
   XRefPartType:string,
      /**  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  */  
   XRefCustNum:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job was rough cut scheduled.  */  
   RoughCutScheduled:boolean,
      /**   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  */  
   EquipID:string,
      /**   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  */  
   PlanNum:number,
      /**  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  */  
   MaintPriority:string,
      /**  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  */  
   SplitJob:boolean,
      /**  Indicates the type of prefix which is used for create jobs in MRP  */  
   NumberSource:boolean,
      /**  The Meter Reading value entered at time of Job Closing.  */  
   CloseMeterReading:number,
      /**  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  */  
   IssueTopicID1:string,
      /**  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  */  
   IssueTopicID2:string,
      /**  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  */  
   IssueTopicID3:string,
      /**  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  */  
   IssueTopicID4:string,
      /**  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  */  
   IssueTopicID5:string,
      /**  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  */  
   IssueTopicID6:string,
      /**  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  */  
   IssueTopicID7:string,
      /**  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  */  
   IssueTopicID8:string,
      /**  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  */  
   IssueTopicID9:string,
      /**  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  */  
   IssueTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   IssueTopics:string,
      /**  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  */  
   ResTopicID1:string,
      /**  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  */  
   ResTopicID2:string,
      /**  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  */  
   ResTopicID3:string,
      /**  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  */  
   ResTopicID4:string,
      /**  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  */  
   ResTopicID5:string,
      /**  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  */  
   ResTopicID6:string,
      /**  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  */  
   ResTopicID7:string,
      /**  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  */  
   ResTopicID8:string,
      /**  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  */  
   ResTopicID9:string,
      /**  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  */  
   ResTopicID10:string,
      /**  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  */  
   ResTopics:string,
      /**  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  */  
   Forward:boolean,
      /**  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedSeq:number,
      /**  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  */  
   PAAExists:boolean,
      /**  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  */  
   DtlsWithinLeadTime:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  */  
   RoughCut:boolean,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  LastChangedBy  */  
   LastChangedBy:string,
      /**  LastChangedOn  */  
   LastChangedOn:string,
      /**  EPMExportLevel  */  
   EPMExportLevel:number,
      /**  JobWorkflowState  */  
   JobWorkflowState:string,
      /**  JobCSR  */  
   JobCSR:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LastExternalMESDate  */  
   LastExternalMESDate:string,
      /**  LastScheduleDate  */  
   LastScheduleDate:string,
      /**  LastScheduleProc  */  
   LastScheduleProc:string,
      /**  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  */  
   SchedPriority:number,
      /**  It indicates the days a job is going to be late in relation to its required due date  */  
   DaysLate:number,
      /**  ContractID  */  
   ContractID:string,
      /**  Logical field to indicate if this record has been read by project analysis process  */  
   ProjProcessed:boolean,
      /**  SyncReqBy  */  
   SyncReqBy:boolean,
      /**  CustName  */  
   CustName:string,
      /**  CustID  */  
   CustID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  UnReadyCostProcess  */  
   UnReadyCostProcess:boolean,
      /**  ProcSuspendedUpdates  */  
   ProcSuspendedUpdates:string,
      /**  DateTime field to indicate when this record has been read by project analysis process  */  
   ProjProcessedDate:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  Indicates if this revision is to use Advanced Staging.  */  
   UseAdvancedStaging:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  PersonIDName  */  
   PersonIDName:string,
      /**  This flag indicates if the job is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  FSMServiceReportID  */  
   FSMServiceReportID:string,
   AdvanceLaborRate:boolean,
      /**  Calculated field is set Not UnReadyCostProcess  */  
   dspReadyCostProcess:boolean,
      /**  Determine if jobengineered is enabled or disabled.  */  
   EnableJobEngineered:boolean,
      /**  Should JobFirm be enabled or disabled?  */  
   EnableJobFirm:boolean,
      /**  Determine if jobreleased is enabled or disabled.  */  
   EnableJobReleased:boolean,
   EnableMaterialStatus:boolean,
   EnableProject:boolean,
      /**  Is the job allowed to be engineered?  */  
   EngineerAllowed:boolean,
   EquipLocDesc:string,
      /**  If some fields except ToFirm have been updated  */  
   ExtUpdated:boolean,
      /**   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  */  
   FinalOpDueDate:string,
      /**  If it's Stocked assembly and PlanAsAsm is true.  */  
   FirmProcEnable:boolean,
      /**  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  */  
   FirmProcess:boolean,
      /**  Job has at least one assembly with flag Plan as Assembly.  */  
   HasPlanAsAsm:boolean,
      /**  Depending on the engineered job flag, is the header information enabled?  */  
   HeaderSensitive:boolean,
      /**  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  */  
   IgnoreMtlConstraints:boolean,
   JobTypeName:string,
      /**  If part is backflush the kit time is ignored.  */  
   KitTime:number,
      /**  Locked Qty Flag  */  
   LockedQty:boolean,
   NewMeter:number,
      /**  The old Job Number when JobFirm is changed from no to yes.  */  
   OldJobNum:string,
      /**  The order qty  */  
   OrderQty:number,
      /**  Logical field signifying whether JobHead.PartNum is a valid part master part.  */  
   PartmasterPart:boolean,
   PhaseDescription:string,
      /**  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  */  
   PMJob:boolean,
      /**  Process Mode Description  */  
   ProcessModeDescription:string,
      /**  Receive Time field for Job Part entered on Job  */  
   ReceiveTime:number,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
   SOExists:boolean,
   StockQty:number,
      /**  To be Firmed  */  
   ToFirm:boolean,
      /**  Description for XRefPartType  */  
   XRefPartTypeDesc:string,
      /**  The audit change description for the jobaudit record.  */  
   ChangeDescription:string,
   ClearDataset:boolean,
      /**  True if more than one co-part exists  */  
   IsCoPart:boolean,
      /**  The identifier of related Process Manufacturing.  */  
   PartRevProcessMfgID:string,
      /**  Type of Process Manufacturing.  */  
   PartRevProcessMfgType:string,
      /**  Determines if the Service Job has to be synchronized with Epicor FSI application.  */  
   SendToFSA:boolean,
   BitFlag:number,
   AnalysisCdDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   EquipMeterUOM:string,
   EquipSerialNum:string,
   EquipLocID:string,
   EquipPlant:string,
   EquipDescription:string,
   EquipBrand:string,
   EquipModel:string,
   EquipCurrentMeter:number,
   EquipTypeID:string,
   EquipOEM:string,
   ExpenseCodeDescription:string,
   HDCaseDescription:string,
   IssueTopicID1Description:string,
   IssueTopicID10Description:string,
   IssueTopicID2Description:string,
   IssueTopicID3Description:string,
   IssueTopicID4Description:string,
   IssueTopicID5Description:string,
   IssueTopicID6Description:string,
   IssueTopicID7Description:string,
   IssueTopicID8Description:string,
   IssueTopicID9Description:string,
   PartNumSalesUM:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumTrackSerialNum:boolean,
   PartNumTrackDimension:boolean,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumLocationIDNumReq:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PlantName:string,
   PlantMaintPlant:string,
   ProdCodeDescription:string,
   ProdTeamIDDescription:string,
   ProdTeamIDName:string,
   ProjectIDDescription:string,
   QuoteLineLineDesc:string,
   QuoteNumCurrencyCode:string,
   ResTopicID1Description:string,
   ResTopicID10Description:string,
   ResTopicID2Description:string,
   ResTopicID3Description:string,
   ResTopicID4Description:string,
   ResTopicID5Description:string,
   ResTopicID6Description:string,
   ResTopicID7Description:string,
   ResTopicID8Description:string,
   ResTopicID9Description:string,
   SchedCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobMtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if  "Job"  is complete.  This is a mirror image of JobHead.Complete.  Not directly maintainable.  When the Job is completed, then all JobMtl records are also marked.  This is used to make database access to open material records more efficient.  */  
   JobComplete:boolean,
      /**  Indicates if this material requirement has been issued complete.  If "yes" then this record is NOT part of the Part.AllocQty total even if it had been issued less than the original required quantity.  The user may toggle the setting if the JobHead.Complete is "NO".  When it is toggled the allocation logic will be triggered if necessary.  */  
   IssuedComplete:boolean,
      /**  Job Number.  */  
   JobNum:string,
      /**  Assembly sequence number that this material is associated with.  */  
   AssemblySeq:number,
      /**  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  */  
   MtlSeq:number,
      /**  Part number.  If the material is being purchased (JobMtl.BuyIt = yes) this does need to be a valid part in the Part file.  */  
   PartNum:string,
      /**  A description of the material.  */  
   Description:string,
      /**  Quantity per parent.  Field Service was EstQty in FSCallMt.  */  
   QtyPer:number,
      /**  Required Quantity per END ITEM.  This is a calculated field.  Calculated as (Parent Required Qty X QtyPer) + calculated Scrap.  The parent quantity is either the JobHead.ProdQty if  JobMtl.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobMtl.AssemblySeq > 0.  */  
   RequiredQty:number,
      /**  Internal unit of measure.  The unit used to measure the material.  */  
   IUM:string,
      /**   Expected purchasing lead time (in days).  This field is only valid if JobMtl.BuyIt = yes.  This can be used to calculate a suggested "Order By Date" based off the Required Date field.
When scheduling the job, purchased material can push a schedule out if the material lead time prevents the material from being available when the operation could start.  */  
   LeadTime:number,
      /**   A material record can be related to a specific operation.  This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  */  
   RelatedOperation:number,
      /**  The material burden rate for this Job Material.  */  
   MtlBurRate:number,
      /**  Estimated Material Burden Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstMtlBurUnitCost:number,
      /**  Estimated Unit Cost of the material.  Defaults from the Part table if valid PartNum.  */  
   EstUnitCost:number,
      /**  This quantity is a summary of all Issue Transactions.  For FS this was FSCallMt.ActQty  */  
   IssuedQty:number,
      /**  Total cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  FS - was UnitCost in FSCallMt  */  
   TotalCost:number,
      /**  Total Material Burden cost to date.  A summary of issue transactions.  This DOES NOT include the salvageable scrap credit amounts.  */  
   MtlBurCost:number,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   ReqDate:string,
      /**  The warehouse that the material is allocated against.  */  
   WarehouseCode:string,
      /**  Part number for salvageable scrap from this material record.  An optional field.  This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via salvage receipt process.  */  
   SalvagePartNum:string,
      /**  Description of Salvageable material.  Use Part.Description for a default.  */  
   SalvageDescription:string,
      /**  A factor that multiplied by the JobMtl.RequiredQty results in the expected total salvage quantity.  */  
   SalvageQtyPer:number,
      /**  Default unit of measure for the Salvaged Part.  Default from the Part.IUM.  */  
   SalvageUM:string,
      /**  The salvage material burden rate for this Job Material.  */  
   SalvageMtlBurRate:number,
      /**  Estimated Salvage Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageUnitCredit:number,
      /**  Estimated Salvage Mtl burden Unit Credit.  Use the appropriate cost from the Part master as a default.  */  
   SalvageEstMtlBurUnitCredit:number,
      /**  This quantity is a summary of all transactions for receipt of salvage to inventory.  This is not directly maintainable.  */  
   SalvageQtyToDate:number,
      /**  Total salvage credit to date.  A summary of salvage receipt transactions.  */  
   SalvageCredit:number,
      /**  Total salvage Mtl Burden credit to date.  A summary of salvage receipt transactions.  */  
   SalvageMtlBurCredit:number,
      /**   Comments for manufacturing about this material record.  These comments are printed on manufacturing reports, such as the router.  For valid Parts use the Part.MfgComment as a default.
View as editor widget.  */  
   MfgComment:string,
      /**  Used to identify a default vendor.  Use the Part.VendorNum as a default.  This will be used as a default for purchasing and miscellaneous receipts.  This field is not directly maintainable, instead its assigned by having the user either entering the "VendorID" and then finding the VendorNum in the Vendor file or by selection list processing.  An optional field, but if entered must be valid.  */  
   VendorNum:number,
      /**  The Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default purchase point defined in the Vendor file.  */  
   PurPoint:string,
      /**  Indicates if this material is to be purchased for the Job.  If this is a non inventory part then this is "Yes" and cannot be changed.  If this is a valid Part then set it to "NO" but the user can override it. Material that is marked to be purchased (BuyIt = Yes) are NOT included in the PartWhse.AllocatedQty.  */  
   BuyIt:boolean,
      /**  FUTURE IMPLEMENTATION.  This logical relates to material that is flagged to be purchased (BuyIt = Yes).  When purchase orders are created for this job material requirement this flag is set to Yes indicating that a purchase order has been placed.  The idea would be to use this within purchasing to quickly see the "direct job requirements" where no purchase orders have been placed.  */  
   Ordered:boolean,
      /**   Comments for purchasing about this material record on this job. These comments will be used as defaults to the PODetail.Comment field when the purchase order references this JobMtl record.
View as editor widget.  */  
   PurComment:string,
      /**   Indicates if this material will be backflushed.
Note: this field is defaulted from Part.BackFlush
Backflushing occurs via the write trigger on LaborDtl.  The basic idea is to issue material based on the labor quantities reported. The formula for the issue quantity is: (JobMtl.RequiredQty/JobOper.RunQty) * (LaborDtl.LaborQty + LaborDtl.SrapQty).  */  
   BackFlush:boolean,
      /**  Estimated Scrap.  */  
   EstScrap:number,
      /**  Qualifies the EstScrapQty entry as being a fixed quantity or a percentage of required quantity.  */  
   EstScrapType:string,
      /**  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  */  
   FixedQty:boolean,
      /**  Characters used on the drawing to show where material is used.  */  
   FindNum:string,
      /**  The revision number for the material.  An optional field. Defaults from the most current  PartRev.RevisionNum.  */  
   RevisionNum:string,
      /**  Controls if an alert is to be sent when this JobMtl is completed.  */  
   SndAlrtCmpl:boolean,
      /**  Indicates if inspection is required when items are received to this JobMtl.  Inspection may also be enforced if the related PartClass, Vendor, PODetail have their "RcvInspectionReq" fields set to Yes.  */  
   RcvInspectionReq:boolean,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Indicates if this material requirement is going to be satisfied by another job (possibly in another Site), as opposed to a warehouse.  If "yes" a WarehouseCode will not be specified.  */  
   Direct:boolean,
      /**  Total Mtl cost to date.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  MaterialMtlCost +  MaterialLabCost +  MaterialSubCost + MaterialBurCost = TotalCost  */  
   MaterialMtlCost:number,
      /**  Total Lab cost to date from parts issued from inventory.  A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialLabCost:number,
      /**  Total  Sub cost to date from part issued from inventory.  A summary of issue transactions used track all costs for manufacured parts that were received into inventory then issued as material..  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialSubCost:number,
      /**  Total Bur cost to date from part issued from inventory.   A summary of issue transactions - used track all costs for manufacured parts that were received into inventory then issued as material.  IssuedMtlCost + IssuedLabCost + IssuedSubCost + IssuedBurCost = TotalCost  */  
   MaterialBurCost:number,
      /**  Total salvage Mtl credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageMtlCredit:number,
      /**  Total salvage Lbr credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageLbrCredit:number,
      /**  Total salvage Burden credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageBurCredit:number,
      /**  Total salvage Subcontract credit to date.  A summary of salvage receipt transactions.  SalvageCredit = SalvageMtlCredit + SalvageLbrCredit + SalvageBurCredit + SalvageSubCredit  */  
   SalvageSubCredit:number,
      /**   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  */  
   APSAddResType:string,
      /**  The service call that this Material belongs to.  */  
   CallNum:number,
      /**  The Service Call Line that this material relates to.  */  
   CallLine:number,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  FS - Unit Price for the Material in base currency.  */  
   UnitPrice:number,
      /**  FS - Billable Unit Price for the Material in base currency.  */  
   BillableUnitPrice:number,
      /**  FS - Billable Price per unit for the material in customers currency.  */  
   DocBillableUnitPrice:number,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each,"C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E".  */  
   PricePerCode:string,
      /**  Is this a billable material item.  */  
   Billable:boolean,
      /**  Holds the quantity of the item that has been shipped through misc.  shipments  */  
   ShippedQty:number,
      /**  FS - Unit Price for the Material in Customer currency.  */  
   DocUnitPrice:number,
      /**  The todate quantity that has been moved to the work centers input Warehouse/Bin.  This is NOT A balance.  It is a todate value. It is not reduced as it is consumed. Used in calculation of "Outstanding" material in the Request Material program (ame30-dg.w). Only updated if the Advanced Material Mgmt module is installed and only by transactions which "move" the material in/out of the staging area(Issues,Returns).  */  
   QtyStagedToDate:number,
      /**  This material was added after initial setup of the job  */  
   AddedMtl:boolean,
      /**  This indicates that this JobMtl record is for a Misc charge related to this job/assembly.  */  
   MiscCharge:boolean,
      /**  The Miscellaneous Charge Code. This must be valid in the PurMisc master file.   It must be a AP Misc. charge.  */  
   MiscCode:string,
      /**  The Miscellaneous Charge Code for Service Call billing. This must be valid in the MiscChrg master file.   It must be a AR Misc. charge.  */  
   SCMiscCode:string,
      /**  A flag to indicate that this job material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  */  
   RFQNeeded:boolean,
      /**  The number of vendor quotes that are required for this job material.  Can be zero if RFQ(s) are not required.  */  
   RFQVendQuotes:number,
      /**  RFQ number that the item is linked to.  */  
   RFQNum:number,
      /**  The line number of this detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  */  
   RFQLine:number,
      /**   RFQ Status.
W= Waiting, A = Accepted, R = Requested, C = Received  */  
   RFQStat:string,
      /**  Analysis Code  */  
   AnalysisCode:string,
      /**  Global RFQ flag.  Used in Consolidated Purchasing.  */  
   GlbRFQ:boolean,
      /**  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  */  
   WhseAllocFlag:boolean,
      /**  Mirror image of related operation (JobOper) or assembly (JobAsmbl) Start Date. (system maintained)  */  
   WIReqDate:string,
      /**  Reporting currency value of this field  */  
   Rpt1BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3BillableUnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnitPrice:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnitPrice:number,
      /**   Required Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the JobMtl.RequiredQty which is in the UOM of the requirement to the JobMtl.BaseUOM which is the UOM of the Part and it's unit costs.
This quantity multiplied by the JobMtl.EstMtlUnitCost is used to update the total estimated costs found in JobAsmbl.TLEMaterialCost  */  
   BaseRequiredQty:number,
      /**   Unit of Measure of the JobMtl.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as JobMtl.IUM  */  
   BaseUOM:string,
      /**  Material Weight defaulted from Part Master.  */  
   Weight:number,
      /**  Material Weight UOM defaulted from Part Master.  */  
   WeightUOM:string,
      /**  Required number of designators  */  
   ReqRefDes:number,
      /**  Base Part Number. Used in the configurator to identify the configurator part Number.  */  
   BasePartNum:string,
      /**  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  */  
   BaseRevisionNum:string,
      /**  Indicates if the job material is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The job pick "Staging" warehouse for the job material.  Defaults from the system default warehouse (PlantConfCtrl.DefJobPickWhse).  */  
   StagingWarehouseCode:string,
      /**  The job pick "Staging" bin for the job material.  Defaults from the system default bin (PlantConfCtrl.DefJobPickBin).  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**   Estimated Material Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstMtlUnitCost:number,
      /**   Estimated Labor Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstLbrUnitCost:number,
      /**   Estimated Burden Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstBurUnitCost:number,
      /**   Estimated Subcontract Unit Cost component of the EstUnitCost.  Defaults from the Part table if valid PartNum.  This field will only have value if the part is a manufactured stock part. This is a subcomponent of the EstUnitCost where:
EstUnitCost = EstMtlUnitCost + EstLbrUnitCost + EstBurUnitCost + EstSubUnitCost.  */  
   EstSubUnitCost:number,
      /**   Estimated Salvage Material Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstMtlUnitCredit:number,
      /**   Estimated Salvage Labor Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstLbrUnitCredit:number,
      /**   Estimated Salvage Burden Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstBurUnitCredit:number,
      /**   Estimated Salvage Subcontract Unit Credit.  Use the appropriate cost from the Part master as a default.  This is a subcomponent of the field SalvageUnitCredit where:
SalvageUnitCredit = SalvageEstMtlUnitCredit + SalvageEstLbrUnitCredit + SalvageEstBurUnitCredit + SalvageEstSubUnitCredit.  */  
   SalvageEstSubUnitCredit:number,
      /**  The material quantity that has been loaned out to another job.  */  
   LoanedQty:number,
      /**  The material quantity that has been borrowed from another job.  */  
   BorrowedQty:number,
      /**  flag used to designate if the serial numbers from the job material/subassembly can be reassigned as the serial number of the parent assembly (top assembly or n deep subassembly) being reworked using a job.  */  
   ReassignSNAsm:boolean,
      /**  GeneralPlanInfo  */  
   GeneralPlanInfo:string,
      /**  EstStdDescription  */  
   EstStdDescription:string,
      /**  PricingUOM  */  
   PricingUOM:string,
      /**  RemovedFromPlan  */  
   RemovedFromPlan:boolean,
      /**  IsPOCostingMaintained  */  
   IsPOCostingMaintained:boolean,
      /**  EstStdType  */  
   EstStdType:number,
      /**  POCostingFactor  */  
   POCostingFactor:number,
      /**  PlannedQtyPerUnit  */  
   PlannedQtyPerUnit:number,
      /**  POCostingDirection  */  
   POCostingDirection:number,
      /**  POCostingUnitVal  */  
   POCostingUnitVal:number,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  When getting details on a multi-level configuration, the StructTag is used to load the configuration at each level so that method rules can be applied at that level.  By storing the original StructTag of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigStructTag:string,
      /**  By storing the original Group Sequence of the configuration as it was defined under its parent, it speeds up the process of determining where the lower level configured was originally configured.  If this field is populated, the lower level was originally configured as a child of another configured part.  */  
   OrigGroupSeq:number,
      /**  ShowStatusIcon  */  
   ShowStatusIcon:string,
      /**  ContractID  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the Planning Contract.  */  
   LinkToContract:boolean,
      /**  Stores the lot number of the material in the Staging Warehouse/Bin.  */  
   StagingLotNum:string,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  */  
   ExternalMESSyncRequired:boolean,
      /**  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  */  
   ExternalMESLastSync:string,
      /**  Controls if this material record is viewable in Location Management or the web.  */  
   LocationView:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvageAttributeSetID:number,
      /**  Salvage planning number of pieces for this attribute set.  */  
   SalvagePlanningNumberOfPieces:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SalvagePlanningAttributeSetID:number,
      /**  The identification of related StageNo.  */  
   RelatedStage:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   SalvageRevisionNum:string,
      /**  Indicates if the job material should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  This flag indicates if the job material is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  The currency switch flag  */  
   CurrencySwitch:boolean,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**  The display of extended price.  */  
   DisplayExtPrice:number,
      /**  The display unit price.  */  
   DisplayUnitPrice:number,
      /**  The document display extended price  */  
   DocDisplayExtPrice:number,
      /**  The document display extended price  */  
   DocDisplayUnitPrice:number,
      /**  BuyIt field for display in the UI.  */  
   dspBuyIt:boolean,
      /**  Display IUM (readonly)  */  
   DspIUM:string,
      /**  Should the backflush field be enabled?  */  
   EnableBackflush:boolean,
      /**  Field used to determine if there is security on JobMtl.BuyIt. If there is a row rule will disable the dspBuyIt.  */  
   EnableBuyIt:boolean,
      /**  flag to determine whether the Configure Option should be enabled.  */  
   EnableConfigure:boolean,
      /**  flag to determine whether the Make Direct field should be enabled.  */  
   EnableDirect:boolean,
      /**  This external field is used as a flag to determine when to enable/disable the FixedQty field according to the rules of Serial numbers design.  */  
   EnableFixedQty:boolean,
   EnableMtlSalvage:boolean,
   EnablePurDir:boolean,
      /**  Field to determine if the the RcvInspectionReq field should be enabled or disabled.  */  
   EnableRcvInspReq:boolean,
      /**  Field to determine if the the sndalrtcmpl field should be enabled or disabled.  */  
   EnableSndAlrtCmpl:boolean,
      /**  Flag to indicate if the Unit Cost Breakdown costs should be enabled or not.  */  
   EnableSplitCosts:boolean,
      /**  RequiredQty * EstUnitCost - RequiredQty * SalvageQtyPer * SalvageUnitCredit  */  
   EstCost:number,
      /**  The name of the calling program  */  
   IPCaller:string,
      /**  IsBaseCurrency  */  
   IsBaseCurrency:boolean,
   IsMtlConfigurationOn:boolean,
   IsMtlConfigureOn:boolean,
   IsMtlExtConfig:boolean,
      /**  IsMtlRevisionApproved  */  
   IsMtlRevisionApproved:boolean,
      /**  Internal flag to identify if current Part is an Inventory Part.  */  
   PartExists:boolean,
      /**  Calculated field gets list of available Sites  */  
   PlantList:string,
      /**  Price Per Code Description  */  
   PricePerCodeDescription:string,
      /**  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  */  
   RDEndNum:number,
      /**  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDPrefix:string,
      /**  This number will be used to create reference designators. This field will be defaulted to ?1?  */  
   RDStartNum:number,
      /**  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  */  
   RDSuffix:string,
      /**  The description of the related operation  */  
   RelatedOperationDesc:string,
      /**  Logical used to determine if record is created from PO Entry.  */  
   RetainValues:boolean,
   Rpt1DisplayExtPrice:number,
   Rpt1DisplayUnitPrice:number,
   Rpt2DisplayExtPrice:number,
   Rpt2DisplayUnitPrice:number,
   Rpt3DisplayExtPrice:number,
   Rpt3DisplayUnitPrice:number,
      /**  BaseUOM for SalvagePartNum  */  
   SalvageBaseUOM:string,
      /**  Satatus of InspectionRequired image on JobMaterial form.  */  
   ShowInspRqdImg:boolean,
      /**  Added for UI Framework?  This flags the material as being a "SubContract" or an "Internal" material.  */  
   SubContract:boolean,
      /**  Can the backflush be unchecked?  */  
   AllowBackflushUncheck:boolean,
   EnableAttributeSetSearch:boolean,
   EnableSalvageAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts  */  
   PlanningNumberOfPiecesDisp:number,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   SalvagePlanningNumberOfPiecesDisp:number,
      /**  Indicates if unit price calculation should occur.  When false the unit price will be calculated.  When false the unit price will remain its current value.  */  
   SkipUnitPriceCalc:boolean,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this job material is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowFulfillmentQueueActions:boolean,
      /**  Indicates this row is selected for action.  */  
   SelectedForAction:boolean,
      /**  The allocated quantity for this job material.  */  
   AllocatedQty:number,
      /**  The reserved quantity for this job material.  */  
   ReservedQty:number,
      /**  The available quantity for this job material.  */  
   AvailableQty:number,
   BitFlag:number,
   AnalysisCdDescription:string,
   AssemblySeqPartNum:string,
   AssemblySeqDescription:string,
   CallLineLineDesc:string,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
   JobNumPartDescription:string,
   JobNumPartNum:string,
   MiscCodeDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   ProdCodeDescription:string,
   PurMiscCodeDescription:string,
   PurMiscCodeLCAmount:number,
   PurMiscCodeLCDisburseMethod:string,
   PurMiscCodeLCCurrencyCode:string,
   ReasonDescription:string,
   RFQLineLineDesc:string,
   SalvageAttributeSetIDDescription:string,
   SalvageAttributeSetIDShortDescription:string,
   SalvagePartNumPartDescription:string,
   SalvagePartNumPricePerCode:string,
   SalvagePartNumTrackInventoryByRevision:boolean,
   SalvagePartNumTrackSerialNum:boolean,
   SalvagePartNumTrackDimension:boolean,
   SalvagePartNumTrackInventoryAttributes:boolean,
   SalvagePartNumAttrClassID:string,
   SalvagePartNumSellingFactor:number,
   SalvagePartNumTrackLots:boolean,
   SalvagePartNumSalesUM:string,
   SalvagePartNumIUM:string,
   SCMiscCodeDescription:string,
   StageNoDescription:string,
   VendorNumTermsCode:string,
   VendorNumVendorID:string,
   VendorNumZIP:string,
   VendorNumAddress2:string,
   VendorNumDefaultFOB:string,
   VendorNumCountry:string,
   VendorNumState:string,
   VendorNumAddress3:string,
   VendorNumCurrencyCode:string,
   VendorNumAddress1:string,
   VendorNumCity:string,
   VendorNumName:string,
   VendorPPState:string,
   VendorPPAddress2:string,
   VendorPPCountry:string,
   VendorPPPrimPCon:number,
   VendorPPZip:string,
   VendorPPCity:string,
   VendorPPAddress1:string,
   VendorPPAddress3:string,
   VendorPPName:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JobStatusTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   JobAsmbl:Erp_Tablesets_JobAsmblRow[],
   JobMtl:Erp_Tablesets_JobMtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtJobStatusTableset{
   JobHead:Erp_Tablesets_JobHeadRow[],
   JobAsmbl:Erp_Tablesets_JobAsmblRow[],
   JobMtl:Erp_Tablesets_JobMtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param jobNum
   */  
export interface GetByIDJobMtl_input{
      /**  Job Number  */  
   jobNum:string,
}

export interface GetByIDJobMtl_output{
   returnObj:Erp_Tablesets_JobStatusTableset[],
}

   /** Required : 
      @param jobNum
   */  
export interface GetByID_input{
   jobNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_JobStatusTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_JobStatusTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_JobStatusTableset[],
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetListFromSelectedKeys_input{
   ds:Erp_Tablesets_JobHeadListTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetListFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobHeadListTableset,
   morePages:boolean,
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
   returnObj:Erp_Tablesets_JobHeadListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param jobNum
   */  
export interface GetNewJobAsmbl_input{
   ds:Erp_Tablesets_JobStatusTableset[],
   jobNum:string,
}

export interface GetNewJobAsmbl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJobHead_input{
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface GetNewJobHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param ds
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsFromSelectedKeys_input{
   ds:Erp_Tablesets_JobStatusTableset[],
      /**  The page size, used only for UI adaptor  */  
   pageSize:number,
      /**  The absolute page, used only for the UI adaptor  */  
   absolutePage:number,
}

export interface GetRowsFromSelectedKeys_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseJobHead
      @param whereClauseJobAsmbl
      @param whereClauseJobMtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseJobHead:string,
   whereClauseJobAsmbl:string,
   whereClauseJobMtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_JobStatusTableset[],
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
export interface MassUpdate_input{
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface MassUpdate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtJobStatusTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtJobStatusTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_JobStatusTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_JobStatusTableset,
}
}

