import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.ConfigurationDesignSvc
// Description: Configuration Design Service
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/$metadata", {
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
   Description: Get ConfigurationDesigns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfigurationDesigns
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusRow
   */  
export function get_ConfigurationDesigns(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfigurationDesigns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConfigurationDesigns(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns", {
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
   Summary: Calls GetByID to retrieve the ConfigurationDesign item
   Description: Calls GetByID to retrieve the ConfigurationDesign item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfigurationDesign
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   */  
export function get_ConfigurationDesigns_Company_ConfigID(Company:string, ConfigID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStatusRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStatusRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ConfigurationDesign for the service
   Description: Calls UpdateExt to update ConfigurationDesign. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfigurationDesign
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ConfigurationDesigns_Company_ConfigID(Company:string, ConfigID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")", {
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
   Summary: Call UpdateExt to delete ConfigurationDesign item
   Description: Call UpdateExt to delete ConfigurationDesign item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfigurationDesign
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ConfigurationDesigns_Company_ConfigID(Company:string, ConfigID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")", {
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
   Description: Get PcPages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcPages1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageRow
   */  
export function get_ConfigurationDesigns_Company_ConfigID_PcPages(Company:string, ConfigID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcPages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcPage item
   Description: Calls GetByID to retrieve the PcPage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPage1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageRow
   */  
export function get_ConfigurationDesigns_Company_ConfigID_PcPages_Company_ConfigID_PageSeq(Company:string, ConfigID:string, PageSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcPageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcPageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcStatusExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcStatusExprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusExprRow
   */  
export function get_ConfigurationDesigns_Company_ConfigID_PcStatusExprs(Company:string, ConfigID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcStatusExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcStatusExpr item
   Description: Calls GetByID to retrieve the PcStatusExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusExpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   */  
export function get_ConfigurationDesigns_Company_ConfigID_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company:string, ConfigID:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStatusExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStatusExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcPages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcPages
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageRow
   */  
export function get_PcPages(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcPages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcPageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcPageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcPages(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages", {
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
   Summary: Calls GetByID to retrieve the PcPage item
   Description: Calls GetByID to retrieve the PcPage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageRow
   */  
export function get_PcPages_Company_ConfigID_PageSeq(Company:string, ConfigID:string, PageSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcPageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcPageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcPage for the service
   Description: Calls UpdateExt to update PcPage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcPage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcPageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcPages_Company_ConfigID_PageSeq(Company:string, ConfigID:string, PageSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")", {
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
   Summary: Call UpdateExt to delete PcPage item
   Description: Call UpdateExt to delete PcPage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcPage
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcPages_Company_ConfigID_PageSeq(Company:string, ConfigID:string, PageSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")", {
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
   Description: Get PcInputs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   */  
export function get_PcPages_Company_ConfigID_PageSeq_PcInputs(Company:string, ConfigID:string, PageSeq:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcInputs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   */  
export function get_PcPages_Company_ConfigID_PageSeq_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, PageSeq:string, InputName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcPageExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcPageExprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageExprRow
   */  
export function get_PcPages_Company_ConfigID_PageSeq_PcPageExprs(Company:string, ConfigID:string, PageSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcPageExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcPageExpr item
   Description: Calls GetByID to retrieve the PcPageExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPageExpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   */  
export function get_PcPages_Company_ConfigID_PageSeq_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PageSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcPageExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcPageExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcInputs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs", {
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
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   */  
export function get_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInput for the service
   Description: Calls UpdateExt to update PcInput. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
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
   Summary: Call UpdateExt to delete PcInput item
   Description: Call UpdateExt to delete PcInput item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInput
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputs_Company_ConfigID_InputName(Company:string, ConfigID:string, InputName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", {
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
   Description: Get PcInputsLayerHeaders items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsLayerHeaders1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsLayerHeaders(Company:string, ConfigID:string, InputName:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsLayerHeaders", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcDynLsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLsts1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcDynLsts(Company:string, ConfigID:string, InputName:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcDynLsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDynLst item
   Description: Calls GetByID to retrieve the PcDynLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLst1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcInputsExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsExprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsExprRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsExprs(Company:string, ConfigID:string, InputName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInputsExpr item
   Description: Calls GetByID to retrieve the PcInputsExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsExpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcInputsRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsRules1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsRules(Company:string, ConfigID:string, InputName:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInputsRule item
   Description: Calls GetByID to retrieve the PcInputsRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRule1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company:string, ConfigID:string, InputName:string, TargetInputName:string, RuleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QBuildObjs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QBuildObjs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildObjRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_QBuildObjs(Company:string, ConfigID:string, InputName:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/QBuildObjs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QBuildObj item
   Description: Calls GetByID to retrieve the QBuildObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildObj1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   */  
export function get_PcInputs_Company_ConfigID_InputName_QBuildObjs_Company_ConfigID_InputName_ObjName(Company:string, ConfigID:string, InputName:string, ObjName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QBuildObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QBuildObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerHeaders
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputsLayerHeaders(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsLayerHeaders(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders", {
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
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   */  
export function get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerHeaderRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerHeaderRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsLayerHeader for the service
   Description: Calls UpdateExt to update PcInputsLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Summary: Call UpdateExt to delete PcInputsLayerHeader item
   Description: Call UpdateExt to delete PcInputsLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerHeader
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", {
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
   Description: Get PcInputsLayerDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsLayerDetails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID_PcInputsLayerDetails(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")/PcInputsLayerDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsLayerDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails", {
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
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   */  
export function get_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsLayerDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsLayerDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsLayerDetail for the service
   Description: Calls UpdateExt to update PcInputsLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Summary: Call UpdateExt to delete PcInputsLayerDetail item
   Description: Call UpdateExt to delete PcInputsLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerDetail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ImageLayerID Desc: ImageLayerID   Required: True   Allow empty value : True
      @param LayerSeq Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company:string, ConfigID:string, InputName:string, ImageLayerID:string, LayerSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", {
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
   Description: Get PcDynLsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLsts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstRow
   */  
export function get_PcDynLsts(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDynLsts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts", {
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
   Summary: Calls GetByID to retrieve the PcDynLst item
   Description: Calls GetByID to retrieve the PcDynLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDynLst for the service
   Description: Calls UpdateExt to update PcDynLst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")", {
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
   Summary: Call UpdateExt to delete PcDynLst item
   Description: Call UpdateExt to delete PcDynLst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLst
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")", {
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
   Description: Get PcDynLstCriterias items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstCriterias1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstCriteriaRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstCriterias(Company:string, ConfigID:string, InputName:string, ListSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstCriterias", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDynLstCriteria item
   Description: Calls GetByID to retrieve the PcDynLstCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstCriteria1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param CriteriaSeq Desc: CriteriaSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, CriteriaSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcDynLstExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstExprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstExprRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstExprs(Company:string, ConfigID:string, InputName:string, ListSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDynLstExpr item
   Description: Calls GetByID to retrieve the PcDynLstExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstExpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, ListSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PcDynLstParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstParams1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstParamsRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstParams(Company:string, ConfigID:string, InputName:string, ListSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcDynLstParam item
   Description: Calls GetByID to retrieve the PcDynLstParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstParam1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   */  
export function get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company:string, ConfigID:string, InputName:string, ListSeq:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcDynLstCriterias items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstCriterias
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstCriteriaRow
   */  
export function get_PcDynLstCriterias(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstCriterias
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDynLstCriterias(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias", {
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
   Summary: Calls GetByID to retrieve the PcDynLstCriteria item
   Description: Calls GetByID to retrieve the PcDynLstCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param CriteriaSeq Desc: CriteriaSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   */  
export function get_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, CriteriaSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstCriteriaRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstCriteriaRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDynLstCriteria for the service
   Description: Calls UpdateExt to update PcDynLstCriteria. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param CriteriaSeq Desc: CriteriaSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, CriteriaSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")", {
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
   Summary: Call UpdateExt to delete PcDynLstCriteria item
   Description: Call UpdateExt to delete PcDynLstCriteria item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstCriteria
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param CriteriaSeq Desc: CriteriaSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company:string, ConfigID:string, InputName:string, ListSeq:string, CriteriaSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")", {
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
   Description: Get PcDynLstExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstExprRow
   */  
export function get_PcDynLstExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDynLstExprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs", {
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
   Summary: Calls GetByID to retrieve the PcDynLstExpr item
   Description: Calls GetByID to retrieve the PcDynLstExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   */  
export function get_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, ListSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDynLstExpr for the service
   Description: Calls UpdateExt to update PcDynLstExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, ListSeq:string, TypeCode:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcDynLstExpr item
   Description: Call UpdateExt to delete PcDynLstExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, ListSeq:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Description: Get PcDynLstParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstParams
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstParamsRow
   */  
export function get_PcDynLstParams(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcDynLstParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams", {
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
   Summary: Calls GetByID to retrieve the PcDynLstParam item
   Description: Calls GetByID to retrieve the PcDynLstParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   */  
export function get_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company:string, ConfigID:string, InputName:string, ListSeq:string, ParamName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcDynLstParamsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcDynLstParamsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcDynLstParam for the service
   Description: Calls UpdateExt to update PcDynLstParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company:string, ConfigID:string, InputName:string, ListSeq:string, ParamName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")", {
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
   Summary: Call UpdateExt to delete PcDynLstParam item
   Description: Call UpdateExt to delete PcDynLstParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstParam
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ListSeq Desc: ListSeq   Required: True
      @param ParamName Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company:string, ConfigID:string, InputName:string, ListSeq:string, ParamName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")", {
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
   Description: Get PcInputsExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsExprRow
   */  
export function get_PcInputsExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsExprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs", {
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
   Summary: Calls GetByID to retrieve the PcInputsExpr item
   Description: Calls GetByID to retrieve the PcInputsExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   */  
export function get_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsExpr for the service
   Description: Calls UpdateExt to update PcInputsExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, TypeCode:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcInputsExpr item
   Description: Call UpdateExt to delete PcInputsExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company:string, ConfigID:string, InputName:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")", {
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
   Description: Get PcInputsRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsRules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleRow
   */  
export function get_PcInputsRules(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsRules(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules", {
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
   Summary: Calls GetByID to retrieve the PcInputsRule item
   Description: Calls GetByID to retrieve the PcInputsRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   */  
export function get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsRule for the service
   Description: Calls UpdateExt to update PcInputsRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")", {
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
   Summary: Call UpdateExt to delete PcInputsRule item
   Description: Call UpdateExt to delete PcInputsRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsRule
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")", {
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
   Description: Get PcInputsRuleDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsRuleDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleDefRow
   */  
export function get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq_PcInputsRuleDefs(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")/PcInputsRuleDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PcInputsRuleDef item
   Description: Calls GetByID to retrieve the PcInputsRuleDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRuleDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   */  
export function get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRuleDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRuleDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PcInputsRuleDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsRuleDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleDefRow
   */  
export function get_PcInputsRuleDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsRuleDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcInputsRuleDefs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs", {
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
   Summary: Calls GetByID to retrieve the PcInputsRuleDef item
   Description: Calls GetByID to retrieve the PcInputsRuleDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRuleDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   */  
export function get_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcInputsRuleDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcInputsRuleDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcInputsRuleDef for the service
   Description: Calls UpdateExt to update PcInputsRuleDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsRuleDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcInputsRuleDef item
   Description: Call UpdateExt to delete PcInputsRuleDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsRuleDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TargetInputName Desc: TargetInputName   Required: True   Allow empty value : True
      @param RuleSeq Desc: RuleSeq   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company:string, ConfigID:string, TargetInputName:string, RuleSeq:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")", {
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
   Description: Get QBuildObjs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildObjs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildObjRow
   */  
export function get_QBuildObjs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildObjs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QBuildObjs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs", {
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
   Summary: Calls GetByID to retrieve the QBuildObj item
   Description: Calls GetByID to retrieve the QBuildObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   */  
export function get_QBuildObjs_Company_ConfigID_InputName_ObjName(Company:string, ConfigID:string, InputName:string, ObjName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QBuildObjRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QBuildObjRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QBuildObj for the service
   Description: Calls UpdateExt to update QBuildObj. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QBuildObjs_Company_ConfigID_InputName_ObjName(Company:string, ConfigID:string, InputName:string, ObjName:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")", {
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
   Summary: Call UpdateExt to delete QBuildObj item
   Description: Call UpdateExt to delete QBuildObj item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildObj
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QBuildObjs_Company_ConfigID_InputName_ObjName(Company:string, ConfigID:string, InputName:string, ObjName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")", {
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
   Description: Get QBuildMappings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QBuildMappings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildObjs_Company_ConfigID_InputName_ObjName_QBuildMappings(Company:string, ConfigID:string, InputName:string, ObjName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")/QBuildMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildObjs_Company_ConfigID_InputName_ObjName_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QBuildMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildMappings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildMappings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_QBuildMappings(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings", {
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
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   */  
export function get_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_QBuildMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_QBuildMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update QBuildMapping for the service
   Description: Calls UpdateExt to update QBuildMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
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
   Summary: Call UpdateExt to delete QBuildMapping item
   Description: Call UpdateExt to delete QBuildMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildMapping
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param InputName Desc: InputName   Required: True   Allow empty value : True
      @param ObjName Desc: ObjName   Required: True   Allow empty value : True
      @param ObjParameter Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company:string, ConfigID:string, InputName:string, ObjName:string, ObjParameter:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", {
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
   Description: Get PcPageExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcPageExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageExprRow
   */  
export function get_PcPageExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcPageExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcPageExprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs", {
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
   Summary: Calls GetByID to retrieve the PcPageExpr item
   Description: Calls GetByID to retrieve the PcPageExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPageExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   */  
export function get_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PageSeq:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcPageExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcPageExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcPageExpr for the service
   Description: Calls UpdateExt to update PcPageExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcPageExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PageSeq:string, TypeCode:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcPageExpr item
   Description: Call UpdateExt to delete PcPageExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcPageExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param PageSeq Desc: PageSeq   Required: True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company:string, ConfigID:string, PageSeq:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")", {
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
   Description: Get PcStatusExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStatusExprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusExprRow
   */  
export function get_PcStatusExprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStatusExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PcStatusExprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs", {
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
   Summary: Calls GetByID to retrieve the PcStatusExpr item
   Description: Calls GetByID to retrieve the PcStatusExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   */  
export function get_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company:string, ConfigID:string, TypeCode:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PcStatusExprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PcStatusExprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PcStatusExpr for the service
   Description: Calls UpdateExt to update PcStatusExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStatusExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company:string, ConfigID:string, TypeCode:string, SeqNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete PcStatusExpr item
   Description: Call UpdateExt to delete PcStatusExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStatusExpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ConfigID Desc: ConfigID   Required: True   Allow empty value : True
      @param TypeCode Desc: TypeCode   Required: True   Allow empty value : True
      @param SeqNum Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company:string, ConfigID:string, TypeCode:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
export function get_GetRows(whereClausePcStatus:string, whereClausePcPage:string, whereClausePcInputs:string, whereClausePcInputsLayerHeader:string, whereClausePcInputsLayerDetail:string, whereClausePcDynLst:string, whereClausePcDynLstCriteria:string, whereClausePcDynLstExpr:string, whereClausePcDynLstParams:string, whereClausePcInputsExpr:string, whereClausePcInputsRule:string, whereClausePcInputsRuleDef:string, whereClauseQBuildObj:string, whereClauseQBuildMapping:string, whereClausePcPageExpr:string, whereClausePcStatusExpr:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePcStatus!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcStatus=" + whereClausePcStatus
   }
   if(typeof whereClausePcPage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcPage=" + whereClausePcPage
   }
   if(typeof whereClausePcInputs!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputs=" + whereClausePcInputs
   }
   if(typeof whereClausePcInputsLayerHeader!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsLayerHeader=" + whereClausePcInputsLayerHeader
   }
   if(typeof whereClausePcInputsLayerDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsLayerDetail=" + whereClausePcInputsLayerDetail
   }
   if(typeof whereClausePcDynLst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDynLst=" + whereClausePcDynLst
   }
   if(typeof whereClausePcDynLstCriteria!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDynLstCriteria=" + whereClausePcDynLstCriteria
   }
   if(typeof whereClausePcDynLstExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDynLstExpr=" + whereClausePcDynLstExpr
   }
   if(typeof whereClausePcDynLstParams!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcDynLstParams=" + whereClausePcDynLstParams
   }
   if(typeof whereClausePcInputsExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsExpr=" + whereClausePcInputsExpr
   }
   if(typeof whereClausePcInputsRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsRule=" + whereClausePcInputsRule
   }
   if(typeof whereClausePcInputsRuleDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcInputsRuleDef=" + whereClausePcInputsRuleDef
   }
   if(typeof whereClauseQBuildObj!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQBuildObj=" + whereClauseQBuildObj
   }
   if(typeof whereClauseQBuildMapping!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQBuildMapping=" + whereClauseQBuildMapping
   }
   if(typeof whereClausePcPageExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcPageExpr=" + whereClausePcPageExpr
   }
   if(typeof whereClausePcStatusExpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePcStatusExpr=" + whereClausePcStatusExpr
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetRows" + params, {
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
export function get_GetByID(configID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof configID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "configID=" + configID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetList" + params, {
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
   Summary: Invoke method NumberOfDecimalPlaces
   Description: Returns number of decimals in the specified format string
   OperationID: NumberOfDecimalPlaces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NumberOfDecimalPlaces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NumberOfDecimalPlaces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NumberOfDecimalPlaces(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/NumberOfDecimalPlaces", {
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
   Summary: Invoke method ValidateAllowedToDeletePcInput
   Description: Validate if the PcInputs is allowed to be deleted
   OperationID: ValidateAllowedToDeletePcInput
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAllowedToDeletePcInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAllowedToDeletePcInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAllowedToDeletePcInput(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidateAllowedToDeletePcInput", {
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
   Summary: Invoke method GetSourceInputNameList
   Description: Gets available list of input names.
   OperationID: GetSourceInputNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceInputNameList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceInputNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSourceInputNameList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetSourceInputNameList", {
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
   Summary: Invoke method DuplicateInputRule
   Description: Duplicate Inputs Rule.
   OperationID: DuplicateInputRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateInputRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateInputRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateInputRule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/DuplicateInputRule", {
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
   Summary: Invoke method OnChangeInputType
   Description: Set defaults based on the control style.
   OperationID: OnChangeInputType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInputType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeInputType", {
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
   Summary: Invoke method OnChangeInputName
   Description: Set defaults when the control name is set.
   OperationID: OnChangeInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInputName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeInputName", {
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
   Summary: Invoke method OnChangeMinOrMaxForDecimal
   Description: Set Increment default1 to 1 if 0 when a min or max is set.
   OperationID: OnChangeMinOrMaxForDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinOrMaxForDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinOrMaxForDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMinOrMaxForDecimal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeMinOrMaxForDecimal", {
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
   Summary: Invoke method OnChangeInputTabOrder
   Description: Finds the Last Tab Order and add 10 to it.  Is used when pasing into a grid.
   OperationID: OnChangeInputTabOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputTabOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputTabOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInputTabOrder(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeInputTabOrder", {
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
   Summary: Invoke method CreateNewEmptyPcInputs
   Description: Create a new PcInput row based on the control style.  This method is used by the grid for list entry input.
   OperationID: CreateNewEmptyPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewEmptyPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewEmptyPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewEmptyPcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/CreateNewEmptyPcInputs", {
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
   Summary: Invoke method CreateNewPcInputs
   Description: Create a new PcInput record based on the control type. This method is used by the designer instead of the generic GetNewInput.
   OperationID: CreateNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateNewPcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/CreateNewPcInputs", {
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
   Summary: Invoke method OnChangeImageLayerID
   Description: Validates the proposed image layer ID in the the ImageLayerHeader table
   OperationID: OnChangeImageLayerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeImageLayerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeImageLayerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeImageLayerID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeImageLayerID", {
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
   Summary: Invoke method ImageLayerScriptCode
   Description: Method used to call the Image Layer Engine code generator and return Script code for execution.
<param name="imageLayerID">Image Layer ID to be used for generating the script code</param>
   OperationID: ImageLayerScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImageLayerScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImageLayerScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImageLayerScriptCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ImageLayerScriptCode", {
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
   Summary: Invoke method ImageLayerUpdateScriptCode
   Description: Method used to call the Image Layer Engine code generator and return updating Script code for execution.
   OperationID: ImageLayerUpdateScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImageLayerUpdateScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImageLayerUpdateScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImageLayerUpdateScriptCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ImageLayerUpdateScriptCode", {
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
   Summary: Invoke method OnChangeAttributeID
   Description: Validates the attribute ID column of PcInputs in theConfiguration 'dirty' row. Also runs the foreign link to populate Attribute Description.
   OperationID: OnChangeAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttributeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeAttributeID", {
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
   Summary: Invoke method OnChangeDynAttributeID
   Description: Call when changing the Attribute ID for a configurator tied to a PartAttrClass.
   OperationID: OnChangeDynAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDynAttributeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeDynAttributeID", {
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
   Summary: Invoke method GetAttributeDesc
   Description: Returns the description of a given attribute as it is set up in Insp Attribute Entry.
   OperationID: GetAttributeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAttributeDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetAttributeDesc", {
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
   Summary: Invoke method GetDynAttributeDesc
   Description: Returns the description of a given dynamioc attribute
   OperationID: GetDynAttributeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynAttributeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynAttributeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDynAttributeDesc(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetDynAttributeDesc", {
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
   Summary: Invoke method OnChangePageDisplaySeq
   Description: Validate that the new PcPage.DisplaySeq value is not in use by another PcPage record.
   OperationID: OnChangePageDisplaySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePageDisplaySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePageDisplaySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePageDisplaySeq(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangePageDisplaySeq", {
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
   Summary: Invoke method OnChangeInputPageNumber
   Description: Recalculates the PcInputs.PageSeq field from the new PcInputs.PageDisplaySeq.
   OperationID: OnChangeInputPageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputPageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputPageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInputPageNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeInputPageNumber", {
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
   Summary: Invoke method ValidateBAQColumnName
   Description: Validates if a QueryField row exists.
   OperationID: ValidateBAQColumnName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBAQColumnName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBAQColumnName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBAQColumnName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidateBAQColumnName", {
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
   Summary: Invoke method ValidatePcLookupTblHed
   Description: Validates if a PcLookupTblHed with a matching ID exists
   OperationID: ValidatePcLookupTblHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcLookupTblHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcLookupTblHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePcLookupTblHed(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidatePcLookupTblHed", {
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
   Summary: Invoke method ValidatePcLookupColSetDtl
   Description: Validates if a PcLookupColSetDtl with a matching ID exists
   OperationID: ValidatePcLookupColSetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcLookupColSetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcLookupColSetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePcLookupColSetDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidatePcLookupColSetDtl", {
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
   Summary: Invoke method GetBAQDisplayColumnList
   Description: This method will provide a list of the selected Display Columns in a BAQ given its Query ID.
   OperationID: GetBAQDisplayColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBAQDisplayColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQDisplayColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBAQDisplayColumnList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetBAQDisplayColumnList", {
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
   Summary: Invoke method GetInputList
   Description: Returns a dataset with a list of PcInputs rows
   OperationID: GetInputList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInputList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInputList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInputList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetInputList", {
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
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before SyncRevision method is called.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptForPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PromptForPassword(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PromptForPassword", {
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
   Summary: Invoke method SyncRevision
   Description: This method synchronizes the part revision approval flag when the PcStatus.Approved
flag changes
   OperationID: SyncRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyncRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyncRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SyncRevision(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/SyncRevision", {
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
   Summary: Invoke method OnChangedGlobalInputVar
   Description: Reset Values when Global Input Variable is false.
   OperationID: OnChangedGlobalInputVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedGlobalInputVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedGlobalInputVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedGlobalInputVar(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangedGlobalInputVar", {
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
   Summary: Invoke method OnChangingGlbInputVarName
   Description: Validate Name and update initial values
   OperationID: OnChangingGlbInputVarName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingGlbInputVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingGlbInputVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingGlbInputVarName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangingGlbInputVarName", {
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
   Summary: Invoke method OnChangeInputReadOnlyExpr
   Description: Reset Values when Read Only flag is false.
   OperationID: OnChangeInputReadOnlyExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputReadOnlyExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputReadOnlyExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeInputReadOnlyExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeInputReadOnlyExpr", {
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
   Summary: Invoke method OnChangePageReadOnlyExpr
   Description: Reset Values when Read Only flag is false.
   OperationID: OnChangePageReadOnlyExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePageReadOnlyExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePageReadOnlyExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePageReadOnlyExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangePageReadOnlyExpr", {
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
   Summary: Invoke method OnChangingBAQName
   Description: Validate Name and update initial values
   OperationID: OnChangingBAQName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingBAQName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingBAQName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingBAQName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangingBAQName", {
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
   Summary: Invoke method OnChangingUserDefinedMethodName
   Description: Validate Name and update initial values
   OperationID: OnChangingUserDefinedMethodName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingUserDefinedMethodName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingUserDefinedMethodName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingUserDefinedMethodName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangingUserDefinedMethodName", {
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
   Summary: Invoke method OnChangingDataLookupFunction
   Description: Validate Name and update initial values
   OperationID: OnChangingDataLookupFunction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDataLookupFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDataLookupFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDataLookupFunction(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangingDataLookupFunction", {
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
   Summary: Invoke method OnChangingListDataSource
   Description: Delete dynamic list's previous values
   OperationID: OnChangingListDataSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingListDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingListDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingListDataSource(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangingListDataSource", {
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
   Summary: Invoke method OnChangeSourceInputName
   Description: Validations for change to Source Input name.
   OperationID: OnChangeSourceInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourceInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSourceInputName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeSourceInputName", {
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
   Summary: Invoke method PageCountForCodeEditor
   Description: Returns the number of pages.  Used by the Code Editor
   OperationID: PageCountForCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PageCountForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PageCountForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PageCountForCodeEditor(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PageCountForCodeEditor", {
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
   Summary: Invoke method ExistsProposedInputName
   Description: Return if an input name already exists
   OperationID: ExistsProposedInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProposedInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProposedInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsProposedInputName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ExistsProposedInputName", {
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
   Summary: Invoke method ValidateInputName
   Description: This method ensures the input name is not a duplicate.  If it is not, then a check is made to
ensure the name does not end in restricted text.
   OperationID: ValidateInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateInputName(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidateInputName", {
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
   Summary: Invoke method ValidateImageLayerID
   Description: Validates the proposed image layer ID in the the ImageLayerHeader table
   OperationID: ValidateImageLayerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateImageLayerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateImageLayerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateImageLayerID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidateImageLayerID", {
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
   Summary: Invoke method GetDefaultListItems
   Description: Return the list items by default when adding a Dynamic List.
   OperationID: GetDefaultListItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultListItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultListItems(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetDefaultListItems", {
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
   Summary: Invoke method UpdateQBuildMapping
   Description: Update the QBuild mapping and set PcInputs.ImageMapping to true or false
   OperationID: UpdateQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateQBuildMapping(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/UpdateQBuildMapping", {
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
   Summary: Invoke method ImportImagesFileStore
   OperationID: ImportImagesFileStore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportImagesFileStore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportImagesFileStore_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportImagesFileStore(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ImportImagesFileStore", {
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
   Summary: Invoke method DeleteQBuildImage
   Description: Call this method when the user has removed all objects from the drawing canvas
   OperationID: DeleteQBuildImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQBuildImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQBuildImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteQBuildImage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/DeleteQBuildImage", {
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
   Summary: Invoke method ValidateMappedInput
   Description: Validates the entered MappedInputName
   OperationID: ValidateMappedInput
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMappedInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMappedInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMappedInput(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ValidateMappedInput", {
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
   Summary: Invoke method OnChangeFormatString
   Description: checks QBuildMapping to see if this input is mapped to an integer object
   OperationID: OnChangeFormatString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFormatString(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/OnChangeFormatString", {
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
   Summary: Invoke method GetPcInputsWithLayerIDForConfiguration
   Description: Retrieve the PcInputs with an ImageLayerID specified for a given configurator
   OperationID: GetPcInputsWithLayerIDForConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcInputsWithLayerIDForConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcInputsWithLayerIDForConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPcInputsWithLayerIDForConfiguration(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetPcInputsWithLayerIDForConfiguration", {
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
   Summary: Invoke method RefreshImageLayerDetails
   Description: Refresh the image layer details for an input
   OperationID: RefreshImageLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshImageLayerDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshImageLayerDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RefreshImageLayerDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/RefreshImageLayerDetails", {
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
   Summary: Invoke method GetNewPcStatus
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcStatus", {
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
   Summary: Invoke method GetNewPcPage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcPage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcPage(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcPage", {
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
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputs", {
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
   Summary: Invoke method GetNewPcInputsLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsLayerHeader(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputsLayerHeader", {
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
   Summary: Invoke method GetNewPcInputsLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsLayerDetail(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputsLayerDetail", {
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
   Summary: Invoke method GetNewPcDynLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDynLst(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcDynLst", {
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
   Summary: Invoke method GetNewPcDynLstCriteria
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstCriteria
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstCriteria_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstCriteria_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDynLstCriteria(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcDynLstCriteria", {
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
   Summary: Invoke method GetNewPcDynLstExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDynLstExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcDynLstExpr", {
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
   Summary: Invoke method GetNewPcDynLstParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcDynLstParams(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcDynLstParams", {
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
   Summary: Invoke method GetNewPcInputsExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputsExpr", {
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
   Summary: Invoke method GetNewPcInputsRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsRule(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputsRule", {
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
   Summary: Invoke method GetNewPcInputsRuleDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsRuleDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsRuleDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsRuleDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcInputsRuleDef(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcInputsRuleDef", {
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
   Summary: Invoke method GetNewQBuildObj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildObj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildObj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildObj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQBuildObj(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewQBuildObj", {
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
   Summary: Invoke method GetNewQBuildMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewQBuildMapping(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewQBuildMapping", {
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
   Summary: Invoke method GetNewPcPageExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcPageExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcPageExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcPageExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcPageExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcPageExpr", {
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
   Summary: Invoke method GetNewPcStatusExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatusExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatusExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatusExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPcStatusExpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetNewPcStatusExpr", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDynLstCriteriaRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDynLstExprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDynLstParamsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcDynLstRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsExprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsLayerDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsLayerHeaderRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsRuleDefRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcInputsRuleRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcPageExprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcPageRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusExprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PcStatusRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QBuildMappingRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow{
   "odatametadata":string,
   "value":Erp_Tablesets_QBuildObjRow[],
}

export interface Erp_Tablesets_PcDynLstCriteriaRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  The unique sequence id for the dynamic list.  */  
   "ListSeq":number,
      /**  Criteria sequence number to make this record unique.  */  
   "CriteriaSeq":number,
      /**  Column name to use for BAQ query criteria  */  
   "ColumnName":string,
      /**  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  */  
   "Condition":string,
      /**  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  */  
   "ValueFrom":string,
      /**  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  */  
   "ColumnValue":string,
      /**  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  */  
   "Operator":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  UseEmptyValue  */  
   "UseEmptyValue":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  */  
   "ColumnType":string,
      /**  Page Sequence where the parent input exists  */  
   "PageSeq":number,
      /**  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  */  
   "ValueFromDisplay":string,
      /**  BAQ Program Name  */  
   "BAQProgramName":string,
   "BitFlag":number,
   "PartNumPricePerCode":string,
   "PartNumSalesUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumTrackLots":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDynLstExprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Input Name  */  
   "InputName":string,
      /**  The unique sequence id for the dynamic list.  */  
   "ListSeq":number,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**  Sequence Number.  */  
   "SeqNum":number,
      /**  The On Leave expression for the control.  */  
   "Expression":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDynLstParamsRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  InputName  */  
   "InputName":string,
      /**  ListSeq  */  
   "ListSeq":number,
      /**  ParamName  */  
   "ParamName":string,
      /**  ParamConst  */  
   "ParamConst":boolean,
      /**  ParamValue  */  
   "ParamValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Page Sequence where the parent input exists  */  
   "PageSeq":number,
      /**  This is the type of Parameter.  */  
   "ParamType":string,
   "ParamInput":string,
   "ParamModifier":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcDynLstRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Input Name  */  
   "InputName":string,
      /**  The unique sequence id for the dynamic list.  */  
   "ListSeq":number,
      /**  Contains the logical expression as to when the list is used.  */  
   "Condition":string,
      /**  Contains the combo-box list items that are used when the condition is true.  */  
   "ListItems":string,
      /**  The Initial value for the list.  */  
   "InitVal":string,
      /**  If TRUE then the dynamic list will be built by running a BAQ program  */  
   "BAQRunProgram":boolean,
      /**  The BAQ program name used for building the dynamic list  */  
   "BAQProgramName":string,
      /**  Value that will be displayed from the BAQ  */  
   "BAQDispValue":string,
      /**  The input value for the BAQ  */  
   "BAQInputVal":string,
      /**  Defines the type of dynamic list from Static, BAQ, Program, etc.  */  
   "ListDataSource":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  RunTblLookup  */  
   "RunTblLookup":boolean,
      /**  TblLookupID  */  
   "TblLookupID":string,
      /**  TblLookupFunc  */  
   "TblLookupFunc":string,
      /**  RunUserDefined  */  
   "RunUserDefined":string,
      /**  UserDefinedName  */  
   "UserDefinedName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  SortOrder  */  
   "SortOrder":string,
      /**  SubReturnColumn  */  
   "SubReturnColumn":string,
      /**  ScriptCondition  */  
   "ScriptCondition":string,
      /**  Reserved for Future Development  */  
   "AttributeID":string,
      /**  Identifies if Script expressions are valid for Dynamic List Conditions  */  
   "EnableScript":boolean,
   "EntprsConf":boolean,
   "PageSeq":number,
      /**  Either Client or Server where the UD Method is executed.  */  
   "UserDefinedFunctionType":string,
      /**  Storing the Return Type for the selected User Defined Method.  */  
   "UserDefinedReturnType":string,
      /**  If true then details on this record can be updated  */  
   "CanUpdate":boolean,
   "BitFlag":number,
   "PartNumSellingFactor":number,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsExprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**  Sequence Number.  */  
   "SeqNum":number,
      /**  The On Leave expression for the control.  */  
   "Expression":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsLayerDetailRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  InputName  */  
   "InputName":string,
      /**  ImageLayerID  */  
   "ImageLayerID":string,
      /**  LayerSeq  */  
   "LayerSeq":number,
      /**  LayerName  */  
   "LayerName":string,
      /**  LayerDesc  */  
   "LayerDesc":string,
      /**  Order in which layers are placed on the base image.  */  
   "ZIndex":number,
      /**  ImageID  */  
   "ImageID":string,
      /**  Png type is supported.  */  
   "FileType":string,
      /**  Free form text enabling users to categorize layers  */  
   "Category":string,
      /**  Width of image  */  
   "Width":number,
      /**  Height of image  */  
   "Height":number,
      /**  Reserved for Future Development  */  
   "xPos":number,
      /**  Reserved for Future Development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsLayerHeaderRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Input name this header is assigned.  */  
   "InputName":string,
      /**  Image Layer ID.  */  
   "ImageLayerID":string,
      /**  File name of the image to be retrieved from the Image URL.  */  
   "ImageID":string,
      /**  Description  */  
   "Description":string,
      /**  The URL location of the image.  */  
   "ImageURL":string,
      /**  File types png and jpg are supported.  */  
   "FileType":string,
      /**  Image Width  */  
   "Width":number,
      /**  Image height  */  
   "Height":number,
      /**  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  */  
   "Version":number,
      /**  Reserved for future development  */  
   "xPos":number,
      /**  Reserved for future development  */  
   "yPos":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   "InputName":string,
      /**  The order that the tab function will step through the inputs.  */  
   "TabOrder":number,
      /**  The type of data that can be stored in the control.  */  
   "DataType":string,
      /**  The format for which the data will be stored.  */  
   "FormatString":string,
      /**  The initial value for the control.  */  
   "InitVal":string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   "StatusText":string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   "Required":boolean,
      /**  On what page does the control exist.  */  
   "PageSeq":number,
      /**  The control's label.  */  
   "SideLabel":string,
      /**  The pixel position for the x axis.  */  
   "xPos":number,
      /**  The pixel position for the Y axis.  */  
   "yPos":number,
      /**  The pixel width of the control.  */  
   "pWidth":number,
      /**  The pixel height of the control.  */  
   "pHeight":number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   "ControlType":string,
      /**  The prompt when expression for the widget.  */  
   "PromptWhen":string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   "ListItems":string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   "StartDec":number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   "EndDec":number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   "IncrPrec":number,
      /**  The starting date for a validated date fill-in.  */  
   "StartDate":string,
      /**  The ending date for a validated date fill-in.  */  
   "EndDate":string,
      /**  The list of valid responses for a validated string input.  */  
   "ValList":string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   "Horizontal":boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   "IsGlobal":boolean,
      /**  The On Leave expression for the control.  */  
   "OnLeave":string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   "WebInputName":string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   "SummaryLabel":string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   "DLRunProgram":boolean,
      /**  The Progress program used for building a dynamic list.  */  
   "DLProgramName":string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   "DLProgramInputs":string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   "SourceDBRecid":string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   "HideInSummary":boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   "OnLeave2":string,
      /**  If true, the input will not be displayed on the input page  */  
   "Invisible":boolean,
      /**  Comments describing the input  */  
   "Comments":string,
      /**  Global Input Variable  */  
   "GlobalInputVar":boolean,
      /**  Global Input Variable Name  */  
   "GlbInputVarName":string,
      /**  Do not display input in Summary  */  
   "NoDispSummary":boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   "ExternalRef":boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   "AttributeID":string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMinValue":boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseMaxValue":boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseIncrValue":boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseInitVal":boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   "UseToolTip":boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseScreenLabel":boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   "UseListValues":boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   "SmartPartSeq":number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   "SmartStringStart":number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   "SmartStringEnd":number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   "ShowDistinct":boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   "DesignControlType":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ReadOnly  */  
   "ReadOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AutoSizeList  */  
   "AutoSizeList":boolean,
      /**  ListWidth  */  
   "ListWidth":number,
      /**  ImageSource  */  
   "ImageSource":string,
      /**  ImageLayerID  */  
   "ImageLayerID":string,
   "AllowSmartString":boolean,
   "AttributeDescription":string,
      /**  If true then fields on the record may be updated  */  
   "CanUpdate":boolean,
   "Content":string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   "DispCharVal":string,
   "DspPageSeq":number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   "FullInputName":string,
   "ImageMapping":boolean,
      /**  The initial value of a date field  */  
   "InitDate":string,
      /**  The initial value of a decimal input  */  
   "InitDecimal":number,
      /**  The initial value for a logical input  */  
   "InitLogical":boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   "InputRules":boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   "InputType":string,
   "IsGlobalInputVar":boolean,
   "OnLaunch":string,
   "PageDisplaySeq":number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   "PcDynLstCount":number,
   "ReadOnlyExpression":string,
   "TestPlan":boolean,
   "ImageURL":string,
   "BitFlag":number,
   "PartNumTrackDimension":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsRuleDefRow{
      /**  Company  */  
   "Company":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  The Input that is updated based upon the rule definition.  */  
   "TargetInputName":string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   "RuleSeq":number,
      /**  The order in which these definitions are interrogated.  */  
   "SeqNum":number,
      /**  Input whose value is used in determining if this rule is executed.  */  
   "SourceInputName":string,
      /**  Reserved for future development.  Defaults to Value.  */  
   "SourceInputProperty":string,
      /**  SourceCharacterValue  */  
   "SourceCharacterValue":string,
      /**  SourceIntegerValue  */  
   "SourceIntegerValue":number,
      /**  SourceDecimalValue  */  
   "SourceDecimalValue":number,
      /**  SourceDateValue  */  
   "SourceDateValue":string,
      /**  SourceLogicalValue  */  
   "SourceLogicalValue":boolean,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   "ProcessSeq":number,
      /**  Reserved for future development.  */  
   "LeftP":string,
      /**  Reserved for future development.  */  
   "RightP":string,
      /**  Defaults to And and permits users to use more than one input in the rule.  */  
   "AndOr":string,
      /**  Comparison operator used when evaluating the rule. Valid value at this time is equals.  */  
   "CompOp":string,
      /**  Reserved for future development.  Defaults to false.  */  
   "Neg":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "ListValues":string,
   "SourceValue":string,
      /**  Input type valid values Label, Character, Numeric, Date, ComboBox  */  
   "InputType":string,
   "BitFlag":number,
   "SourcePcInputsDesignControlType":string,
   "SourcePcInputsFormatString":string,
   "SourcePcInputsListItems":string,
   "SourcePcInputsDataType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcInputsRuleRow{
      /**  Company  */  
   "Company":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  The Input that is updated based upon the rule definition.  */  
   "TargetInputName":string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   "RuleSeq":number,
      /**  Enter text that describes what the rule does.  */  
   "RuleDesc":string,
      /**  Reserved for future development.  Defaults to Value.  */  
   "TargetInputProperty":string,
      /**  The new value of the input when this rule executes.  */  
   "TargetInputValue":string,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   "ProcessSeq":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Associated Rule Defintion descriptions  */  
   "DefinitionDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcPageExprRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  The configuration page sequence.  */  
   "PageSeq":number,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Sequence Number.  */  
   "SeqNum":number,
      /**  Ex: Customization, Personalization  */  
   "TypeCode":string,
      /**  The On Leave expression for the control.  */  
   "Expression":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcPageRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   "RevisionNum":string,
      /**  The configuration page sequence.  */  
   "PageSeq":number,
      /**  The title of the configuration page.  */  
   "PageTitle":string,
      /**  The prompt when expression for the page.  */  
   "PromptWhen":string,
      /**  The On Leave expression for the page  */  
   "OnLeave":string,
      /**  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  */  
   "SkipOnLeaveOPL":boolean,
      /**  Additional field to add OnLeave expressions to the page  */  
   "OnLeave2":string,
      /**  Comments  */  
   "Comments":string,
      /**  Process dynamic lists before on leave expressions for this page  */  
   "ProcessDynLstFirst":boolean,
      /**  Only process dynamic lists with higher tab sequences  */  
   "DynLstHigher":boolean,
      /**  Skip processing page on leave on load  */  
   "SkipPageProcessOL":boolean,
      /**  Do not process on leave expressions when page loads  */  
   "SkipPageNoInputs":boolean,
      /**  Do not process on leave expressions when leaving pages  */  
   "SkipOnLeaveOPE":boolean,
      /**  Width of panel  */  
   "pWidth":number,
      /**  Height of panel  */  
   "pHeight":number,
      /**  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  */  
   "DisplaySeq":number,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  ReadOnly  */  
   "ReadOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CanUpdate":boolean,
   "FirstPage":boolean,
   "TestPlan":boolean,
   "ReadOnlyExpression":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStatusExprRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  TypeCode  */  
   "TypeCode":string,
      /**  SeqNum  */  
   "SeqNum":number,
      /**  Expression  */  
   "Expression":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStatusListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number.  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Configurator Approval Status  */  
   "Approved":boolean,
      /**  Date the configuration was approved.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Smart String Style  */  
   "StringStyle":string,
      /**  Smart String Seperator character  */  
   "Separator":string,
      /**  Smart String Digit Structure  */  
   "NumberFormat":string,
      /**  Smart String Starting Sequence  */  
   "StartNumber":number,
      /**  Part Creation Method  */  
   "CrtCustPart":boolean,
      /**  Smart String preface with part numbner  */  
   "PrefacePart":boolean,
      /**  Configurator Version  */  
   "ConfigVersion":number,
      /**  Quote Price Code  */  
   "QuotePCode":string,
      /**  Order Price Code  */  
   "OrderPCode":string,
      /**  OrdQuoCom  */  
   "OrdQuoCom":boolean,
      /**  JobPickCom  */  
   "JobPickCom":boolean,
      /**  ShipCom  */  
   "ShipCom":boolean,
      /**  InvCom  */  
   "InvCom":boolean,
      /**  Create Part Flag  */  
   "CreatePart":boolean,
      /**  Create part method  */  
   "CrtPartUsing":string,
      /**  Create New Part In Quote Entry  */  
   "InQuoting":boolean,
      /**  Automatically create a new part number  */  
   "AutoCrtPart":boolean,
      /**  Do not prompt user if part exists  */  
   "NotUnique":boolean,
      /**  Create New Part In Sales Order Entry  */  
   "InOrderEntry":boolean,
      /**  Create New Part In Job Entry  */  
   "InJobEntry":boolean,
      /**  Create Bill of Material  */  
   "CreateBOM":boolean,
      /**  Create Part at zero cost  */  
   "ZeroCost":boolean,
      /**  Create Smart String in part description  */  
   "CrtPartDesc":boolean,
      /**  File Name  */  
   "FileName":string,
      /**  Added to provide backward compatibility to previous releases.  */  
   "SingleLevelConf":boolean,
      /**  Indicates if the input values should be saved.  */  
   "SaveInputValues":boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   "SetPartNumOnly":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   "AprvRev":boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   "EntprsConf":boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   "Synchronize":boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   "DispConfSummary":boolean,
      /**  Part creation comments  */  
   "PartComments":string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   "CompPricing":boolean,
      /**  External configurator  */  
   "ExtConfig":boolean,
      /**  External company ID  */  
   "ExtMfgCompID":string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   "TestPlan":boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   "MarkMtlGlb":boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   "SIValuesUseQt":boolean,
      /**  This field will enable smart string processing for this configuration  */  
   "AllowSmartString":boolean,
   "InDemandEntry":boolean,
      /**  Demand Price Code  */  
   "DemandPCode":string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   "AllAltMethods":boolean,
      /**  SIValuesUseGenMethod  */  
   "SIValuesUseGenMethod":boolean,
      /**  Description  */  
   "Description":string,
      /**  ConfigType  */  
   "ConfigType":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ShrinkFieldProperties  */  
   "ShrinkFieldProperties":boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   "AuditDesc":string,
      /**  A sample smart string constructed from the smart string options  */  
   "SampleSmartString":string,
      /**  The available inputs available for use in the smart string  */  
   "AvailSmartStringInputs":string,
      /**  The inputs that have been selected for use in the smart string  */  
   "SelectedSmartStringInputs":string,
      /**  True if the PartRev record is approved  */  
   "RevApproved":boolean,
      /**  If true then detail fields other than Approved can be updated  */  
   "CanUpdate":boolean,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   "ECOGroup":string,
   "IsValidPwd":boolean,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PcStatusRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Part Number.  */  
   "PartNum":string,
      /**  Revision Number of the associated configurator  */  
   "RevisionNum":string,
      /**  Configurator Approval Status  */  
   "Approved":boolean,
      /**  Date the configuration was approved.  */  
   "ApprovedDate":string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   "ApprovedBy":string,
      /**  Smart String Style  */  
   "StringStyle":string,
      /**  Smart String Seperator character  */  
   "Separator":string,
      /**  Smart String Digit Structure  */  
   "NumberFormat":string,
      /**  Smart String Starting Sequence  */  
   "StartNumber":number,
      /**  Part Creation Method  */  
   "CrtCustPart":boolean,
      /**  Smart String preface with part numbner  */  
   "PrefacePart":boolean,
      /**  Configurator Version  */  
   "ConfigVersion":number,
      /**  Quote Price Code  */  
   "QuotePCode":string,
      /**  Order Price Code  */  
   "OrderPCode":string,
      /**  OrdQuoCom  */  
   "OrdQuoCom":boolean,
      /**  JobPickCom  */  
   "JobPickCom":boolean,
      /**  ShipCom  */  
   "ShipCom":boolean,
      /**  InvCom  */  
   "InvCom":boolean,
      /**  Create Part Flag  */  
   "CreatePart":boolean,
      /**  Create part method  */  
   "CrtPartUsing":string,
      /**  Create New Part In Quote Entry  */  
   "InQuoting":boolean,
      /**  Automatically create a new part number  */  
   "AutoCrtPart":boolean,
      /**  Do not prompt user if part exists  */  
   "NotUnique":boolean,
      /**  Create New Part In Sales Order Entry  */  
   "InOrderEntry":boolean,
      /**  Create New Part In Job Entry  */  
   "InJobEntry":boolean,
      /**  Create Bill of Material  */  
   "CreateBOM":boolean,
      /**  Create Part at zero cost  */  
   "ZeroCost":boolean,
      /**  Create Smart String in part description  */  
   "CrtPartDesc":boolean,
      /**  File Name  */  
   "FileName":string,
      /**  Added to provide backward compatibility to previous releases.  */  
   "SingleLevelConf":boolean,
      /**  Indicates if the input values should be saved.  */  
   "SaveInputValues":boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   "SetPartNumOnly":boolean,
      /**  Comments  */  
   "Comments":string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   "AprvRev":boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   "EntprsConf":boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   "Synchronize":boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   "DispConfSummary":boolean,
      /**  Part creation comments  */  
   "PartComments":string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   "CompPricing":boolean,
      /**  External configurator  */  
   "ExtConfig":boolean,
      /**  External company ID  */  
   "ExtMfgCompID":string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   "TestPlan":boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   "MarkMtlGlb":boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   "SIValuesUseQt":boolean,
      /**  This field will enable smart string processing for this configuration  */  
   "AllowSmartString":boolean,
   "InDemandEntry":boolean,
      /**  Demand Price Code  */  
   "DemandPCode":string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   "AllAltMethods":boolean,
      /**  AllowReconPO  */  
   "AllowReconPO":boolean,
      /**  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  */  
   "CompPricingJobMethod":boolean,
      /**  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  */  
   "CreateRev":boolean,
      /**  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  */  
   "DefaultECO":string,
      /**  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  */  
   "GenerateMethod":boolean,
      /**  PromptForConfig  */  
   "PromptForConfig":boolean,
      /**  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  */  
   "PromptForCheckout":boolean,
      /**  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  */  
   "RemoveLink":boolean,
      /**  SIValuesUseGenMethod  */  
   "SIValuesUseGenMethod":boolean,
      /**  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  */  
   "UseSavedLayout":boolean,
      /**  Description  */  
   "Description":string,
      /**  ConfigType  */  
   "ConfigType":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  RegenConfig  */  
   "RegenConfig":boolean,
      /**  CreateNewConfigID  */  
   "CreateNewConfigID":boolean,
      /**  UseTemplatePartDefaults  */  
   "UseTemplatePartDefaults":boolean,
      /**  DefaultPartNum  */  
   "DefaultPartNum":string,
      /**  DefaultRevisionNum  */  
   "DefaultRevisionNum":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  */  
   "AttrClassID":string,
      /**  RecycleJobs  */  
   "RecycleJobs":boolean,
      /**  ClientDeployedToEWCDate  */  
   "ClientDeployedToEWCDate":string,
      /**  EWCClientSyncRequired  */  
   "EWCClientSyncRequired":boolean,
      /**  ShrinkFieldProperties  */  
   "ShrinkFieldProperties":boolean,
      /**  Kinetic  */  
   "Kinetic":boolean,
      /**  KBConfigID  */  
   "KBConfigID":number,
      /**  KBConfigDesc  */  
   "KBConfigDesc":string,
      /**  The available inputs available for use in the smart string  */  
   "AvailSmartStringInputs":string,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   "ECOGroup":string,
      /**  Indicates if the configurator has inputs in its design.  */  
   "HasInputs":boolean,
   "IsValidPwd":boolean,
      /**  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  */  
   "ResetPCInputsAttributes":boolean,
      /**  True if the PartRev record is approved  */  
   "RevApproved":boolean,
      /**  A sample smart string constructed from the smart string options  */  
   "SampleSmartString":string,
      /**  The inputs that have been selected for use in the smart string  */  
   "SelectedSmartStringInputs":string,
      /**  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  */  
   "UpdateCreatePartTarget":boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   "AuditDesc":string,
      /**  If true then detail fields other than Approved can be updated  */  
   "CanUpdate":boolean,
      /**  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  */  
   "EnableCPQPartCreation":boolean,
   "BitFlag":number,
   "PartNumTypeCode":string,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
   "PartNumTrackDimension":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumPartDescription":string,
   "PartNumSellingFactor":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QBuildMappingRow{
      /**  Company  */  
   "Company":string,
      /**  Configuration ID  */  
   "ConfigID":string,
      /**  Input Name  */  
   "InputName":string,
      /**  This is the object name.  */  
   "ObjName":string,
      /**  This is the name of the object parameter.  */  
   "ObjParameter":string,
      /**  Name of the input mapped to this object parameter.  */  
   "MappedInputName":string,
      /**  This is the data type of the object parameter.  */  
   "ObjParameterDataType":string,
      /**  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  */  
   "ObjParameterInitValue":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "DataType":string,
   "PageSeq":number,
   "BitFlag":number,
   "QBuildObjObjType":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_QBuildObjRow{
      /**  Company  */  
   "Company":string,
      /**  ConfigID  */  
   "ConfigID":string,
      /**  Input Name  */  
   "InputName":string,
      /**  This is the name of the object.  */  
   "ObjName":string,
      /**  This is the object type.  */  
   "ObjType":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "PageSeq":number,
   "DataType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param configId
      @param pageSeq
      @param ds
   */  
export interface CreateNewEmptyPcInputs_input{
      /**  Configuration ID  */  
   configId:string,
      /**  Page Sequence where the input is being placed  */  
   pageSeq:number,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface CreateNewEmptyPcInputs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configId
      @param pageSeq
      @param controlType
      @param designControlType
      @param ds
   */  
export interface CreateNewPcInputs_input{
      /**  Configuration ID  */  
   configId:string,
      /**  Page Sequence where the input is being placed.  */  
   pageSeq:number,
      /**  Control type of the input, this is the control type used at runtime.  */  
   controlType:string,
      /**  Control type used at design time, depending on this value the data type will be defaulted.  */  
   designControlType:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface CreateNewPcInputs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface DeleteByID_input{
   configID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ConfigID
      @param InputName
      @param ConfigurationDesignTS
   */  
export interface DeleteQBuildImage_input{
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Name of control that is of type QBuild  */  
   InputName:string,
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface DeleteQBuildImage_output{
parameters : {
      /**  output parameters  */  
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configID
      @param targetInputName
      @param ruleSeq
      @param newRuleDesc
      @param ds
   */  
export interface DuplicateInputRule_input{
      /**  Configuration used.  */  
   configID:string,
      /**  targetInputName used.  */  
   targetInputName:string,
      /**  ruleSeq used.  */  
   ruleSeq:number,
      /**  new rule description to use.  */  
   newRuleDesc:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface DuplicateInputRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

export interface Erp_Tablesets_ConfigurationDesignListTableset{
   PcStatusList:Erp_Tablesets_PcStatusListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ConfigurationDesignTableset{
   PcStatus:Erp_Tablesets_PcStatusRow[],
   PcPage:Erp_Tablesets_PcPageRow[],
   PcInputs:Erp_Tablesets_PcInputsRow[],
   PcInputsLayerHeader:Erp_Tablesets_PcInputsLayerHeaderRow[],
   PcInputsLayerDetail:Erp_Tablesets_PcInputsLayerDetailRow[],
   PcDynLst:Erp_Tablesets_PcDynLstRow[],
   PcDynLstCriteria:Erp_Tablesets_PcDynLstCriteriaRow[],
   PcDynLstExpr:Erp_Tablesets_PcDynLstExprRow[],
   PcDynLstParams:Erp_Tablesets_PcDynLstParamsRow[],
   PcInputsExpr:Erp_Tablesets_PcInputsExprRow[],
   PcInputsRule:Erp_Tablesets_PcInputsRuleRow[],
   PcInputsRuleDef:Erp_Tablesets_PcInputsRuleDefRow[],
   QBuildObj:Erp_Tablesets_QBuildObjRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   PcPageExpr:Erp_Tablesets_PcPageExprRow[],
   PcStatusExpr:Erp_Tablesets_PcStatusExprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcDynLstCriteriaRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The unique sequence id for the dynamic list.  */  
   ListSeq:number,
      /**  Criteria sequence number to make this record unique.  */  
   CriteriaSeq:number,
      /**  Column name to use for BAQ query criteria  */  
   ColumnName:string,
      /**  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  */  
   Condition:string,
      /**  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  */  
   ValueFrom:string,
      /**  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  */  
   ColumnValue:string,
      /**  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  */  
   Operator:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  UseEmptyValue  */  
   UseEmptyValue:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  */  
   ColumnType:string,
      /**  Page Sequence where the parent input exists  */  
   PageSeq:number,
      /**  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  */  
   ValueFromDisplay:string,
      /**  BAQ Program Name  */  
   BAQProgramName:string,
   BitFlag:number,
   PartNumPricePerCode:string,
   PartNumSalesUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumTrackLots:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Input Name  */  
   InputName:string,
      /**  The unique sequence id for the dynamic list.  */  
   ListSeq:number,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  The On Leave expression for the control.  */  
   Expression:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstParamsRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  InputName  */  
   InputName:string,
      /**  ListSeq  */  
   ListSeq:number,
      /**  ParamName  */  
   ParamName:string,
      /**  ParamConst  */  
   ParamConst:boolean,
      /**  ParamValue  */  
   ParamValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Page Sequence where the parent input exists  */  
   PageSeq:number,
      /**  This is the type of Parameter.  */  
   ParamType:string,
   ParamInput:string,
   ParamModifier:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcDynLstRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Input Name  */  
   InputName:string,
      /**  The unique sequence id for the dynamic list.  */  
   ListSeq:number,
      /**  Contains the logical expression as to when the list is used.  */  
   Condition:string,
      /**  Contains the combo-box list items that are used when the condition is true.  */  
   ListItems:string,
      /**  The Initial value for the list.  */  
   InitVal:string,
      /**  If TRUE then the dynamic list will be built by running a BAQ program  */  
   BAQRunProgram:boolean,
      /**  The BAQ program name used for building the dynamic list  */  
   BAQProgramName:string,
      /**  Value that will be displayed from the BAQ  */  
   BAQDispValue:string,
      /**  The input value for the BAQ  */  
   BAQInputVal:string,
      /**  Defines the type of dynamic list from Static, BAQ, Program, etc.  */  
   ListDataSource:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  RunTblLookup  */  
   RunTblLookup:boolean,
      /**  TblLookupID  */  
   TblLookupID:string,
      /**  TblLookupFunc  */  
   TblLookupFunc:string,
      /**  RunUserDefined  */  
   RunUserDefined:string,
      /**  UserDefinedName  */  
   UserDefinedName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SortOrder  */  
   SortOrder:string,
      /**  SubReturnColumn  */  
   SubReturnColumn:string,
      /**  ScriptCondition  */  
   ScriptCondition:string,
      /**  Reserved for Future Development  */  
   AttributeID:string,
      /**  Identifies if Script expressions are valid for Dynamic List Conditions  */  
   EnableScript:boolean,
   EntprsConf:boolean,
   PageSeq:number,
      /**  Either Client or Server where the UD Method is executed.  */  
   UserDefinedFunctionType:string,
      /**  Storing the Return Type for the selected User Defined Method.  */  
   UserDefinedReturnType:string,
      /**  If true then details on this record can be updated  */  
   CanUpdate:boolean,
   BitFlag:number,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  The On Leave expression for the control.  */  
   Expression:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerDetailRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  InputName  */  
   InputName:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
      /**  LayerSeq  */  
   LayerSeq:number,
      /**  LayerName  */  
   LayerName:string,
      /**  LayerDesc  */  
   LayerDesc:string,
      /**  Order in which layers are placed on the base image.  */  
   ZIndex:number,
      /**  ImageID  */  
   ImageID:string,
      /**  Png type is supported.  */  
   FileType:string,
      /**  Free form text enabling users to categorize layers  */  
   Category:string,
      /**  Width of image  */  
   Width:number,
      /**  Height of image  */  
   Height:number,
      /**  Reserved for Future Development  */  
   xPos:number,
      /**  Reserved for Future Development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerHeaderRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input name this header is assigned.  */  
   InputName:string,
      /**  Image Layer ID.  */  
   ImageLayerID:string,
      /**  File name of the image to be retrieved from the Image URL.  */  
   ImageID:string,
      /**  Description  */  
   Description:string,
      /**  The URL location of the image.  */  
   ImageURL:string,
      /**  File types png and jpg are supported.  */  
   FileType:string,
      /**  Image Width  */  
   Width:number,
      /**  Image height  */  
   Height:number,
      /**  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  */  
   Version:number,
      /**  Reserved for future development  */  
   xPos:number,
      /**  Reserved for future development  */  
   yPos:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerIDWhereUsedRow{
   Company:string,
   ConfigID:string,
   ImageLayerID:string,
   InputName:string,
   RefreshLayerDetails:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsLayerIDWhereUsedTableset{
   PcInputsLayerIDWhereUsed:Erp_Tablesets_PcInputsLayerIDWhereUsedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcInputsRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  Actual name of the control.  Used to identify the control through out the system.  */  
   InputName:string,
      /**  The order that the tab function will step through the inputs.  */  
   TabOrder:number,
      /**  The type of data that can be stored in the control.  */  
   DataType:string,
      /**  The format for which the data will be stored.  */  
   FormatString:string,
      /**  The initial value for the control.  */  
   InitVal:string,
      /**  The popup help message that appears when the cursor is over the control.  */  
   StatusText:string,
      /**  Determines if the contol must have a value before leaving the widget or the page of controls.  */  
   Required:boolean,
      /**  On what page does the control exist.  */  
   PageSeq:number,
      /**  The control's label.  */  
   SideLabel:string,
      /**  The pixel position for the x axis.  */  
   xPos:number,
      /**  The pixel position for the Y axis.  */  
   yPos:number,
      /**  The pixel width of the control.  */  
   pWidth:number,
      /**  The pixel height of the control.  */  
   pHeight:number,
      /**  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  */  
   ControlType:string,
      /**  The prompt when expression for the widget.  */  
   PromptWhen:string,
      /**  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  */  
   ListItems:string,
      /**  The starting decimal for a validated numeric fill-in.  */  
   StartDec:number,
      /**  The ending decimal for a validated numeric fill-in.  */  
   EndDec:number,
      /**  The precision used to determine the list of numbers to validate against.  */  
   IncrPrec:number,
      /**  The starting date for a validated date fill-in.  */  
   StartDate:string,
      /**  The ending date for a validated date fill-in.  */  
   EndDate:string,
      /**  The list of valid responses for a validated string input.  */  
   ValList:string,
      /**  If the control is a radio-set, is it a horizontal or vertical radio-set.  */  
   Horizontal:boolean,
      /**  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  */  
   IsGlobal:boolean,
      /**  The On Leave expression for the control.  */  
   OnLeave:string,
      /**  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  */  
   WebInputName:string,
      /**  The label that will be used for the input when displaying a configuration summary.  */  
   SummaryLabel:string,
      /**  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  */  
   DLRunProgram:boolean,
      /**  The Progress program used for building a dynamic list.  */  
   DLProgramName:string,
      /**  The inputs used for the Progress program used for building a dynamic list.  */  
   DLProgramInputs:string,
      /**  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  */  
   SourceDBRecid:string,
      /**  If TRUE then this input will not be shown in the configuration summary  */  
   HideInSummary:boolean,
      /**  Additional field to add On Leave expressions to this control  */  
   OnLeave2:string,
      /**  If true, the input will not be displayed on the input page  */  
   Invisible:boolean,
      /**  Comments describing the input  */  
   Comments:string,
      /**  Global Input Variable  */  
   GlobalInputVar:boolean,
      /**  Global Input Variable Name  */  
   GlbInputVarName:string,
      /**  Do not display input in Summary  */  
   NoDispSummary:boolean,
      /**  If true, allows entry to link input to inspection attribute data  */  
   ExternalRef:boolean,
      /**  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  */  
   AttributeID:string,
      /**  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMinValue:boolean,
      /**  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseMaxValue:boolean,
      /**  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseIncrValue:boolean,
      /**  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseInitVal:boolean,
      /**  Setting to true will use the Tool Tip value from the specification detail table.  */  
   UseToolTip:boolean,
      /**  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseScreenLabel:boolean,
      /**  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  */  
   UseListValues:boolean,
      /**  Defines the sequence of this input value in a smart part string sent for automatic processing.  */  
   SmartPartSeq:number,
      /**  Defines a starting position for the value of this input in a smart string  */  
   SmartStringStart:number,
      /**  Defines an ending position for the value of this input in a smart string  */  
   SmartStringEnd:number,
      /**  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  */  
   ShowDistinct:boolean,
      /**  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  */  
   DesignControlType:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ReadOnly  */  
   ReadOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AutoSizeList  */  
   AutoSizeList:boolean,
      /**  ListWidth  */  
   ListWidth:number,
      /**  ImageSource  */  
   ImageSource:string,
      /**  ImageLayerID  */  
   ImageLayerID:string,
   AllowSmartString:boolean,
   AttributeDescription:string,
      /**  If true then fields on the record may be updated  */  
   CanUpdate:boolean,
   Content:string,
      /**  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  */  
   DispCharVal:string,
   DspPageSeq:number,
      /**  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  */  
   FullInputName:string,
   ImageMapping:boolean,
      /**  The initial value of a date field  */  
   InitDate:string,
      /**  The initial value of a decimal input  */  
   InitDecimal:number,
      /**  The initial value for a logical input  */  
   InitLogical:boolean,
      /**  Indicates whether or not Input Rules have been defined.  */  
   InputRules:boolean,
      /**  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  */  
   InputType:string,
   IsGlobalInputVar:boolean,
   OnLaunch:string,
   PageDisplaySeq:number,
      /**  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  */  
   PcDynLstCount:number,
   ReadOnlyExpression:string,
   TestPlan:boolean,
   ImageURL:string,
   BitFlag:number,
   PartNumTrackDimension:boolean,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsRuleDefRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  The Input that is updated based upon the rule definition.  */  
   TargetInputName:string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   RuleSeq:number,
      /**  The order in which these definitions are interrogated.  */  
   SeqNum:number,
      /**  Input whose value is used in determining if this rule is executed.  */  
   SourceInputName:string,
      /**  Reserved for future development.  Defaults to Value.  */  
   SourceInputProperty:string,
      /**  SourceCharacterValue  */  
   SourceCharacterValue:string,
      /**  SourceIntegerValue  */  
   SourceIntegerValue:number,
      /**  SourceDecimalValue  */  
   SourceDecimalValue:number,
      /**  SourceDateValue  */  
   SourceDateValue:string,
      /**  SourceLogicalValue  */  
   SourceLogicalValue:boolean,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   ProcessSeq:number,
      /**  Reserved for future development.  */  
   LeftP:string,
      /**  Reserved for future development.  */  
   RightP:string,
      /**  Defaults to And and permits users to use more than one input in the rule.  */  
   AndOr:string,
      /**  Comparison operator used when evaluating the rule. Valid value at this time is equals.  */  
   CompOp:string,
      /**  Reserved for future development.  Defaults to false.  */  
   Neg:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ListValues:string,
   SourceValue:string,
      /**  Input type valid values Label, Character, Numeric, Date, ComboBox  */  
   InputType:string,
   BitFlag:number,
   SourcePcInputsDesignControlType:string,
   SourcePcInputsFormatString:string,
   SourcePcInputsListItems:string,
   SourcePcInputsDataType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsRuleRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  The Input that is updated based upon the rule definition.  */  
   TargetInputName:string,
      /**  Internal column used to keep the rows unique and permit the rule to be resequenced.  */  
   RuleSeq:number,
      /**  Enter text that describes what the rule does.  */  
   RuleDesc:string,
      /**  Reserved for future development.  Defaults to Value.  */  
   TargetInputProperty:string,
      /**  The new value of the input when this rule executes.  */  
   TargetInputValue:string,
      /**  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  */  
   ProcessSeq:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Associated Rule Defintion descriptions  */  
   DefinitionDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcInputsTableset{
   PcInputs:Erp_Tablesets_PcInputsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PcPageExprRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The configuration page sequence.  */  
   PageSeq:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Sequence Number.  */  
   SeqNum:number,
      /**  Ex: Customization, Personalization  */  
   TypeCode:string,
      /**  The On Leave expression for the control.  */  
   Expression:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcPageRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
      /**  The configuration page sequence.  */  
   PageSeq:number,
      /**  The title of the configuration page.  */  
   PageTitle:string,
      /**  The prompt when expression for the page.  */  
   PromptWhen:string,
      /**  The On Leave expression for the page  */  
   OnLeave:string,
      /**  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  */  
   SkipOnLeaveOPL:boolean,
      /**  Additional field to add OnLeave expressions to the page  */  
   OnLeave2:string,
      /**  Comments  */  
   Comments:string,
      /**  Process dynamic lists before on leave expressions for this page  */  
   ProcessDynLstFirst:boolean,
      /**  Only process dynamic lists with higher tab sequences  */  
   DynLstHigher:boolean,
      /**  Skip processing page on leave on load  */  
   SkipPageProcessOL:boolean,
      /**  Do not process on leave expressions when page loads  */  
   SkipPageNoInputs:boolean,
      /**  Do not process on leave expressions when leaving pages  */  
   SkipOnLeaveOPE:boolean,
      /**  Width of panel  */  
   pWidth:number,
      /**  Height of panel  */  
   pHeight:number,
      /**  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  */  
   DisplaySeq:number,
      /**  ConfigID  */  
   ConfigID:string,
      /**  ReadOnly  */  
   ReadOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CanUpdate:boolean,
   FirstPage:boolean,
   TestPlan:boolean,
   ReadOnlyExpression:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusExprRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  TypeCode  */  
   TypeCode:string,
      /**  SeqNum  */  
   SeqNum:number,
      /**  Expression  */  
   Expression:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number.  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Configurator Approval Status  */  
   Approved:boolean,
      /**  Date the configuration was approved.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Smart String Style  */  
   StringStyle:string,
      /**  Smart String Seperator character  */  
   Separator:string,
      /**  Smart String Digit Structure  */  
   NumberFormat:string,
      /**  Smart String Starting Sequence  */  
   StartNumber:number,
      /**  Part Creation Method  */  
   CrtCustPart:boolean,
      /**  Smart String preface with part numbner  */  
   PrefacePart:boolean,
      /**  Configurator Version  */  
   ConfigVersion:number,
      /**  Quote Price Code  */  
   QuotePCode:string,
      /**  Order Price Code  */  
   OrderPCode:string,
      /**  OrdQuoCom  */  
   OrdQuoCom:boolean,
      /**  JobPickCom  */  
   JobPickCom:boolean,
      /**  ShipCom  */  
   ShipCom:boolean,
      /**  InvCom  */  
   InvCom:boolean,
      /**  Create Part Flag  */  
   CreatePart:boolean,
      /**  Create part method  */  
   CrtPartUsing:string,
      /**  Create New Part In Quote Entry  */  
   InQuoting:boolean,
      /**  Automatically create a new part number  */  
   AutoCrtPart:boolean,
      /**  Do not prompt user if part exists  */  
   NotUnique:boolean,
      /**  Create New Part In Sales Order Entry  */  
   InOrderEntry:boolean,
      /**  Create New Part In Job Entry  */  
   InJobEntry:boolean,
      /**  Create Bill of Material  */  
   CreateBOM:boolean,
      /**  Create Part at zero cost  */  
   ZeroCost:boolean,
      /**  Create Smart String in part description  */  
   CrtPartDesc:boolean,
      /**  File Name  */  
   FileName:string,
      /**  Added to provide backward compatibility to previous releases.  */  
   SingleLevelConf:boolean,
      /**  Indicates if the input values should be saved.  */  
   SaveInputValues:boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   SetPartNumOnly:boolean,
      /**  Comments  */  
   Comments:string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   AprvRev:boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   EntprsConf:boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   Synchronize:boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   DispConfSummary:boolean,
      /**  Part creation comments  */  
   PartComments:string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   CompPricing:boolean,
      /**  External configurator  */  
   ExtConfig:boolean,
      /**  External company ID  */  
   ExtMfgCompID:string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   TestPlan:boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   MarkMtlGlb:boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   SIValuesUseQt:boolean,
      /**  This field will enable smart string processing for this configuration  */  
   AllowSmartString:boolean,
   InDemandEntry:boolean,
      /**  Demand Price Code  */  
   DemandPCode:string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   AllAltMethods:boolean,
      /**  SIValuesUseGenMethod  */  
   SIValuesUseGenMethod:boolean,
      /**  Description  */  
   Description:string,
      /**  ConfigType  */  
   ConfigType:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ShrinkFieldProperties  */  
   ShrinkFieldProperties:boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   AuditDesc:string,
      /**  A sample smart string constructed from the smart string options  */  
   SampleSmartString:string,
      /**  The available inputs available for use in the smart string  */  
   AvailSmartStringInputs:string,
      /**  The inputs that have been selected for use in the smart string  */  
   SelectedSmartStringInputs:string,
      /**  True if the PartRev record is approved  */  
   RevApproved:boolean,
      /**  If true then detail fields other than Approved can be updated  */  
   CanUpdate:boolean,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   ECOGroup:string,
   IsValidPwd:boolean,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PcStatusRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Part Number.  */  
   PartNum:string,
      /**  Revision Number of the associated configurator  */  
   RevisionNum:string,
      /**  Configurator Approval Status  */  
   Approved:boolean,
      /**  Date the configuration was approved.  */  
   ApprovedDate:string,
      /**  UserID who approved the revision.  Not maintainable by the user.  */  
   ApprovedBy:string,
      /**  Smart String Style  */  
   StringStyle:string,
      /**  Smart String Seperator character  */  
   Separator:string,
      /**  Smart String Digit Structure  */  
   NumberFormat:string,
      /**  Smart String Starting Sequence  */  
   StartNumber:number,
      /**  Part Creation Method  */  
   CrtCustPart:boolean,
      /**  Smart String preface with part numbner  */  
   PrefacePart:boolean,
      /**  Configurator Version  */  
   ConfigVersion:number,
      /**  Quote Price Code  */  
   QuotePCode:string,
      /**  Order Price Code  */  
   OrderPCode:string,
      /**  OrdQuoCom  */  
   OrdQuoCom:boolean,
      /**  JobPickCom  */  
   JobPickCom:boolean,
      /**  ShipCom  */  
   ShipCom:boolean,
      /**  InvCom  */  
   InvCom:boolean,
      /**  Create Part Flag  */  
   CreatePart:boolean,
      /**  Create part method  */  
   CrtPartUsing:string,
      /**  Create New Part In Quote Entry  */  
   InQuoting:boolean,
      /**  Automatically create a new part number  */  
   AutoCrtPart:boolean,
      /**  Do not prompt user if part exists  */  
   NotUnique:boolean,
      /**  Create New Part In Sales Order Entry  */  
   InOrderEntry:boolean,
      /**  Create New Part In Job Entry  */  
   InJobEntry:boolean,
      /**  Create Bill of Material  */  
   CreateBOM:boolean,
      /**  Create Part at zero cost  */  
   ZeroCost:boolean,
      /**  Create Smart String in part description  */  
   CrtPartDesc:boolean,
      /**  File Name  */  
   FileName:string,
      /**  Added to provide backward compatibility to previous releases.  */  
   SingleLevelConf:boolean,
      /**  Indicates if the input values should be saved.  */  
   SaveInputValues:boolean,
      /**  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  */  
   SetPartNumOnly:boolean,
      /**  Comments  */  
   Comments:string,
      /**  If true, revision will also be approved when configuration is approved.  */  
   AprvRev:boolean,
      /**  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  */  
   EntprsConf:boolean,
      /**  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  */  
   Synchronize:boolean,
      /**  If true, the configuration summary grid will be displayed when reconfiguring a part  */  
   DispConfSummary:boolean,
      /**  Part creation comments  */  
   PartComments:string,
      /**  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  */  
   CompPricing:boolean,
      /**  External configurator  */  
   ExtConfig:boolean,
      /**  External company ID  */  
   ExtMfgCompID:string,
      /**  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  */  
   TestPlan:boolean,
      /**  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  */  
   MarkMtlGlb:boolean,
      /**  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  */  
   SIValuesUseQt:boolean,
      /**  This field will enable smart string processing for this configuration  */  
   AllowSmartString:boolean,
   InDemandEntry:boolean,
      /**  Demand Price Code  */  
   DemandPCode:string,
      /**  If checked, all alternate methods of the part revision will be created  */  
   AllAltMethods:boolean,
      /**  AllowReconPO  */  
   AllowReconPO:boolean,
      /**  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  */  
   CompPricingJobMethod:boolean,
      /**  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  */  
   CreateRev:boolean,
      /**  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  */  
   DefaultECO:string,
      /**  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  */  
   GenerateMethod:boolean,
      /**  PromptForConfig  */  
   PromptForConfig:boolean,
      /**  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  */  
   PromptForCheckout:boolean,
      /**  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  */  
   RemoveLink:boolean,
      /**  SIValuesUseGenMethod  */  
   SIValuesUseGenMethod:boolean,
      /**  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  */  
   UseSavedLayout:boolean,
      /**  Description  */  
   Description:string,
      /**  ConfigType  */  
   ConfigType:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  RegenConfig  */  
   RegenConfig:boolean,
      /**  CreateNewConfigID  */  
   CreateNewConfigID:boolean,
      /**  UseTemplatePartDefaults  */  
   UseTemplatePartDefaults:boolean,
      /**  DefaultPartNum  */  
   DefaultPartNum:string,
      /**  DefaultRevisionNum  */  
   DefaultRevisionNum:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  */  
   AttrClassID:string,
      /**  RecycleJobs  */  
   RecycleJobs:boolean,
      /**  ClientDeployedToEWCDate  */  
   ClientDeployedToEWCDate:string,
      /**  EWCClientSyncRequired  */  
   EWCClientSyncRequired:boolean,
      /**  ShrinkFieldProperties  */  
   ShrinkFieldProperties:boolean,
      /**  Kinetic  */  
   Kinetic:boolean,
      /**  KBConfigID  */  
   KBConfigID:number,
      /**  KBConfigDesc  */  
   KBConfigDesc:string,
      /**  The available inputs available for use in the smart string  */  
   AvailSmartStringInputs:string,
      /**  If not null, indicates the revision is checked out to an ECO group.  */  
   ECOGroup:string,
      /**  Indicates if the configurator has inputs in its design.  */  
   HasInputs:boolean,
   IsValidPwd:boolean,
      /**  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  */  
   ResetPCInputsAttributes:boolean,
      /**  True if the PartRev record is approved  */  
   RevApproved:boolean,
      /**  A sample smart string constructed from the smart string options  */  
   SampleSmartString:string,
      /**  The inputs that have been selected for use in the smart string  */  
   SelectedSmartStringInputs:string,
      /**  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  */  
   UpdateCreatePartTarget:boolean,
      /**  The change description to use for the PcAudit when approving a configuration  */  
   AuditDesc:string,
      /**  If true then detail fields other than Approved can be updated  */  
   CanUpdate:boolean,
      /**  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  */  
   EnableCPQPartCreation:boolean,
   BitFlag:number,
   PartNumTypeCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumPartDescription:string,
   PartNumSellingFactor:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildDrawingObjectsRow{
   Company:string,
   ConfigID:string,
   InputName:string,
   ObjName:string,
   ObjParameter:string,
   ObjType:string,
   ObjParameterDataType:string,
   ObjParameterInitValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildDrawingObjectsTableset{
   QBuildDrawingObjects:Erp_Tablesets_QBuildDrawingObjectsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_QBuildMappingRow{
      /**  Company  */  
   Company:string,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  This is the object name.  */  
   ObjName:string,
      /**  This is the name of the object parameter.  */  
   ObjParameter:string,
      /**  Name of the input mapped to this object parameter.  */  
   MappedInputName:string,
      /**  This is the data type of the object parameter.  */  
   ObjParameterDataType:string,
      /**  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  */  
   ObjParameterInitValue:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   DataType:string,
   PageSeq:number,
   BitFlag:number,
   QBuildObjObjType:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QBuildObjRow{
      /**  Company  */  
   Company:string,
      /**  ConfigID  */  
   ConfigID:string,
      /**  Input Name  */  
   InputName:string,
      /**  This is the name of the object.  */  
   ObjName:string,
      /**  This is the object type.  */  
   ObjType:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   PageSeq:number,
   DataType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QueryFieldListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence  */  
   Seq:number,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Data Type  */  
   DataType:string,
      /**  Description  */  
   Description:string,
      /**  External  */  
   External:boolean,
      /**  IsCalculated  */  
   IsCalculated:boolean,
      /**  Formula  */  
   Formula:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Label  */  
   FieldLabel:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
      /**  Like Data Field Sequence  */  
   LikeDataFieldSeq:number,
      /**  Aggregation  */  
   Aggregation:string,
      /**  IsGroupBy  */  
   IsGroupBy:boolean,
      /**  Use Like  */  
   UseLike:boolean,
      /**  Like Data Field Name  */  
   LikeDataFieldName:string,
      /**  Wheither field can be updated  */  
   Updatable:boolean,
      /**  Raise event on update  */  
   RaiseEvent:boolean,
      /**  ID of Quick Search assigned to this query field  */  
   QuickSearchID:string,
      /**  This flag tells whether this display field is used as source of distinct values for drop down list in IW  */  
   DropDown:boolean,
      /**  Initial expression for updatable field, filled on UBAQ.GetNew  */  
   UpdInitExpression:string,
      /**  Alias  */  
   Alias:string,
      /**  IsRequired  */  
   IsRequired:boolean,
      /**  IsReadOnly  */  
   IsReadOnly:boolean,
      /**  DefaultValue  */  
   DefaultValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DisplayName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_QueryFieldListTableset{
   QueryFieldList:Erp_Tablesets_QueryFieldListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtConfigurationDesignTableset{
   PcStatus:Erp_Tablesets_PcStatusRow[],
   PcPage:Erp_Tablesets_PcPageRow[],
   PcInputs:Erp_Tablesets_PcInputsRow[],
   PcInputsLayerHeader:Erp_Tablesets_PcInputsLayerHeaderRow[],
   PcInputsLayerDetail:Erp_Tablesets_PcInputsLayerDetailRow[],
   PcDynLst:Erp_Tablesets_PcDynLstRow[],
   PcDynLstCriteria:Erp_Tablesets_PcDynLstCriteriaRow[],
   PcDynLstExpr:Erp_Tablesets_PcDynLstExprRow[],
   PcDynLstParams:Erp_Tablesets_PcDynLstParamsRow[],
   PcInputsExpr:Erp_Tablesets_PcInputsExprRow[],
   PcInputsRule:Erp_Tablesets_PcInputsRuleRow[],
   PcInputsRuleDef:Erp_Tablesets_PcInputsRuleDefRow[],
   QBuildObj:Erp_Tablesets_QBuildObjRow[],
   QBuildMapping:Erp_Tablesets_QBuildMappingRow[],
   PcPageExpr:Erp_Tablesets_PcPageExprRow[],
   PcStatusExpr:Erp_Tablesets_PcStatusExprRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param configID
      @param proposedValue
   */  
export interface ExistsProposedInputName_input{
      /**  Configuration ID  */  
   configID:string,
      /**  Proposed Value  */  
   proposedValue:string,
}

export interface ExistsProposedInputName_output{
   returnObj:boolean,
}

   /** Required : 
      @param attributeID
   */  
export interface GetAttributeDesc_input{
      /**  Target Attribute ID  */  
   attributeID:string,
}

export interface GetAttributeDesc_output{
      /**  Inspection Attribute Description  */  
   returnObj:string,
}

   /** Required : 
      @param searchExpression
   */  
export interface GetBAQDisplayColumnList_input{
      /**  Search filter expression  */  
   searchExpression:string,
}

export interface GetBAQDisplayColumnList_output{
   returnObj:Erp_Tablesets_QueryFieldListTableset[],
}

   /** Required : 
      @param configID
   */  
export interface GetByID_input{
   configID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ConfigurationDesignTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ConfigurationDesignTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface GetDefaultListItems_output{
   returnObj:string,
}

   /** Required : 
      @param schemaName
      @param tableName
      @param attrClassID
      @param attributeID
   */  
export interface GetDynAttributeDesc_input{
      /**  Schema Name  */  
   schemaName:string,
      /**  Related to table Name  */  
   tableName:string,
      /**  Part Attribute Class ID to use to validate the Attribute ID  */  
   attrClassID:string,
      /**  Target Attribute ID  */  
   attributeID:string,
}

export interface GetDynAttributeDesc_output{
      /**  Part Attribute Description  */  
   returnObj:string,
}

   /** Required : 
      @param searchExpression
   */  
export interface GetInputList_input{
      /**  Seatch expression  */  
   searchExpression:string,
}

export interface GetInputList_output{
   returnObj:Erp_Tablesets_PcInputsTableset[],
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
   returnObj:Erp_Tablesets_ConfigurationDesignListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param listSeq
   */  
export interface GetNewPcDynLstCriteria_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   listSeq:number,
}

export interface GetNewPcDynLstCriteria_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param listSeq
      @param typeCode
   */  
export interface GetNewPcDynLstExpr_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   listSeq:number,
   typeCode:string,
}

export interface GetNewPcDynLstExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param listSeq
   */  
export interface GetNewPcDynLstParams_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   listSeq:number,
}

export interface GetNewPcDynLstParams_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
   */  
export interface GetNewPcDynLst_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
}

export interface GetNewPcDynLst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param typeCode
   */  
export interface GetNewPcInputsExpr_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   typeCode:string,
}

export interface GetNewPcInputsExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param imageLayerID
   */  
export interface GetNewPcInputsLayerDetail_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   imageLayerID:string,
}

export interface GetNewPcInputsLayerDetail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
   */  
export interface GetNewPcInputsLayerHeader_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
}

export interface GetNewPcInputsLayerHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param targetInputName
      @param ruleSeq
   */  
export interface GetNewPcInputsRuleDef_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   targetInputName:string,
   ruleSeq:number,
}

export interface GetNewPcInputsRuleDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param targetInputName
   */  
export interface GetNewPcInputsRule_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   targetInputName:string,
}

export interface GetNewPcInputsRule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcInputs_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
}

export interface GetNewPcInputs_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param pageSeq
      @param typeCode
   */  
export interface GetNewPcPageExpr_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   pageSeq:number,
   typeCode:string,
}

export interface GetNewPcPageExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
   */  
export interface GetNewPcPage_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
}

export interface GetNewPcPage_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param typeCode
   */  
export interface GetNewPcStatusExpr_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   typeCode:string,
}

export interface GetNewPcStatusExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPcStatus_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface GetNewPcStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
      @param objName
   */  
export interface GetNewQBuildMapping_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
   objName:string,
}

export interface GetNewQBuildMapping_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
      @param configID
      @param inputName
   */  
export interface GetNewQBuildObj_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   configID:string,
   inputName:string,
}

export interface GetNewQBuildObj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface GetPcInputsWithLayerIDForConfiguration_input{
      /**  Configuration to retrieve the Inputs with an ImageLayerID specified.  */  
   configID:string,
}

export interface GetPcInputsWithLayerIDForConfiguration_output{
   returnObj:Erp_Tablesets_PcInputsLayerIDWhereUsedTableset[],
}

   /** Required : 
      @param whereClausePcStatus
      @param whereClausePcPage
      @param whereClausePcInputs
      @param whereClausePcInputsLayerHeader
      @param whereClausePcInputsLayerDetail
      @param whereClausePcDynLst
      @param whereClausePcDynLstCriteria
      @param whereClausePcDynLstExpr
      @param whereClausePcDynLstParams
      @param whereClausePcInputsExpr
      @param whereClausePcInputsRule
      @param whereClausePcInputsRuleDef
      @param whereClauseQBuildObj
      @param whereClauseQBuildMapping
      @param whereClausePcPageExpr
      @param whereClausePcStatusExpr
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePcStatus:string,
   whereClausePcPage:string,
   whereClausePcInputs:string,
   whereClausePcInputsLayerHeader:string,
   whereClausePcInputsLayerDetail:string,
   whereClausePcDynLst:string,
   whereClausePcDynLstCriteria:string,
   whereClausePcDynLstExpr:string,
   whereClausePcDynLstParams:string,
   whereClausePcInputsExpr:string,
   whereClausePcInputsRule:string,
   whereClausePcInputsRuleDef:string,
   whereClauseQBuildObj:string,
   whereClauseQBuildMapping:string,
   whereClausePcPageExpr:string,
   whereClausePcStatusExpr:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ConfigurationDesignTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param configID
      @param targetInputName
   */  
export interface GetSourceInputNameList_input{
      /**  Configuration used.  */  
   configID:string,
      /**  targetInputName used.  */  
   targetInputName:string,
}

export interface GetSourceInputNameList_output{
   returnObj:string,
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
      @param imageLayerID
   */  
export interface ImageLayerScriptCode_input{
   imageLayerID:string,
}

export interface ImageLayerScriptCode_output{
   returnObj:string,
}

   /** Required : 
      @param imageLayerID
   */  
export interface ImageLayerUpdateScriptCode_input{
   imageLayerID:string,
}

export interface ImageLayerUpdateScriptCode_output{
   returnObj:string,
}

   /** Required : 
      @param FileName
      @param Image
      @param RenameDuplicates
      @param UpdateDuplicates
      @param ConfigID
      @param InputName
      @param ConfigurationDesignTS
      @param ttQBuildDrawingObjectsTablesetTS
   */  
export interface ImportImagesFileStore_input{
      /**  Name of Image file  */  
   FileName:string,
      /**  byte array of the content  */  
   Image:string,
      /**  boolean indicating whether or not to rename duplicates.  */  
   RenameDuplicates:boolean,
      /**  boolean indicating whether or not to update duplicates.  */  
   UpdateDuplicates:boolean,
      /**  Configuration ID  */  
   ConfigID:string,
      /**  Input that is being updated  */  
   InputName:string,
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
   ttQBuildDrawingObjectsTablesetTS:Erp_Tablesets_QBuildDrawingObjectsTableset[],
}

export interface ImportImagesFileStore_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param inParam
   */  
export interface NumberOfDecimalPlaces_input{
      /**  Format string  */  
   inParam:string,
}

export interface NumberOfDecimalPlaces_output{
   returnObj:number,
}

   /** Required : 
      @param schemaName
      @param tableName
      @param attributeID
      @param ds
   */  
export interface OnChangeAttributeID_input{
      /**  Schema Name  */  
   schemaName:string,
      /**  Related to table Name  */  
   tableName:string,
      /**  proposed attribute ID to validate  */  
   attributeID:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeAttributeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param schemaName
      @param tableName
      @param attributeID
      @param ds
   */  
export interface OnChangeDynAttributeID_input{
      /**  Schema Name  */  
   schemaName:string,
      /**  Related to table Name  */  
   tableName:string,
      /**  proposed attribute ID to validate  */  
   attributeID:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeDynAttributeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   warningMessage:string,
}
}

   /** Required : 
      @param ConfigID
      @param InputName
      @param NewFormatString
   */  
export interface OnChangeFormatString_input{
   ConfigID:string,
   InputName:string,
   NewFormatString:string,
}

export interface OnChangeFormatString_output{
}

   /** Required : 
      @param proposedImageLayerID
      @param ds
   */  
export interface OnChangeImageLayerID_input{
      /**  Image layer id to validate  */  
   proposedImageLayerID:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeImageLayerID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
   imageURL:string,
}
}

   /** Required : 
      @param inputName
      @param ds
   */  
export interface OnChangeInputName_input{
      /**  The control name.  */  
   inputName:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeInputName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param newPageDispSeq
      @param ds
   */  
export interface OnChangeInputPageNumber_input{
      /**  Target Display Sequence  */  
   newPageDispSeq:number,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeInputPageNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param readOnlyExpr
      @param ds
   */  
export interface OnChangeInputReadOnlyExpr_input{
      /**  Is ReadOnlyExpr Variable  */  
   readOnlyExpr:boolean,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeInputReadOnlyExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeInputTabOrder_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeInputTabOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param inputType
      @param ds
   */  
export interface OnChangeInputType_input{
      /**  The control style.  Options are Label, Character, Date, Decimal, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser  */  
   inputType:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeInputType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeMinOrMaxForDecimal_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeMinOrMaxForDecimal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param newPageDispSeq
      @param ds
   */  
export interface OnChangePageDisplaySeq_input{
      /**  Target Display Sequence  */  
   newPageDispSeq:number,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangePageDisplaySeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param readOnlyExpr
      @param ds
   */  
export interface OnChangePageReadOnlyExpr_input{
      /**  Is ReadOnlyExpr Variable  */  
   readOnlyExpr:boolean,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangePageReadOnlyExpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param sourceInputName
      @param ds
   */  
export interface OnChangeSourceInputName_input{
      /**  Source Input Name  */  
   sourceInputName:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangeSourceInputName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param globalInputVar
      @param ds
   */  
export interface OnChangedGlobalInputVar_input{
      /**  Is Global Input Variable  */  
   globalInputVar:boolean,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangedGlobalInputVar_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param inputName
      @param listSeq
      @param ds
   */  
export interface OnChangingBAQName_input{
      /**  Input Name  */  
   inputName:string,
      /**  List Seq  */  
   listSeq:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangingBAQName_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param functionName
      @param ds
   */  
export interface OnChangingDataLookupFunction_input{
      /**  Function Method Name  */  
   functionName:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangingDataLookupFunction_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param glbInputVarName
      @param ds
   */  
export interface OnChangingGlbInputVarName_input{
      /**  Global Input Variable Name  */  
   glbInputVarName:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangingGlbInputVarName_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param listDataSource
      @param ds
   */  
export interface OnChangingListDataSource_input{
      /**  Data Source Type  */  
   listDataSource:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangingListDataSource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param userDefinedMethodName
      @param configId
      @param company
      @param ds
   */  
export interface OnChangingUserDefinedMethodName_input{
      /**  User Defined Method Name  */  
   userDefinedMethodName:string,
      /**  Current ConfigID  */  
   configId:string,
      /**  Current Company  */  
   company:string,
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface OnChangingUserDefinedMethodName_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configID
   */  
export interface PageCountForCodeEditor_input{
      /**  Configuration ID  */  
   configID:string,
}

export interface PageCountForCodeEditor_output{
parameters : {
      /**  output parameters  */  
   pageCount:number,
}
}

   /** Required : 
      @param ipConfigID
   */  
export interface PromptForPassword_input{
      /**  Configuration ID  */  
   ipConfigID:string,
}

export interface PromptForPassword_output{
parameters : {
      /**  output parameters  */  
   opPromptForPassword:boolean,
   opRevisionStatus:boolean,
   opRevisionFound:boolean,
}
}

   /** Required : 
      @param ds
      @param dsConfigDesign
   */  
export interface RefreshImageLayerDetails_input{
   ds:Erp_Tablesets_PcInputsLayerIDWhereUsedTableset[],
   dsConfigDesign:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface RefreshImageLayerDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PcInputsLayerIDWhereUsedTableset[],
   dsConfigDesign:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ipApproved
      @param ipValidPassword
      @param ipConfigID
      @param ipAuditDesc
   */  
export interface SyncRevision_input{
      /**  The proposed approval flag  */  
   ipApproved:boolean,
      /**  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  */  
   ipValidPassword:boolean,
      /**  Configuration ID  */  
   ipConfigID:string,
      /**  The audit description entered for the configuration approval  */  
   ipAuditDesc:string,
}

export interface SyncRevision_output{
parameters : {
      /**  output parameters  */  
   revSynched:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtConfigurationDesignTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtConfigurationDesignTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ConfigurationDesignTS
   */  
export interface UpdateQBuildMapping_input{
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface UpdateQBuildMapping_output{
parameters : {
      /**  output parameters  */  
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param configID
      @param inputName
      @param skipQBuildMappingChecks
   */  
export interface ValidateAllowedToDeletePcInput_input{
      /**  Configurator ID  */  
   configID:string,
      /**  PcInput name  */  
   inputName:string,
      /**  Skip Validate QBuild Mapping  */  
   skipQBuildMappingChecks:boolean,
}

export interface ValidateAllowedToDeletePcInput_output{
}

   /** Required : 
      @param queryID
      @param fieldName
   */  
export interface ValidateBAQColumnName_input{
      /**  Query ID  */  
   queryID:string,
      /**  Field Name  */  
   fieldName:string,
}

export interface ValidateBAQColumnName_output{
      /**  True if a QueryField record exists with the given parameters  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   dataType:string,
}
}

   /** Required : 
      @param proposedImageLayerID
   */  
export interface ValidateImageLayerID_input{
      /**  Image layer id to validate  */  
   proposedImageLayerID:string,
}

export interface ValidateImageLayerID_output{
}

   /** Required : 
      @param ConfigID
      @param ProposedInputName
   */  
export interface ValidateInputName_input{
      /**  the configuration ID of the Input  */  
   ConfigID:string,
      /**  The name the user wants to use as a name  */  
   ProposedInputName:string,
}

export interface ValidateInputName_output{
}

   /** Required : 
      @param ConfigurationDesignTS
      @param MappedInputName
   */  
export interface ValidateMappedInput_input{
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
      /**  Proposed Mapped Input Name to validate  */  
   MappedInputName:string,
}

export interface ValidateMappedInput_output{
parameters : {
      /**  output parameters  */  
   ConfigurationDesignTS:Erp_Tablesets_ConfigurationDesignTableset[],
}
}

   /** Required : 
      @param inLookupTblID
      @param colName
   */  
export interface ValidatePcLookupColSetDtl_input{
      /**  LookupTblID  */  
   inLookupTblID:string,
      /**  ColName  */  
   colName:string,
}

export interface ValidatePcLookupColSetDtl_output{
      /**  True if a PcLookupColSetDtl record exists with the given parameter  */  
   returnObj:boolean,
}

   /** Required : 
      @param inLookupTblID
   */  
export interface ValidatePcLookupTblHed_input{
      /**  LookupTblID  */  
   inLookupTblID:string,
}

export interface ValidatePcLookupTblHed_output{
      /**  True if a PcLookupTblHed record exists with the given parameter  */  
   returnObj:boolean,
}

