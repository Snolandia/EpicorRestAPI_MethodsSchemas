import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.COAMapDataSvc
// Description: Object to manage COA map data: COAMap, AccStrLink, SegmentLink
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/$metadata", {
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
   Description: Get COAMapDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAMapDatas
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAMapRow
   */  
export function get_COAMapDatas(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAMapDatas
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COAMapRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.COAMapRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_COAMapDatas(requestBody:Erp_Tablesets_COAMapRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas", {
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
   Summary: Calls GetByID to retrieve the COAMapData item
   Description: Calls GetByID to retrieve the COAMapData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COAMapData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.COAMapRow
   */  
export function get_COAMapDatas_Company_COAMapUID(Company:string, COAMapUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_COAMapRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")", {
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
         resolve(data as Erp_Tablesets_COAMapRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update COAMapData for the service
   Description: Calls UpdateExt to update COAMapData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COAMapData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.COAMapRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_COAMapDatas_Company_COAMapUID(Company:string, COAMapUID:string, requestBody:Erp_Tablesets_COAMapRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")", {
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
   Summary: Call UpdateExt to delete COAMapData item
   Description: Call UpdateExt to delete COAMapData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COAMapData
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_COAMapDatas_Company_COAMapUID(Company:string, COAMapUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")", {
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
   Description: Get GLAccLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAccLinks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccLinkRow
   */  
export function get_COAMapDatas_Company_COAMapUID_GLAccLinks(Company:string, COAMapUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/GLAccLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLAccLink item
   Description: Calls GetByID to retrieve the GLAccLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccLink1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param GLAccLinkUID Desc: GLAccLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLAccLinkRow
   */  
export function get_COAMapDatas_Company_COAMapUID_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company:string, COAMapUID:string, GLAccLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLAccLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_GLAccLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get SegmentLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SegmentLinks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegmentLinkRow
   */  
export function get_COAMapDatas_Company_COAMapUID_SegmentLinks(Company:string, COAMapUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/SegmentLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the SegmentLink item
   Description: Calls GetByID to retrieve the SegmentLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegmentLink1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param SegmentLinkUID Desc: SegmentLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegmentLinkRow
   */  
export function get_COAMapDatas_Company_COAMapUID_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company:string, COAMapUID:string, SegmentLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegmentLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_SegmentLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLAccLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccLinks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccLinkRow
   */  
export function get_GLAccLinks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccLinks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLAccLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLAccLinks(requestBody:Erp_Tablesets_GLAccLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks", {
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
   Summary: Calls GetByID to retrieve the GLAccLink item
   Description: Calls GetByID to retrieve the GLAccLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param GLAccLinkUID Desc: GLAccLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLAccLinkRow
   */  
export function get_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company:string, COAMapUID:string, GLAccLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLAccLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_GLAccLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLAccLink for the service
   Description: Calls UpdateExt to update GLAccLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param GLAccLinkUID Desc: GLAccLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company:string, COAMapUID:string, GLAccLinkUID:string, requestBody:Erp_Tablesets_GLAccLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")", {
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
   Summary: Call UpdateExt to delete GLAccLink item
   Description: Call UpdateExt to delete GLAccLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param GLAccLinkUID Desc: GLAccLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company:string, COAMapUID:string, GLAccLinkUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")", {
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
   Description: Get SegmentLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegmentLinks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegmentLinkRow
   */  
export function get_SegmentLinks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegmentLinks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SegmentLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SegmentLinks(requestBody:Erp_Tablesets_SegmentLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks", {
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
   Summary: Calls GetByID to retrieve the SegmentLink item
   Description: Calls GetByID to retrieve the SegmentLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegmentLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param SegmentLinkUID Desc: SegmentLinkUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SegmentLinkRow
   */  
export function get_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company:string, COAMapUID:string, SegmentLinkUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SegmentLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")", {
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
         resolve(data as Erp_Tablesets_SegmentLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SegmentLink for the service
   Description: Calls UpdateExt to update SegmentLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegmentLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param SegmentLinkUID Desc: SegmentLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company:string, COAMapUID:string, SegmentLinkUID:string, requestBody:Erp_Tablesets_SegmentLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")", {
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
   Summary: Call UpdateExt to delete SegmentLink item
   Description: Call UpdateExt to delete SegmentLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegmentLink
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param COAMapUID Desc: COAMapUID   Required: True
      @param SegmentLinkUID Desc: SegmentLinkUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company:string, COAMapUID:string, SegmentLinkUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAMapListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapListRow)
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
export function get_GetRows(whereClauseCOAMap:string, whereClauseGLAccLink:string, whereClauseSegmentLink:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCOAMap!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCOAMap=" + whereClauseCOAMap
   }
   if(typeof whereClauseGLAccLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLAccLink=" + whereClauseGLAccLink
   }
   if(typeof whereClauseSegmentLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSegmentLink=" + whereClauseSegmentLink
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetRows" + params, {
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
export function get_GetByID(coAMapUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof coAMapUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "coAMapUID=" + coAMapUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetList" + params, {
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
   Summary: Invoke method GetByDisplayName
   Description: This method returns COAMapData dataset if display name is known
   OperationID: GetByDisplayName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByDisplayName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDisplayName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByDisplayName(requestBody:GetByDisplayName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByDisplayName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetByDisplayName", {
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
         resolve(data as GetByDisplayName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCOA
   Description: This method called when value of Source/Target COA were changed.
   OperationID: OnChangeCOA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCOA(requestBody:OnChangeCOA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCOA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/OnChangeCOA", {
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
         resolve(data as OnChangeCOA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Populate
   Description: Populates dataset
   OperationID: Populate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Populate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Populate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Populate(requestBody:Populate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Populate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/Populate", {
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
         resolve(data as Populate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTargetCOA
   Description: Validate target coa against correct table
   OperationID: ValidateTargetCOA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateTargetCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTargetCOA(requestBody:ValidateTargetCOA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateTargetCOA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/ValidateTargetCOA", {
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
         resolve(data as ValidateTargetCOA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateTargetCompany
   Description: Validate target coa against correct table
   OperationID: ValidateTargetCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateTargetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateTargetCompany(requestBody:ValidateTargetCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateTargetCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/ValidateTargetCompany", {
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
         resolve(data as ValidateTargetCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSegmentLink_WithSegmentsFilled
   Description: Get New Segment Link with Source/Target segment columns filled.
   OperationID: GetNewSegmentLink_WithSegmentsFilled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSegmentLink_WithSegmentsFilled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegmentLink_WithSegmentsFilled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSegmentLink_WithSegmentsFilled(requestBody:GetNewSegmentLink_WithSegmentsFilled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSegmentLink_WithSegmentsFilled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetNewSegmentLink_WithSegmentsFilled", {
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
         resolve(data as GetNewSegmentLink_WithSegmentsFilled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMapTypeDescList
   OperationID: GetMapTypeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapTypeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMapTypeDescList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMapTypeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetMapTypeDescList", {
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
         resolve(data as GetMapTypeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCOAGlobalStatus
   Description: Returns true if COA is global and false otherwise.
   OperationID: CheckCOAGlobalStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCOAGlobalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOAGlobalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCOAGlobalStatus(requestBody:CheckCOAGlobalStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCOAGlobalStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/CheckCOAGlobalStatus", {
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
         resolve(data as CheckCOAGlobalStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCOAMap
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOAMap
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCOAMap(requestBody:GetNewCOAMap_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCOAMap_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetNewCOAMap", {
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
         resolve(data as GetNewCOAMap_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLAccLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLAccLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLAccLink(requestBody:GetNewGLAccLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLAccLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetNewGLAccLink", {
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
         resolve(data as GetNewGLAccLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSegmentLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSegmentLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSegmentLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegmentLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSegmentLink(requestBody:GetNewSegmentLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSegmentLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetNewSegmentLink", {
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
         resolve(data as GetNewSegmentLink_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COAMapListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapRow{
   "odatametadata":string,
   "value":Erp_Tablesets_COAMapRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLAccLinkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SegmentLinkRow,
}

export interface Erp_Tablesets_COAMapListRow{
      /**  COA map unique ID.  */  
   "COAMapUID":number,
      /**  Display name  */  
   "DisplayName":string,
      /**  Detailed Description  */  
   "DetailedDescription":string,
      /**  type of COA for company  */  
   "SourceCOA":string,
      /**  type of COA for company  */  
   "TargetCOA":string,
      /**  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  */  
   "MapType":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  */  
   "GlobalCOASegmentTransform":boolean,
      /**  The description or Name of this Chart of Accounts.  */  
   "SourceCOADescription":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "TargetCOADescription":string,
      /**  The description or Name of this Chart of Accounts.  */  
   "TargetGLBCOADescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_COAMapRow{
      /**  COA map unique ID.  */  
   "COAMapUID":number,
      /**  Display name  */  
   "DisplayName":string,
      /**  Detailed Description  */  
   "DetailedDescription":string,
      /**  type of COA for company  */  
   "SourceCOA":string,
      /**  type of COA for company  */  
   "TargetCOA":string,
      /**  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  */  
   "MapType":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Target Company Identifier.  */  
   "TgtCompany":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  */  
   "GlobalCOASegmentTransform":boolean,
      /**  The ID of the interfaced company for Global Transform only.  */  
   "ExtCompanyID":string,
      /**  Target Segment - combobox filter.  */  
   "TargetSegment":number,
      /**  Target Segment - combobox filter.  */  
   "SourceSegment":number,
   "BitFlag":number,
   "SourceCOADescription":string,
   "TargetCOADescription":string,
   "TargetGLBCOADescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLAccLinkRow{
      /**  GLAccount Link unique ID.  */  
   "GLAccLinkUID":number,
      /**  COA map unique ID.  */  
   "COAMapUID":number,
      /**  System date when the link was created.  */  
   "CreationDate":string,
      /**  System time when the link was created (seconds since midnight format).  */  
   "CreationTime":number,
      /**  Source Chart of Account ID  */  
   "SourceCOA":string,
      /**  Source full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   "SourceGLAccount":string,
      /**  Source SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "SourceSegValue1":string,
      /**  Source SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "SourceSegValue2":string,
      /**  Source SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "SourceSegValue3":string,
      /**  Source SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "SourceSegValue4":string,
      /**  Source SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "SourceSegValue5":string,
      /**  Source SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "SourceSegValue6":string,
      /**  Source SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "SourceSegValue7":string,
      /**  Source SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "SourceSegValue8":string,
      /**  Source SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "SourceSegValue9":string,
      /**  Source SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "SourceSegValue10":string,
      /**  Source SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "SourceSegValue11":string,
      /**  Source SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "SourceSegValue12":string,
      /**  Source SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "SourceSegValue13":string,
      /**  Source SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "SourceSegValue14":string,
      /**  Source SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "SourceSegValue15":string,
      /**  Source SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "SourceSegValue16":string,
      /**  Source SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "SourceSegValue17":string,
      /**  Source SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "SourceSegValue18":string,
      /**  Source SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "SourceSegValue19":string,
      /**  Source SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "SourceSegValue20":string,
      /**  Target Chart of Account ID  */  
   "TargetCOA":string,
      /**  Target full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   "TargetGLAccount":string,
      /**  Target SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   "TargetSegValue1":string,
      /**  Target SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   "TargetSegValue2":string,
      /**  Target SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   "TargetSegValue3":string,
      /**  Target SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   "TargetSegValue4":string,
      /**  Target SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   "TargetSegValue5":string,
      /**  Target SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   "TargetSegValue6":string,
      /**  Target SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   "TargetSegValue7":string,
      /**  Target SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   "TargetSegValue8":string,
      /**  Target SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   "TargetSegValue9":string,
      /**  Target SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   "TargetSegValue10":string,
      /**  Target SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   "TargetSegValue11":string,
      /**  Target SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   "TargetSegValue12":string,
      /**  Target SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   "TargetSegValue13":string,
      /**  Target SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   "TargetSegValue14":string,
      /**  Target SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   "TargetSegValue15":string,
      /**  Target SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   "TargetSegValue16":string,
      /**  Target SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   "TargetSegValue17":string,
      /**  Target SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   "TargetSegValue18":string,
      /**  Target SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   "TargetSegValue19":string,
      /**  Target SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   "TargetSegValue20":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Target Company  */  
   "TargetCompany":string,
   "BitFlag":number,
   "SrcGLAccountDisplayGLShortAcct":string,
   "SrcGLAccountDisplayAccountDesc":string,
   "SrcGLAccountDisplayGLAcctDisp":string,
   "TgtGLAccountDisplayGLAcctDisp":string,
   "TgtGLAccountDisplayAccountDesc":string,
   "TgtGLAccountDisplayGLShortAcct":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SegmentLinkRow{
      /**  Segment Link unique ID.  */  
   "SegmentLinkUID":number,
      /**  COA map unique ID.  */  
   "COAMapUID":number,
      /**  type of COA for company  */  
   "SourceCOA":string,
      /**  1-30  */  
   "SourceSegment":number,
      /**  Source Segment Value  */  
   "SourceSegValue":string,
      /**  type of COA for company  */  
   "TargetCOA":string,
      /**  1-30  */  
   "TargetSegment":number,
      /**  Target Segment Value  */  
   "TargetSegValue":string,
      /**  System date when the link was created.  */  
   "CreationDate":string,
      /**  System time when the link was created (seconds since midnight format).  */  
   "CreationTime":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Short name of the segment value used for Global Transform only.  */  
   "SegmentAbbrev":string,
      /**  Segment description used for Global Transform only.  */  
   "SegmentDesc":string,
   "BitFlag":number,
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
      @param ipCOACode
   */  
export interface CheckCOAGlobalStatus_input{
   ipCOACode:string,
}

export interface CheckCOAGlobalStatus_output{
   returnObj:boolean,
}

   /** Required : 
      @param coAMapUID
   */  
export interface DeleteByID_input{
   coAMapUID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_COAMapDataTableset{
   COAMap:Erp_Tablesets_COAMapRow[],
   GLAccLink:Erp_Tablesets_GLAccLinkRow[],
   SegmentLink:Erp_Tablesets_SegmentLinkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_COAMapListRow{
      /**  COA map unique ID.  */  
   COAMapUID:number,
      /**  Display name  */  
   DisplayName:string,
      /**  Detailed Description  */  
   DetailedDescription:string,
      /**  type of COA for company  */  
   SourceCOA:string,
      /**  type of COA for company  */  
   TargetCOA:string,
      /**  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  */  
   MapType:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  */  
   GlobalCOASegmentTransform:boolean,
      /**  The description or Name of this Chart of Accounts.  */  
   SourceCOADescription:string,
      /**  The description or Name of this Chart of Accounts.  */  
   TargetCOADescription:string,
      /**  The description or Name of this Chart of Accounts.  */  
   TargetGLBCOADescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_COAMapListTableset{
   COAMapList:Erp_Tablesets_COAMapListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_COAMapRow{
      /**  COA map unique ID.  */  
   COAMapUID:number,
      /**  Display name  */  
   DisplayName:string,
      /**  Detailed Description  */  
   DetailedDescription:string,
      /**  type of COA for company  */  
   SourceCOA:string,
      /**  type of COA for company  */  
   TargetCOA:string,
      /**  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  */  
   MapType:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Target Company Identifier.  */  
   TgtCompany:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  */  
   GlobalCOASegmentTransform:boolean,
      /**  The ID of the interfaced company for Global Transform only.  */  
   ExtCompanyID:string,
      /**  Target Segment - combobox filter.  */  
   TargetSegment:number,
      /**  Target Segment - combobox filter.  */  
   SourceSegment:number,
   BitFlag:number,
   SourceCOADescription:string,
   TargetCOADescription:string,
   TargetGLBCOADescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLAccLinkRow{
      /**  GLAccount Link unique ID.  */  
   GLAccLinkUID:number,
      /**  COA map unique ID.  */  
   COAMapUID:number,
      /**  System date when the link was created.  */  
   CreationDate:string,
      /**  System time when the link was created (seconds since midnight format).  */  
   CreationTime:number,
      /**  Source Chart of Account ID  */  
   SourceCOA:string,
      /**  Source full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   SourceGLAccount:string,
      /**  Source SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   SourceSegValue1:string,
      /**  Source SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   SourceSegValue2:string,
      /**  Source SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   SourceSegValue3:string,
      /**  Source SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   SourceSegValue4:string,
      /**  Source SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   SourceSegValue5:string,
      /**  Source SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   SourceSegValue6:string,
      /**  Source SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   SourceSegValue7:string,
      /**  Source SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   SourceSegValue8:string,
      /**  Source SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   SourceSegValue9:string,
      /**  Source SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   SourceSegValue10:string,
      /**  Source SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   SourceSegValue11:string,
      /**  Source SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   SourceSegValue12:string,
      /**  Source SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   SourceSegValue13:string,
      /**  Source SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   SourceSegValue14:string,
      /**  Source SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   SourceSegValue15:string,
      /**  Source SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   SourceSegValue16:string,
      /**  Source SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   SourceSegValue17:string,
      /**  Source SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   SourceSegValue18:string,
      /**  Source SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   SourceSegValue19:string,
      /**  Source SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   SourceSegValue20:string,
      /**  Target Chart of Account ID  */  
   TargetCOA:string,
      /**  Target full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  */  
   TargetGLAccount:string,
      /**  Target SegmentValue 1.  See COASegment segment number 1 for a description of this field.  */  
   TargetSegValue1:string,
      /**  Target SegmentValue 2.  See COASegment segment number 2 for a description of this field.  */  
   TargetSegValue2:string,
      /**  Target SegmentValue 3.  See COASegment segment number 3 for a description of this field.  */  
   TargetSegValue3:string,
      /**  Target SegmentValue 4.  See COASegment segment number 4 for a description of this field.  */  
   TargetSegValue4:string,
      /**  Target SegmentValue 5.  See COASegment segment number 5 for a description of this field.  */  
   TargetSegValue5:string,
      /**  Target SegmentValue 6.  See COASegment segment number 6 for a description of this field.  */  
   TargetSegValue6:string,
      /**  Target SegmentValue 7.  See COASegment segment number 7 for a description of this field.  */  
   TargetSegValue7:string,
      /**  Target SegmentValue 8.  See COASegment segment number 8 for a description of this field.  */  
   TargetSegValue8:string,
      /**  Target SegmentValue 9.  See COASegment segment number 9 for a description of this field.  */  
   TargetSegValue9:string,
      /**  Target SegmentValue 10.  See COASegment segment number 10 for a description of this field.  */  
   TargetSegValue10:string,
      /**  Target SegmentValue 11.  See COASegment segment number 11 for a description of this field.  */  
   TargetSegValue11:string,
      /**  Target SegmentValue 12.  See COASegment segment number 12 for a description of this field.  */  
   TargetSegValue12:string,
      /**  Target SegmentValue 13.  See COASegment segment number 13 for a description of this field.  */  
   TargetSegValue13:string,
      /**  Target SegmentValue 14.  See COASegment segment number 14 for a description of this field.  */  
   TargetSegValue14:string,
      /**  Target SegmentValue 15.  See COASegment segment number 15 for a description of this field.  */  
   TargetSegValue15:string,
      /**  Target SegmentValue 16.  See COASegment segment number 16 for a description of this field.  */  
   TargetSegValue16:string,
      /**  Target SegmentValue 17.  See COASegment segment number 17 for a description of this field.  */  
   TargetSegValue17:string,
      /**  Target SegmentValue 18.  See COASegment segment number 18 for a description of this field.  */  
   TargetSegValue18:string,
      /**  Target SegmentValue 19.  See COASegment segment number 19 for a description of this field.  */  
   TargetSegValue19:string,
      /**  Target SegmentValue 20.  See COASegment segment number 20 for a description of this field.  */  
   TargetSegValue20:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Target Company  */  
   TargetCompany:string,
   BitFlag:number,
   SrcGLAccountDisplayGLShortAcct:string,
   SrcGLAccountDisplayAccountDesc:string,
   SrcGLAccountDisplayGLAcctDisp:string,
   TgtGLAccountDisplayGLAcctDisp:string,
   TgtGLAccountDisplayAccountDesc:string,
   TgtGLAccountDisplayGLShortAcct:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SegmentLinkRow{
      /**  Segment Link unique ID.  */  
   SegmentLinkUID:number,
      /**  COA map unique ID.  */  
   COAMapUID:number,
      /**  type of COA for company  */  
   SourceCOA:string,
      /**  1-30  */  
   SourceSegment:number,
      /**  Source Segment Value  */  
   SourceSegValue:string,
      /**  type of COA for company  */  
   TargetCOA:string,
      /**  1-30  */  
   TargetSegment:number,
      /**  Target Segment Value  */  
   TargetSegValue:string,
      /**  System date when the link was created.  */  
   CreationDate:string,
      /**  System time when the link was created (seconds since midnight format).  */  
   CreationTime:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Short name of the segment value used for Global Transform only.  */  
   SegmentAbbrev:string,
      /**  Segment description used for Global Transform only.  */  
   SegmentDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCOAMapDataTableset{
   COAMap:Erp_Tablesets_COAMapRow[],
   GLAccLink:Erp_Tablesets_GLAccLinkRow[],
   SegmentLink:Erp_Tablesets_SegmentLinkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param displayName
   */  
export interface GetByDisplayName_input{
      /**  Display Name  */  
   displayName:string,
}

export interface GetByDisplayName_output{
   returnObj:Erp_Tablesets_COAMapDataTableset[],
}

   /** Required : 
      @param coAMapUID
   */  
export interface GetByID_input{
   coAMapUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_COAMapDataTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_COAMapDataTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_COAMapDataTableset[],
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
   returnObj:Erp_Tablesets_COAMapListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMapTypeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface GetNewCOAMap_input{
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface GetNewCOAMap_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param ds
      @param coAMapUID
   */  
export interface GetNewGLAccLink_input{
   ds:Erp_Tablesets_COAMapDataTableset[],
   coAMapUID:number,
}

export interface GetNewGLAccLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param coAMapUID
      @param sourceSegment
      @param targetSegment
      @param ds
   */  
export interface GetNewSegmentLink_WithSegmentsFilled_input{
   coAMapUID:number,
   sourceSegment:number,
   targetSegment:number,
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface GetNewSegmentLink_WithSegmentsFilled_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param ds
      @param coAMapUID
   */  
export interface GetNewSegmentLink_input{
   ds:Erp_Tablesets_COAMapDataTableset[],
   coAMapUID:number,
}

export interface GetNewSegmentLink_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param whereClauseCOAMap
      @param whereClauseGLAccLink
      @param whereClauseSegmentLink
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCOAMap:string,
   whereClauseGLAccLink:string,
   whereClauseSegmentLink:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_COAMapDataTableset[],
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
      @param coa
   */  
export interface OnChangeCOA_input{
      /**  Source/Target COA  */  
   coa:string,
}

export interface OnChangeCOA_output{
}

   /** Required : 
      @param iCoaMap
      @param cSource
      @param cTarget
      @param iSrcSeg
      @param iTrgSeg
      @param cFld
      @param ds
   */  
export interface Populate_input{
      /**  srcSeg  */  
   iCoaMap:number,
      /**  field  */  
   cSource:string,
      /**  field  */  
   cTarget:string,
      /**  srcSeg  */  
   iSrcSeg:number,
      /**  trgSeg  */  
   iTrgSeg:number,
      /**  field  */  
   cFld:string,
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface Populate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCOAMapDataTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCOAMapDataTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param ipTargetCOA
      @param ds
   */  
export interface ValidateTargetCOA_input{
      /**  Proposed COA code  */  
   ipTargetCOA:string,
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface ValidateTargetCOA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

   /** Required : 
      @param ipTargetCompany
      @param ds
   */  
export interface ValidateTargetCompany_input{
      /**  Proposed target Company  */  
   ipTargetCompany:string,
   ds:Erp_Tablesets_COAMapDataTableset[],
}

export interface ValidateTargetCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_COAMapDataTableset,
}
}

