import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GlRptMasSvc
// Description: Financial Report Designer business object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/$metadata", {
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
   Description: Get GlRptMas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlRptMas
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptMasRow
   */  
export function get_GlRptMas(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlRptMas
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlRptMasRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlRptMas(requestBody:Erp_Tablesets_GlRptMasRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas", {
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
   Summary: Calls GetByID to retrieve the GlRptMa item
   Description: Calls GetByID to retrieve the GlRptMa item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlRptMasRow
   */  
export function get_GlRptMas_Company_ReportID(Company:string, ReportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlRptMasRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")", {
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
         resolve(data as Erp_Tablesets_GlRptMasRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlRptMa for the service
   Description: Calls UpdateExt to update GlRptMa. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlRptMasRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlRptMas_Company_ReportID(Company:string, ReportID:string, requestBody:Erp_Tablesets_GlRptMasRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")", {
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
   Summary: Call UpdateExt to delete GlRptMa item
   Description: Call UpdateExt to delete GlRptMa item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlRptMa
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlRptMas_Company_ReportID(Company:string, ReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")", {
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
   Description: Get GLRptColSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptColSets1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColSetRow
   */  
export function get_GlRptMas_Company_ReportID_GLRptColSets(Company:string, ReportID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GLRptColSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLRptColSet item
   Description: Calls GetByID to retrieve the GLRptColSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptColSet1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptColSetRow
   */  
export function get_GlRptMas_Company_ReportID_GLRptColSets_Company_ReportID_ColSetSeq(Company:string, ReportID:string, ColSetSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptColSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLRptColSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GlRptRows items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlRptRows1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptRowRow
   */  
export function get_GlRptMas_Company_ReportID_GlRptRows(Company:string, ReportID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GlRptRows", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GlRptRow item
   Description: Calls GetByID to retrieve the GlRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptRow1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlRptRowRow
   */  
export function get_GlRptMas_Company_ReportID_GlRptRows_Company_ReportID_LineNum(Company:string, ReportID:string, LineNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptMas(" + Company + "," + ReportID + ")/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")", {
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
         resolve(data as Erp_Tablesets_GlRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLRptColSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptColSets
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColSetRow
   */  
export function get_GLRptColSets(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptColSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLRptColSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLRptColSets(requestBody:Erp_Tablesets_GLRptColSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets", {
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
   Summary: Calls GetByID to retrieve the GLRptColSet item
   Description: Calls GetByID to retrieve the GLRptColSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptColSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptColSetRow
   */  
export function get_GLRptColSets_Company_ReportID_ColSetSeq(Company:string, ReportID:string, ColSetSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptColSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")", {
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
         resolve(data as Erp_Tablesets_GLRptColSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLRptColSet for the service
   Description: Calls UpdateExt to update GLRptColSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptColSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptColSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLRptColSets_Company_ReportID_ColSetSeq(Company:string, ReportID:string, ColSetSeq:string, requestBody:Erp_Tablesets_GLRptColSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")", {
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
   Summary: Call UpdateExt to delete GLRptColSet item
   Description: Call UpdateExt to delete GLRptColSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptColSet
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLRptColSets_Company_ReportID_ColSetSeq(Company:string, ReportID:string, ColSetSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")", {
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
   Description: Get GLRptCols items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptCols1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColRow
   */  
export function get_GLRptColSets_Company_ReportID_ColSetSeq_GLRptCols(Company:string, ReportID:string, ColSetSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")/GLRptCols", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLRptCol item
   Description: Calls GetByID to retrieve the GLRptCol item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptCol1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetSeq Desc: ColSetSeq   Required: True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColumnNum Desc: ColumnNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptColRow
   */  
export function get_GLRptColSets_Company_ReportID_ColSetSeq_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company:string, ReportID:string, ColSetSeq:string, ColSetID:string, ColumnNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptColRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptColSets(" + Company + "," + ReportID + "," + ColSetSeq + ")/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GLRptColRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLRptCols items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptCols
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptColRow
   */  
export function get_GLRptCols(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptCols
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLRptColRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLRptCols(requestBody:Erp_Tablesets_GLRptColRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols", {
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
   Summary: Calls GetByID to retrieve the GLRptCol item
   Description: Calls GetByID to retrieve the GLRptCol item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptCol
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColumnNum Desc: ColumnNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptColRow
   */  
export function get_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company:string, ReportID:string, ColSetID:string, ColumnNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptColRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")", {
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
         resolve(data as Erp_Tablesets_GLRptColRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLRptCol for the service
   Description: Calls UpdateExt to update GLRptCol. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptCol
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColumnNum Desc: ColumnNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptColRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company:string, ReportID:string, ColSetID:string, ColumnNum:string, SysRowID:string, requestBody:Erp_Tablesets_GLRptColRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete GLRptCol item
   Description: Call UpdateExt to delete GLRptCol item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptCol
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param ColSetID Desc: ColSetID   Required: True   Allow empty value : True
      @param ColumnNum Desc: ColumnNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLRptCols_Company_ReportID_ColSetID_ColumnNum_SysRowID(Company:string, ReportID:string, ColSetID:string, ColumnNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptCols(" + Company + "," + ReportID + "," + ColSetID + "," + ColumnNum + "," + SysRowID + ")", {
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
   Description: Get GlRptRows items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlRptRows
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptRowRow
   */  
export function get_GlRptRows(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlRptRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlRptRowRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlRptRows(requestBody:Erp_Tablesets_GlRptRowRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows", {
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
   Summary: Calls GetByID to retrieve the GlRptRow item
   Description: Calls GetByID to retrieve the GlRptRow item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlRptRowRow
   */  
export function get_GlRptRows_Company_ReportID_LineNum(Company:string, ReportID:string, LineNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlRptRowRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")", {
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
         resolve(data as Erp_Tablesets_GlRptRowRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlRptRow for the service
   Description: Calls UpdateExt to update GlRptRow. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlRptRowRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlRptRows_Company_ReportID_LineNum(Company:string, ReportID:string, LineNum:string, requestBody:Erp_Tablesets_GlRptRowRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")", {
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
   Summary: Call UpdateExt to delete GlRptRow item
   Description: Call UpdateExt to delete GlRptRow item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlRptRow
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlRptRows_Company_ReportID_LineNum(Company:string, ReportID:string, LineNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")", {
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
   Description: Get GLRptRowAccts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLRptRowAccts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptRowAcctRow
   */  
export function get_GlRptRows_Company_ReportID_LineNum_GLRptRowAccts(Company:string, ReportID:string, LineNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")/GLRptRowAccts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLRptRowAcct item
   Description: Calls GetByID to retrieve the GLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptRowAcct1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   */  
export function get_GlRptRows_Company_ReportID_LineNum_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company:string, ReportID:string, LineNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GlRptRows(" + Company + "," + ReportID + "," + LineNum + ")/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_GLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GLRptRowAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLRptRowAccts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLRptRowAcctRow
   */  
export function get_GLRptRowAccts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLRptRowAccts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLRptRowAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLRptRowAccts(requestBody:Erp_Tablesets_GLRptRowAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts", {
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
   Summary: Calls GetByID to retrieve the GLRptRowAcct item
   Description: Calls GetByID to retrieve the GLRptRowAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   */  
export function get_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company:string, ReportID:string, LineNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLRptRowAcctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")", {
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
         resolve(data as Erp_Tablesets_GLRptRowAcctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLRptRowAcct for the service
   Description: Calls UpdateExt to update GLRptRowAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLRptRowAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company:string, ReportID:string, LineNum:string, SeqNum:string, requestBody:Erp_Tablesets_GLRptRowAcctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete GLRptRowAcct item
   Description: Call UpdateExt to delete GLRptRowAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLRptRowAcct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param LineNum Desc: LineNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLRptRowAccts_Company_ReportID_LineNum_SeqNum(Company:string, ReportID:string, LineNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GLRptRowAccts(" + Company + "," + ReportID + "," + LineNum + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlRptMasListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasListRow)
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
export function get_GetRows(whereClauseGlRptMas:string, whereClauseGLRptColSet:string, whereClauseGLRptCol:string, whereClauseGlRptRow:string, whereClauseGLRptRowAcct:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlRptMas!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlRptMas=" + whereClauseGlRptMas
   }
   if(typeof whereClauseGLRptColSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRptColSet=" + whereClauseGLRptColSet
   }
   if(typeof whereClauseGLRptCol!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRptCol=" + whereClauseGLRptCol
   }
   if(typeof whereClauseGlRptRow!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlRptRow=" + whereClauseGlRptRow
   }
   if(typeof whereClauseGLRptRowAcct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLRptRowAcct=" + whereClauseGLRptRowAcct
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetRows" + params, {
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
export function get_GetByID(reportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reportID=" + reportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetList" + params, {
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
   Summary: Invoke method CategoryOrAccountsList
   Description: Method to call to get the list for Category or Accounts option.  The list is
returned in code1`code desc1~code2`code desc2 format.
   OperationID: CategoryOrAccountsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CategoryOrAccountsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CategoryOrAccountsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CategoryOrAccountsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/CategoryOrAccountsList", {
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
         resolve(data as CategoryOrAccountsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptColColSetID
   Description: Method to call when the GLRptCol.ColSetID value changes.  The ColSetID can only
be changed for a new record.  This method will reassign the ColSetID of the
GLRptColSet record.
Prior to calling this method, the GLRptColSet record that exists for the GLRptCol
record needs to have the RowMod field set to 'U'.
   OperationID: ChangeGLRptColColSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColColSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColColSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptColColSetID(requestBody:ChangeGLRptColColSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptColColSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptColColSetID", {
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
         resolve(data as ChangeGLRptColColSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptColColumnType
   Description: Method to call to reset values in a GLRptCol record when the column type changes.
   OperationID: ChangeGLRptColColumnType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColColumnType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColColumnType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptColColumnType(requestBody:ChangeGLRptColColumnType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptColColumnType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptColColumnType", {
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
         resolve(data as ChangeGLRptColColumnType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptColIntervalType
   Description: Method to call when the GLRptCol.IntervalType value changes.
   OperationID: ChangeGLRptColIntervalType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptColIntervalType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptColIntervalType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptColIntervalType(requestBody:ChangeGLRptColIntervalType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptColIntervalType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptColIntervalType", {
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
         resolve(data as ChangeGLRptColIntervalType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptMasBookID
   Description: Method to call when the GLRptMas.BookID value changes.
   OperationID: ChangeGLRptMasBookID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptMasBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptMasBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptMasBookID(requestBody:ChangeGLRptMasBookID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptMasBookID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptMasBookID", {
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
         resolve(data as ChangeGLRptMasBookID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptRowCategoryOrAccounts
   Description: Method to call to reset values in a GLRptRow record when the category or accounts
option changes.
Prior to calling this method, any GLRptRow subrecords that exist for the GLRptRow
record need to have the RowMod field set to 'U'.  The subtables for GLRptRow are:
GLRptRowAccounts, GLRptRowCharts, GLRptRowDepts, GLRptRowDivisions.
   OperationID: ChangeGLRptRowCategoryOrAccounts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptRowCategoryOrAccounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptRowCategoryOrAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptRowCategoryOrAccounts(requestBody:ChangeGLRptRowCategoryOrAccounts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptRowCategoryOrAccounts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptRowCategoryOrAccounts", {
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
         resolve(data as ChangeGLRptRowCategoryOrAccounts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGLRptRowLineType
   Description: Method to call to reset values in a GLRptRow record when the line type changes.
Prior to calling this method, any GLRptRow subrecords that exist for the GLRptRow
record need to have the RowMod field set to 'U'.  The subtables for GLRptRow are:
GLRptRowAccounts, GLRptRowCharts, GLRptRowDepts, GLRptRowDivisions.
   OperationID: ChangeGLRptRowLineType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGLRptRowLineType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLRptRowLineType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGLRptRowLineType(requestBody:ChangeGLRptRowLineType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGLRptRowLineType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ChangeGLRptRowLineType", {
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
         resolve(data as ChangeGLRptRowLineType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ColumnTypeList
   Description: Method to call to get the list of valid column types.  The list is returned in
code1`code desc1~code2`code desc2 format.
   OperationID: ColumnTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ColumnTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ColumnTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ColumnTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ColumnTypeList", {
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
         resolve(data as ColumnTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteColSet
   Description: Method to call to delete a column set for a financial report.  This method
delete the records in the column set and return the GlRptMas dataset.
   OperationID: DeleteColSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteColSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteColSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteColSet(requestBody:DeleteColSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteColSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/DeleteColSet", {
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
         resolve(data as DeleteColSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateFinancialReport
   Description: Method to call to duplicate a financial report.  This method will return the
newly created records in the GlRptMas dataset.
   OperationID: DuplicateFinancialReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateFinancialReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateFinancialReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateFinancialReport(requestBody:DuplicateFinancialReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateFinancialReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/DuplicateFinancialReport", {
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
         resolve(data as DuplicateFinancialReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLRptRowAcctForType
   Description: Creates a new GLRptRowAcct record based on type.
   OperationID: GetNewGLRptRowAcctForType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLRptRowAcctForType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptRowAcctForType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRptRowAcctForType(requestBody:GetNewGLRptRowAcctForType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLRptRowAcctForType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetNewGLRptRowAcctForType", {
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
         resolve(data as GetNewGLRptRowAcctForType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetCodeDescList", {
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
   Summary: Invoke method LineTypeList
   Description: Method to call to get the list of valid line types.  The list is returned in
code1`code desc1~code2`code desc2 format.
   OperationID: LineTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/LineTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LineTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LineTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/LineTypeList", {
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
         resolve(data as LineTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveGLRptColDown
   Description: Method to call to move a report column down within a column set.  This method
resequences the columns as appropriate and returns the updated dataset.
   OperationID: MoveGLRptColDown
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveGLRptColDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveGLRptColDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveGLRptColDown(requestBody:MoveGLRptColDown_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveGLRptColDown_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/MoveGLRptColDown", {
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
         resolve(data as MoveGLRptColDown_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MoveGLRptColUp
   Description: Method to call to move a report column up within a column set.  This method
resequences the columns as appropriate and returns the updated dataset.
   OperationID: MoveGLRptColUp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MoveGLRptColUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveGLRptColUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MoveGLRptColUp(requestBody:MoveGLRptColUp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MoveGLRptColUp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/MoveGLRptColUp", {
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
         resolve(data as MoveGLRptColUp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReportWizard
   Description: Method to call to create a financial report using a wizard.  The wizard
will create a template report that be modified via the GlRptMas dataset.
   OperationID: ReportWizard
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReportWizard_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportWizard_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportWizard(requestBody:ReportWizard_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReportWizard_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ReportWizard", {
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
         resolve(data as ReportWizard_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReportWizardOptionsList
   Description: Method to call to get the list of valid options for the report wizard.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: ReportWizardOptionsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportWizardOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportWizardOptionsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReportWizardOptionsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ReportWizardOptionsList", {
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
         resolve(data as ReportWizardOptionsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SyntaxCheck
   Description: Method to call to check the syntax of a report.  Syntax errors that occured
will be stored in datatable GLRptSyntaxErrors.
   OperationID: SyntaxCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SyntaxCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyntaxCheck(requestBody:SyntaxCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SyntaxCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/SyntaxCheck", {
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
         resolve(data as SyntaxCheck_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SyntaxCheckForWeb
   Description: Method to call to check the syntax of a report.  Syntax errors that occured
will be stored in datatable GLRptSyntaxErrors.
Introduced for web use only.
   OperationID: SyntaxCheckForWeb
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SyntaxCheckForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheckForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyntaxCheckForWeb(requestBody:SyntaxCheckForWeb_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SyntaxCheckForWeb_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/SyntaxCheckForWeb", {
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
         resolve(data as SyntaxCheckForWeb_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SyntaxCheckOptionsList
   Description: Method to call to get the list of valid options for the syntax check.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: SyntaxCheckOptionsList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyntaxCheckOptionsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyntaxCheckOptionsList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SyntaxCheckOptionsList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/SyntaxCheckOptionsList", {
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
         resolve(data as SyntaxCheckOptionsList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGLRptRow
   Description: Method to call to validate that accounts or charts have been added to a row.
if applicable.  If accounts or charts are required, an exception will be thrown.
This method should be called prior to leaving the row for a different row.
   OperationID: ValidateGLRptRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGLRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGLRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGLRptRow(requestBody:ValidateGLRptRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGLRptRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ValidateGLRptRow", {
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
         resolve(data as ValidateGLRptRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method YesNoDefaultList
   Description: Method to call to get the list of valid entries for Yes/No/Default options.
The list is returned in code1`code desc1~code2`code desc2 format.
   OperationID: YesNoDefaultList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/YesNoDefaultList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_YesNoDefaultList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<YesNoDefaultList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/YesNoDefaultList", {
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
         resolve(data as YesNoDefaultList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportDefinition
   Description: Export Report Definition to XML
   OperationID: ExportReportDefinition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportDefinition(requestBody:ExportReportDefinition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportDefinition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ExportReportDefinition", {
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
         resolve(data as ExportReportDefinition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportDefinition2
   Description: Export Report Definition to XML, web make.
   OperationID: ExportReportDefinition2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportDefinition2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportDefinition2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportDefinition2(requestBody:ExportReportDefinition2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportDefinition2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ExportReportDefinition2", {
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
         resolve(data as ExportReportDefinition2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateImportedReportDefinition
   Description: Validates imported (as an XML file) report definition.
   OperationID: ValidateImportedReportDefinition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateImportedReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateImportedReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateImportedReportDefinition(requestBody:ValidateImportedReportDefinition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateImportedReportDefinition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ValidateImportedReportDefinition", {
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
         resolve(data as ValidateImportedReportDefinition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReportDefinition
   Description: Import Report Definition from XML Data
   OperationID: ImportReportDefinition
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportDefinition(requestBody:ImportReportDefinition_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReportDefinition_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ImportReportDefinition", {
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
         resolve(data as ImportReportDefinition_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReportDefinition2
   Description: Import Report Definition from XML Data, web make.
   OperationID: ImportReportDefinition2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReportDefinition2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportDefinition2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportDefinition2(requestBody:ImportReportDefinition2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReportDefinition2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/ImportReportDefinition2", {
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
         resolve(data as ImportReportDefinition2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGlRptMas
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlRptMas
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlRptMas_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlRptMas_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlRptMas(requestBody:GetNewGlRptMas_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlRptMas_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetNewGlRptMas", {
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
         resolve(data as GetNewGlRptMas_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLRptCol
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRptCol
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLRptCol_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptCol_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRptCol(requestBody:GetNewGLRptCol_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLRptCol_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetNewGLRptCol", {
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
         resolve(data as GetNewGLRptCol_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGlRptRow
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlRptRow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlRptRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlRptRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlRptRow(requestBody:GetNewGlRptRow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlRptRow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetNewGlRptRow", {
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
         resolve(data as GetNewGlRptRow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLRptRowAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLRptRowAcct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLRptRowAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLRptRowAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLRptRowAcct(requestBody:GetNewGLRptRowAcct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLRptRowAcct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetNewGLRptRowAcct", {
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
         resolve(data as GetNewGLRptRowAcct_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlRptMasSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRptColRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptColSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRptColSetRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLRptRowAcctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLRptRowAcctRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlRptMasListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptMasRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlRptMasRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlRptRowRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlRptRowRow,
}

export interface Erp_Tablesets_GLRptColRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Column Set Identifier used to establish different sets of columns for the same report specifications.  */  
   "ColSetID":string,
      /**  Indicates the number (position/order) of the column.  */  
   "ColumnNum":number,
      /**  This pertains to a  "Variance Column" only. Indicates if the variance is to be shown as a percentage or amount.  */  
   "ShowAsPercent":boolean,
      /**  Used only for "Variance" columns.  Contains the "ColumnID" of the first column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  */  
   "VarCol1":number,
      /**  Used only for "Variance" columns.  Contains the "ColumnID" of the second column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  */  
   "VarCol2":number,
      /**  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the first column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  */  
   "TotalCol1":number,
      /**  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the  last column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  */  
   "TotalCol2":number,
      /**  Column title line one.  */  
   "ColumnTitle1":string,
      /**  Column title line two.  */  
   "ColumnTitle2":string,
      /**  A = Actuals,  B = Budget,  C = Comparative %, N = Acct #,  T = Text,   V = Variance, X = Crossfoot Total , U = statistical Unit of Measure, Q = Statistical Quantity , R - Report Category , D = Report Category Description  */  
   "ColumnType":string,
      /**  (Reporting year - YearOffset) = Fiscal Year of data in this column.  Ex: zero equal current year, 1 = prior year, etc...  */  
   "YearOffset":number,
      /**  (Reporting Period - PeriodOffset) = Fiscal Period of data in this column.  Ex: zero = current period, 1 = prior period, etc...  */  
   "PeriodOffset":number,
      /**   Number of fiscal period balances to be summarized into column.
Examples: Single Period = 01, Quarters = 3, Ytd = # of periods in fiscal year.  The system begins summarizing GL period balances starting at  "Given fiscal year - Year Offset", "Given fiscal period - period offset for the Number of periods indicated here.  If RollPeriods = No the summarization stops at period 1 of the "Given Fiscal Year - Year Offset", else it continues to the prior year.
NOTE: NumOfPeriods should not be > GLSyst.NumberofPeriods.  If it is logic will only summarize to the greater of the two.  */  
   "NumOfPeriods":number,
      /**  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfPeriods indicated.  In most cases this would be NO.  To produce a rolling number of periods the answer would be Yes.  */  
   "RollingPeriods":boolean,
      /**   Override FontName that is used for the Column Heading.
Default is GLRptMas.ReportFont  */  
   "TitleFont":string,
      /**  Override Font Size used for the column title. Default is Report.FontSize.  */  
   "TitleFontSize":number,
      /**   Override underline attribute for the column title.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "TitleUnderline":string,
      /**   Override Bold attribute for the column title.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "TitleBold":string,
      /**   Override Italic attribute for the column title.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "TitleItalic":string,
      /**  Override Font default that is used for the data in this column.  Default is GLRptMas.ReportFont  */  
   "DataFont":string,
      /**  Override default Font Size used for data in this column. Default is GLRptMas.ReportFontSize.  */  
   "DataFontSize":number,
      /**   Underline attribute for the data in this column.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "DataUnderline":string,
      /**   Bold attribute for data in this column.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "DataBold":string,
      /**   Italic attribute for data in this column.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "DataItalic":string,
      /**  Daily Average Balance option  */  
   "DailyAveBalance":boolean,
      /**  Number of day balances to be summarized into column.  */  
   "NumOfDays":number,
      /**  Days offset  */  
   "DaysOffset":number,
      /**   Indicates if balances will be calculated by days or by periods.  Values are:
P - By Period
D - By Day  */  
   "IntervalType":string,
      /**  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfDays indicated.  In most cases this would be NO.  To produce a rolling number of days the answer would be Yes.  */  
   "RollingDays":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  OverrideBudgetCode  */  
   "OverrideBudgetCode":boolean,
      /**  BudgetCodeID  */  
   "BudgetCodeID":string,
   "ColSetSeq":number,
   "BitFlag":number,
   "ReportIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLRptColSetRow{
   "Company":string,
   "ReportID":string,
   "ColSetID":string,
   "ColumnTitle01":string,
   "ColumnTitle02":string,
   "ColumnTitle03":string,
   "ColumnTitle04":string,
   "ColumnTitle05":string,
   "ColumnTitle06":string,
   "ColumnTitle07":string,
   "ColumnTitle08":string,
   "ColumnTitle09":string,
   "ColumnTitle10":string,
   "ColumnTitle11":string,
   "ColumnTitle12":string,
   "ColumnTitle13":string,
   "ColumnTitle14":string,
   "ColumnTitle15":string,
   "ColumnTitle16":string,
   "ColumnTitle17":string,
   "ColumnTitle18":string,
   "ColumnTitle19":string,
   "ColumnTitle20":string,
   "ColSetSeq":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLRptRowAcctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Line number  */  
   "LineNum":number,
      /**  Sequence number.   This along with ReportID and LineNum uniquely identifies the record.  */  
   "SeqNum":number,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**  The segment number.  Blank if using a full account.  */  
   "SegmentNbr":number,
      /**  From Segement Value 1.  */  
   "FromSegValue1":string,
      /**  From Segement Value 2.  */  
   "FromSegValue2":string,
      /**  From Segement Value 3.  */  
   "FromSegValue3":string,
      /**  From Segement Value 4.  */  
   "FromSegValue4":string,
      /**  From Segement Value 5.  */  
   "FromSegValue5":string,
      /**  From Segement Value 6.  */  
   "FromSegValue6":string,
      /**  From Segement Value 7.  */  
   "FromSegValue7":string,
      /**  From Segement Value 8.  */  
   "FromSegValue8":string,
      /**  From Segement Value 9.  */  
   "FromSegValue9":string,
      /**  From Segement Value 10.  */  
   "FromSegValue10":string,
      /**  From Segement Value 11.  */  
   "FromSegValue11":string,
      /**  From Segement Value 12.  */  
   "FromSegValue12":string,
      /**  From Segement Value 13.  */  
   "FromSegValue13":string,
      /**  From Segement Value 14.  */  
   "FromSegValue14":string,
      /**  From Segement Value 15.  */  
   "FromSegValue15":string,
      /**  From Segement Value 16.  */  
   "FromSegValue16":string,
      /**  From Segement Value 17.  */  
   "FromSegValue17":string,
      /**  From Segement Value 18.  */  
   "FromSegValue18":string,
      /**  From Segement Value 19.  */  
   "FromSegValue19":string,
      /**  From Segement Value 20.  */  
   "FromSegValue20":string,
      /**  To Segement Value 1.  */  
   "ToSegValue1":string,
      /**  To Segement Value 2.  */  
   "ToSegValue2":string,
      /**  To Segement Value 3.  */  
   "ToSegValue3":string,
      /**  To Segement Value 4.  */  
   "ToSegValue4":string,
      /**  To Segement Value 5.  */  
   "ToSegValue5":string,
      /**  To Segement Value 6.  */  
   "ToSegValue6":string,
      /**  To Segement Value 7.  */  
   "ToSegValue7":string,
      /**  To Segement Value 8.  */  
   "ToSegValue8":string,
      /**  To Segement Value 9.  */  
   "ToSegValue9":string,
      /**  To Segement Value 10.  */  
   "ToSegValue10":string,
      /**  To Segement Value 11.  */  
   "ToSegValue11":string,
      /**  To Segement Value 12.  */  
   "ToSegValue12":string,
      /**  To Segement Value 13.  */  
   "ToSegValue13":string,
      /**  To Segement Value 14.  */  
   "ToSegValue14":string,
      /**  To Segement Value 15.  */  
   "ToSegValue15":string,
      /**  To Segement Value 16.  */  
   "ToSegValue16":string,
      /**  To Segement Value 17.  */  
   "ToSegValue17":string,
      /**  To Segement Value 18.  */  
   "ToSegValue18":string,
      /**  To Segement Value 19.  */  
   "ToSegValue19":string,
      /**  To Segement Value 20.  */  
   "ToSegValue20":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "FromGLAccount":string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   "ToGLAcct":string,
      /**   Indicates if this record contains a specific account or only a single segment.  Values are:
S - single segment
A - full account  */  
   "RowAcctType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  From Segment Value entered by the user  */  
   "DspFromSegValue":string,
      /**  The To Segment value entered by the user.  */  
   "DspToSegValue":string,
   "BitFlag":number,
   "COASegmentSegmentName":string,
   "FrmGLAccountAccountDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlRptMasListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID that user assigns to uniquely identify a report definition.  */  
   "ReportID":string,
      /**  Description  */  
   "Description":string,
      /**  Title that will be used for the report.  */  
   "ReportTitle":string,
      /**  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  */  
   "PctCalcTlLine":number,
      /**  FontName that is used for the Report Heading.  */  
   "HeadingFont":string,
      /**  Font Size used for the Report Heading.  */  
   "HeadingFontSize":number,
      /**  Indicates if the Report Heading should be underlined.  */  
   "HeadingUnderline":boolean,
      /**  Indicates if the report heading lines should be Bold.  */  
   "HeadingBold":boolean,
      /**  Indicates if the report heading lines should be italic.  */  
   "HeadingItalic":boolean,
      /**  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  */  
   "ReportFont":string,
      /**  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  */  
   "ReportFontSize":number,
      /**  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  */  
   "ReportUnderline":boolean,
      /**  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  */  
   "ReportBold":boolean,
      /**  Default Italic attribute for the report.   This may be overridden by specifications on the column.  */  
   "ReportItalic":boolean,
      /**   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  */  
   "AmountFactor":number,
      /**  Default Book Identifier  */  
   "BookID":string,
      /**  Chart of Account Code  */  
   "COACode":string,
      /**   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  */  
   "BalanceLevel":string,
      /**   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  */  
   "BalanceFrequency":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the book id is enabled.  */  
   "EnableBookID":boolean,
      /**  Indicates if the COA Code is enabled.  */  
   "EnableCOACode":boolean,
      /**  The description or Name of this Chart of Accounts.  */  
   "COADescription":string,
      /**  Indicates the base currency for the book  */  
   "GLBookCurrencyCode":string,
      /**  Descripiton of Book  */  
   "GLBookDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlRptMasRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  ID that user assigns to uniquely identify a report definition.  */  
   "ReportID":string,
      /**  Description  */  
   "Description":string,
      /**  Title that will be used for the report.  */  
   "ReportTitle":string,
      /**  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  */  
   "PctCalcTlLine":number,
      /**  FontName that is used for the Report Heading.  */  
   "HeadingFont":string,
      /**  Font Size used for the Report Heading.  */  
   "HeadingFontSize":number,
      /**  Indicates if the Report Heading should be underlined.  */  
   "HeadingUnderline":boolean,
      /**  Indicates if the report heading lines should be Bold.  */  
   "HeadingBold":boolean,
      /**  Indicates if the report heading lines should be italic.  */  
   "HeadingItalic":boolean,
      /**  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  */  
   "ReportFont":string,
      /**  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  */  
   "ReportFontSize":number,
      /**  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  */  
   "ReportUnderline":boolean,
      /**  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  */  
   "ReportBold":boolean,
      /**  Default Italic attribute for the report.   This may be overridden by specifications on the column.  */  
   "ReportItalic":boolean,
      /**   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  */  
   "AmountFactor":number,
      /**  Default Book Identifier  */  
   "BookID":string,
      /**  Chart of Account Code  */  
   "COACode":string,
      /**   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  */  
   "BalanceLevel":string,
      /**   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  */  
   "BalanceFrequency":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the book id is enabled.  */  
   "EnableBookID":boolean,
      /**  Indicates if the COA Code is enabled.  */  
   "EnableCOACode":boolean,
   "BitFlag":number,
   "COADescription":string,
   "GLBookDescription":string,
   "GLBookCurrencyCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlRptRowRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Line number  */  
   "LineNum":number,
      /**   H = Heading Line - Defines a Heading that is printed.
A = Account Details - Prints GL accounts in specified range
S = Summary - a summary of accounts in specified range.
R = Ratio between two rows. 
T = Total - prints a total line for specified total field.  */  
   "LineType":string,
      /**  For LineType H, S and T this description is used to identify the line. For LineType A (acct detail) it is only a reference; the actual description from the GLAcct is used when printing details.  */  
   "Description":string,
      /**  Defines a field to which the values on this line are accumulated into.  */  
   "TotalTo":string,
      /**  Identifies the "TotalTo"  field that should be printed on this line. Pertains only to Total lines ( LineType = "T" ).  */  
   "PrintTotal":string,
      /**  Indicates if the "signs" of the amounts for this line are to be flipped before they are printed.  */  
   "Reverse":boolean,
      /**  New Page flag  */  
   "NewPage":boolean,
      /**  # of lines to skip before printing this line.  */  
   "SkipBefore":number,
      /**  # of lines to skip after printing this line.  */  
   "SkipAfter":number,
      /**  # of spaces that the line will be indented  */  
   "Indents":number,
      /**   Resets the total field defined by "PrintTotal" to zero after printing.
Pertains only to Total lines ( LineType = T ).  */  
   "ClearAfterPrint":boolean,
      /**  Override Font that is used for the Text portion of a row. Default is either GLRptCol.DataFont or GLRptMas.ReportFont.  */  
   "TextFont":string,
      /**  Override Text Font Size used for the Text portion of the row. Default is GLRptCol.DataFontSize or GLRptMas.ReportFontSize.  */  
   "TextFontSize":number,
      /**   Underline attribute for the text portion of the line. Default is either GLRptCol.DataUnderLine or GLRptMas.ReportUnderline.
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   "TextUnderline":string,
      /**   Bold attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold or GLRptMas.ReportBold  */  
   "TextBold":string,
      /**   Override Italic attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic or GLRptMas.ReporItalic.  */  
   "TextItalic":string,
      /**  Font that is used for ALL the data in this row.  Blank = use default. Default is either GLRptCol.DataFont/GLRptMas.ReportFont.  */  
   "DataFont":string,
      /**   Override FontSize used for ALL DATA in this line. 0 = Use default.
Default is GLRptCol.DataFontSize/GLRptMas.ReportFontSize.  */  
   "DataFontSize":number,
      /**   Underline attribute for ALL DATA in the line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataUnderLine/GLRptMas.ReportUnderline.  */  
   "DataUnderline":string,
      /**   Bold attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold/GLRptMas.ReportBold  */  
   "DataBold":string,
      /**   Italic attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic/GLRptMas.ReporItalic.  */  
   "DataItalic":string,
      /**  The GLRptRow.LineNum that defines the values that are to be used the numerator in the ratio calculation. This only pertains to LineType = "R".  */  
   "RatioLine1":number,
      /**  The GLRptRow.LineNum that defines the values that are to be used the denominator in the ratio calculation. This only pertains to LineType = "R".  */  
   "RatioLine2":number,
      /**  Report Category  */  
   "Category":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text. Only for LineType="T"  */  
   "ReportCategory":string,
      /**  ReverseReportCategory  */  
   "ReverseReportCategory":string,
   "CategoryOrAccounts":string,
   "COAActCatDescription":string,
   "IndentedDescription":string,
   "PercentCalc":boolean,
   "RptCOACode":string,
      /**  Indicates of adding a new specific account is allowed.  */  
   "AllowNewAcct":boolean,
   "BitFlag":number,
   "ReportIDDescription":string,
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
export interface CategoryOrAccountsList_output{
parameters : {
      /**  output parameters  */  
   CategoryOrAccountsList:string,
}
}

   /** Required : 
      @param ProposedColSetID
      @param ds
   */  
export interface ChangeGLRptColColSetID_input{
      /**  The proposed column set id  */  
   ProposedColSetID:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptColColSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ProposedColumnType
      @param ds
   */  
export interface ChangeGLRptColColumnType_input{
      /**  The proposed column type  */  
   ProposedColumnType:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptColColumnType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param proposedIntervalType
      @param ds
   */  
export interface ChangeGLRptColIntervalType_input{
      /**  The proposed interval type value  */  
   proposedIntervalType:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptColIntervalType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param proposedBookID
      @param ds
   */  
export interface ChangeGLRptMasBookID_input{
      /**  The proposed book id  */  
   proposedBookID:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptMasBookID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ProposedCategoryOrAccounts
      @param ds
   */  
export interface ChangeGLRptRowCategoryOrAccounts_input{
      /**  The proposed value  */  
   ProposedCategoryOrAccounts:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptRowCategoryOrAccounts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ProposedLineType
      @param ds
   */  
export interface ChangeGLRptRowLineType_input{
      /**  The proposed column type  */  
   ProposedLineType:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ChangeGLRptRowLineType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

export interface ColumnTypeList_output{
parameters : {
      /**  output parameters  */  
   ColumnTypeList:string,
}
}

   /** Required : 
      @param reportID
   */  
export interface DeleteByID_input{
   reportID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param DeleteFromReportID
      @param DeleteColSetID
      @param ds
   */  
export interface DeleteColSet_input{
      /**  The report id to delete from  */  
   DeleteFromReportID:string,
      /**  The column set to delete  */  
   DeleteColSetID:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface DeleteColSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param DuplicateFromReportID
      @param NewReportID
      @param NewReportDesc
      @param NewReportTitle
      @param ds
   */  
export interface DuplicateFinancialReport_input{
      /**  The report id to duplicate from  */  
   DuplicateFromReportID:string,
      /**  The new report id  */  
   NewReportID:string,
      /**  The new report description  */  
   NewReportDesc:string,
      /**  The new report title  */  
   NewReportTitle:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface DuplicateFinancialReport_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

export interface Erp_Tablesets_GLRptColRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Column Set Identifier used to establish different sets of columns for the same report specifications.  */  
   ColSetID:string,
      /**  Indicates the number (position/order) of the column.  */  
   ColumnNum:number,
      /**  This pertains to a  "Variance Column" only. Indicates if the variance is to be shown as a percentage or amount.  */  
   ShowAsPercent:boolean,
      /**  Used only for "Variance" columns.  Contains the "ColumnID" of the first column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  */  
   VarCol1:number,
      /**  Used only for "Variance" columns.  Contains the "ColumnID" of the second column to be used to calculate the variance.  Variance is calculated as VarCol1 - VarCol2.  */  
   VarCol2:number,
      /**  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the first column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  */  
   TotalCol1:number,
      /**  Used only for "Total" columns (ColumnType = "T").  Contains the "UniqueID" of the  last column to be used to calculate the Total.  Column Totals are the sum of all "Data" columns beginning with TotalCol1 through TotalCol2.  */  
   TotalCol2:number,
      /**  Column title line one.  */  
   ColumnTitle1:string,
      /**  Column title line two.  */  
   ColumnTitle2:string,
      /**  A = Actuals,  B = Budget,  C = Comparative %, N = Acct #,  T = Text,   V = Variance, X = Crossfoot Total , U = statistical Unit of Measure, Q = Statistical Quantity , R - Report Category , D = Report Category Description  */  
   ColumnType:string,
      /**  (Reporting year - YearOffset) = Fiscal Year of data in this column.  Ex: zero equal current year, 1 = prior year, etc...  */  
   YearOffset:number,
      /**  (Reporting Period - PeriodOffset) = Fiscal Period of data in this column.  Ex: zero = current period, 1 = prior period, etc...  */  
   PeriodOffset:number,
      /**   Number of fiscal period balances to be summarized into column.
Examples: Single Period = 01, Quarters = 3, Ytd = # of periods in fiscal year.  The system begins summarizing GL period balances starting at  "Given fiscal year - Year Offset", "Given fiscal period - period offset for the Number of periods indicated here.  If RollPeriods = No the summarization stops at period 1 of the "Given Fiscal Year - Year Offset", else it continues to the prior year.
NOTE: NumOfPeriods should not be > GLSyst.NumberofPeriods.  If it is logic will only summarize to the greater of the two.  */  
   NumOfPeriods:number,
      /**  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfPeriods indicated.  In most cases this would be NO.  To produce a rolling number of periods the answer would be Yes.  */  
   RollingPeriods:boolean,
      /**   Override FontName that is used for the Column Heading.
Default is GLRptMas.ReportFont  */  
   TitleFont:string,
      /**  Override Font Size used for the column title. Default is Report.FontSize.  */  
   TitleFontSize:number,
      /**   Override underline attribute for the column title.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   TitleUnderline:string,
      /**   Override Bold attribute for the column title.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   TitleBold:string,
      /**   Override Italic attribute for the column title.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   TitleItalic:string,
      /**  Override Font default that is used for the data in this column.  Default is GLRptMas.ReportFont  */  
   DataFont:string,
      /**  Override default Font Size used for data in this column. Default is GLRptMas.ReportFontSize.  */  
   DataFontSize:number,
      /**   Underline attribute for the data in this column.
Default is GLRptMas.ReportUnderline. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   DataUnderline:string,
      /**   Bold attribute for data in this column.
Default is GLRptMas.ReportBold
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   DataBold:string,
      /**   Italic attribute for data in this column.
Default is GLRptMas.ReporItalic. 
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   DataItalic:string,
      /**  Daily Average Balance option  */  
   DailyAveBalance:boolean,
      /**  Number of day balances to be summarized into column.  */  
   NumOfDays:number,
      /**  Days offset  */  
   DaysOffset:number,
      /**   Indicates if balances will be calculated by days or by periods.  Values are:
P - By Period
D - By Day  */  
   IntervalType:string,
      /**  Indicates if the system should span fiscal year when summarizing the GL balances for the NumOfDays indicated.  In most cases this would be NO.  To produce a rolling number of days the answer would be Yes.  */  
   RollingDays:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OverrideBudgetCode  */  
   OverrideBudgetCode:boolean,
      /**  BudgetCodeID  */  
   BudgetCodeID:string,
   ColSetSeq:number,
   BitFlag:number,
   ReportIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRptColSetRow{
   Company:string,
   ReportID:string,
   ColSetID:string,
   ColumnTitle01:string,
   ColumnTitle02:string,
   ColumnTitle03:string,
   ColumnTitle04:string,
   ColumnTitle05:string,
   ColumnTitle06:string,
   ColumnTitle07:string,
   ColumnTitle08:string,
   ColumnTitle09:string,
   ColumnTitle10:string,
   ColumnTitle11:string,
   ColumnTitle12:string,
   ColumnTitle13:string,
   ColumnTitle14:string,
   ColumnTitle15:string,
   ColumnTitle16:string,
   ColumnTitle17:string,
   ColumnTitle18:string,
   ColumnTitle19:string,
   ColumnTitle20:string,
   ColSetSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRptRowAcctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Line number  */  
   LineNum:number,
      /**  Sequence number.   This along with ReportID and LineNum uniquely identifies the record.  */  
   SeqNum:number,
      /**  Chart of Account ID  */  
   COACode:string,
      /**  The segment number.  Blank if using a full account.  */  
   SegmentNbr:number,
      /**  From Segement Value 1.  */  
   FromSegValue1:string,
      /**  From Segement Value 2.  */  
   FromSegValue2:string,
      /**  From Segement Value 3.  */  
   FromSegValue3:string,
      /**  From Segement Value 4.  */  
   FromSegValue4:string,
      /**  From Segement Value 5.  */  
   FromSegValue5:string,
      /**  From Segement Value 6.  */  
   FromSegValue6:string,
      /**  From Segement Value 7.  */  
   FromSegValue7:string,
      /**  From Segement Value 8.  */  
   FromSegValue8:string,
      /**  From Segement Value 9.  */  
   FromSegValue9:string,
      /**  From Segement Value 10.  */  
   FromSegValue10:string,
      /**  From Segement Value 11.  */  
   FromSegValue11:string,
      /**  From Segement Value 12.  */  
   FromSegValue12:string,
      /**  From Segement Value 13.  */  
   FromSegValue13:string,
      /**  From Segement Value 14.  */  
   FromSegValue14:string,
      /**  From Segement Value 15.  */  
   FromSegValue15:string,
      /**  From Segement Value 16.  */  
   FromSegValue16:string,
      /**  From Segement Value 17.  */  
   FromSegValue17:string,
      /**  From Segement Value 18.  */  
   FromSegValue18:string,
      /**  From Segement Value 19.  */  
   FromSegValue19:string,
      /**  From Segement Value 20.  */  
   FromSegValue20:string,
      /**  To Segement Value 1.  */  
   ToSegValue1:string,
      /**  To Segement Value 2.  */  
   ToSegValue2:string,
      /**  To Segement Value 3.  */  
   ToSegValue3:string,
      /**  To Segement Value 4.  */  
   ToSegValue4:string,
      /**  To Segement Value 5.  */  
   ToSegValue5:string,
      /**  To Segement Value 6.  */  
   ToSegValue6:string,
      /**  To Segement Value 7.  */  
   ToSegValue7:string,
      /**  To Segement Value 8.  */  
   ToSegValue8:string,
      /**  To Segement Value 9.  */  
   ToSegValue9:string,
      /**  To Segement Value 10.  */  
   ToSegValue10:string,
      /**  To Segement Value 11.  */  
   ToSegValue11:string,
      /**  To Segement Value 12.  */  
   ToSegValue12:string,
      /**  To Segement Value 13.  */  
   ToSegValue13:string,
      /**  To Segement Value 14.  */  
   ToSegValue14:string,
      /**  To Segement Value 15.  */  
   ToSegValue15:string,
      /**  To Segement Value 16.  */  
   ToSegValue16:string,
      /**  To Segement Value 17.  */  
   ToSegValue17:string,
      /**  To Segement Value 18.  */  
   ToSegValue18:string,
      /**  To Segement Value 19.  */  
   ToSegValue19:string,
      /**  To Segement Value 20.  */  
   ToSegValue20:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   FromGLAccount:string,
      /**  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  */  
   ToGLAcct:string,
      /**   Indicates if this record contains a specific account or only a single segment.  Values are:
S - single segment
A - full account  */  
   RowAcctType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  From Segment Value entered by the user  */  
   DspFromSegValue:string,
      /**  The To Segment value entered by the user.  */  
   DspToSegValue:string,
   BitFlag:number,
   COASegmentSegmentName:string,
   FrmGLAccountAccountDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRptSyntaxErrorsRow{
   Company:string,
   ReportID:string,
   DisplayAccount:string,
   SeqNum:number,
   ErrorType:number,
   ErrorDescription:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLRptSyntaxErrorsTableset{
   GLRptSyntaxErrors:Erp_Tablesets_GLRptSyntaxErrorsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlRptMasListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID that user assigns to uniquely identify a report definition.  */  
   ReportID:string,
      /**  Description  */  
   Description:string,
      /**  Title that will be used for the report.  */  
   ReportTitle:string,
      /**  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  */  
   PctCalcTlLine:number,
      /**  FontName that is used for the Report Heading.  */  
   HeadingFont:string,
      /**  Font Size used for the Report Heading.  */  
   HeadingFontSize:number,
      /**  Indicates if the Report Heading should be underlined.  */  
   HeadingUnderline:boolean,
      /**  Indicates if the report heading lines should be Bold.  */  
   HeadingBold:boolean,
      /**  Indicates if the report heading lines should be italic.  */  
   HeadingItalic:boolean,
      /**  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  */  
   ReportFont:string,
      /**  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  */  
   ReportFontSize:number,
      /**  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  */  
   ReportUnderline:boolean,
      /**  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  */  
   ReportBold:boolean,
      /**  Default Italic attribute for the report.   This may be overridden by specifications on the column.  */  
   ReportItalic:boolean,
      /**   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  */  
   AmountFactor:number,
      /**  Default Book Identifier  */  
   BookID:string,
      /**  Chart of Account Code  */  
   COACode:string,
      /**   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  */  
   BalanceLevel:string,
      /**   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  */  
   BalanceFrequency:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the book id is enabled.  */  
   EnableBookID:boolean,
      /**  Indicates if the COA Code is enabled.  */  
   EnableCOACode:boolean,
      /**  The description or Name of this Chart of Accounts.  */  
   COADescription:string,
      /**  Indicates the base currency for the book  */  
   GLBookCurrencyCode:string,
      /**  Descripiton of Book  */  
   GLBookDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlRptMasListTableset{
   GlRptMasList:Erp_Tablesets_GlRptMasListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlRptMasRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  ID that user assigns to uniquely identify a report definition.  */  
   ReportID:string,
      /**  Description  */  
   Description:string,
      /**  Title that will be used for the report.  */  
   ReportTitle:string,
      /**  LineNum of the GLRptRow record which is to provide the denominator values in the Percent Of calculations.  */  
   PctCalcTlLine:number,
      /**  FontName that is used for the Report Heading.  */  
   HeadingFont:string,
      /**  Font Size used for the Report Heading.  */  
   HeadingFontSize:number,
      /**  Indicates if the Report Heading should be underlined.  */  
   HeadingUnderline:boolean,
      /**  Indicates if the report heading lines should be Bold.  */  
   HeadingBold:boolean,
      /**  Indicates if the report heading lines should be italic.  */  
   HeadingItalic:boolean,
      /**  Default Font that is used for the Report. This may be overridden by specifications on the columns/Rows.TextFont  */  
   ReportFont:string,
      /**  Default font size used for the report.  This may be overridden by specifications on the columns/rows.  */  
   ReportFontSize:number,
      /**  Default underline attribute for the report.   This may be overridden by specifications on the columns/rows.  */  
   ReportUnderline:boolean,
      /**  Default Bold attribute for the report.  This may be overridden by specifications on the columns/rows.  */  
   ReportBold:boolean,
      /**  Default Italic attribute for the report.   This may be overridden by specifications on the column.  */  
   ReportItalic:boolean,
      /**   The base 10 exponential factor for reported amounts and budgets.
Value 2 means 10 exp 3 = 1.000 resulting in the division of all amounts and budgets by 1.000.  */  
   AmountFactor:number,
      /**  Default Book Identifier  */  
   BookID:string,
      /**  Chart of Account Code  */  
   COACode:string,
      /**   The balance level for the report.  Values are:
D - Detail Account
S- Summary Account
N - Natural Account  */  
   BalanceLevel:string,
      /**   Balance Frequence.  Values are:
P - Period balances
D - Daily balances  */  
   BalanceFrequency:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the book id is enabled.  */  
   EnableBookID:boolean,
      /**  Indicates if the COA Code is enabled.  */  
   EnableCOACode:boolean,
   BitFlag:number,
   COADescription:string,
   GLBookDescription:string,
   GLBookCurrencyCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlRptMasTableset{
   GlRptMas:Erp_Tablesets_GlRptMasRow[],
   GLRptColSet:Erp_Tablesets_GLRptColSetRow[],
   GLRptCol:Erp_Tablesets_GLRptColRow[],
   GlRptRow:Erp_Tablesets_GlRptRowRow[],
   GLRptRowAcct:Erp_Tablesets_GLRptRowAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlRptRowRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Line number  */  
   LineNum:number,
      /**   H = Heading Line - Defines a Heading that is printed.
A = Account Details - Prints GL accounts in specified range
S = Summary - a summary of accounts in specified range.
R = Ratio between two rows. 
T = Total - prints a total line for specified total field.  */  
   LineType:string,
      /**  For LineType H, S and T this description is used to identify the line. For LineType A (acct detail) it is only a reference; the actual description from the GLAcct is used when printing details.  */  
   Description:string,
      /**  Defines a field to which the values on this line are accumulated into.  */  
   TotalTo:string,
      /**  Identifies the "TotalTo"  field that should be printed on this line. Pertains only to Total lines ( LineType = "T" ).  */  
   PrintTotal:string,
      /**  Indicates if the "signs" of the amounts for this line are to be flipped before they are printed.  */  
   Reverse:boolean,
      /**  New Page flag  */  
   NewPage:boolean,
      /**  # of lines to skip before printing this line.  */  
   SkipBefore:number,
      /**  # of lines to skip after printing this line.  */  
   SkipAfter:number,
      /**  # of spaces that the line will be indented  */  
   Indents:number,
      /**   Resets the total field defined by "PrintTotal" to zero after printing.
Pertains only to Total lines ( LineType = T ).  */  
   ClearAfterPrint:boolean,
      /**  Override Font that is used for the Text portion of a row. Default is either GLRptCol.DataFont or GLRptMas.ReportFont.  */  
   TextFont:string,
      /**  Override Text Font Size used for the Text portion of the row. Default is GLRptCol.DataFontSize or GLRptMas.ReportFontSize.  */  
   TextFontSize:number,
      /**   Underline attribute for the text portion of the line. Default is either GLRptCol.DataUnderLine or GLRptMas.ReportUnderline.
Values: Y = Underline, N = No Underline, "D" = Use default.  */  
   TextUnderline:string,
      /**   Bold attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold or GLRptMas.ReportBold  */  
   TextBold:string,
      /**   Override Italic attribute for the text portion of this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic or GLRptMas.ReporItalic.  */  
   TextItalic:string,
      /**  Font that is used for ALL the data in this row.  Blank = use default. Default is either GLRptCol.DataFont/GLRptMas.ReportFont.  */  
   DataFont:string,
      /**   Override FontSize used for ALL DATA in this line. 0 = Use default.
Default is GLRptCol.DataFontSize/GLRptMas.ReportFontSize.  */  
   DataFontSize:number,
      /**   Underline attribute for ALL DATA in the line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataUnderLine/GLRptMas.ReportUnderline.  */  
   DataUnderline:string,
      /**   Bold attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataBold/GLRptMas.ReportBold  */  
   DataBold:string,
      /**   Italic attribute for ALL DATA on this line.
Values: Y = Underline, N = No Underline, "D" = Use default.
Default is GLRptCol.DataItalic/GLRptMas.ReporItalic.  */  
   DataItalic:string,
      /**  The GLRptRow.LineNum that defines the values that are to be used the numerator in the ratio calculation. This only pertains to LineType = "R".  */  
   RatioLine1:number,
      /**  The GLRptRow.LineNum that defines the values that are to be used the denominator in the ratio calculation. This only pertains to LineType = "R".  */  
   RatioLine2:number,
      /**  Report Category  */  
   Category:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  One of the UD codes having a CodeTypeID equal to GLRepCat. Or, if GLRepCat does not exist, then it may be free text. Only for LineType="T"  */  
   ReportCategory:string,
      /**  ReverseReportCategory  */  
   ReverseReportCategory:string,
   CategoryOrAccounts:string,
   COAActCatDescription:string,
   IndentedDescription:string,
   PercentCalc:boolean,
   RptCOACode:string,
      /**  Indicates of adding a new specific account is allowed.  */  
   AllowNewAcct:boolean,
   BitFlag:number,
   ReportIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtGlRptMasTableset{
   GlRptMas:Erp_Tablesets_GlRptMasRow[],
   GLRptColSet:Erp_Tablesets_GLRptColSetRow[],
   GLRptCol:Erp_Tablesets_GLRptColRow[],
   GlRptRow:Erp_Tablesets_GlRptRowRow[],
   GLRptRowAcct:Erp_Tablesets_GLRptRowAcctRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param reportID
      @param sFileName
   */  
export interface ExportReportDefinition2_input{
      /**  ID of the Report Definition to be exported.  */  
   reportID:string,
      /**  Desired output file name, optional, no extension required.  */  
   sFileName:string,
}

export interface ExportReportDefinition2_output{
      /**  Exported file subpath of SpecialFolder.UserData.  */  
   returnObj:string,
}

   /** Required : 
      @param reportID
   */  
export interface ExportReportDefinition_input{
      /**  ID of the Report Definition to be exported  */  
   reportID:string,
}

export interface ExportReportDefinition_output{
      /**  Exported XML Data  */  
   returnObj:string,
}

   /** Required : 
      @param reportID
   */  
export interface GetByID_input{
   reportID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlRptMasTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlRptMasTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlRptMasTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  Table Name  */  
   tableName:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
      /**  List of code destioptions  */  
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
   returnObj:Erp_Tablesets_GlRptMasListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param colSetID
      @param columnNum
   */  
export interface GetNewGLRptCol_input{
   ds:Erp_Tablesets_GlRptMasTableset[],
   reportID:string,
   colSetID:string,
   columnNum:number,
}

export interface GetNewGLRptCol_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param reportID
      @param lineNum
      @param rowAcctType
      @param ds
   */  
export interface GetNewGLRptRowAcctForType_input{
      /**  Report ID  */  
   reportID:string,
      /**  Line number  */  
   lineNum:number,
      /**  Row account type. Valid types are
            S - Single segment.
            A - Account.  */  
   rowAcctType:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface GetNewGLRptRowAcctForType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param lineNum
   */  
export interface GetNewGLRptRowAcct_input{
   ds:Erp_Tablesets_GlRptMasTableset[],
   reportID:string,
   lineNum:number,
}

export interface GetNewGLRptRowAcct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGlRptMas_input{
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface GetNewGlRptMas_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
   */  
export interface GetNewGlRptRow_input{
   ds:Erp_Tablesets_GlRptMasTableset[],
   reportID:string,
}

export interface GetNewGlRptRow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param whereClauseGlRptMas
      @param whereClauseGLRptColSet
      @param whereClauseGLRptCol
      @param whereClauseGlRptRow
      @param whereClauseGLRptRowAcct
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlRptMas:string,
   whereClauseGLRptColSet:string,
   whereClauseGLRptCol:string,
   whereClauseGlRptRow:string,
   whereClauseGLRptRowAcct:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlRptMasTableset[],
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
      @param sFileSubPath
      @param newReportID
      @param overwriteExisting
   */  
export interface ImportReportDefinition2_input{
      /**  Imported file subpath of SpecialFolder.UserData.  */  
   sFileSubPath:string,
      /**  New report ID.  */  
   newReportID:string,
      /**  Overwrite existing configurations.  */  
   overwriteExisting:boolean,
}

export interface ImportReportDefinition2_output{
}

   /** Required : 
      @param definitionData
      @param newReportID
      @param overwriteExisting
   */  
export interface ImportReportDefinition_input{
      /**  XML Data to be imported  */  
   definitionData:string,
      /**  New ReportID  */  
   newReportID:string,
      /**  Overwrite existing configurations  */  
   overwriteExisting:boolean,
}

export interface ImportReportDefinition_output{
}

export interface LineTypeList_output{
parameters : {
      /**  output parameters  */  
   LineTypeList:string,
}
}

   /** Required : 
      @param ColReportID
      @param ColColSetID
      @param ColColumnNum
      @param ColColSetSeq
      @param ds
   */  
export interface MoveGLRptColDown_input{
      /**  The report id of the column to move down  */  
   ColReportID:string,
      /**  The column set id of the column to move down  */  
   ColColSetID:string,
      /**  The column number of the column to move down  */  
   ColColumnNum:number,
      /**  The column sequence number of the column to move down  */  
   ColColSetSeq:number,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface MoveGLRptColDown_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ColReportID
      @param ColColSetID
      @param ColColumnNum
      @param ColColSetSeq
      @param ds
   */  
export interface MoveGLRptColUp_input{
      /**  The report id of the column to move up  */  
   ColReportID:string,
      /**  The column set id of the column to move up  */  
   ColColSetID:string,
      /**  The column number of the column to move up  */  
   ColColumnNum:number,
      /**  The column sequence number of the column to move up  */  
   ColColSetSeq:number,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface MoveGLRptColUp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

export interface ReportWizardOptionsList_output{
parameters : {
      /**  output parameters  */  
   ReportWizardOptionsList:string,
}
}

   /** Required : 
      @param ReportID
      @param ReportType
      @param ds
   */  
export interface ReportWizard_input{
      /**  The report id to create the template for  */  
   ReportID:string,
      /**  The type of report to create.
            Valid values are: B (Balance Sheet) or I (Income Statement)  */  
   ReportType:string,
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface ReportWizard_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param CheckReportID
      @param SyntaxCheckType
   */  
export interface SyntaxCheckForWeb_input{
      /**  The report id to check the syntax of  */  
   CheckReportID:string,
      /**  The type of syntax check to perform.  Values are:
            I (Income Statment), B (Balance Sheet), or O (Other)  */  
   SyntaxCheckType:string,
}

export interface SyntaxCheckForWeb_output{
   returnObj:Erp_Tablesets_GLRptSyntaxErrorsTableset[],
}

export interface SyntaxCheckOptionsList_output{
parameters : {
      /**  output parameters  */  
   SyntaxCheckOptionsList:string,
}
}

   /** Required : 
      @param CheckReportID
      @param SyntaxCheckType
   */  
export interface SyntaxCheck_input{
      /**  The report id to check the syntax of  */  
   CheckReportID:string,
      /**  The type of syntax check to perform.  Values are:
            I (Income Statment), B (Balance Sheet), or O (Other)  */  
   SyntaxCheckType:string,
}

export interface SyntaxCheck_output{
   returnObj:Erp_Tablesets_GLRptSyntaxErrorsTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGlRptMasTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlRptMasTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlRptMasTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlRptMasTableset,
}
}

   /** Required : 
      @param ReportID
      @param LineNum
      @param CategoryOrAccounts
   */  
export interface ValidateGLRptRow_input{
      /**  The ReportID of the row  */  
   ReportID:string,
      /**  The LineNum of the row  */  
   LineNum:number,
      /**  The CategoryOrAccounts option of the row  */  
   CategoryOrAccounts:string,
}

export interface ValidateGLRptRow_output{
}

   /** Required : 
      @param sFileSubPath
   */  
export interface ValidateImportedReportDefinition_input{
      /**  Imported file subpath of SpecialFolder.UserData.  */  
   sFileSubPath:string,
}

export interface ValidateImportedReportDefinition_output{
      /**  Report ID of the imported report definition.  */  
   returnObj:string,
}

export interface YesNoDefaultList_output{
parameters : {
      /**  output parameters  */  
   YesNoDefaultList:string,
}
}

