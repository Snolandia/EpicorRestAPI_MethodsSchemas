import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.GlbCurrRateGrpSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/$metadata", {
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
   Description: Get GlbCurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrRateGrps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateGrpRow
   */  
export function get_GlbCurrRateGrps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrRateGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrRateGrps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps", {
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
   Summary: Calls GetByID to retrieve the GlbCurrRateGrp item
   Description: Calls GetByID to retrieve the GlbCurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   */  
export function get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCurrRateGrp for the service
   Description: Calls UpdateExt to update GlbCurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")", {
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
   Summary: Call UpdateExt to delete GlbCurrRateGrp item
   Description: Call UpdateExt to delete GlbCurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")", {
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
   Description: Get GlbCurrConvRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrConvRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrConvRuleRow
   */  
export function get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrConvRules(Company:string, GlbCompany:string, GlbRateGrpCode:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrConvRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GlbCurrConvRule item
   Description: Calls GetByID to retrieve the GlbCurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrConvRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   */  
export function get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GlbCurrRateDisps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrRateDisps1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateDispRow
   */  
export function get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrRateDisps(Company:string, GlbCompany:string, GlbRateGrpCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrRateDisps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GlbCurrRateDisp item
   Description: Calls GetByID to retrieve the GlbCurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateDisp1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSeq Desc: GlbSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   */  
export function get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrConvRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrConvRules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrConvRuleRow
   */  
export function get_GlbCurrConvRules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrConvRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrConvRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules", {
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
   Summary: Calls GetByID to retrieve the GlbCurrConvRule item
   Description: Calls GetByID to retrieve the GlbCurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   */  
export function get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrConvRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrConvRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCurrConvRule for the service
   Description: Calls UpdateExt to update GlbCurrConvRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")", {
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
   Summary: Call UpdateExt to delete GlbCurrConvRule item
   Description: Call UpdateExt to delete GlbCurrConvRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrConvRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")", {
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
   Description: Get GlbCurrExRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrExRates1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrExRateRow
   */  
export function get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbCurrExRates(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")/GlbCurrExRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GlbCurrExRate item
   Description: Calls GetByID to retrieve the GlbCurrExRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrExRate1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param GlbEffectiveDate Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   */  
export function get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, GlbEffectiveDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrExRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrExRates
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrExRateRow
   */  
export function get_GlbCurrExRates(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrExRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrExRates(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates", {
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
   Summary: Calls GetByID to retrieve the GlbCurrExRate item
   Description: Calls GetByID to retrieve the GlbCurrExRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrExRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param GlbEffectiveDate Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   */  
export function get_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, GlbEffectiveDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCurrExRate for the service
   Description: Calls UpdateExt to update GlbCurrExRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrExRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param GlbEffectiveDate Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, GlbEffectiveDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")", {
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
   Summary: Call UpdateExt to delete GlbCurrExRate item
   Description: Call UpdateExt to delete GlbCurrExRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrExRate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSourceCurrCode Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      @param GlbTargetCurrCode Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      @param GlbEffectiveDate Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSourceCurrCode:string, GlbTargetCurrCode:string, GlbEffectiveDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")", {
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
   Description: Get GlbCurrRateDisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrRateDisps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateDispRow
   */  
export function get_GlbCurrRateDisps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrRateDisps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCurrRateDisps(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps", {
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
   Summary: Calls GetByID to retrieve the GlbCurrRateDisp item
   Description: Calls GetByID to retrieve the GlbCurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSeq Desc: GlbSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   */  
export function get_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCurrRateDispRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCurrRateDispRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCurrRateDisp for the service
   Description: Calls UpdateExt to update GlbCurrRateDisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSeq Desc: GlbSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")", {
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
   Summary: Call UpdateExt to delete GlbCurrRateDisp item
   Description: Call UpdateExt to delete GlbCurrRateDisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrRateDisp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GlbCompany Desc: GlbCompany   Required: True   Allow empty value : True
      @param GlbRateGrpCode Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      @param GlbSeq Desc: GlbSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company:string, GlbCompany:string, GlbRateGrpCode:string, GlbSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseGlbCurrRateGrp:string, whereClauseGlbCurrConvRule:string, whereClauseGlbCurrExRate:string, whereClauseGlbCurrRateDisp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbCurrRateGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCurrRateGrp=" + whereClauseGlbCurrRateGrp
   }
   if(typeof whereClauseGlbCurrConvRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCurrConvRule=" + whereClauseGlbCurrConvRule
   }
   if(typeof whereClauseGlbCurrExRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCurrExRate=" + whereClauseGlbCurrExRate
   }
   if(typeof whereClauseGlbCurrRateDisp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCurrRateDisp=" + whereClauseGlbCurrRateDisp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetRows" + params, {
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
export function get_GetByID(glbCompany:string, glbRateGrpCode:string, epicorHeaders?:Headers){
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
   if(typeof glbRateGrpCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "glbRateGrpCode=" + glbRateGrpCode
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetList" + params, {
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
   Summary: Invoke method GetNewGlbCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCurrRateGrp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetNewGlbCurrRateGrp", {
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
   Summary: Invoke method GetNewGlbCurrConvRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrConvRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCurrConvRule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetNewGlbCurrConvRule", {
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
   Summary: Invoke method GetNewGlbCurrExRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCurrExRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetNewGlbCurrExRate", {
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
   Summary: Invoke method GetNewGlbCurrRateDisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrRateDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrRateDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrRateDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCurrRateDisp(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetNewGlbCurrRateDisp", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrConvRuleRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrExRateRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrRateDispRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrRateGrpListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCurrRateGrpRow[],
}

export interface Erp_Tablesets_GlbCurrConvRuleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the source currency.  */  
   "SourceCurrCode":string,
      /**  A unique code that identifies the target currency.  */  
   "TargetCurrCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Determine if the user should use the base rate group defined in CurrRateGrp  */  
   "UseBaseRate":boolean,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   "RuleCode":number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   "FixedRate":boolean,
      /**  Currency Rate Group Code from Source Company  */  
   "GlbRateGrpCode":string,
      /**  Source Currency from Source Company  */  
   "GlbSourceCurrCode":string,
      /**  Target Currency from Source Company  */  
   "GlbTargetCurrCode":string,
      /**  Source Company  */  
   "GlbCompany":string,
   "DisplayMode":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCurrExRateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the source currency.  */  
   "SourceCurrCode":string,
      /**  This rate is effective as of this date.  */  
   "EffectiveDate":string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "CurrentRate":number,
      /**  System date at time that record was modified.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   "SysTime":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "Reference":string,
      /**  A unique code that identifies the target currency.  */  
   "TargetCurrCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Currency Rate Group Code from Source Company  */  
   "GlbRateGrpCode":string,
      /**  Source Currency from Source Company  */  
   "GlbSourceCurrCode":string,
      /**  Target Currency from Source Company  */  
   "GlbTargetCurrCode":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Effective Date from Source Company  */  
   "GlbEffectiveDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCurrRateDispRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Order in which the currencies should be displayed in the matrix grids  */  
   "Seq":number,
      /**  Currency code to be displayed  */  
   "CurrencyCode":string,
      /**  Currency Rate Group Code from source company  */  
   "GlbRateGrpCode":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Sequence from Source Company  */  
   "GlbSeq":number,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCurrRateGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Currency Rate Group Code from source company  */  
   "GlbRateGrpCode":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   "Skipped":boolean,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Description  */  
   "Description":string,
      /**  Determines if the record is inactive  */  
   "Inactive":boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   "BaseRateGrpCode":string,
      /**  Currency to use during single or double currency conversions  */  
   "CrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "CrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "CrossRoundDec":number,
      /**  Currency used for double currency conversions  */  
   "AltCrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "AltCrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "AltCrossRoundDec":number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   "GlobalGrp":boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   "DisplayMode":number,
   "RateNumDec":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CurrRateGrp.RateGrpCode to link to (new or existing)  */  
   "LinkRateGrpCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCurrRateGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Currency Rate Group Code from source company  */  
   "GlbRateGrpCode":string,
      /**  Source Company  */  
   "GlbCompany":string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   "Skipped":boolean,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Description  */  
   "Description":string,
      /**  Determines if the record is inactive  */  
   "Inactive":boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   "BaseRateGrpCode":string,
      /**  Currency to use during single or double currency conversions  */  
   "CrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "CrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "CrossRoundDec":number,
      /**  Currency used for double currency conversions  */  
   "AltCrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "AltCrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "AltCrossRoundDec":number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   "GlobalGrp":boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   "DisplayMode":number,
   "RateNumDec":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CurrRateGrp.RateGrpCode to link to (new or existing)  */  
   "LinkRateGrpCode":string,
      /**  holds description of currency rate group from local rate group linked.  */  
   "LocalDesc":string,
   "Select":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param glbCompany
      @param glbRateGrpCode
   */  
export interface DeleteByID_input{
   glbCompany:string,
   glbRateGrpCode:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbCurrConvRuleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Determine if the user should use the base rate group defined in CurrRateGrp  */  
   UseBaseRate:boolean,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   RuleCode:number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   FixedRate:boolean,
      /**  Currency Rate Group Code from Source Company  */  
   GlbRateGrpCode:string,
      /**  Source Currency from Source Company  */  
   GlbSourceCurrCode:string,
      /**  Target Currency from Source Company  */  
   GlbTargetCurrCode:string,
      /**  Source Company  */  
   GlbCompany:string,
   DisplayMode:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrExRateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  This rate is effective as of this date.  */  
   EffectiveDate:string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   CurrentRate:number,
      /**  System date at time that record was modified.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   SysTime:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   Reference:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Currency Rate Group Code from Source Company  */  
   GlbRateGrpCode:string,
      /**  Source Currency from Source Company  */  
   GlbSourceCurrCode:string,
      /**  Target Currency from Source Company  */  
   GlbTargetCurrCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Effective Date from Source Company  */  
   GlbEffectiveDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateDispRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Order in which the currencies should be displayed in the matrix grids  */  
   Seq:number,
      /**  Currency code to be displayed  */  
   CurrencyCode:string,
      /**  Currency Rate Group Code from source company  */  
   GlbRateGrpCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Sequence from Source Company  */  
   GlbSeq:number,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Currency Rate Group Code from source company  */  
   GlbRateGrpCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   DisplayMode:number,
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CurrRateGrp.RateGrpCode to link to (new or existing)  */  
   LinkRateGrpCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateGrpListTableset{
   GlbCurrRateGrpList:Erp_Tablesets_GlbCurrRateGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCurrRateGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Currency Rate Group Code from source company  */  
   GlbRateGrpCode:string,
      /**  Source Company  */  
   GlbCompany:string,
      /**  Indicates that the user has reviewed the record but its not going to be linked currently  */  
   Skipped:boolean,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   DisplayMode:number,
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CurrRateGrp.RateGrpCode to link to (new or existing)  */  
   LinkRateGrpCode:string,
      /**  holds description of currency rate group from local rate group linked.  */  
   LocalDesc:string,
   Select:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbCurrRateGrpTableset{
   GlbCurrRateGrp:Erp_Tablesets_GlbCurrRateGrpRow[],
   GlbCurrConvRule:Erp_Tablesets_GlbCurrConvRuleRow[],
   GlbCurrExRate:Erp_Tablesets_GlbCurrExRateRow[],
   GlbCurrRateDisp:Erp_Tablesets_GlbCurrRateDispRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbCurrRateGrpTableset{
   GlbCurrRateGrp:Erp_Tablesets_GlbCurrRateGrpRow[],
   GlbCurrConvRule:Erp_Tablesets_GlbCurrConvRuleRow[],
   GlbCurrExRate:Erp_Tablesets_GlbCurrExRateRow[],
   GlbCurrRateDisp:Erp_Tablesets_GlbCurrRateDispRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param glbCompany
      @param glbRateGrpCode
   */  
export interface GetByID_input{
   glbCompany:string,
   glbRateGrpCode:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
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
   returnObj:Erp_Tablesets_GlbCurrRateGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param glbCompany
      @param glbRateGrpCode
      @param glbSourceCurrCode
   */  
export interface GetNewGlbCurrConvRule_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
   glbCompany:string,
   glbRateGrpCode:string,
   glbSourceCurrCode:string,
}

export interface GetNewGlbCurrConvRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}
}

   /** Required : 
      @param ds
      @param glbCompany
      @param glbRateGrpCode
      @param glbSourceCurrCode
      @param glbTargetCurrCode
   */  
export interface GetNewGlbCurrExRate_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
   glbCompany:string,
   glbRateGrpCode:string,
   glbSourceCurrCode:string,
   glbTargetCurrCode:string,
}

export interface GetNewGlbCurrExRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}
}

   /** Required : 
      @param ds
      @param glbCompany
      @param glbRateGrpCode
   */  
export interface GetNewGlbCurrRateDisp_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
   glbCompany:string,
   glbRateGrpCode:string,
}

export interface GetNewGlbCurrRateDisp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}
}

   /** Required : 
      @param ds
      @param glbCompany
   */  
export interface GetNewGlbCurrRateGrp_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
   glbCompany:string,
}

export interface GetNewGlbCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}
}

   /** Required : 
      @param whereClauseGlbCurrRateGrp
      @param whereClauseGlbCurrConvRule
      @param whereClauseGlbCurrExRate
      @param whereClauseGlbCurrRateDisp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbCurrRateGrp:string,
   whereClauseGlbCurrConvRule:string,
   whereClauseGlbCurrExRate:string,
   whereClauseGlbCurrRateDisp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbCurrRateGrpTableset[],
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
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGlbCurrRateGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbCurrRateGrpTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbCurrRateGrpTableset[],
}
}

