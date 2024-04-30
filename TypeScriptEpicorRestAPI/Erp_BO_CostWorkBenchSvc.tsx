import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CostWorkBenchSvc
// Description: Costing work bench
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/$metadata", {
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
   Description: Get CostWorkBenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostWorkBenches
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostGrpRow
   */  
export function get_CostWorkBenches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostWorkBenches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CostGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostWorkBenches(requestBody:Erp_Tablesets_CostGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches", {
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
   Summary: Calls GetByID to retrieve the CostWorkBench item
   Description: Calls GetByID to retrieve the CostWorkBench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostGrpRow
   */  
export function get_CostWorkBenches_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")", {
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
         resolve(data as Erp_Tablesets_CostGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CostWorkBench for the service
   Description: Calls UpdateExt to update CostWorkBench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CostWorkBenches_Company_GroupID(Company:string, GroupID:string, requestBody:Erp_Tablesets_CostGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete CostWorkBench item
   Description: Call UpdateExt to delete CostWorkBench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostWorkBench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CostWorkBenches_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")", {
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
   Description: Get CostBurdens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostBurdens1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostBurdenRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostBurdens(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostBurdens", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CostBurden item
   Description: Calls GetByID to retrieve the CostBurden item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostBurden1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostBurdenRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostBurdenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
         resolve(data as Erp_Tablesets_CostBurdenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CostLabors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostLabors1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostLaborRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostLabors(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostLabors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CostLabor item
   Description: Calls GetByID to retrieve the CostLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostLabor1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostLaborRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostLaborRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
         resolve(data as Erp_Tablesets_CostLaborRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CostParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CostParts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostParts(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostParts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CostPart item
   Description: Calls GetByID to retrieve the CostPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPart1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostPartRow
   */  
export function get_CostWorkBenches_Company_GroupID_CostParts_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostWorkBenches(" + Company + "," + GroupID + ")/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
         resolve(data as Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CostBurdens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostBurdens
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostBurdenRow
   */  
export function get_CostBurdens(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostBurdens
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CostBurdenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostBurdens(requestBody:Erp_Tablesets_CostBurdenRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens", {
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
   Summary: Calls GetByID to retrieve the CostBurden item
   Description: Calls GetByID to retrieve the CostBurden item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostBurden
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostBurdenRow
   */  
export function get_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostBurdenRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
         resolve(data as Erp_Tablesets_CostBurdenRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CostBurden for the service
   Description: Calls UpdateExt to update CostBurden. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostBurden
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostBurdenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, requestBody:Erp_Tablesets_CostBurdenRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
   Summary: Call UpdateExt to delete CostBurden item
   Description: Call UpdateExt to delete CostBurden item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostBurden
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CostBurdens_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostBurdens(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
   Description: Get CostLabors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostLabors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostLaborRow
   */  
export function get_CostLabors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostLabors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CostLaborRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostLabors(requestBody:Erp_Tablesets_CostLaborRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors", {
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
   Summary: Calls GetByID to retrieve the CostLabor item
   Description: Calls GetByID to retrieve the CostLabor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostLaborRow
   */  
export function get_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostLaborRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
         resolve(data as Erp_Tablesets_CostLaborRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CostLabor for the service
   Description: Calls UpdateExt to update CostLabor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostLaborRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, requestBody:Erp_Tablesets_CostLaborRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
   Summary: Call UpdateExt to delete CostLabor item
   Description: Call UpdateExt to delete CostLabor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostLabor
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param RateSourceTableName Desc: RateSourceTableName   Required: True   Allow empty value : True
      @param SourceID Desc: SourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CostLabors_Company_GroupID_RateSourceTableName_SourceID(Company:string, GroupID:string, RateSourceTableName:string, SourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostLabors(" + Company + "," + GroupID + "," + RateSourceTableName + "," + SourceID + ")", {
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
   Description: Get CostParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CostParts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostPartRow
   */  
export function get_CostParts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CostParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CostPartRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostParts(requestBody:Erp_Tablesets_CostPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts", {
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
   Summary: Calls GetByID to retrieve the CostPart item
   Description: Calls GetByID to retrieve the CostPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CostPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CostPartRow
   */  
export function get_CostParts_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CostPartRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
         resolve(data as Erp_Tablesets_CostPartRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CostPart for the service
   Description: Calls UpdateExt to update CostPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CostPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CostPartRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CostParts_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, requestBody:Erp_Tablesets_CostPartRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
   Summary: Call UpdateExt to delete CostPart item
   Description: Call UpdateExt to delete CostPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CostPart
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CostParts_Company_GroupID_TypeCode_PartNum(Company:string, GroupID:string, TypeCode:string, PartNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostParts(" + Company + "," + GroupID + "," + TypeCode + "," + PartNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CostGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseCostGrp:string, whereClauseCostBurden:string, whereClauseCostLabor:string, whereClauseCostPart:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCostGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCostGrp=" + whereClauseCostGrp
   }
   if(typeof whereClauseCostBurden!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCostBurden=" + whereClauseCostBurden
   }
   if(typeof whereClauseCostLabor!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCostLabor=" + whereClauseCostLabor
   }
   if(typeof whereClauseCostPart!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCostPart=" + whereClauseCostPart
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetRows" + params, {
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

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: Get Code Descripotion List
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCopyFromGroupID
   Description: Method to call when changing the copy from group id on the cost group.  Validates the
group id and updates CostGrp with default values based on the new group id.
   OperationID: ChangeCopyFromGroupID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCopyFromGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyFromGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCopyFromGroupID(requestBody:ChangeCopyFromGroupID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCopyFromGroupID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ChangeCopyFromGroupID", {
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
         resolve(data as ChangeCopyFromGroupID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCopyFromPlantCostID
   Description: Method to call when changing the copy from plant cost id on the cost group.  Validates the
plant cost id and updates CostGrp with default values based on the new plant cost id.
   OperationID: ChangeCopyFromPlantCostID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCopyFromPlantCostID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCopyFromPlantCostID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCopyFromPlantCostID(requestBody:ChangeCopyFromPlantCostID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCopyFromPlantCostID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ChangeCopyFromPlantCostID", {
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
         resolve(data as ChangeCopyFromPlantCostID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeCWBPostPostToPlantCostID
   Description: Method to call when changing the post to cost id on the post cost table (CostWorkBenchPost).
Validates the plant cost id recreates CostWorkBenchPostPlants records for
the new cost id.
Prior to calling this method all CostWorkBenchPostPlants records must have the
RowMod value set to U because they will be deleted.
   OperationID: ChangeCWBPostPostToPlantCostID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCWBPostPostToPlantCostID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCWBPostPostToPlantCostID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCWBPostPostToPlantCostID(requestBody:ChangeCWBPostPostToPlantCostID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCWBPostPostToPlantCostID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ChangeCWBPostPostToPlantCostID", {
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
         resolve(data as ChangeCWBPostPostToPlantCostID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePrimaryPlant
   Description: Method to call when changing the primary plant on the cost group.  Validates the plant id
and updates CostGrp with default values based on the new plant.
   OperationID: ChangePrimaryPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePrimaryPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePrimaryPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePrimaryPlant(requestBody:ChangePrimaryPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePrimaryPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ChangePrimaryPlant", {
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
         resolve(data as ChangePrimaryPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CostPost
   Description: Post costs for the group.
   OperationID: CostPost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CostPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CostPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostPost(requestBody:CostPost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CostPost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostPost", {
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
         resolve(data as CostPost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CostRollUp
   Description: Roll up costs for the group.
   OperationID: CostRollUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CostRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CostRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CostRollUp(requestBody:CostRollUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CostRollUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/CostRollUp", {
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
         resolve(data as CostRollUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DEGetImportRatesLockStatus
   Description: Parameters:  none
   OperationID: DEGetImportRatesLockStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DEGetImportRatesLockStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DEGetImportRatesLockStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DEGetImportRatesLockStatus(requestBody:DEGetImportRatesLockStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DEGetImportRatesLockStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/DEGetImportRatesLockStatus", {
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
         resolve(data as DEGetImportRatesLockStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostSet
   Description: This method creates/refreshes the costs for the Cost Group.
   OperationID: GetCostSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostSet(requestBody:GetCostSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostSet", {
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
         resolve(data as GetCostSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostWBInternalPrices
   Description: This method will create an empty CostWBInternalPrices record to use in
populating the parameters required to update the internal prices
The WorkstationID, DateFormat and NumericFormat fields are not user updatable
The Action field is one of 3 values 'All' = 'Calculate, Print, Update', 'Print' = 'Calculate, Print', 'Update' = 'Calculate, Update'
   OperationID: GetCostWBInternalPrices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostWBInternalPrices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWBInternalPrices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostWBInternalPrices(requestBody:GetCostWBInternalPrices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostWBInternalPrices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostWBInternalPrices", {
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
         resolve(data as GetCostWBInternalPrices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostWorkBenchCostSet
   Description: This method will create a CostWorkbenchCostSet record which is used to store
user options for the getting the CostPart, CostLabor, and CostBurden records.
   OperationID: GetCostWorkBenchCostSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchCostSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchCostSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostWorkBenchCostSet(requestBody:GetCostWorkBenchCostSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostWorkBenchCostSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostWorkBenchCostSet", {
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
         resolve(data as GetCostWorkBenchCostSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostWorkBenchPost
   Description: This method will create a CostWorkbenchPost record which is used to store
user options for the Post option.
   OperationID: GetCostWorkBenchPost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostWorkBenchPost(requestBody:GetCostWorkBenchPost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostWorkBenchPost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostWorkBenchPost", {
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
         resolve(data as GetCostWorkBenchPost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostWorkBenchRefresh
   Description: This method will create a CostWorkbenchRefresh record which is used to store
user options for refreshing costs in the CostPart, CostLabor, and CostBurden records.
   OperationID: GetCostWorkBenchRefresh
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostWorkBenchRefresh(requestBody:GetCostWorkBenchRefresh_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostWorkBenchRefresh_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostWorkBenchRefresh", {
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
         resolve(data as GetCostWorkBenchRefresh_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCostWorkBenchRollUp
   Description: This method will create a CostWorkbenchRollUp record which is used to store
user options for the rollup option.
   OperationID: GetCostWorkBenchRollUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCostWorkBenchRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCostWorkBenchRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCostWorkBenchRollUp(requestBody:GetCostWorkBenchRollUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCostWorkBenchRollUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetCostWorkBenchRollUp", {
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
         resolve(data as GetCostWorkBenchRollUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListCostingEdits
   Description: Returns the list for Costing Edits.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListCostingEdits
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListCostingEdits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListCostingEdits(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListCostingEdits_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListCostingEdits", {
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
         resolve(data as ListCostingEdits_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListFilters
   Description: Returns the list for filter options for parts.  The list is in code1`desc1~code2`desc2 format.
   OperationID: ListFilters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListFilters(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListFilters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListFilters", {
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
         resolve(data as ListFilters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListOprAndResourceSortBy
   Description: Returns the list for sort by options for Operations and Resource Groups.
The list is in code1`desc1~code2`desc2 format.
   OperationID: ListOprAndResourceSortBy
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOprAndResourceSortBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListOprAndResourceSortBy(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListOprAndResourceSortBy_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListOprAndResourceSortBy", {
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
         resolve(data as ListOprAndResourceSortBy_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListPartCostingMethod
   Description: Returns the list of available costing methods for a part.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListPartCostingMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListPartCostingMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListPartCostingMethod(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListPartCostingMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListPartCostingMethod", {
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
         resolve(data as ListPartCostingMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListPartSortBy
   Description: Returns the list for sort by options for parts.  The list is in code1`desc1~code2`desc2 format.
   OperationID: ListPartSortBy
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListPartSortBy_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListPartSortBy(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListPartSortBy_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListPartSortBy", {
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
         resolve(data as ListPartSortBy_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ListRates
   Description: Returns the list of available rates for Resource Groups and Operations.  The list is in
code1`desc1~code2`desc2 format.
   OperationID: ListRates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListRates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ListRates(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ListRates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ListRates", {
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
         resolve(data as ListRates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreCostRollUp
   Description: Pre-processing before the rolling up of costs for the group.
Check if there are unapproved revisions that are in the rollup criteria.  If
there are, return a message to the UI to ask the user if it is ok to proceed.  If
pcQuestion is blank, a question does not need to be asked.
   OperationID: PreCostRollUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreCostRollUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCostRollUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCostRollUp(requestBody:PreCostRollUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreCostRollUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/PreCostRollUp", {
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
         resolve(data as PreCostRollUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RefreshCosts
   Description: This method refreshes the costs for the Cost Group.
   OperationID: RefreshCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RefreshCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshCosts(requestBody:RefreshCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RefreshCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/RefreshCosts", {
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
         resolve(data as RefreshCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ViewCosts
   Description: This method will return the data need to display Part Rev costs.
   OperationID: ViewCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ViewCosts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ViewCosts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ViewCosts(requestBody:ViewCosts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ViewCosts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/ViewCosts", {
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
         resolve(data as ViewCosts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostGrp(requestBody:GetNewCostGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetNewCostGrp", {
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
         resolve(data as GetNewCostGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostBurden
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostBurden
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostBurden_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostBurden_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostBurden(requestBody:GetNewCostBurden_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostBurden_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetNewCostBurden", {
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
         resolve(data as GetNewCostBurden_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostLabor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostLabor
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostLabor(requestBody:GetNewCostLabor_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostLabor_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetNewCostLabor", {
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
         resolve(data as GetNewCostLabor_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCostPart
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCostPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCostPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCostPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCostPart(requestBody:GetNewCostPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCostPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetNewCostPart", {
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
         resolve(data as GetNewCostPart_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CostWorkBenchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostBurdenRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostBurdenRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostGrpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostLaborRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostLaborRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CostPartRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CostPartRow,
}

export interface Erp_Tablesets_CostBurdenRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  Indicates the source table name of the labor rates.  */  
   "RateSourceTableName":string,
      /**  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  */  
   "SourceID":string,
      /**  The description of SourceID.  Will be the description from Resource or ResourceGroup.  */  
   "Description":string,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   "BurdenType":string,
      /**  The burden rate for production.  */  
   "ProdBurRate":number,
      /**  Default burden rate for Setup time.  */  
   "SetupBurRate":number,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   "Linked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DispTableName":string,
   "BurdenDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CostGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  Description  */  
   "Description":string,
      /**  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  */  
   "BOMRollupDate":string,
      /**  The user ID that created this cost group.  */  
   "CreatedBy":string,
      /**  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  */  
   "CostMethod":string,
      /**   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   "LastPartRefresh":string,
      /**  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   "LastWCRefresh":string,
      /**  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   "Burden":string,
      /**  Indicated the group has been posted.  */  
   "Posted":boolean,
      /**  The user ID that posted this cost group.  */  
   "PostedBy":string,
      /**  Group posted date.  */  
   "PostedDate":string,
      /**  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   "Labor":string,
      /**  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  */  
   "LastOPRefresh":string,
      /**  The primary Site for the cost group.  */  
   "PrimaryPlant":string,
      /**  Load Alternate Method  */  
   "LoadAltMethod":boolean,
      /**  Load Costing Lot Sizes  */  
   "LoadCostLot":boolean,
      /**  The Site Cost ID to copy costs from  */  
   "CopyFromPlantCostID":string,
      /**  The Cost Group to copy costs from  */  
   "CopyFromGroupID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CopyFromGroupDesc":string,
   "EnableCostMethod":boolean,
   "InternalPricePctChange":number,
      /**  Description  */  
   "CopyFromPlantCostDescription":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CostGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  Description  */  
   "Description":string,
      /**  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  */  
   "BOMRollupDate":string,
      /**  The user ID that created this cost group.  */  
   "CreatedBy":string,
      /**  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  */  
   "CostMethod":string,
      /**   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   "Comment":string,
      /**  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   "LastPartRefresh":string,
      /**  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   "LastWCRefresh":string,
      /**  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   "Burden":string,
      /**  Indicated the group has been posted.  */  
   "Posted":boolean,
      /**  The user ID that posted this cost group.  */  
   "PostedBy":string,
      /**  Group posted date.  */  
   "PostedDate":string,
      /**  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   "Labor":string,
      /**  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  */  
   "LastOPRefresh":string,
      /**  The primary Site for the cost group.  */  
   "PrimaryPlant":string,
      /**  Load Alternate Method  */  
   "LoadAltMethod":boolean,
      /**  Load Costing Lot Sizes  */  
   "LoadCostLot":boolean,
      /**  The Site Cost ID to copy costs from  */  
   "CopyFromPlantCostID":string,
      /**  The Cost Group to copy costs from  */  
   "CopyFromGroupID":string,
      /**  Flag used to indicate the status of the Import Rates process, if it finished succesfully for the Costing WorkBench Group or did not  */  
   "DEImportRateStatus":boolean,
      /**  Flag used to indicate that the Import Rates process is active  */  
   "DEImpRtsLockStatus":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CopyFromGroupDesc":string,
      /**  DE Rates Imported flag  */  
   "DERatesImported":boolean,
   "EnableCostMethod":boolean,
   "InternalPricePctChange":number,
   "BitFlag":number,
   "CopyFromPlantCostDescription":string,
   "PlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CostLaborRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  Indicates the source table name of the labor rates.  */  
   "RateSourceTableName":string,
      /**  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  */  
   "SourceID":string,
      /**  The description of SourceID.  Will be the description from Resource or ResourceGroup.  */  
   "Description":string,
      /**  The labor rate used for setup time.  */  
   "SetupLRate":number,
      /**  Labor rate used for production time on an operation.  */  
   "ProdLRate":number,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   "Linked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DispTableName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CostPartRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   "GroupID":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   "SearchWord":string,
      /**  Describes the Part.  This field can not be blank.  */  
   "PartDescription":string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   "ClassID":string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   "TypeCode":string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   "ProdCode":string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   "StdLaborCost":number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   "StdBurdenCost":number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   "StdMaterialCost":number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   "StdSubContCost":number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   "StdMtlBurCost":number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   "RevisionNum":string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   "EffectiveDate":string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRLaborCost":number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRBurdenCost":number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMaterialCost":number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRSubcontractCost":number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   "TLRMtlBurCost":number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   "TLRSetupLaborCost":number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "TLRSetupBurdenCost":number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRLaborCost":number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRBurdenCost":number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMaterialCost":number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRSubcontractCost":number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   "LLRMtlBurCost":number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   "LLRSetupLaborCost":number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   "LLRSetupBurdenCost":number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   "RollupDate":string,
      /**  Alternate Routing method to be used for this revision.  */  
   "AltMethod":string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   "Linked":boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   "MfgLotSize":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrimCostPart  */  
   "PrimCostPart":string,
      /**  PrimCostRev  */  
   "PrimCostRev":string,
      /**  PrimCostAltMethod  */  
   "PrimCostAltMethod":string,
      /**  CoPartsReqQty  */  
   "CoPartsReqQty":number,
      /**  MtlCostPct  */  
   "MtlCostPct":number,
      /**  LaborCostPct  */  
   "LaborCostPct":number,
      /**  OrigStdMaterialCost  */  
   "OrigStdMaterialCost":number,
      /**  OrigStdLaborCost  */  
   "OrigStdLaborCost":number,
      /**  OrigStdBurdenCost  */  
   "OrigStdBurdenCost":number,
      /**  OrigStdSubContCost  */  
   "OrigStdSubContCost":number,
      /**  OrigStdMtlBurCost  */  
   "OrigStdMtlBurCost":number,
      /**  IsTransferCostID  */  
   "IsTransferCostID":boolean,
   "ApprovedMethod":boolean,
   "CurrentRevDescription":string,
   "CurrentRevisionNum":string,
   "IsMethod":boolean,
   "LastMaterialCost":number,
   "BitFlag":number,
   "GroupIDDescription":string,
   "ProdCodeDescription":string,
   "RevisionNumRevDescription":string,
   "RevisionNumRevShortDesc":string,
   "RevisionNumPartDescription":string,
   "TypeCodeTypeDescription":string,
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
      @param ProposedPlantCostID
      @param ds
   */  
export interface ChangeCWBPostPostToPlantCostID_input{
      /**  The proposed plant cost id  */  
   ProposedPlantCostID:string,
   ds:Erp_Tablesets_CostWorkBenchPostTableset[],
}

export interface ChangeCWBPostPostToPlantCostID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchPostTableset,
}
}

   /** Required : 
      @param ProposedGroupID
      @param ds
   */  
export interface ChangeCopyFromGroupID_input{
      /**  The proposed plant cost id  */  
   ProposedGroupID:string,
   ds:Erp_Tablesets_CostWorkBenchTableset[],
}

export interface ChangeCopyFromGroupID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ProposedPlantCostID
      @param ds
   */  
export interface ChangeCopyFromPlantCostID_input{
      /**  The proposed plant cost id  */  
   ProposedPlantCostID:string,
   ds:Erp_Tablesets_CostWorkBenchTableset[],
}

export interface ChangeCopyFromPlantCostID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ProposedPlant
      @param ds
   */  
export interface ChangePrimaryPlant_input{
      /**  The proposed plant  */  
   ProposedPlant:string,
   ds:Erp_Tablesets_CostWorkBenchTableset[],
}

export interface ChangePrimaryPlant_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CostPost_input{
   ds:Erp_Tablesets_CostWorkBenchPostTableset[],
}

export interface CostPost_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchPostTableset,
   pcCostsNotUpdatedMsg:string,
   pcLegalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CostRollUp_input{
   ds:Erp_Tablesets_CostWorkBenchRollUpTableset[],
}

export interface CostRollUp_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchRollUpTableset,
   pcPartsNotUpdatedMsg:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface DEGetImportRatesLockStatus_input{
   groupID:string,
}

export interface DEGetImportRatesLockStatus_output{
   returnObj:boolean,
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CostBurdenRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  Indicates the source table name of the labor rates.  */  
   RateSourceTableName:string,
      /**  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  */  
   SourceID:string,
      /**  The description of SourceID.  Will be the description from Resource or ResourceGroup.  */  
   Description:string,
      /**  Indicates if the BurdenRate fields are either a flat hourly dollar rate or a percentage of LaborRate. Default is Hourly dollar rate.   Set to "F" (flat) or "P" (percent).  */  
   BurdenType:string,
      /**  The burden rate for production.  */  
   ProdBurRate:number,
      /**  Default burden rate for Setup time.  */  
   SetupBurRate:number,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   Linked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispTableName:string,
   BurdenDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  Description  */  
   Description:string,
      /**  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  */  
   BOMRollupDate:string,
      /**  The user ID that created this cost group.  */  
   CreatedBy:string,
      /**  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  */  
   CostMethod:string,
      /**   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   LastPartRefresh:string,
      /**  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   LastWCRefresh:string,
      /**  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   Burden:string,
      /**  Indicated the group has been posted.  */  
   Posted:boolean,
      /**  The user ID that posted this cost group.  */  
   PostedBy:string,
      /**  Group posted date.  */  
   PostedDate:string,
      /**  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   Labor:string,
      /**  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  */  
   LastOPRefresh:string,
      /**  The primary Site for the cost group.  */  
   PrimaryPlant:string,
      /**  Load Alternate Method  */  
   LoadAltMethod:boolean,
      /**  Load Costing Lot Sizes  */  
   LoadCostLot:boolean,
      /**  The Site Cost ID to copy costs from  */  
   CopyFromPlantCostID:string,
      /**  The Cost Group to copy costs from  */  
   CopyFromGroupID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CopyFromGroupDesc:string,
   EnableCostMethod:boolean,
   InternalPricePctChange:number,
      /**  Description  */  
   CopyFromPlantCostDescription:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostGrpListTableset{
   CostGrpList:Erp_Tablesets_CostGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  Description  */  
   Description:string,
      /**  Used as the effectivity date that will include the BOM revision that is in effect as of that date.  */  
   BOMRollupDate:string,
      /**  The user ID that created this cost group.  */  
   CreatedBy:string,
      /**  Defines the Costing method to be associated with this Cost Group.   When using this cost group all the Cost Set Parts will use this field to determine which one of the four sets of cost fields should be used.  A = Use Average, L= Use Last, S = Use Standard, C = Costing method for the part, T = Use Lot.  */  
   CostMethod:string,
      /**   Cost Group Comments that can be used to define this cost set.  View as an EDITOR widget.
To be view-as EDITOR widget.  */  
   Comment:string,
      /**  The date the Cost group parts were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   LastPartRefresh:string,
      /**  The date the Cost group work centers were last refreshed.  This is saved since only the parts available at the time the group is created or last refreshed  will be part of the cost part set.  */  
   LastWCRefresh:string,
      /**  Specifies the Burden Rate to be used when geting work center costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   Burden:string,
      /**  Indicated the group has been posted.  */  
   Posted:boolean,
      /**  The user ID that posted this cost group.  */  
   PostedBy:string,
      /**  Group posted date.  */  
   PostedDate:string,
      /**  Specifies the Labor Rate to be used when geting operation costs for this Cost Group.    C = Cost, Q = Quoting.  */  
   Labor:string,
      /**  The date the Cost group operations were last refreshed.  This is saved since only the operations available at the time the group is created or last refreshed  will be part of the cost operation set.  */  
   LastOPRefresh:string,
      /**  The primary Site for the cost group.  */  
   PrimaryPlant:string,
      /**  Load Alternate Method  */  
   LoadAltMethod:boolean,
      /**  Load Costing Lot Sizes  */  
   LoadCostLot:boolean,
      /**  The Site Cost ID to copy costs from  */  
   CopyFromPlantCostID:string,
      /**  The Cost Group to copy costs from  */  
   CopyFromGroupID:string,
      /**  Flag used to indicate the status of the Import Rates process, if it finished succesfully for the Costing WorkBench Group or did not  */  
   DEImportRateStatus:boolean,
      /**  Flag used to indicate that the Import Rates process is active  */  
   DEImpRtsLockStatus:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CopyFromGroupDesc:string,
      /**  DE Rates Imported flag  */  
   DERatesImported:boolean,
   EnableCostMethod:boolean,
   InternalPricePctChange:number,
   BitFlag:number,
   CopyFromPlantCostDescription:string,
   PlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostLaborRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  Indicates the source table name of the labor rates.  */  
   RateSourceTableName:string,
      /**  The source id of the record the rates came from.  Will be either ResourceGrpID or ResourceID.  */  
   SourceID:string,
      /**  The description of SourceID.  Will be the description from Resource or ResourceGroup.  */  
   Description:string,
      /**  The labor rate used for setup time.  */  
   SetupLRate:number,
      /**  Labor rate used for production time on an operation.  */  
   ProdLRate:number,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   Linked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DispTableName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostPartRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A Cost Set Group ID is required for each cost set.  A Cost Set works with a copy of the costs for all parts.  */  
   GroupID:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  An abbreviated part description field by which the user can search the Part file. During Part maintenance a change to the Part.Description field causes this field to be updated with the first 8 bytes of the Part.Description.  */  
   SearchWord:string,
      /**  Describes the Part.  This field can not be blank.  */  
   PartDescription:string,
      /**   The Inventory class that this Part belongs to. The Class field can be blank or must be valid in the PartClass master file.
Classes could be set up for different type of raw materials.  */  
   ClassID:string,
      /**   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part
This type code does limit referencing any part in any way. For example a type "P" can be entered on a sales order, or a type "M" can be referenced in a Purchase Order.
This field will also be used as a selection parameter in certain reports, such as Time Phase Requirements.  */  
   TypeCode:string,
      /**  Product Group ID for the Cost Part. This can be blank or must be valid in the ProdGrup file.  This will be used for report sorting and selection.  */  
   ProdCode:string,
      /**   Standard Unit Labor Cost. Standard costs are directly maintainable via the Part Maintenance Program or indirectly by Bill of Material cost rollup program.

(See AvgLaborCost for more info.)  */  
   StdLaborCost:number,
      /**   Standard Burden Unit Cost.

( see StdLaborCost for more info )  */  
   StdBurdenCost:number,
      /**   Standard Material Unit cost.

( see StdLaborCost for more info).  */  
   StdMaterialCost:number,
      /**   Standard Subcontract Unit cost.
( see StdLaborCost for more info).  */  
   StdSubContCost:number,
      /**   Standard Material Burden Unit cost.
( see StdLaborCost for more info).  */  
   StdMtlBurCost:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  This was the revision used when the rollup was run.  If this field is blank the part is not part of the rollup processing and will not be posted.  */  
   RevisionNum:string,
      /**  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  */  
   EffectiveDate:string,
      /**  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRLaborCost:number,
      /**   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRBurdenCost:number,
      /**  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMaterialCost:number,
      /**  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRSubcontractCost:number,
      /**  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  */  
   TLRMtlBurCost:number,
      /**  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  */  
   TLRSetupLaborCost:number,
      /**   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   TLRSetupBurdenCost:number,
      /**  Lower Level Unit Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRLaborCost:number,
      /**   Lower Level Unit Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRBurdenCost:number,
      /**  Lower Level Unit Material Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMaterialCost:number,
      /**  Lower Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRSubcontractCost:number,
      /**  Lower Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "Lower level" cost excludes costs from sub assemblies.  */  
   LLRMtlBurCost:number,
      /**  Lower Level Setup Labor Cost calculated by the BOM Cost rollup routine. Lower level cost excludes costs from sub assemblies.  */  
   LLRSetupLaborCost:number,
      /**   Lower Level Setup Burden Cost calculated by the BOM Cost rollup routine. "Lower level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  */  
   LLRSetupBurdenCost:number,
      /**  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  */  
   RollupDate:string,
      /**  Alternate Routing method to be used for this revision.  */  
   AltMethod:string,
      /**  For display purposes only.  Indicates if the record is linked to any of the manufactured parts in the CostPart table (CostPart.TypeCode = M).  CostPart, CostBurden, and CostLabor records are created based on the method of manufacturing of a part, but they can also be created regardless of the method of manufacturing.  A record is considered linked if it is used in the method of manufacturing structure of a manufactured part.  */  
   Linked:boolean,
      /**  This is the lot size that is used when performing a BOM cost rollup to distribute setup costs.  */  
   MfgLotSize:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrimCostPart  */  
   PrimCostPart:string,
      /**  PrimCostRev  */  
   PrimCostRev:string,
      /**  PrimCostAltMethod  */  
   PrimCostAltMethod:string,
      /**  CoPartsReqQty  */  
   CoPartsReqQty:number,
      /**  MtlCostPct  */  
   MtlCostPct:number,
      /**  LaborCostPct  */  
   LaborCostPct:number,
      /**  OrigStdMaterialCost  */  
   OrigStdMaterialCost:number,
      /**  OrigStdLaborCost  */  
   OrigStdLaborCost:number,
      /**  OrigStdBurdenCost  */  
   OrigStdBurdenCost:number,
      /**  OrigStdSubContCost  */  
   OrigStdSubContCost:number,
      /**  OrigStdMtlBurCost  */  
   OrigStdMtlBurCost:number,
      /**  IsTransferCostID  */  
   IsTransferCostID:boolean,
   ApprovedMethod:boolean,
   CurrentRevDescription:string,
   CurrentRevisionNum:string,
   IsMethod:boolean,
   LastMaterialCost:number,
   BitFlag:number,
   GroupIDDescription:string,
   ProdCodeDescription:string,
   RevisionNumRevDescription:string,
   RevisionNumRevShortDesc:string,
   RevisionNumPartDescription:string,
   TypeCodeTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWBInternalPricesPartsRow{
   Company:string,
   GroupID:string,
   PctChg:number,
   WorkstationID:string,
   DateFormat:string,
   NumericFormat:string,
   Action:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWBInternalPricesTableset{
   CostWBInternalPricesParts:Erp_Tablesets_CostWBInternalPricesPartsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchCostSetRow{
   GroupID:string,
   EffectivityDate:string,
   LastPartRefreshDate:string,
   GetManufacturingParts:boolean,
   GetPurchasedParts:boolean,
   GetOperations:boolean,
   GetResourceGroups:boolean,
   RefreshAllCosts:boolean,
   PartList:string,
   ProdGroupList:string,
   PartClassList:string,
   PartCostMethod:string,
   BurdenCostMethod:string,
   LaborCostMethod:string,
   GetUnlinkedPurchasedParts:boolean,
   GetUnlinkedRates:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWorkBenchCostSetTableset{
   CostWorkBenchCostSet:Erp_Tablesets_CostWorkBenchCostSetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchCostsTableset{
   PartRevCosts:Erp_Tablesets_PartRevCostsRow[],
   PartRevCostsDetail:Erp_Tablesets_PartRevCostsDetailRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchPostPlantsRow{
   GroupID:string,
   Plant:string,
   Name:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWorkBenchPostRow{
   GroupID:string,
      /**  Delimited list of Parts to run the post for  */  
   PartList:string,
      /**  Delimited list of Prod Groups to run the rollup for  */  
   ProdGrupList:string,
      /**  Delimited list of Part Classes to run the rollup for  */  
   PartClassList:string,
   ReasonCode:string,
   EnableReasonCode:boolean,
   PostToPlantCostID:string,
   PostBurden:boolean,
   PostLabor:boolean,
   ReasonCodeDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWorkBenchPostTableset{
   CostWorkBenchPost:Erp_Tablesets_CostWorkBenchPostRow[],
   CostWorkBenchPostPlants:Erp_Tablesets_CostWorkBenchPostPlantsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchRefreshRow{
   GroupID:string,
   RefreshPurchasedParts:boolean,
   PartCostMethod:string,
   RefreshLaborRates:boolean,
   LaborCostMethod:string,
   RefreshBurdenRates:boolean,
   BurdenCostMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWorkBenchRefreshTableset{
   CostWorkBenchRefresh:Erp_Tablesets_CostWorkBenchRefreshRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchRollUpRow{
   GroupID:string,
   EffectivityDate:string,
      /**  Delimited list of Parts to run the rollup for  */  
   PartList:string,
      /**  Delimited list of Product Groups to run the rollup for  */  
   ProdGrupList:string,
      /**  Delimited list of Part Classes to run the rollup for  */  
   PartClassList:string,
   ConsiderPullAsAsmSettings:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CostWorkBenchRollUpTableset{
   CostWorkBenchRollUp:Erp_Tablesets_CostWorkBenchRollUpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CostWorkBenchTableset{
   CostGrp:Erp_Tablesets_CostGrpRow[],
   CostBurden:Erp_Tablesets_CostBurdenRow[],
   CostLabor:Erp_Tablesets_CostLaborRow[],
   CostPart:Erp_Tablesets_CostPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartRevCostsDetailRow{
      /**  The part number.  */  
   PartNum:string,
      /**  The revision number  */  
   RevisionNum:string,
      /**  The quantity  */  
   Quantity:number,
      /**  Is this approved?  */  
   Approved:boolean,
      /**  The BOM type  */  
   BOMType:string,
      /**  The BOM Level  */  
   BOMLevel:number,
      /**  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  */  
   MtlRevision:string,
      /**  The Part Number of the component material record for the related Parent Part.  */  
   MtlPartNum:string,
      /**  The material cost  */  
   MaterialCost:number,
      /**  The labor cost  */  
   LaborCost:number,
      /**  The burden cost  */  
   BurdenCost:number,
      /**  The subcontract cost  */  
   SubcontractCost:number,
      /**  The material burden cost  */  
   MaterialBurdenCost:number,
      /**  The total cost  */  
   TotalCost:number,
      /**  The material unit cost  */  
   MaterialUnitCost:number,
      /**  The labor unit cost  */  
   LaborUnitCost:number,
      /**  The burden unit cost  */  
   BurdenUnitCost:number,
      /**  The subcontract unit cost  */  
   SubcontractUnitCost:number,
      /**  The material burden unit cost  */  
   MaterialBurdenUnitCost:number,
      /**  The total unit cost  */  
   TotalUnitCost:number,
      /**  The quantity per parent  */  
   QtyPer:number,
      /**  The required quantity  */  
   RequiredQty:number,
      /**  The description of the part  */  
   PartDescription:string,
      /**  The effective date  */  
   EffectiveDate:string,
      /**  The BOM Sequence  */  
   BomSequence:number,
      /**  The company id.  */  
   Company:string,
      /**  The Alternate Method  */  
   AltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartRevCostsRow{
      /**  The company id.  */  
   Company:string,
      /**  The part number  */  
   PartNum:string,
      /**  The effective date  */  
   EffectiveDate:string,
      /**  The maximum level  */  
   MaxLevel:number,
      /**  Assemblies Only flag  */  
   AssembliesOnly:boolean,
      /**  The quantity  */  
   Quantity:number,
      /**  The material total cost.  */  
   MaterialTotalCost:number,
      /**  The material unit cost  */  
   MaterialUnitCost:number,
      /**  The material part cost  */  
   MaterialPartCost:number,
      /**  The labor total cost  */  
   LaborTotalCost:number,
      /**  The unit cost of labor  */  
   LaborUnitCost:number,
      /**  The part cost of labor  */  
   LaborPartCost:number,
      /**  The burden total cost  */  
   BurdenTotalCost:number,
      /**  The burden unit cost  */  
   BurdenUnitCost:number,
      /**  The burden part cost  */  
   BurdenPartCost:number,
      /**  The subcontract total cost  */  
   SubcontractTotalCost:number,
      /**  The subcontract unit cost  */  
   SubcontractUnitCost:number,
      /**  The subcontract part cost  */  
   SubcontractPartCost:number,
      /**  The material burden total cost  */  
   MtlBurdenTotalCost:number,
      /**  The material burden unit cost  */  
   MtlBurdenUnitCost:number,
      /**  The material burden part cost  */  
   MtlBurdenPartCost:number,
      /**  The cost method label  */  
   CostMethodLabel:string,
      /**  The revision number.  */  
   RevisionNum:string,
      /**  The alternate method  */  
   AltMethod:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCostWorkBenchTableset{
   CostGrp:Erp_Tablesets_CostGrpRow[],
   CostBurden:Erp_Tablesets_CostBurdenRow[],
   CostLabor:Erp_Tablesets_CostLaborRow[],
   CostPart:Erp_Tablesets_CostPartRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetCostSet_input{
   ds:Erp_Tablesets_CostWorkBenchCostSetTableset[],
}

export interface GetCostSet_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchCostSetTableset,
   cReturnMessage:string,
}
}

   /** Required : 
      @param cGroupID
   */  
export interface GetCostWBInternalPrices_input{
      /**  The Group ID  */  
   cGroupID:string,
}

export interface GetCostWBInternalPrices_output{
   returnObj:Erp_Tablesets_CostWBInternalPricesTableset[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetCostWorkBenchCostSet_input{
      /**  The Group ID  */  
   cGroupID:string,
}

export interface GetCostWorkBenchCostSet_output{
   returnObj:Erp_Tablesets_CostWorkBenchCostSetTableset[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetCostWorkBenchPost_input{
      /**  The Group ID  */  
   cGroupID:string,
}

export interface GetCostWorkBenchPost_output{
   returnObj:Erp_Tablesets_CostWorkBenchPostTableset[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetCostWorkBenchRefresh_input{
      /**  The Group ID  */  
   cGroupID:string,
}

export interface GetCostWorkBenchRefresh_output{
   returnObj:Erp_Tablesets_CostWorkBenchRefreshTableset[],
}

   /** Required : 
      @param cGroupID
   */  
export interface GetCostWorkBenchRollUp_input{
      /**  The Group ID  */  
   cGroupID:string,
}

export interface GetCostWorkBenchRollUp_output{
   returnObj:Erp_Tablesets_CostWorkBenchRollUpTableset[],
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
   returnObj:Erp_Tablesets_CostGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param rateSourceTableName
   */  
export interface GetNewCostBurden_input{
   ds:Erp_Tablesets_CostWorkBenchTableset[],
   groupID:string,
   rateSourceTableName:string,
}

export interface GetNewCostBurden_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCostGrp_input{
   ds:Erp_Tablesets_CostWorkBenchTableset[],
}

export interface GetNewCostGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param rateSourceTableName
   */  
export interface GetNewCostLabor_input{
   ds:Erp_Tablesets_CostWorkBenchTableset[],
   groupID:string,
   rateSourceTableName:string,
}

export interface GetNewCostLabor_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ds
      @param groupID
      @param typeCode
   */  
export interface GetNewCostPart_input{
   ds:Erp_Tablesets_CostWorkBenchTableset[],
   groupID:string,
   typeCode:string,
}

export interface GetNewCostPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param whereClauseCostGrp
      @param whereClauseCostBurden
      @param whereClauseCostLabor
      @param whereClauseCostPart
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCostGrp:string,
   whereClauseCostBurden:string,
   whereClauseCostLabor:string,
   whereClauseCostPart:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
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

export interface ListCostingEdits_output{
parameters : {
      /**  output parameters  */  
   cCostingEditList:string,
}
}

export interface ListFilters_output{
parameters : {
      /**  output parameters  */  
   cFilterList:string,
}
}

export interface ListOprAndResourceSortBy_output{
parameters : {
      /**  output parameters  */  
   cOprResourceSortByList:string,
}
}

export interface ListPartCostingMethod_output{
parameters : {
      /**  output parameters  */  
   cPartCostingMethodList:string,
}
}

export interface ListPartSortBy_output{
parameters : {
      /**  output parameters  */  
   cPartSortByList:string,
}
}

export interface ListRates_output{
parameters : {
      /**  output parameters  */  
   cRatesList:string,
}
}

   /** Required : 
      @param ds
   */  
export interface PreCostRollUp_input{
   ds:Erp_Tablesets_CostWorkBenchRollUpTableset[],
}

export interface PreCostRollUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchRollUpTableset,
   pcQuestion:string,
}
}

   /** Required : 
      @param ds
   */  
export interface RefreshCosts_input{
   ds:Erp_Tablesets_CostWorkBenchRefreshTableset[],
}

export interface RefreshCosts_output{
   returnObj:Erp_Tablesets_CostWorkBenchTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchRefreshTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCostWorkBenchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCostWorkBenchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CostWorkBenchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CostWorkBenchTableset,
}
}

   /** Required : 
      @param ipGroupID
      @param ipTypeCode
      @param ipPartNum
      @param ipQuantity
      @param ipMaxLevel
      @param ipAssembliesOnly
   */  
export interface ViewCosts_input{
      /**  The Cost Group ID to return costs for.  */  
   ipGroupID:string,
      /**  The Type Code of the Part to return costs for (CostPart.TypeCode).  */  
   ipTypeCode:string,
      /**  The Part Number to return costs for.  */  
   ipPartNum:string,
      /**  The Quantity to return costs for.  */  
   ipQuantity:number,
      /**  The Max Level to return costs for.  */  
   ipMaxLevel:number,
      /**  Assemblies only  */  
   ipAssembliesOnly:boolean,
}

export interface ViewCosts_output{
   returnObj:Erp_Tablesets_CostWorkBenchCostsTableset[],
}

