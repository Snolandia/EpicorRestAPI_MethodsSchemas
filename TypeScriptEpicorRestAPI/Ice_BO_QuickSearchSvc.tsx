import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Ice.BO.QuickSearchSvc
// Description: Provide a way to define and run a user-defined search
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/$metadata", {
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
   Description: Get QuickSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchRow
   */  
export function get_QuickSearches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches", {
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
   Summary: Calls GetByID to retrieve the QuickSearch item
   Description: Calls GetByID to retrieve the QuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   */  
export function get_QuickSearches_Company_GlbCompany_QuickSearchID(Company:string, GlbCompany:string, QuickSearchID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuickSearchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuickSearchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickSearch for the service
   Description: Calls UpdateExt to update QuickSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickSearches_Company_GlbCompany_QuickSearchID(Company:string, GlbCompany:string, QuickSearchID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")", {
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
   Summary: Call UpdateExt to delete QuickSearch item
   Description: Call UpdateExt to delete QuickSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickSearches_Company_GlbCompany_QuickSearchID(Company:string, GlbCompany:string, QuickSearchID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")", {
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
   Description: Get QuickSearchCriterias items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickSearchCriterias1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchCriteriaRow
   */  
export function get_QuickSearches_Company_GlbCompany_QuickSearchID_QuickSearchCriterias(Company:string, GlbCompany:string, QuickSearchID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")/QuickSearchCriterias", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuickSearchCriteria item
   Description: Calls GetByID to retrieve the QuickSearchCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchCriteria1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   */  
export function get_QuickSearches_Company_GlbCompany_QuickSearchID_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuickSearchCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuickSearchCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuickSearchCriterias items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearchCriterias
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchCriteriaRow
   */  
export function get_QuickSearchCriterias(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearchCriterias
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickSearchCriterias(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias", {
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
   Summary: Calls GetByID to retrieve the QuickSearchCriteria item
   Description: Calls GetByID to retrieve the QuickSearchCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   */  
export function get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuickSearchCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuickSearchCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickSearchCriteria for the service
   Description: Calls UpdateExt to update QuickSearchCriteria. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearchCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete QuickSearchCriteria item
   Description: Call UpdateExt to delete QuickSearchCriteria item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearchCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")", {
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
   Description: Get QuickSearchValueLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickSearchValueLists1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchValueListRow
   */  
export function get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq_QuickSearchValueLists(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")/QuickSearchValueLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuickSearchValueList item
   Description: Calls GetByID to retrieve the QuickSearchValueList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchValueList1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param ValueSeq Desc: ValueSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   */  
export function get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, ValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuickSearchValueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuickSearchValueListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuickSearchValueLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearchValueLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchValueListRow
   */  
export function get_QuickSearchValueLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearchValueLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QuickSearchValueLists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists", {
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
   Summary: Calls GetByID to retrieve the QuickSearchValueList item
   Description: Calls GetByID to retrieve the QuickSearchValueList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchValueList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param ValueSeq Desc: ValueSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   */  
export function get_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, ValueSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuickSearchValueListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Ice_Tablesets_QuickSearchValueListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QuickSearchValueList for the service
   Description: Calls UpdateExt to update QuickSearchValueList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearchValueList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param ValueSeq Desc: ValueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, ValueSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")", {
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
   Summary: Call UpdateExt to delete QuickSearchValueList item
   Description: Call UpdateExt to delete QuickSearchValueList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearchValueList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param QuickSearchID Desc: QuickSearchID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param ValueSeq Desc: ValueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company:string, GlbCompany:string, QuickSearchID:string, Seq:string, ValueSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchListRow)
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
export function get_GetRows(whereClauseQuickSearch:string, whereClauseQuickSearchCriteria:string, whereClauseQuickSearchValueList:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseQuickSearch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickSearch=" + whereClauseQuickSearch
   }
   if(typeof whereClauseQuickSearchCriteria!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickSearchCriteria=" + whereClauseQuickSearchCriteria
   }
   if(typeof whereClauseQuickSearchValueList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuickSearchValueList=" + whereClauseQuickSearchValueList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetRows" + params, {
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(glbCompany:string, quickSearchID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof glbCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbCompany=" + glbCompany
   }
   if(typeof quickSearchID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "quickSearchID=" + quickSearchID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetBAQConstants
   Description: Returns BAQ constant names in an untyped dataset
   OperationID: GetBAQConstants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQConstants_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBAQConstants(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetBAQConstants", {
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
   Summary: Invoke method BAQExists
   Description: This method returns a list of quick searches for this user
   OperationID: BAQExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/BAQExists", {
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
   Summary: Invoke method BAQsExist
   Description: This method returns a dataset of quick searches indicating if a BAQ exists
for each Quick Search
   OperationID: BAQsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQsExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BAQsExist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/BAQsExist", {
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
   Summary: Invoke method CopyQuickSearch
   Description: This method copies a quick search
   OperationID: CopyQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyQuickSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/CopyQuickSearch", {
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
   Summary: Invoke method GetBaseDefault
   Description: This method returns a quick search dataset with the given like field and call from name.
   OperationID: GetBaseDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaseDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBaseDefault(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetBaseDefault", {
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
   Summary: Invoke method GetContextDefault
   Description: This method returns a quick search dataset with the given like field and call from name.
   OperationID: GetContextDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContextDefault(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetContextDefault", {
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
   Summary: Invoke method GetUserQuickSearches
   Description: This method returns a list of quick searches for this user
   OperationID: GetUserQuickSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserQuickSearches_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetUserQuickSearches(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetUserQuickSearches", {
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
   Summary: Invoke method GetVersion
   Description: This method returns the version code of a quick searches
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetVersion(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetVersion", {
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
   Summary: Invoke method GetLikeFieldSearches
   Description: This method returns a list of quick searches for a like field
A like field has a format of table.field
   OperationID: GetLikeFieldSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLikeFieldSearches_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeFieldSearches_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLikeFieldSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetLikeFieldSearches", {
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
   Summary: Invoke method GetListForBAQ
   Description: This method returns a list of quick searches that use a given BAQ
   OperationID: GetListForBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForBAQ(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetListForBAQ", {
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
   Summary: Invoke method RunQuickSearch
   Description: This method runs a quick search based on a QuickSearchDataSet.
   OperationID: RunQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunQuickSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/RunQuickSearch", {
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
   Summary: Invoke method RunQuickSearchPaged
   Description: This method runs a quick search based on a QuickSearchDataSet.
   OperationID: RunQuickSearchPaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunQuickSearchPaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunQuickSearchPaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunQuickSearchPaged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/RunQuickSearchPaged", {
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
   Summary: Invoke method GetNewQuickSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickSearch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetNewQuickSearch", {
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
   Summary: Invoke method GetNewQuickSearchCriteria
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearchCriteria
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearchCriteria_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearchCriteria_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickSearchCriteria(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetNewQuickSearchCriteria", {
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
   Summary: Invoke method GetNewQuickSearchValueList
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearchValueList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearchValueList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearchValueList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQuickSearchValueList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetNewQuickSearchValueList", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuickSearchCriteriaRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuickSearchListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuickSearchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuickSearchValueListRow[],
}

export interface Ice_Tablesets_QuickSearchCriteriaRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for this quick search  */  
   "QuickSearchID":string,
      /**  Global Record  */  
   "GlbCompany":string,
   "Seq":number,
      /**  The DataTableID this column bolongs to. If blank then this column is a calculated column.  */  
   "DataTableID":string,
   "FieldName":string,
   "DataType":string,
   "FieldLabel":string,
      /**  Operator to use for relation between left value and right value.  */  
   "CompOp":string,
      /**   Indicating the type of this criteria: valid values are:
"prompt" - prompt for user input
"constant" - either a literal constant or a field from Conatants table, similar to BAQ  */  
   "CriteriaType":string,
      /**  Indicates that this column is the returned column that the original text field asks.  */  
   "IsReturnCol":boolean,
   "CriteriaValue":string,
   "FilterOnNull":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CriteriaField":string,
   "CriteriaLikeFieldName":string,
   "CriteriaLikeTableID":string,
      /**  The display format for this criteria column  */  
   "FieldFormat":string,
   "LikeField":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuickSearchListRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   "Company":string,
      /**  The unique identifier for this quick search  */  
   "QuickSearchID":string,
   "GlbCompany":string,
      /**  Description  */  
   "Description":string,
      /**  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  */  
   "UserID":string,
      /**  The unique export identifier.  */  
   "ExportID":string,
      /**  TableID to use with LikeField  */  
   "LikeDataFieldTableID":string,
   "LikeDataFieldName":string,
      /**  true if this search is available to all fields that have the same like table/field.  */  
   "GlobalSearch":boolean,
      /**  true if this quick search is for validating during data entry  */  
   "ForValidation":boolean,
   "IsShared":boolean,
      /**  Used for indicating this quick search is provided by system, not by an end user.  */  
   "SystemFlag":boolean,
      /**  TableID to of the returned column  */  
   "ReturnFieldTableID":string,
      /**  Field name of the returned column  */  
   "ReturnFieldName":string,
   "CallFrom":string,
   "ContextDefault":boolean,
   "BaseDefault":boolean,
   "Version":string,
   "HotKey":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  IsPredictive  */  
   "IsPredictive":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The combined return field name in the format of <table>.<field>  */  
   "ReturnField":string,
      /**  The combined like field name in the format of <table>.<field>  */  
   "LikeField":string,
      /**  The data type of the return column  */  
   "ReturnDataType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuickSearchRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   "Company":string,
      /**  The unique identifier for this quick search  */  
   "QuickSearchID":string,
   "GlbCompany":string,
      /**  Description  */  
   "Description":string,
      /**  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  */  
   "UserID":string,
      /**  The unique export identifier.  */  
   "ExportID":string,
      /**  TableID to use with LikeField  */  
   "LikeDataFieldTableID":string,
   "LikeDataFieldName":string,
      /**  true if this search is available to all fields that have the same like table/field.  */  
   "GlobalSearch":boolean,
      /**  true if this quick search is for validating during data entry  */  
   "ForValidation":boolean,
   "IsShared":boolean,
      /**  Used for indicating this quick search is provided by system, not by an end user.  */  
   "SystemFlag":boolean,
      /**  TableID to of the returned column  */  
   "ReturnFieldTableID":string,
      /**  Field name of the returned column  */  
   "ReturnFieldName":string,
   "CallFrom":string,
   "ContextDefault":boolean,
   "BaseDefault":boolean,
   "Version":string,
   "HotKey":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  IsPredictive  */  
   "IsPredictive":boolean,
      /**  SourceSystemCode  */  
   "SourceSystemCode":string,
      /**  SourceTableID  */  
   "SourceTableID":string,
      /**  SourceFieldName  */  
   "SourceFieldName":string,
      /**  SearchOnFieldSystemCode  */  
   "SearchOnFieldSystemCode":string,
      /**  SearchOnFieldTableID  */  
   "SearchOnFieldTableID":string,
      /**  SearchOnFieldName  */  
   "SearchOnFieldName":string,
      /**  SuppressBaseSearch  */  
   "SuppressBaseSearch":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The data type of the return column  */  
   "ReturnDataType":string,
      /**  The combined return field name in the format of <table>.<field>  */  
   "ReturnField":string,
      /**  The combined like field name in the format of <table>.<field>  */  
   "LikeField":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuickSearchValueListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The unique identifier for this quick search  */  
   "QuickSearchID":string,
      /**  Global Record  */  
   "GlbCompany":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Value Sequence  */  
   "ValueSeq":number,
      /**  Display Field  */  
   "DisplayMember":string,
      /**  Value Field  */  
   "ValueMember":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param quickSearchId
   */  
export interface BAQExists_input{
      /**  The identifier of the global company.  */  
   glbCompany:string,
      /**  The identifier of the quick search.  */  
   quickSearchId:string,
}

export interface BAQExists_output{
parameters : {
      /**  output parameters  */  
   baqExists:boolean,
}
}

   /** Required : 
      @param glbCompany
      @param ds
   */  
export interface BAQsExist_input{
      /**  The ID of the global company  */  
   glbCompany:string,
   ds:Ice_Tablesets_QuickSearchBAQsExistTableset[],
}

export interface BAQsExist_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QuickSearchBAQsExistTableset[],
}
}

   /** Required : 
      @param sourceQuickSearchId
      @param targetQuickSearchId
      @param targetQuickSearchDescription
   */  
export interface CopyQuickSearch_input{
      /**  The ID of source quick search  */  
   sourceQuickSearchId:string,
      /**  The ID of target quick search  */  
   targetQuickSearchId:string,
      /**  The description for the new quick search.  */  
   targetQuickSearchDescription:string,
}

export interface CopyQuickSearch_output{
parameters : {
      /**  output parameters  */  
   succeeded:boolean,
}
}

   /** Required : 
      @param glbCompany
      @param quickSearchID
   */  
export interface DeleteByID_input{
   glbCompany:string,
   quickSearchID:string,
}

export interface DeleteByID_output{
}

export interface GetBAQConstants_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param likeTableAndField
      @param callFrom
   */  
export interface GetBaseDefault_input{
      /**  The Like Field  */  
   likeTableAndField:string,
      /**  The name of the call from  */  
   callFrom:string,
}

export interface GetBaseDefault_output{
parameters : {
      /**  output parameters  */  
   baseSearchId:string,
}
}

   /** Required : 
      @param glbCompany
      @param quickSearchID
   */  
export interface GetByID_input{
   glbCompany:string,
   quickSearchID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_QuickSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_QuickSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_QuickSearchTableset[],
}

   /** Required : 
      @param likeTableAndField
      @param callFrom
   */  
export interface GetContextDefault_input{
      /**  The Like Field  */  
   likeTableAndField:string,
      /**  The name of the call from  */  
   callFrom:string,
}

export interface GetContextDefault_output{
parameters : {
      /**  output parameters  */  
   contextSearchId:string,
}
}

   /** Required : 
      @param likeTableAndField
   */  
export interface GetLikeFieldSearches_input{
      /**  The name of the like field  */  
   likeTableAndField:string,
}

export interface GetLikeFieldSearches_output{
   returnObj:Ice_Tablesets_QuickSearchListTableset[],
}

   /** Required : 
      @param baqId
   */  
export interface GetListForBAQ_input{
      /**  The BAQ ID  */  
   baqId:string,
}

export interface GetListForBAQ_output{
   returnObj:Ice_Tablesets_QuickSearchListTableset[],
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
   returnObj:Ice_Tablesets_QuickSearchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
      @param quickSearchID
   */  
export interface GetNewQuickSearchCriteria_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
   glbCompany:string,
   quickSearchID:string,
}

export interface GetNewQuickSearchCriteria_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QuickSearchTableset[],
}
}

   /** Required : 
      @param ds
      @param glbCompany
      @param quickSearchID
      @param seq
   */  
export interface GetNewQuickSearchValueList_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
   glbCompany:string,
   quickSearchID:string,
   seq:number,
}

export interface GetNewQuickSearchValueList_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QuickSearchTableset[],
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewQuickSearch_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
   glbCompany:string,
}

export interface GetNewQuickSearch_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QuickSearchTableset[],
}
}

   /** Required : 
      @param whereClauseQuickSearch
      @param whereClauseQuickSearchCriteria
      @param whereClauseQuickSearchValueList
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseQuickSearch:string,
   whereClauseQuickSearchCriteria:string,
   whereClauseQuickSearchValueList:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_QuickSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetUserQuickSearches_output{
   returnObj:Ice_Tablesets_QuickSearchListTableset[],
}

   /** Required : 
      @param glbCompany
      @param quickSearchId
   */  
export interface GetVersion_input{
      /**  The ID of the global company  */  
   glbCompany:string,
      /**  The ID of the quick search  */  
   quickSearchId:string,
}

export interface GetVersion_output{
parameters : {
      /**  output parameters  */  
   version:string,
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

export interface Ice_Tablesets_QuickSearchBAQsExistRow{
   QuickSearchID:string,
   BAQExist:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuickSearchBAQsExistTableset{
   QuickSearchBAQsExist:Ice_Tablesets_QuickSearchBAQsExistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QuickSearchCriteriaRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
      /**  Global Record  */  
   GlbCompany:string,
   Seq:number,
      /**  The DataTableID this column bolongs to. If blank then this column is a calculated column.  */  
   DataTableID:string,
   FieldName:string,
   DataType:string,
   FieldLabel:string,
      /**  Operator to use for relation between left value and right value.  */  
   CompOp:string,
      /**   Indicating the type of this criteria: valid values are:
"prompt" - prompt for user input
"constant" - either a literal constant or a field from Conatants table, similar to BAQ  */  
   CriteriaType:string,
      /**  Indicates that this column is the returned column that the original text field asks.  */  
   IsReturnCol:boolean,
   CriteriaValue:string,
   FilterOnNull:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CriteriaField:string,
   CriteriaLikeFieldName:string,
   CriteriaLikeTableID:string,
      /**  The display format for this criteria column  */  
   FieldFormat:string,
   LikeField:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuickSearchListRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   Company:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
   GlbCompany:string,
      /**  Description  */  
   Description:string,
      /**  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  */  
   UserID:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
      /**  true if this search is available to all fields that have the same like table/field.  */  
   GlobalSearch:boolean,
      /**  true if this quick search is for validating during data entry  */  
   ForValidation:boolean,
   IsShared:boolean,
      /**  Used for indicating this quick search is provided by system, not by an end user.  */  
   SystemFlag:boolean,
      /**  TableID to of the returned column  */  
   ReturnFieldTableID:string,
      /**  Field name of the returned column  */  
   ReturnFieldName:string,
   CallFrom:string,
   ContextDefault:boolean,
   BaseDefault:boolean,
   Version:string,
   HotKey:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  IsPredictive  */  
   IsPredictive:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The combined return field name in the format of <table>.<field>  */  
   ReturnField:string,
      /**  The combined like field name in the format of <table>.<field>  */  
   LikeField:string,
      /**  The data type of the return column  */  
   ReturnDataType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuickSearchListTableset{
   QuickSearchList:Ice_Tablesets_QuickSearchListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QuickSearchRow{
      /**  Company Identifier. If blank then this quick search is for all companies.  */  
   Company:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
   GlbCompany:string,
      /**  Description  */  
   Description:string,
      /**  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  */  
   UserID:string,
      /**  The unique export identifier.  */  
   ExportID:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
   LikeDataFieldName:string,
      /**  true if this search is available to all fields that have the same like table/field.  */  
   GlobalSearch:boolean,
      /**  true if this quick search is for validating during data entry  */  
   ForValidation:boolean,
   IsShared:boolean,
      /**  Used for indicating this quick search is provided by system, not by an end user.  */  
   SystemFlag:boolean,
      /**  TableID to of the returned column  */  
   ReturnFieldTableID:string,
      /**  Field name of the returned column  */  
   ReturnFieldName:string,
   CallFrom:string,
   ContextDefault:boolean,
   BaseDefault:boolean,
   Version:string,
   HotKey:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  IsPredictive  */  
   IsPredictive:boolean,
      /**  SourceSystemCode  */  
   SourceSystemCode:string,
      /**  SourceTableID  */  
   SourceTableID:string,
      /**  SourceFieldName  */  
   SourceFieldName:string,
      /**  SearchOnFieldSystemCode  */  
   SearchOnFieldSystemCode:string,
      /**  SearchOnFieldTableID  */  
   SearchOnFieldTableID:string,
      /**  SearchOnFieldName  */  
   SearchOnFieldName:string,
      /**  SuppressBaseSearch  */  
   SuppressBaseSearch:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The data type of the return column  */  
   ReturnDataType:string,
      /**  The combined return field name in the format of <table>.<field>  */  
   ReturnField:string,
      /**  The combined like field name in the format of <table>.<field>  */  
   LikeField:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuickSearchTableset{
   QuickSearch:Ice_Tablesets_QuickSearchRow[],
   QuickSearchCriteria:Ice_Tablesets_QuickSearchCriteriaRow[],
   QuickSearchValueList:Ice_Tablesets_QuickSearchValueListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QuickSearchValueListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The unique identifier for this quick search  */  
   QuickSearchID:string,
      /**  Global Record  */  
   GlbCompany:string,
      /**  Sequence  */  
   Seq:number,
      /**  Value Sequence  */  
   ValueSeq:number,
      /**  Display Field  */  
   DisplayMember:string,
      /**  Value Field  */  
   ValueMember:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtQuickSearchTableset{
   QuickSearch:Ice_Tablesets_QuickSearchRow[],
   QuickSearchCriteria:Ice_Tablesets_QuickSearchCriteriaRow[],
   QuickSearchValueList:Ice_Tablesets_QuickSearchValueListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param pageSize
   */  
export interface RunQuickSearchPaged_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
      /**  The size of page  */  
   pageSize:number,
}

export interface RunQuickSearchPaged_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface RunQuickSearch_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
}

export interface RunQuickSearch_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtQuickSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtQuickSearchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_QuickSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_QuickSearchTableset[],
}
}

