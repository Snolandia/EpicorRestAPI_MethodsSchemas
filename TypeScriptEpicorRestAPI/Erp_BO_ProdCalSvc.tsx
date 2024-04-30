import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ProdCalSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/$metadata", {
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
   Description: Get ProdCals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCals
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRow
   */  
export function get_ProdCals(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProdCalRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProdCals(requestBody:Erp_Tablesets_ProdCalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals", {
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
   Summary: Calls GetByID to retrieve the ProdCal item
   Description: Calls GetByID to retrieve the ProdCal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalRow
   */  
export function get_ProdCals_Company_CalendarID(Company:string, CalendarID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProdCal for the service
   Description: Calls UpdateExt to update ProdCal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProdCals_Company_CalendarID(Company:string, CalendarID:string, requestBody:Erp_Tablesets_ProdCalRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")", {
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
   Summary: Call UpdateExt to delete ProdCal item
   Description: Call UpdateExt to delete ProdCal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCal
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProdCals_Company_CalendarID(Company:string, CalendarID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")", {
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
   Description: Get ProdCalDays items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalDays1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalDayRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalDays(Company:string, CalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalDays", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProdCalDay item
   Description: Calls GetByID to retrieve the ProdCalDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalDay1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ModifiedDay Desc: ModifiedDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalDayRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalDays_Company_CalendarID_ModifiedDay(Company:string, CalendarID:string, ModifiedDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalDayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalDayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ProdCalPlantLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalPlantLists1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalPlantListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalPlantLists(Company:string, CalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalPlantLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProdCalPlantList item
   Description: Calls GetByID to retrieve the ProdCalPlantList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalPlantList1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalPlantLists_Company_CalendarID_Plant(Company:string, CalendarID:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalPlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalPlantListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ProdCalRsrcLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalRsrcLists1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRsrcListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalRsrcLists(Company:string, CalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalRsrcLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProdCalRsrcList item
   Description: Calls GetByID to retrieve the ProdCalRsrcList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalRsrcList1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company:string, CalendarID:string, ResourceGrpID:string, ResourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalRsrcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalRsrcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ProdCalVendLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProdCalVendLists1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalVendListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalVendLists(Company:string, CalendarID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalVendLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ProdCalVendList item
   Description: Calls GetByID to retrieve the ProdCalVendList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalVendList1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param VendorID Desc: VendorID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalVendListRow
   */  
export function get_ProdCals_Company_CalendarID_ProdCalVendLists_Company_CalendarID_VendorID(Company:string, CalendarID:string, VendorID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCals(" + Company + "," + CalendarID + ")/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalVendListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ProdCalDays items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalDays
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalDayRow
   */  
export function get_ProdCalDays(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalDays
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProdCalDayRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProdCalDays(requestBody:Erp_Tablesets_ProdCalDayRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays", {
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
   Summary: Calls GetByID to retrieve the ProdCalDay item
   Description: Calls GetByID to retrieve the ProdCalDay item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ModifiedDay Desc: ModifiedDay   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalDayRow
   */  
export function get_ProdCalDays_Company_CalendarID_ModifiedDay(Company:string, CalendarID:string, ModifiedDay:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalDayRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalDayRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProdCalDay for the service
   Description: Calls UpdateExt to update ProdCalDay. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ModifiedDay Desc: ModifiedDay   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalDayRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProdCalDays_Company_CalendarID_ModifiedDay(Company:string, CalendarID:string, ModifiedDay:string, requestBody:Erp_Tablesets_ProdCalDayRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")", {
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
   Summary: Call UpdateExt to delete ProdCalDay item
   Description: Call UpdateExt to delete ProdCalDay item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalDay
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ModifiedDay Desc: ModifiedDay   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProdCalDays_Company_CalendarID_ModifiedDay(Company:string, CalendarID:string, ModifiedDay:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalDays(" + Company + "," + CalendarID + "," + ModifiedDay + ")", {
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
   Description: Get ProdCalPlantLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalPlantLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalPlantListRow
   */  
export function get_ProdCalPlantLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalPlantLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProdCalPlantListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProdCalPlantLists(requestBody:Erp_Tablesets_ProdCalPlantListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists", {
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
   Summary: Calls GetByID to retrieve the ProdCalPlantList item
   Description: Calls GetByID to retrieve the ProdCalPlantList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalPlantList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   */  
export function get_ProdCalPlantLists_Company_CalendarID_Plant(Company:string, CalendarID:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalPlantListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalPlantListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProdCalPlantList for the service
   Description: Calls UpdateExt to update ProdCalPlantList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalPlantList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalPlantListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProdCalPlantLists_Company_CalendarID_Plant(Company:string, CalendarID:string, Plant:string, requestBody:Erp_Tablesets_ProdCalPlantListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete ProdCalPlantList item
   Description: Call UpdateExt to delete ProdCalPlantList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalPlantList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProdCalPlantLists_Company_CalendarID_Plant(Company:string, CalendarID:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalPlantLists(" + Company + "," + CalendarID + "," + Plant + ")", {
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
   Description: Get ProdCalRsrcLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalRsrcLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalRsrcListRow
   */  
export function get_ProdCalRsrcLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalRsrcLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProdCalRsrcLists(requestBody:Erp_Tablesets_ProdCalRsrcListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists", {
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
   Summary: Calls GetByID to retrieve the ProdCalRsrcList item
   Description: Calls GetByID to retrieve the ProdCalRsrcList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalRsrcList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   */  
export function get_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company:string, CalendarID:string, ResourceGrpID:string, ResourceID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalRsrcListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalRsrcListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProdCalRsrcList for the service
   Description: Calls UpdateExt to update ProdCalRsrcList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalRsrcList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalRsrcListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company:string, CalendarID:string, ResourceGrpID:string, ResourceID:string, requestBody:Erp_Tablesets_ProdCalRsrcListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")", {
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
   Summary: Call UpdateExt to delete ProdCalRsrcList item
   Description: Call UpdateExt to delete ProdCalRsrcList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalRsrcList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param ResourceGrpID Desc: ResourceGrpID   Required: True   Allow empty value : True
      @param ResourceID Desc: ResourceID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProdCalRsrcLists_Company_CalendarID_ResourceGrpID_ResourceID(Company:string, CalendarID:string, ResourceGrpID:string, ResourceID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalRsrcLists(" + Company + "," + CalendarID + "," + ResourceGrpID + "," + ResourceID + ")", {
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
   Description: Get ProdCalVendLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdCalVendLists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalVendListRow
   */  
export function get_ProdCalVendLists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdCalVendLists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ProdCalVendListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProdCalVendLists(requestBody:Erp_Tablesets_ProdCalVendListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists", {
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
   Summary: Calls GetByID to retrieve the ProdCalVendList item
   Description: Calls GetByID to retrieve the ProdCalVendList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdCalVendList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param VendorID Desc: VendorID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ProdCalVendListRow
   */  
export function get_ProdCalVendLists_Company_CalendarID_VendorID(Company:string, CalendarID:string, VendorID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ProdCalVendListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")", {
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
         resolve(data as Erp_Tablesets_ProdCalVendListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ProdCalVendList for the service
   Description: Calls UpdateExt to update ProdCalVendList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdCalVendList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param VendorID Desc: VendorID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProdCalVendListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ProdCalVendLists_Company_CalendarID_VendorID(Company:string, CalendarID:string, VendorID:string, requestBody:Erp_Tablesets_ProdCalVendListRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")", {
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
   Summary: Call UpdateExt to delete ProdCalVendList item
   Description: Call UpdateExt to delete ProdCalVendList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdCalVendList
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CalendarID Desc: CalendarID   Required: True   Allow empty value : True
      @param VendorID Desc: VendorID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ProdCalVendLists_Company_CalendarID_VendorID(Company:string, CalendarID:string, VendorID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ProdCalVendLists(" + Company + "," + CalendarID + "," + VendorID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProdCalListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseProdCal:string, whereClauseProdCalDay:string, whereClauseProdCalPlantList:string, whereClauseProdCalRsrcList:string, whereClauseProdCalVendList:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseProdCal!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProdCal=" + whereClauseProdCal
   }
   if(typeof whereClauseProdCalDay!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProdCalDay=" + whereClauseProdCalDay
   }
   if(typeof whereClauseProdCalPlantList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProdCalPlantList=" + whereClauseProdCalPlantList
   }
   if(typeof whereClauseProdCalRsrcList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProdCalRsrcList=" + whereClauseProdCalRsrcList
   }
   if(typeof whereClauseProdCalVendList!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseProdCalVendList=" + whereClauseProdCalVendList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetRows" + params, {
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
export function get_GetByID(calendarID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof calendarID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "calendarID=" + calendarID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetList" + params, {
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
   Summary: Invoke method CustomizeDay
   Description: Call this method to specify a special working day or non working day.
When this method is called, if a ProdCalDay record exists it will be deleted
(undo the special working or non working day).  If a ProdCalDay record doesn't
exist, it will create a ProdCalDay record.  If the date specified is a normal
working day, then the WorkingDay field will be set to false and the capacity
is set to 0.  If the date specified is not a normal working day, then the
WorkingDay field will be set to true and the ProdHour fields will be set to
true depending on the number of ProdCal.HoursPerDay (example: If the ProdCal.HoursPerDay
is 8 then ProdHour 1 through 8 would be set to true) and the capacity for the
working day is set equal to the ProdCal.HoursPerDay.
   OperationID: CustomizeDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomizeDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizeDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomizeDay(requestBody:CustomizeDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomizeDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/CustomizeDay", {
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
         resolve(data as CustomizeDay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DecideReadOnlyFields
   Description: Decides if start processReadOnlyFieldsor not
   OperationID: DecideReadOnlyFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DecideReadOnlyFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DecideReadOnlyFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DecideReadOnlyFields(requestBody:DecideReadOnlyFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DecideReadOnlyFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/DecideReadOnlyFields", {
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
         resolve(data as DecideReadOnlyFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateCalendar
   Description: This duplicates the production calendar for calendar ID.
   OperationID: DuplicateCalendar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateCalendar(requestBody:DuplicateCalendar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateCalendar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/DuplicateCalendar", {
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
         resolve(data as DuplicateCalendar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPlantCalendar
   Description: This method gets the plant calendar.
   OperationID: GetPlantCalendar
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPlantCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPlantCalendar(requestBody:GetPlantCalendar_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPlantCalendar_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetPlantCalendar", {
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
         resolve(data as GetPlantCalendar_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetResourceList
   Description: Used for the Resources/Where Used button.
This method will get list of all resources, resource groups,
vendors, and plants associated with the specified production calendar and
creates tables ttProdCalRsrcList, ttProdCalVendList, and ttProdCalPlantList.
   OperationID: GetResourceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetResourceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetResourceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetResourceList(requestBody:GetResourceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetResourceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetResourceList", {
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
         resolve(data as GetResourceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsWorkDay
   Description: Returns if a selected date is a work day
   OperationID: IsWorkDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsWorkDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsWorkDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsWorkDay(requestBody:IsWorkDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsWorkDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/IsWorkDay", {
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
         resolve(data as IsWorkDay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateHoursSelected
   Description: Updates hours selected per day when the calendar hours per day is changed
   OperationID: UpdateHoursSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateHoursSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHoursSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateHoursSelected(requestBody:UpdateHoursSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateHoursSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/UpdateHoursSelected", {
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
         resolve(data as UpdateHoursSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProdCalHoursPerDayHour
   Description: Calculates DayHours when an hour is toggled on or off
   OperationID: ChangeProdCalHoursPerDayHour
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProdCalHoursPerDayHour_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCalHoursPerDayHour_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProdCalHoursPerDayHour(requestBody:ChangeProdCalHoursPerDayHour_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProdCalHoursPerDayHour_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ChangeProdCalHoursPerDayHour", {
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
         resolve(data as ChangeProdCalHoursPerDayHour_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProdCalHoursPerDaySelectRow
   Description: Updates hours on a row when SelectRow is checked or unchecked
   OperationID: ChangeProdCalHoursPerDaySelectRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProdCalHoursPerDaySelectRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProdCalHoursPerDaySelectRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProdCalHoursPerDaySelectRow(requestBody:ChangeProdCalHoursPerDaySelectRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProdCalHoursPerDaySelectRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ChangeProdCalHoursPerDaySelectRow", {
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
         resolve(data as ChangeProdCalHoursPerDaySelectRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateProdCalHours
   Description: Updates ProdCal Hour fields with selections from ProdCalHoursPerDay
   OperationID: UpdateProdCalHours
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateProdCalHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateProdCalHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateProdCalHours(requestBody:UpdateProdCalHours_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateProdCalHours_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/UpdateProdCalHours", {
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
         resolve(data as UpdateProdCalHours_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetProdCalHoursPerDay
   Description: Returns the ProdCalHoursPerDay dataset
   OperationID: GetProdCalHoursPerDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetProdCalHoursPerDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProdCalHoursPerDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProdCalHoursPerDay(requestBody:GetProdCalHoursPerDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetProdCalHoursPerDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetProdCalHoursPerDay", {
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
         resolve(data as GetProdCalHoursPerDay_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWeekRangeStartingDate
   Description: Validate starting date for adding a week range
   OperationID: ValidateWeekRangeStartingDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeStartingDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeStartingDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWeekRangeStartingDate(requestBody:ValidateWeekRangeStartingDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWeekRangeStartingDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ValidateWeekRangeStartingDate", {
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
         resolve(data as ValidateWeekRangeStartingDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWeekRangeStartingWeek
   Description: Validate starting week number when adding a week range
   OperationID: ValidateWeekRangeStartingWeek
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeStartingWeek_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeStartingWeek_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWeekRangeStartingWeek(requestBody:ValidateWeekRangeStartingWeek_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWeekRangeStartingWeek_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ValidateWeekRangeStartingWeek", {
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
         resolve(data as ValidateWeekRangeStartingWeek_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateWeekRangeNumberOfWeeks
   Description: Validate number of weeks when adding a week range
   OperationID: ValidateWeekRangeNumberOfWeeks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateWeekRangeNumberOfWeeks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWeekRangeNumberOfWeeks_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateWeekRangeNumberOfWeeks(requestBody:ValidateWeekRangeNumberOfWeeks_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateWeekRangeNumberOfWeeks_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/ValidateWeekRangeNumberOfWeeks", {
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
         resolve(data as ValidateWeekRangeNumberOfWeeks_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProdCal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProdCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProdCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProdCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProdCal(requestBody:GetNewProdCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProdCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetNewProdCal", {
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
         resolve(data as GetNewProdCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewProdCalDay
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProdCalDay
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewProdCalDay_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProdCalDay_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewProdCalDay(requestBody:GetNewProdCalDay_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewProdCalDay_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetNewProdCalDay", {
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
         resolve(data as GetNewProdCalDay_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ProdCalSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalDayRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalDayRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalPlantListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalPlantListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalRsrcListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalRsrcListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProdCalVendListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ProdCalVendListRow,
}

export interface Erp_Tablesets_ProdCalDayRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  The date that will have hours that do not conform with the hours for the associated ProdCal.  */  
   "ModifiedDay":string,
      /**  ProdHour01  */  
   "ProdHour01":boolean,
      /**  ProdHour02  */  
   "ProdHour02":boolean,
      /**  ProdHour03  */  
   "ProdHour03":boolean,
      /**  ProdHour04  */  
   "ProdHour04":boolean,
      /**  ProdHour05  */  
   "ProdHour05":boolean,
      /**  ProdHour06  */  
   "ProdHour06":boolean,
      /**  ProdHour07  */  
   "ProdHour07":boolean,
      /**  ProdHour08  */  
   "ProdHour08":boolean,
      /**  ProdHour09  */  
   "ProdHour09":boolean,
      /**  ProdHour10  */  
   "ProdHour10":boolean,
      /**  ProdHour11  */  
   "ProdHour11":boolean,
      /**  ProdHour12  */  
   "ProdHour12":boolean,
      /**  ProdHour13  */  
   "ProdHour13":boolean,
      /**  ProdHour14  */  
   "ProdHour14":boolean,
      /**  ProdHour15  */  
   "ProdHour15":boolean,
      /**  ProdHour16  */  
   "ProdHour16":boolean,
      /**  ProdHour17  */  
   "ProdHour17":boolean,
      /**  ProdHour18  */  
   "ProdHour18":boolean,
      /**  ProdHour19  */  
   "ProdHour19":boolean,
      /**  ProdHour20  */  
   "ProdHour20":boolean,
      /**  ProdHour21  */  
   "ProdHour21":boolean,
      /**  ProdHour22  */  
   "ProdHour22":boolean,
      /**  ProdHour23  */  
   "ProdHour23":boolean,
      /**  ProdHour24  */  
   "ProdHour24":boolean,
      /**  If this is set to NO, then record is being used to identify a non-working day.  The ProdHour field is not used for non-working days.  */  
   "WorkingDay":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ExceptionLabel  */  
   "ExceptionLabel":string,
   "BitFlag":number,
   "CalendarIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProdCalListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  Calendar description.  */  
   "Description":string,
      /**  WorkWeek1  */  
   "WorkWeek1":boolean,
      /**  WorkWeek2  */  
   "WorkWeek2":boolean,
      /**  WorkWeek3  */  
   "WorkWeek3":boolean,
      /**  WorkWeek4  */  
   "WorkWeek4":boolean,
      /**  WorkWeek5  */  
   "WorkWeek5":boolean,
      /**  WorkWeek6  */  
   "WorkWeek6":boolean,
      /**  WorkWeek7  */  
   "WorkWeek7":boolean,
      /**  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  */  
   "ReloadStatus":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProdCalPlantListRow{
   "Company":string,
   "Plant":string,
   "PlantName":string,
   "CalendarID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProdCalRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  Calendar description.  */  
   "Description":string,
      /**  WorkWeek1  */  
   "WorkWeek1":boolean,
      /**  WorkWeek2  */  
   "WorkWeek2":boolean,
      /**  WorkWeek3  */  
   "WorkWeek3":boolean,
      /**  WorkWeek4  */  
   "WorkWeek4":boolean,
      /**  WorkWeek5  */  
   "WorkWeek5":boolean,
      /**  WorkWeek6  */  
   "WorkWeek6":boolean,
      /**  WorkWeek7  */  
   "WorkWeek7":boolean,
      /**  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  */  
   "ReloadStatus":string,
      /**  Hour001  */  
   "Hour001":boolean,
      /**  Hour002  */  
   "Hour002":boolean,
      /**  Hour003  */  
   "Hour003":boolean,
      /**  Hour004  */  
   "Hour004":boolean,
      /**  Hour005  */  
   "Hour005":boolean,
      /**  Hour006  */  
   "Hour006":boolean,
      /**  Hour007  */  
   "Hour007":boolean,
      /**  Hour008  */  
   "Hour008":boolean,
      /**  Hour009  */  
   "Hour009":boolean,
      /**  Hour010  */  
   "Hour010":boolean,
      /**  Hour011  */  
   "Hour011":boolean,
      /**  Hour012  */  
   "Hour012":boolean,
      /**  Hour013  */  
   "Hour013":boolean,
      /**  Hour014  */  
   "Hour014":boolean,
      /**  Hour015  */  
   "Hour015":boolean,
      /**  Hour016  */  
   "Hour016":boolean,
      /**  Hour017  */  
   "Hour017":boolean,
      /**  Hour018  */  
   "Hour018":boolean,
      /**  Hour019  */  
   "Hour019":boolean,
      /**  Hour020  */  
   "Hour020":boolean,
      /**  Hour021  */  
   "Hour021":boolean,
      /**  Hour022  */  
   "Hour022":boolean,
      /**  Hour023  */  
   "Hour023":boolean,
      /**  Hour024  */  
   "Hour024":boolean,
      /**  Hour025  */  
   "Hour025":boolean,
      /**  Hour026  */  
   "Hour026":boolean,
      /**  Hour027  */  
   "Hour027":boolean,
      /**  Hour028  */  
   "Hour028":boolean,
      /**  Hour029  */  
   "Hour029":boolean,
      /**  Hour030  */  
   "Hour030":boolean,
      /**  Hour031  */  
   "Hour031":boolean,
      /**  Hour032  */  
   "Hour032":boolean,
      /**  Hour033  */  
   "Hour033":boolean,
      /**  Hour034  */  
   "Hour034":boolean,
      /**  Hour035  */  
   "Hour035":boolean,
      /**  Hour036  */  
   "Hour036":boolean,
      /**  Hour037  */  
   "Hour037":boolean,
      /**  Hour038  */  
   "Hour038":boolean,
      /**  Hour039  */  
   "Hour039":boolean,
      /**  Hour040  */  
   "Hour040":boolean,
      /**  Hour041  */  
   "Hour041":boolean,
      /**  Hour042  */  
   "Hour042":boolean,
      /**  Hour043  */  
   "Hour043":boolean,
      /**  Hour044  */  
   "Hour044":boolean,
      /**  Hour045  */  
   "Hour045":boolean,
      /**  Hour046  */  
   "Hour046":boolean,
      /**  Hour047  */  
   "Hour047":boolean,
      /**  Hour048  */  
   "Hour048":boolean,
      /**  Hour049  */  
   "Hour049":boolean,
      /**  Hour050  */  
   "Hour050":boolean,
      /**  Hour051  */  
   "Hour051":boolean,
      /**  Hour052  */  
   "Hour052":boolean,
      /**  Hour053  */  
   "Hour053":boolean,
      /**  Hour054  */  
   "Hour054":boolean,
      /**  Hour055  */  
   "Hour055":boolean,
      /**  Hour056  */  
   "Hour056":boolean,
      /**  Hour057  */  
   "Hour057":boolean,
      /**  Hour058  */  
   "Hour058":boolean,
      /**  Hour059  */  
   "Hour059":boolean,
      /**  Hour060  */  
   "Hour060":boolean,
      /**  Hour061  */  
   "Hour061":boolean,
      /**  Hour062  */  
   "Hour062":boolean,
      /**  Hour063  */  
   "Hour063":boolean,
      /**  Hour064  */  
   "Hour064":boolean,
      /**  Hour065  */  
   "Hour065":boolean,
      /**  Hour066  */  
   "Hour066":boolean,
      /**  Hour067  */  
   "Hour067":boolean,
      /**  Hour068  */  
   "Hour068":boolean,
      /**  Hour069  */  
   "Hour069":boolean,
      /**  Hour070  */  
   "Hour070":boolean,
      /**  Hour071  */  
   "Hour071":boolean,
      /**  Hour072  */  
   "Hour072":boolean,
      /**  Hour073  */  
   "Hour073":boolean,
      /**  Hour074  */  
   "Hour074":boolean,
      /**  Hour075  */  
   "Hour075":boolean,
      /**  Hour076  */  
   "Hour076":boolean,
      /**  Hour077  */  
   "Hour077":boolean,
      /**  Hour078  */  
   "Hour078":boolean,
      /**  Hour079  */  
   "Hour079":boolean,
      /**  Hour080  */  
   "Hour080":boolean,
      /**  Hour081  */  
   "Hour081":boolean,
      /**  Hour082  */  
   "Hour082":boolean,
      /**  Hour083  */  
   "Hour083":boolean,
      /**  Hour084  */  
   "Hour084":boolean,
      /**  Hour085  */  
   "Hour085":boolean,
      /**  Hour086  */  
   "Hour086":boolean,
      /**  Hour087  */  
   "Hour087":boolean,
      /**  Hour088  */  
   "Hour088":boolean,
      /**  Hour089  */  
   "Hour089":boolean,
      /**  Hour090  */  
   "Hour090":boolean,
      /**  Hour091  */  
   "Hour091":boolean,
      /**  Hour092  */  
   "Hour092":boolean,
      /**  Hour093  */  
   "Hour093":boolean,
      /**  Hour094  */  
   "Hour094":boolean,
      /**  Hour095  */  
   "Hour095":boolean,
      /**  Hour096  */  
   "Hour096":boolean,
      /**  Hour097  */  
   "Hour097":boolean,
      /**  Hour098  */  
   "Hour098":boolean,
      /**  Hour099  */  
   "Hour099":boolean,
      /**  Hour100  */  
   "Hour100":boolean,
      /**  Hour101  */  
   "Hour101":boolean,
      /**  Hour102  */  
   "Hour102":boolean,
      /**  Hour103  */  
   "Hour103":boolean,
      /**  Hour104  */  
   "Hour104":boolean,
      /**  Hour105  */  
   "Hour105":boolean,
      /**  Hour106  */  
   "Hour106":boolean,
      /**  Hour107  */  
   "Hour107":boolean,
      /**  Hour108  */  
   "Hour108":boolean,
      /**  Hour109  */  
   "Hour109":boolean,
      /**  Hour110  */  
   "Hour110":boolean,
      /**  Hour111  */  
   "Hour111":boolean,
      /**  Hour112  */  
   "Hour112":boolean,
      /**  Hour113  */  
   "Hour113":boolean,
      /**  Hour114  */  
   "Hour114":boolean,
      /**  Hour115  */  
   "Hour115":boolean,
      /**  Hour116  */  
   "Hour116":boolean,
      /**  Hour117  */  
   "Hour117":boolean,
      /**  Hour118  */  
   "Hour118":boolean,
      /**  Hour119  */  
   "Hour119":boolean,
      /**  Hour120  */  
   "Hour120":boolean,
      /**  Hour121  */  
   "Hour121":boolean,
      /**  Hour122  */  
   "Hour122":boolean,
      /**  Hour123  */  
   "Hour123":boolean,
      /**  Hour124  */  
   "Hour124":boolean,
      /**  Hour125  */  
   "Hour125":boolean,
      /**  Hour126  */  
   "Hour126":boolean,
      /**  Hour127  */  
   "Hour127":boolean,
      /**  Hour128  */  
   "Hour128":boolean,
      /**  Hour129  */  
   "Hour129":boolean,
      /**  Hour130  */  
   "Hour130":boolean,
      /**  Hour131  */  
   "Hour131":boolean,
      /**  Hour132  */  
   "Hour132":boolean,
      /**  Hour133  */  
   "Hour133":boolean,
      /**  Hour134  */  
   "Hour134":boolean,
      /**  Hour135  */  
   "Hour135":boolean,
      /**  Hour136  */  
   "Hour136":boolean,
      /**  Hour137  */  
   "Hour137":boolean,
      /**  Hour138  */  
   "Hour138":boolean,
      /**  Hour139  */  
   "Hour139":boolean,
      /**  Hour140  */  
   "Hour140":boolean,
      /**  Hour141  */  
   "Hour141":boolean,
      /**  Hour142  */  
   "Hour142":boolean,
      /**  Hour143  */  
   "Hour143":boolean,
      /**  Hour144  */  
   "Hour144":boolean,
      /**  Hour145  */  
   "Hour145":boolean,
      /**  Hour146  */  
   "Hour146":boolean,
      /**  Hour147  */  
   "Hour147":boolean,
      /**  Hour148  */  
   "Hour148":boolean,
      /**  Hour149  */  
   "Hour149":boolean,
      /**  Hour150  */  
   "Hour150":boolean,
      /**  Hour151  */  
   "Hour151":boolean,
      /**  Hour152  */  
   "Hour152":boolean,
      /**  Hour153  */  
   "Hour153":boolean,
      /**  Hour154  */  
   "Hour154":boolean,
      /**  Hour155  */  
   "Hour155":boolean,
      /**  Hour156  */  
   "Hour156":boolean,
      /**  Hour157  */  
   "Hour157":boolean,
      /**  Hour158  */  
   "Hour158":boolean,
      /**  Hour159  */  
   "Hour159":boolean,
      /**  Hour160  */  
   "Hour160":boolean,
      /**  Hour161  */  
   "Hour161":boolean,
      /**  Hour162  */  
   "Hour162":boolean,
      /**  Hour163  */  
   "Hour163":boolean,
      /**  Hour164  */  
   "Hour164":boolean,
      /**  Hour165  */  
   "Hour165":boolean,
      /**  Hour166  */  
   "Hour166":boolean,
      /**  Hour167  */  
   "Hour167":boolean,
      /**  Hour168  */  
   "Hour168":boolean,
      /**  The Number of Hours that a single Resouce is available per day.  */  
   "HoursPerDay":number,
      /**  Day of the week on which the Production Calendar begins.  Values mirror the values returned by the Progress "weekday" function.  Valid values:  1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Sunday.  */  
   "BeginWeekday":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Num of machines assigned to the workcenter  */  
   "NumberOfMachines":number,
   "PlantCalendar":boolean,
   "ProposedCalendarID":string,
      /**  Delimited list of read-only fields  */  
   "ReadOnlyFields":string,
   "StartTime1":number,
   "StartTime2":number,
   "StartTime3":number,
   "StartTime4":number,
   "StartTime5":number,
   "StartTime6":number,
   "StartTime7":number,
   "EndTime1":number,
   "EndTime2":number,
   "EndTime3":number,
   "EndTime4":number,
   "EndTime5":number,
   "EndTime6":number,
   "EndTime7":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProdCalRsrcListRow{
   "ResourceID":string,
   "ResourceGrpID":string,
   "ResourceDescription":string,
   "Company":string,
   "CalendarID":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ProdCalVendListRow{
      /**  Vendor ID  */  
   "VendorID":string,
   "Company":string,
   "VendorName":string,
   "CalendarID":string,
   "SysRowID":string,
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
      @param rowSeq
      @param columnChanged
      @param ds
   */  
export interface ChangeProdCalHoursPerDayHour_input{
      /**  RowSeq value of the row that was modified  */  
   rowSeq:number,
      /**  Name of the column that was changed  */  
   columnChanged:string,
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset[],
}

export interface ChangeProdCalHoursPerDayHour_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset,
}
}

   /** Required : 
      @param rowSeq
      @param defaultHoursPerDay
      @param ds
   */  
export interface ChangeProdCalHoursPerDaySelectRow_input{
      /**  RowSeq value of the row that was modified  */  
   rowSeq:number,
      /**  Default Hours Per Day for the calendar  */  
   defaultHoursPerDay:number,
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset[],
}

export interface ChangeProdCalHoursPerDaySelectRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset,
}
}

   /** Required : 
      @param cCalendarID
      @param daDate
      @param exceptionLabel
      @param ds
   */  
export interface CustomizeDay_input{
      /**  cCalendar Descriptive Code  */  
   cCalendarID:string,
      /**  Modified date  */  
   daDate:string,
      /**  Exception Label  */  
   exceptionLabel:string,
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface CustomizeDay_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface DecideReadOnlyFields_input{
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface DecideReadOnlyFields_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param calendarID
   */  
export interface DeleteByID_input{
   calendarID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param cOldCalendarID
      @param cNewCalendarID
      @param ds
   */  
export interface DuplicateCalendar_input{
      /**  The Current Calendar ID.  */  
   cOldCalendarID:string,
      /**  Calendar ID of the new Calendar  */  
   cNewCalendarID:string,
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface DuplicateCalendar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

export interface Erp_Tablesets_ProdCalDayRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  The date that will have hours that do not conform with the hours for the associated ProdCal.  */  
   ModifiedDay:string,
      /**  ProdHour01  */  
   ProdHour01:boolean,
      /**  ProdHour02  */  
   ProdHour02:boolean,
      /**  ProdHour03  */  
   ProdHour03:boolean,
      /**  ProdHour04  */  
   ProdHour04:boolean,
      /**  ProdHour05  */  
   ProdHour05:boolean,
      /**  ProdHour06  */  
   ProdHour06:boolean,
      /**  ProdHour07  */  
   ProdHour07:boolean,
      /**  ProdHour08  */  
   ProdHour08:boolean,
      /**  ProdHour09  */  
   ProdHour09:boolean,
      /**  ProdHour10  */  
   ProdHour10:boolean,
      /**  ProdHour11  */  
   ProdHour11:boolean,
      /**  ProdHour12  */  
   ProdHour12:boolean,
      /**  ProdHour13  */  
   ProdHour13:boolean,
      /**  ProdHour14  */  
   ProdHour14:boolean,
      /**  ProdHour15  */  
   ProdHour15:boolean,
      /**  ProdHour16  */  
   ProdHour16:boolean,
      /**  ProdHour17  */  
   ProdHour17:boolean,
      /**  ProdHour18  */  
   ProdHour18:boolean,
      /**  ProdHour19  */  
   ProdHour19:boolean,
      /**  ProdHour20  */  
   ProdHour20:boolean,
      /**  ProdHour21  */  
   ProdHour21:boolean,
      /**  ProdHour22  */  
   ProdHour22:boolean,
      /**  ProdHour23  */  
   ProdHour23:boolean,
      /**  ProdHour24  */  
   ProdHour24:boolean,
      /**  If this is set to NO, then record is being used to identify a non-working day.  The ProdHour field is not used for non-working days.  */  
   WorkingDay:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExceptionLabel  */  
   ExceptionLabel:string,
   BitFlag:number,
   CalendarIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalHoursPerDayRow{
   Company:string,
   CalendarID:string,
      /**  Number of hours selected for the week day  */  
   DayHours:number,
      /**  Hour 1  */  
   Hour01:boolean,
      /**  Hour 2  */  
   Hour02:boolean,
   Hour03:boolean,
   Hour04:boolean,
   Hour05:boolean,
   Hour06:boolean,
      /**  Hour 7  */  
   Hour07:boolean,
      /**  Hour 8  */  
   Hour08:boolean,
   Hour09:boolean,
      /**  Hour 10  */  
   Hour10:boolean,
      /**  Hour 11  */  
   Hour11:boolean,
      /**  Hour 12  */  
   Hour12:boolean,
      /**  Hour 13  */  
   Hour13:boolean,
   Hour14:boolean,
      /**  Hour 15  */  
   Hour15:boolean,
      /**  Hour 16  */  
   Hour16:boolean,
      /**  Hour 17  */  
   Hour17:boolean,
      /**  Hour 18  */  
   Hour18:boolean,
      /**  Hour 19  */  
   Hour19:boolean,
      /**  Hour 20  */  
   Hour20:boolean,
      /**  Hour 21  */  
   Hour21:boolean,
      /**  Hour 22  */  
   Hour22:boolean,
      /**  Hour 23  */  
   Hour23:boolean,
      /**  Hour 24  */  
   Hour24:boolean,
      /**  Day of the week the row represents, i.e. Monday, Tuesday, etc  */  
   DayOfWeek:string,
      /**  Row Sequence  */  
   RowSeq:number,
   SelectRow:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalHoursPerDayTableset{
   ProdCalHoursPerDay:Erp_Tablesets_ProdCalHoursPerDayRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProdCalListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  Calendar description.  */  
   Description:string,
      /**  WorkWeek1  */  
   WorkWeek1:boolean,
      /**  WorkWeek2  */  
   WorkWeek2:boolean,
      /**  WorkWeek3  */  
   WorkWeek3:boolean,
      /**  WorkWeek4  */  
   WorkWeek4:boolean,
      /**  WorkWeek5  */  
   WorkWeek5:boolean,
      /**  WorkWeek6  */  
   WorkWeek6:boolean,
      /**  WorkWeek7  */  
   WorkWeek7:boolean,
      /**  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  */  
   ReloadStatus:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalListTableset{
   ProdCalList:Erp_Tablesets_ProdCalListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProdCalPlantListRow{
   Company:string,
   Plant:string,
   PlantName:string,
   CalendarID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  Calendar description.  */  
   Description:string,
      /**  WorkWeek1  */  
   WorkWeek1:boolean,
      /**  WorkWeek2  */  
   WorkWeek2:boolean,
      /**  WorkWeek3  */  
   WorkWeek3:boolean,
      /**  WorkWeek4  */  
   WorkWeek4:boolean,
      /**  WorkWeek5  */  
   WorkWeek5:boolean,
      /**  WorkWeek6  */  
   WorkWeek6:boolean,
      /**  WorkWeek7  */  
   WorkWeek7:boolean,
      /**  A  recovery flag which indicates the status of the "Reload" process when the calendar is changed.  Values; Blank or "Started". (See WrkCenter.ReloadStatus, WrkCenter.ReloadNum)  */  
   ReloadStatus:string,
      /**  Hour001  */  
   Hour001:boolean,
      /**  Hour002  */  
   Hour002:boolean,
      /**  Hour003  */  
   Hour003:boolean,
      /**  Hour004  */  
   Hour004:boolean,
      /**  Hour005  */  
   Hour005:boolean,
      /**  Hour006  */  
   Hour006:boolean,
      /**  Hour007  */  
   Hour007:boolean,
      /**  Hour008  */  
   Hour008:boolean,
      /**  Hour009  */  
   Hour009:boolean,
      /**  Hour010  */  
   Hour010:boolean,
      /**  Hour011  */  
   Hour011:boolean,
      /**  Hour012  */  
   Hour012:boolean,
      /**  Hour013  */  
   Hour013:boolean,
      /**  Hour014  */  
   Hour014:boolean,
      /**  Hour015  */  
   Hour015:boolean,
      /**  Hour016  */  
   Hour016:boolean,
      /**  Hour017  */  
   Hour017:boolean,
      /**  Hour018  */  
   Hour018:boolean,
      /**  Hour019  */  
   Hour019:boolean,
      /**  Hour020  */  
   Hour020:boolean,
      /**  Hour021  */  
   Hour021:boolean,
      /**  Hour022  */  
   Hour022:boolean,
      /**  Hour023  */  
   Hour023:boolean,
      /**  Hour024  */  
   Hour024:boolean,
      /**  Hour025  */  
   Hour025:boolean,
      /**  Hour026  */  
   Hour026:boolean,
      /**  Hour027  */  
   Hour027:boolean,
      /**  Hour028  */  
   Hour028:boolean,
      /**  Hour029  */  
   Hour029:boolean,
      /**  Hour030  */  
   Hour030:boolean,
      /**  Hour031  */  
   Hour031:boolean,
      /**  Hour032  */  
   Hour032:boolean,
      /**  Hour033  */  
   Hour033:boolean,
      /**  Hour034  */  
   Hour034:boolean,
      /**  Hour035  */  
   Hour035:boolean,
      /**  Hour036  */  
   Hour036:boolean,
      /**  Hour037  */  
   Hour037:boolean,
      /**  Hour038  */  
   Hour038:boolean,
      /**  Hour039  */  
   Hour039:boolean,
      /**  Hour040  */  
   Hour040:boolean,
      /**  Hour041  */  
   Hour041:boolean,
      /**  Hour042  */  
   Hour042:boolean,
      /**  Hour043  */  
   Hour043:boolean,
      /**  Hour044  */  
   Hour044:boolean,
      /**  Hour045  */  
   Hour045:boolean,
      /**  Hour046  */  
   Hour046:boolean,
      /**  Hour047  */  
   Hour047:boolean,
      /**  Hour048  */  
   Hour048:boolean,
      /**  Hour049  */  
   Hour049:boolean,
      /**  Hour050  */  
   Hour050:boolean,
      /**  Hour051  */  
   Hour051:boolean,
      /**  Hour052  */  
   Hour052:boolean,
      /**  Hour053  */  
   Hour053:boolean,
      /**  Hour054  */  
   Hour054:boolean,
      /**  Hour055  */  
   Hour055:boolean,
      /**  Hour056  */  
   Hour056:boolean,
      /**  Hour057  */  
   Hour057:boolean,
      /**  Hour058  */  
   Hour058:boolean,
      /**  Hour059  */  
   Hour059:boolean,
      /**  Hour060  */  
   Hour060:boolean,
      /**  Hour061  */  
   Hour061:boolean,
      /**  Hour062  */  
   Hour062:boolean,
      /**  Hour063  */  
   Hour063:boolean,
      /**  Hour064  */  
   Hour064:boolean,
      /**  Hour065  */  
   Hour065:boolean,
      /**  Hour066  */  
   Hour066:boolean,
      /**  Hour067  */  
   Hour067:boolean,
      /**  Hour068  */  
   Hour068:boolean,
      /**  Hour069  */  
   Hour069:boolean,
      /**  Hour070  */  
   Hour070:boolean,
      /**  Hour071  */  
   Hour071:boolean,
      /**  Hour072  */  
   Hour072:boolean,
      /**  Hour073  */  
   Hour073:boolean,
      /**  Hour074  */  
   Hour074:boolean,
      /**  Hour075  */  
   Hour075:boolean,
      /**  Hour076  */  
   Hour076:boolean,
      /**  Hour077  */  
   Hour077:boolean,
      /**  Hour078  */  
   Hour078:boolean,
      /**  Hour079  */  
   Hour079:boolean,
      /**  Hour080  */  
   Hour080:boolean,
      /**  Hour081  */  
   Hour081:boolean,
      /**  Hour082  */  
   Hour082:boolean,
      /**  Hour083  */  
   Hour083:boolean,
      /**  Hour084  */  
   Hour084:boolean,
      /**  Hour085  */  
   Hour085:boolean,
      /**  Hour086  */  
   Hour086:boolean,
      /**  Hour087  */  
   Hour087:boolean,
      /**  Hour088  */  
   Hour088:boolean,
      /**  Hour089  */  
   Hour089:boolean,
      /**  Hour090  */  
   Hour090:boolean,
      /**  Hour091  */  
   Hour091:boolean,
      /**  Hour092  */  
   Hour092:boolean,
      /**  Hour093  */  
   Hour093:boolean,
      /**  Hour094  */  
   Hour094:boolean,
      /**  Hour095  */  
   Hour095:boolean,
      /**  Hour096  */  
   Hour096:boolean,
      /**  Hour097  */  
   Hour097:boolean,
      /**  Hour098  */  
   Hour098:boolean,
      /**  Hour099  */  
   Hour099:boolean,
      /**  Hour100  */  
   Hour100:boolean,
      /**  Hour101  */  
   Hour101:boolean,
      /**  Hour102  */  
   Hour102:boolean,
      /**  Hour103  */  
   Hour103:boolean,
      /**  Hour104  */  
   Hour104:boolean,
      /**  Hour105  */  
   Hour105:boolean,
      /**  Hour106  */  
   Hour106:boolean,
      /**  Hour107  */  
   Hour107:boolean,
      /**  Hour108  */  
   Hour108:boolean,
      /**  Hour109  */  
   Hour109:boolean,
      /**  Hour110  */  
   Hour110:boolean,
      /**  Hour111  */  
   Hour111:boolean,
      /**  Hour112  */  
   Hour112:boolean,
      /**  Hour113  */  
   Hour113:boolean,
      /**  Hour114  */  
   Hour114:boolean,
      /**  Hour115  */  
   Hour115:boolean,
      /**  Hour116  */  
   Hour116:boolean,
      /**  Hour117  */  
   Hour117:boolean,
      /**  Hour118  */  
   Hour118:boolean,
      /**  Hour119  */  
   Hour119:boolean,
      /**  Hour120  */  
   Hour120:boolean,
      /**  Hour121  */  
   Hour121:boolean,
      /**  Hour122  */  
   Hour122:boolean,
      /**  Hour123  */  
   Hour123:boolean,
      /**  Hour124  */  
   Hour124:boolean,
      /**  Hour125  */  
   Hour125:boolean,
      /**  Hour126  */  
   Hour126:boolean,
      /**  Hour127  */  
   Hour127:boolean,
      /**  Hour128  */  
   Hour128:boolean,
      /**  Hour129  */  
   Hour129:boolean,
      /**  Hour130  */  
   Hour130:boolean,
      /**  Hour131  */  
   Hour131:boolean,
      /**  Hour132  */  
   Hour132:boolean,
      /**  Hour133  */  
   Hour133:boolean,
      /**  Hour134  */  
   Hour134:boolean,
      /**  Hour135  */  
   Hour135:boolean,
      /**  Hour136  */  
   Hour136:boolean,
      /**  Hour137  */  
   Hour137:boolean,
      /**  Hour138  */  
   Hour138:boolean,
      /**  Hour139  */  
   Hour139:boolean,
      /**  Hour140  */  
   Hour140:boolean,
      /**  Hour141  */  
   Hour141:boolean,
      /**  Hour142  */  
   Hour142:boolean,
      /**  Hour143  */  
   Hour143:boolean,
      /**  Hour144  */  
   Hour144:boolean,
      /**  Hour145  */  
   Hour145:boolean,
      /**  Hour146  */  
   Hour146:boolean,
      /**  Hour147  */  
   Hour147:boolean,
      /**  Hour148  */  
   Hour148:boolean,
      /**  Hour149  */  
   Hour149:boolean,
      /**  Hour150  */  
   Hour150:boolean,
      /**  Hour151  */  
   Hour151:boolean,
      /**  Hour152  */  
   Hour152:boolean,
      /**  Hour153  */  
   Hour153:boolean,
      /**  Hour154  */  
   Hour154:boolean,
      /**  Hour155  */  
   Hour155:boolean,
      /**  Hour156  */  
   Hour156:boolean,
      /**  Hour157  */  
   Hour157:boolean,
      /**  Hour158  */  
   Hour158:boolean,
      /**  Hour159  */  
   Hour159:boolean,
      /**  Hour160  */  
   Hour160:boolean,
      /**  Hour161  */  
   Hour161:boolean,
      /**  Hour162  */  
   Hour162:boolean,
      /**  Hour163  */  
   Hour163:boolean,
      /**  Hour164  */  
   Hour164:boolean,
      /**  Hour165  */  
   Hour165:boolean,
      /**  Hour166  */  
   Hour166:boolean,
      /**  Hour167  */  
   Hour167:boolean,
      /**  Hour168  */  
   Hour168:boolean,
      /**  The Number of Hours that a single Resouce is available per day.  */  
   HoursPerDay:number,
      /**  Day of the week on which the Production Calendar begins.  Values mirror the values returned by the Progress "weekday" function.  Valid values:  1 = Sunday, 2 = Monday, 3 = Tuesday, 4 = Wednesday, 5 = Thursday, 6 = Friday, 7 = Sunday.  */  
   BeginWeekday:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Num of machines assigned to the workcenter  */  
   NumberOfMachines:number,
   PlantCalendar:boolean,
   ProposedCalendarID:string,
      /**  Delimited list of read-only fields  */  
   ReadOnlyFields:string,
   StartTime1:number,
   StartTime2:number,
   StartTime3:number,
   StartTime4:number,
   StartTime5:number,
   StartTime6:number,
   StartTime7:number,
   EndTime1:number,
   EndTime2:number,
   EndTime3:number,
   EndTime4:number,
   EndTime5:number,
   EndTime6:number,
   EndTime7:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalRsrcListRow{
   ResourceID:string,
   ResourceGrpID:string,
   ResourceDescription:string,
   Company:string,
   CalendarID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ProdCalTableset{
   ProdCal:Erp_Tablesets_ProdCalRow[],
   ProdCalDay:Erp_Tablesets_ProdCalDayRow[],
   ProdCalPlantList:Erp_Tablesets_ProdCalPlantListRow[],
   ProdCalRsrcList:Erp_Tablesets_ProdCalRsrcListRow[],
   ProdCalVendList:Erp_Tablesets_ProdCalVendListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ProdCalVendListRow{
      /**  Vendor ID  */  
   VendorID:string,
   Company:string,
   VendorName:string,
   CalendarID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtProdCalTableset{
   ProdCal:Erp_Tablesets_ProdCalRow[],
   ProdCalDay:Erp_Tablesets_ProdCalDayRow[],
   ProdCalPlantList:Erp_Tablesets_ProdCalPlantListRow[],
   ProdCalRsrcList:Erp_Tablesets_ProdCalRsrcListRow[],
   ProdCalVendList:Erp_Tablesets_ProdCalVendListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param calendarID
   */  
export interface GetByID_input{
   calendarID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ProdCalTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ProdCalTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ProdCalTableset[],
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
   returnObj:Erp_Tablesets_ProdCalListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param calendarID
   */  
export interface GetNewProdCalDay_input{
   ds:Erp_Tablesets_ProdCalTableset[],
   calendarID:string,
}

export interface GetNewProdCalDay_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewProdCal_input{
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface GetNewProdCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetPlantCalendar_input{
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface GetPlantCalendar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param calendarID
   */  
export interface GetProdCalHoursPerDay_input{
      /**  Calendar  */  
   calendarID:string,
}

export interface GetProdCalHoursPerDay_output{
   returnObj:Erp_Tablesets_ProdCalHoursPerDayTableset[],
}

   /** Required : 
      @param ds
      @param calendarID
   */  
export interface GetResourceList_input{
   ds:Erp_Tablesets_ProdCalTableset[],
      /**  Calendar ID  */  
   calendarID:string,
}

export interface GetResourceList_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param whereClauseProdCal
      @param whereClauseProdCalDay
      @param whereClauseProdCalPlantList
      @param whereClauseProdCalRsrcList
      @param whereClauseProdCalVendList
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseProdCal:string,
   whereClauseProdCalDay:string,
   whereClauseProdCalPlantList:string,
   whereClauseProdCalRsrcList:string,
   whereClauseProdCalVendList:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ProdCalTableset[],
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
      @param calendarID
      @param selectedDate
   */  
export interface IsWorkDay_input{
      /**  Calendar ID to check  */  
   calendarID:string,
      /**  Date to check  */  
   selectedDate:string,
}

export interface IsWorkDay_output{
parameters : {
      /**  output parameters  */  
   isWorkingDay:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtProdCalTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtProdCalTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param hoursPerDay
      @param ds
   */  
export interface UpdateHoursSelected_input{
      /**  Hours per day  */  
   hoursPerDay:number,
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset[],
}

export interface UpdateHoursSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalHoursPerDayTableset,
}
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface UpdateProdCalHours_input{
   ds:Erp_Tablesets_ProdCalTableset[],
   ds1:Erp_Tablesets_ProdCalHoursPerDayTableset[],
}

export interface UpdateProdCalHours_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
   ds1:Erp_Tablesets_ProdCalHoursPerDayTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ProdCalTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ProdCalTableset,
}
}

   /** Required : 
      @param numberOfWeeks
      @param startingDate
   */  
export interface ValidateWeekRangeNumberOfWeeks_input{
      /**  The number of weeks to validate  */  
   numberOfWeeks:number,
      /**  The week range start date  */  
   startingDate:string,
}

export interface ValidateWeekRangeNumberOfWeeks_output{
}

   /** Required : 
      @param startDate
   */  
export interface ValidateWeekRangeStartingDate_input{
      /**  The date to validate  */  
   startDate:string,
}

export interface ValidateWeekRangeStartingDate_output{
}

   /** Required : 
      @param startingWeekNumber
   */  
export interface ValidateWeekRangeStartingWeek_input{
      /**  Starting week number to validate  */  
   startingWeekNumber:number,
}

export interface ValidateWeekRangeStartingWeek_output{
}

