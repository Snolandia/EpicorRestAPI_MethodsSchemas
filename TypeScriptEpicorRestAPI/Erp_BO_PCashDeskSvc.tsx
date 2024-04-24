import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PCashDeskSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/$metadata", {
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
   Description: Get PCashDesks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDesks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskRow
   */  
export function get_PCashDesks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDesks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDesks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks", {
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
   Summary: Calls GetByID to retrieve the PCashDesk item
   Description: Calls GetByID to retrieve the PCashDesk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   */  
export function get_PCashDesks_Company_CashDeskID(Company:string, CashDeskID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDesk for the service
   Description: Calls UpdateExt to update PCashDesk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDesks_Company_CashDeskID(Company:string, CashDeskID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")", {
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
   Summary: Call UpdateExt to delete PCashDesk item
   Description: Call UpdateExt to delete PCashDesk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDesk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDesks_Company_CashDeskID(Company:string, CashDeskID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_PCashDesks_Company_CashDeskID_EntityGLCs(Company:string, CashDeskID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_PCashDesks_Company_CashDeskID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, CashDeskID:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskAuths1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAuthRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskAuths(Company:string, CashDeskID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAuths", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDeskAuth item
   Description: Calls GetByID to retrieve the PCashDeskAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAuth1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company:string, CashDeskID:string, DcdUserID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskOprs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskOprRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskOprs(Company:string, CashDeskID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDeskOpr item
   Description: Calls GetByID to retrieve the PCashDeskOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskOpr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param OprTypeCode Desc: OprTypeCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company:string, CashDeskID:string, OprTypeCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAttchRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskAttches(Company:string, CashDeskID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PCashDeskAttch item
   Description: Calls GetByID to retrieve the PCashDeskAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   */  
export function get_PCashDesks_Company_CashDeskID_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company:string, CashDeskID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs", {
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PCashDeskAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskAuths
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAuthRow
   */  
export function get_PCashDeskAuths(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskAuths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDeskAuths(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths", {
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
   Summary: Calls GetByID to retrieve the PCashDeskAuth item
   Description: Calls GetByID to retrieve the PCashDeskAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   */  
export function get_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company:string, CashDeskID:string, DcdUserID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskAuthRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskAuthRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDeskAuth for the service
   Description: Calls UpdateExt to update PCashDeskAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company:string, CashDeskID:string, DcdUserID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")", {
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
   Summary: Call UpdateExt to delete PCashDeskAuth item
   Description: Call UpdateExt to delete PCashDeskAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskAuth
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DcdUserID Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company:string, CashDeskID:string, DcdUserID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")", {
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
   Description: Get PCashDeskOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskOprs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskOprRow
   */  
export function get_PCashDeskOprs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDeskOprs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs", {
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
   Summary: Calls GetByID to retrieve the PCashDeskOpr item
   Description: Calls GetByID to retrieve the PCashDeskOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param OprTypeCode Desc: OprTypeCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   */  
export function get_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company:string, CashDeskID:string, OprTypeCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskOprRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskOprRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDeskOpr for the service
   Description: Calls UpdateExt to update PCashDeskOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param OprTypeCode Desc: OprTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company:string, CashDeskID:string, OprTypeCode:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")", {
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
   Summary: Call UpdateExt to delete PCashDeskOpr item
   Description: Call UpdateExt to delete PCashDeskOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskOpr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param OprTypeCode Desc: OprTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company:string, CashDeskID:string, OprTypeCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")", {
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
   Description: Get PCashDeskAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAttchRow
   */  
export function get_PCashDeskAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PCashDeskAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches", {
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
   Summary: Calls GetByID to retrieve the PCashDeskAttch item
   Description: Calls GetByID to retrieve the PCashDeskAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   */  
export function get_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company:string, CashDeskID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PCashDeskAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PCashDeskAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PCashDeskAttch for the service
   Description: Calls UpdateExt to update PCashDeskAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company:string, CashDeskID:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PCashDeskAttch item
   Description: Call UpdateExt to delete PCashDeskAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CashDeskID Desc: CashDeskID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company:string, CashDeskID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePCashDesk:string, whereClausePCashDeskAttch:string, whereClausePCashDeskAuth:string, whereClausePCashDeskOpr:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePCashDesk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDesk=" + whereClausePCashDesk
   }
   if(typeof whereClausePCashDeskAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDeskAttch=" + whereClausePCashDeskAttch
   }
   if(typeof whereClausePCashDeskAuth!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDeskAuth=" + whereClausePCashDeskAuth
   }
   if(typeof whereClausePCashDeskOpr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePCashDeskOpr=" + whereClausePCashDeskOpr
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetRows" + params, {
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
export function get_GetByID(cashDeskID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof cashDeskID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "cashDeskID=" + cashDeskID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetList" + params, {
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
   Summary: Invoke method GetCodeDescList
   Description: Method to get the Code Description List.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetCodeDescList", {
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
   Summary: Invoke method ChangePCashDeskCurrencyCode
   Description: Method to call when changing the currency code.
   OperationID: ChangePCashDeskCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskCurrencyCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskCurrencyCode", {
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
   Summary: Invoke method ChangePCashDeskEntrustedCashier
   Description: Method to call when changing the entrusted cashier.
   OperationID: ChangePCashDeskEntrustedCashier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskEntrustedCashier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskEntrustedCashier_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskEntrustedCashier(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskEntrustedCashier", {
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
   Summary: Invoke method ChangePCashDeskInitPayrollBal
   Description: Method to call when changing the initial payroll balance.
   OperationID: ChangePCashDeskInitPayrollBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskInitPayrollBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskInitPayrollBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskInitPayrollBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskInitPayrollBal", {
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
   Summary: Invoke method ChangePCashDeskInitTotalBal
   Description: Method to call when changing the initial balance.
   OperationID: ChangePCashDeskInitTotalBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskInitTotalBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskInitTotalBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskInitTotalBal(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskInitTotalBal", {
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
   Summary: Invoke method ChangePCashDeskOpenedFrom
   Description: Method to call when changing the initial balances date.
   OperationID: ChangePCashDeskOpenedFrom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOpenedFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOpenedFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskOpenedFrom(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskOpenedFrom", {
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
   Summary: Invoke method ChangePCashDeskOprOprTypeCode
   Description: Method to call when changing the operation type code.
   OperationID: ChangePCashDeskOprOprTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOprOprTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOprOprTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskOprOprTypeCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskOprOprTypeCode", {
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
   Summary: Invoke method ChangePCashDeskOprTranDocTypeID
   Description: Method to call when changing the tran doc type id.
   OperationID: ChangePCashDeskOprTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOprTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOprTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskOprTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskOprTranDocTypeID", {
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
   Summary: Invoke method ChangePCashDeskRateGrpCode
   Description: Method to call when changing the rate group code.
   OperationID: ChangePCashDeskRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskRateGrpCode(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskRateGrpCode", {
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
   Summary: Invoke method ChangePCashDeskReportTranDocType
   Description: Method to call when changing the report tran document type.
   OperationID: ChangePCashDeskReportTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskReportTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskReportTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCashDeskReportTranDocType(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/ChangePCashDeskReportTranDocType", {
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
   Summary: Invoke method GetCashDeskBalance
   Description: Get overall balance for defined Cash Desk
   OperationID: GetCashDeskBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashDeskBalance(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetCashDeskBalance", {
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
   Summary: Invoke method GetCashDeskBalHist
   Description: Get day balances for defined Cash Desk
   OperationID: GetCashDeskBalHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskBalHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskBalHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashDeskBalHist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetCashDeskBalHist", {
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
   Summary: Invoke method GetCashDeskDocsHist
   Description: Get documents for defined Cash Desk and Date
   OperationID: GetCashDeskDocsHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskDocsHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskDocsHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashDeskDocsHist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetCashDeskDocsHist", {
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
   Summary: Invoke method CheckSecurity
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: CheckSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSecurity(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/CheckSecurity", {
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
   Summary: Invoke method GetNewPCashDesk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDesk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDesk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDesk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDesk(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetNewPCashDesk", {
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
   Summary: Invoke method GetNewPCashDeskAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDeskAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetNewPCashDeskAttch", {
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
   Summary: Invoke method GetNewPCashDeskAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskAuth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDeskAuth(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetNewPCashDeskAuth", {
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
   Summary: Invoke method GetNewPCashDeskOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPCashDeskOpr(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetNewPCashDeskOpr", {
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
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetNewEntityGLC", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDeskAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDeskAuthRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDeskListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDeskOprRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PCashDeskRow[],
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDeskAttchRow{
   "Company":string,
   "CashDeskID":string,
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

export interface Erp_Tablesets_PCashDeskAuthRow{
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**   Checked: User can enter/modify and print petty cash issues (including authorization of draft documents).
Unchecked: User cannot enter/modify cash issues.  */  
   "CashIssue":boolean,
      /**   Checked: User can enter/modify and print petty cash receipts (including authorization of draft documents)
Unchecked (default): User cannot enter/modify cash receipts.  */  
   "CashReceipts":boolean,
      /**   Checked: User can change Petty Cash Desk Definition (including modification of authorized users, available operations and GL controls)
Unchecked : User cannot change Petty Cash Desk Definition.  */  
   "ChangeSetup":boolean,
      /**  If Yes, user can perform day closing and print daily reports for not yet closed cash days. If No, user cannot perform day closing.  */  
   "CloseCashDays":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  User ID of the related UserFile record.  */  
   "DcdUserID":string,
      /**  If yes, user access is restricted by read-only mode (access to petty cash tracker, reprint authorized and posted  documents and daily documents for closed days only).If No, user has no access to Petty cash Desk.  */  
   "ReadOnlyAccess":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "UserFileName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDeskListRow{
      /**   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  */  
   "AllowDraftCI":boolean,
      /**   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  */  
   "AllowDraftCR":boolean,
      /**  Allow Negative Balance  */  
   "AllowNegBal":boolean,
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  Cashier Name  */  
   "Cashier":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  */  
   "DayCloseMode":string,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "DocInitPayrollBal":number,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "DocInitTotalBal":number,
      /**  Entrusted Cashier  */  
   "EntrustedCashier":string,
      /**   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  */  
   "EntrustedFrom":string,
      /**   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  */  
   "EntrustedTill":string,
      /**   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  */  
   "Inactive":boolean,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "InitTotalBal":number,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "InitPayrollBal":number,
      /**  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  */  
   "LimitExptPayroll":number,
      /**  Defines Limit (in Cash Desk Currency)  */  
   "LimitTotal":number,
      /**  Cash Desk Location  */  
   "Location":string,
      /**  Cash Desk Name  */  
   "Name":string,
      /**  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "OpenedFrom":string,
      /**   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  */  
   "PostingOpt":string,
      /**  Rate Type  */  
   "RateGrpCode":string,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt1InitPayrollBal":number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt2InitPayrollBal":number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt3InitPayrollBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt1InitTotalBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt2InitTotalBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt3InitTotalBal":number,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   "UseExtnNumForCI":boolean,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   "UseExtnNumForCR":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  */  
   "OperationExists":boolean,
      /**  Indicates if the user is authorized to make changes.  */  
   "IsAuthorizedUser":boolean,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  Description  */  
   "CurrRateGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDeskOprRow{
      /**   Checked: Draft Documents can be used.
Unchecked: Draft Documents are not used.  */  
   "AllowDraftDoc":boolean,
      /**   Checked: External document numbers can be used.
Unchecked: External document numbers are not used.  */  
   "AllowUseExtnNum":boolean,
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  Company Identifier  */  
   "Company":string,
      /**  Indicates that operation type is enabled for this petty cash desk.  */  
   "OprTypeEnabled":boolean,
      /**  Defines Legal Number related to Transaction Document Type and therefore used for this Operation type.  */  
   "LegalNumberID":string,
      /**  Unique identifier of Cash Operation Type.  */  
   "OprTypeCode":string,
      /**  Used only in case of Supplier/Customer Recipient/Payer Type and defines contact used to retrieve personal data.  */  
   "RoleCode":string,
      /**  Transaction Document Type for system transactions PCashRcpt and PCashIssue  */  
   "TranDocTypeID":string,
      /**  Report ID to define Document Template used for printing  */  
   "ReportID":string,
      /**  Report Style to define document template for printing  */  
   "ReportStyleNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Description of the operation class  */  
   "OprClassDesc":string,
      /**  Direction description  */  
   "DirectionDesc":string,
      /**  Description of the RecPayerType  */  
   "RecPayerTypeDesc":string,
      /**  The system transaction type - PCI or PCR.  Used to filter combo list for TranDocTypeID.  */  
   "SystemTranType":string,
   "BitFlag":number,
   "LegalNumCnfgDescription":string,
   "PCashOprTypeDirection":string,
   "PCashOprTypePayrollBal":boolean,
   "PCashOprTypeOprClass":string,
   "PCashOprTypeDescription":string,
   "PCashOprTypeRecPayerType":string,
   "ReportRptDescription":string,
   "RoleCdRoleDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PCashDeskRow{
      /**   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  */  
   "AllowDraftCI":boolean,
      /**   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  */  
   "AllowDraftCR":boolean,
      /**  Allow Negative Balance  */  
   "AllowNegBal":boolean,
      /**  Unique identifier of Cash Desk  */  
   "CashDeskID":string,
      /**  Cashier Name  */  
   "Cashier":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  */  
   "DayCloseMode":string,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "DocInitPayrollBal":number,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "DocInitTotalBal":number,
      /**  Entrusted Cashier  */  
   "EntrustedCashier":string,
      /**   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  */  
   "EntrustedFrom":string,
      /**   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  */  
   "EntrustedTill":string,
      /**   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  */  
   "Inactive":boolean,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "InitTotalBal":number,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "InitPayrollBal":number,
      /**  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  */  
   "LimitExptPayroll":number,
      /**  Defines Limit (in Cash Desk Currency)  */  
   "LimitTotal":number,
      /**  Cash Desk Location  */  
   "Location":string,
      /**  Cash Desk Name  */  
   "Name":string,
      /**  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   "OpenedFrom":string,
      /**   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  */  
   "PostingOpt":string,
      /**  Rate Type  */  
   "RateGrpCode":string,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt1InitPayrollBal":number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt2InitPayrollBal":number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   "Rpt3InitPayrollBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt1InitTotalBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt2InitTotalBal":number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   "Rpt3InitTotalBal":number,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   "UseExtnNumForCI":boolean,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   "UseExtnNumForCR":boolean,
      /**  FloatAmt  */  
   "FloatAmt":number,
      /**  CashPayMethodPMUID  */  
   "CashPayMethodPMUID":number,
      /**  CashPayMethodName  */  
   "CashPayMethodName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrintLastPage  */  
   "PrintLastPage":number,
      /**  PrintPerPage  */  
   "PrintPerPage":number,
      /**  ReportTranDocType  */  
   "ReportTranDocType":string,
      /**  Indicates if the user is authorized to make changes.  */  
   "IsAuthorizedUser":boolean,
   "LegalNumberDesc":string,
      /**  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  */  
   "OperationExists":boolean,
   "ReportTranDocTypeDesc":string,
      /**  BD ? Both Directions; CI ? Only Issues; CR ? Only Receipts;  */  
   "Direction":string,
      /**  The user is authorized for Cash Receipt  */  
   "IsAuthorizedCR":boolean,
      /**  The user is authorized for Cash Issue  */  
   "IsAuthorizedCI":boolean,
      /**  User has access to read the Petty Cash Desk.  */  
   "UserCanRead":boolean,
   "BitFlag":number,
   "BaseCurrCurrDesc":string,
   "BaseCurrCurrSymbol":string,
   "BaseCurrCurrName":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrDocumentDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyDocumentDesc":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyCurrDesc":string,
   "CurrRateGrpDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param proposedCurrencyCode
      @param ds
   */  
export interface ChangePCashDeskCurrencyCode_input{
      /**  The proposed currency code  */  
   proposedCurrencyCode:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskCurrencyCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedEntrustedCashier
      @param ds
   */  
export interface ChangePCashDeskEntrustedCashier_input{
      /**  The proposed entrusted cashier  */  
   proposedEntrustedCashier:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskEntrustedCashier_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedInitPayrollBal
      @param docOrBase
      @param ds
   */  
export interface ChangePCashDeskInitPayrollBal_input{
      /**  The proposed initial payroll balance  */  
   proposedInitPayrollBal:number,
      /**  Was the base amount (Base) or doc amount (Doc) changed  */  
   docOrBase:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskInitPayrollBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedInitTotalBal
      @param docOrBase
      @param ds
   */  
export interface ChangePCashDeskInitTotalBal_input{
      /**  The proposed initial balance  */  
   proposedInitTotalBal:number,
      /**  Was the base amount (Base) or doc amount (Doc) changed  */  
   docOrBase:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskInitTotalBal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedOpenedFrom
      @param ds
   */  
export interface ChangePCashDeskOpenedFrom_input{
      /**  The proposed opened from date  */  
   proposedOpenedFrom:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskOpenedFrom_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedOprTypeCode
      @param ds
   */  
export interface ChangePCashDeskOprOprTypeCode_input{
      /**  The proposed operation type code  */  
   proposedOprTypeCode:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskOprOprTypeCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedTranDocTypeID
      @param ds
   */  
export interface ChangePCashDeskOprTranDocTypeID_input{
      /**  The proposed tran doc type id  */  
   proposedTranDocTypeID:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskOprTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedRateGrpCode
      @param ds
   */  
export interface ChangePCashDeskRateGrpCode_input{
      /**  The proposed rate group code  */  
   proposedRateGrpCode:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskRateGrpCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param proposedReportTranDocType
      @param ds
   */  
export interface ChangePCashDeskReportTranDocType_input{
      /**  The proposed report tran document type  */  
   proposedReportTranDocType:string,
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface ChangePCashDeskReportTranDocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param cashDeskID
      @param raiseException
   */  
export interface CheckSecurity_input{
   cashDeskID:string,
   raiseException:boolean,
}

export interface CheckSecurity_output{
   returnObj:boolean,
}

   /** Required : 
      @param cashDeskID
   */  
export interface DeleteByID_input{
   cashDeskID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key3:string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key4:string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key5:string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   Key6:string,
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskAttchRow{
   Company:string,
   CashDeskID:string,
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

export interface Erp_Tablesets_PCashDeskAuthRow{
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**   Checked: User can enter/modify and print petty cash issues (including authorization of draft documents).
Unchecked: User cannot enter/modify cash issues.  */  
   CashIssue:boolean,
      /**   Checked: User can enter/modify and print petty cash receipts (including authorization of draft documents)
Unchecked (default): User cannot enter/modify cash receipts.  */  
   CashReceipts:boolean,
      /**   Checked: User can change Petty Cash Desk Definition (including modification of authorized users, available operations and GL controls)
Unchecked : User cannot change Petty Cash Desk Definition.  */  
   ChangeSetup:boolean,
      /**  If Yes, user can perform day closing and print daily reports for not yet closed cash days. If No, user cannot perform day closing.  */  
   CloseCashDays:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  User ID of the related UserFile record.  */  
   DcdUserID:string,
      /**  If yes, user access is restricted by read-only mode (access to petty cash tracker, reprint authorized and posted  documents and daily documents for closed days only).If No, user has no access to Petty cash Desk.  */  
   ReadOnlyAccess:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   UserFileName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskBalHistRow{
   Date:string,
   Closed:boolean,
   OpeningBalance:number,
   DocOpeningBalance:number,
   CurrencyCode:string,
   Rpt1OpeningBalance:number,
   Rpt2OpeningBalance:number,
   Rpt3OpeningBalance:number,
   Receipts:number,
   AmountReceived:number,
   DocAmountReceived:number,
   Rpt1AmountReceived:number,
   Rpt2AmountReceived:number,
   Rpt3AmountReceived:number,
   Issues:number,
      /**  Amount issued per Cash Day  */  
   AmountIssued:number,
   DocAmountIssued:number,
   Rpt1AmountIssued:number,
   Rpt2AmountIssued:number,
   Rpt3AmountIssued:number,
   ClosingBalance:number,
   DocClosingBalance:number,
   Rpt1ClosingBalance:number,
   Rpt2ClosingBalance:number,
   Rpt3ClosingBalance:number,
      /**  Revaluation Gain / Loss  */  
   GainLossBal:number,
   Rpt1GainLossBal:number,
   Rpt2GainLossBal:number,
   Rpt3GainLossBal:number,
   DocGainLossBal:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskBalanceRow{
      /**  The Last Petty Cash Desk Closed Date  */  
   DateLastClosed:string,
      /**  Total Balance as per above date  */  
   LastClosedDayBalTotal:number,
      /**  Total Balance as per above date in document currency  */  
   DocLastClosedDayBalTotal:number,
   CurrencyCode:string,
   Rpt1LastClosedDayBalTotal:number,
   Rpt2LastClosedDayBalTotal:number,
   Rpt3LastClosedDayBalTotal:number,
      /**  Payroll Balance as per above date  */  
   LastClosedDayBalPayroll:number,
   DocLastClosedDayBalPayroll:number,
   Rpt1LastClosedDayBalPayroll:number,
   Rpt2LastClosedDayBalPayroll:number,
   Rpt3LastClosedDayBalPayroll:number,
      /**  Latest Authorized Document Date  */  
   LatestAuthDocDate:string,
      /**  Current Balance (Total)  */  
   CurrBalTotal:number,
   DocCurrBalTotal:number,
   Rpt1CurrBalTotal:number,
   Rpt2CurrBalTotal:number,
   Rpt3CurrBalTotal:number,
      /**  Payroll Balance as per above date  */  
   CurrBalPayroll:number,
      /**  Payroll Balance as per above date  */  
   DocCurrBalPayroll:number,
      /**  Payroll Balance as per above date  */  
   Rpt1CurrBalPayroll:number,
      /**  Payroll Balance as per above date  */  
   Rpt2CurrBalPayroll:number,
      /**  Payroll Balance as per above date  */  
   Rpt3CurrBalPayroll:number,
      /**  Date of Last Draft Document  */  
   LastDraftDocDate:string,
      /**  Total Balance as per above date (including draft documents)  */  
   CurrDraftBalTotal:number,
   Rpt1CurrDraftBalTotal:number,
   DocCurrDraftBalTotal:number,
   Rpt2CurrDraftBalTotal:number,
   Rpt3CurrDraftBalTotal:number,
   CurrDraftBalPayroll:number,
   DocCurrDraftBalPayroll:number,
   Rpt1CurrDraftBalPayroll:number,
   Rpt2CurrDraftBalPayroll:number,
   Rpt3CurrDraftBalPayroll:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskDocsHistRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  */  
   ReferenceNum:number,
      /**  Apply Date of Operation  */  
   ApplyDate:string,
      /**  User Id of the user who authorize the record.  */  
   AuthorizedBy:string,
      /**  Cashier Name  */  
   Cashier:string,
      /**  Comment  */  
   Comment:string,
      /**  User ID of the user who created the record.  */  
   CreatedBy:string,
      /**  Date when the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  A unique code that identifies the currency  */  
   CurrencyCode:string,
      /**  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  */  
   DaySeqNum:number,
      /**   CI ? Cash Issue
CR ? Cash Receipt  */  
   Direction:string,
      /**  Available only when configuration of operation type allows using of draft documents.  */  
   Draft:boolean,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   ExternalNum:string,
      /**  Fiscal Calendar is Company Calendar  */  
   FiscalCalendarID:string,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalPeriod:number,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalYear:number,
      /**  Defined by Apply Date for Company Calendar  */  
   FiscalYearSuffix:string,
      /**  Legal Number of the record. Available only for Authorized Documents.  */  
   LegalNumber:string,
      /**  Unique identifier of Petty Cash Operation Type  */  
   OprTypeCode:string,
      /**  According to Operation Type  */  
   PayrollBalOpr:boolean,
      /**  Posted  */  
   Posted:boolean,
      /**  Printed  */  
   Printed:boolean,
      /**  Reason  */  
   ReasonCode:string,
      /**  Review Journal.  */  
   RvJrnUID:number,
      /**   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  */  
   RecipientType:string,
      /**  Customer  */  
   CustNum:number,
      /**  Ship To Customer (CustCon.ShipToNum)  */  
   CustShipTo:string,
      /**  Customer Contact Number (CustCon.ConNum)  */  
   CustConNum:number,
      /**  Supplier  */  
   VendorNum:number,
      /**  Purchase point from Vendor.(VendCon.PurPoint)  */  
   VendPurPoint:string,
      /**  Supplier Contact number (VendCon.ConNum)  */  
   VendConNum:number,
   EmployeeNum:string,
      /**  Bank Account  */  
   BankAcctID:string,
      /**  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  */  
   OrganizationID:string,
      /**   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  */  
   OrganizationName:string,
      /**   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  */  
   PersonName:string,
      /**  Default of Personal Data can be composed using BPM, and can be adjusted by user.  */  
   PersonalData:string,
      /**  Amount to be paid/received in cash  */  
   DocCashAmt:number,
      /**  Amount to be paid/received in cash  */  
   CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt1CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt2CashAmt:number,
      /**  Amount to be paid/received in cash in reporting Currency  */  
   Rpt3CashAmt:number,
      /**  Gross Amount to update AP or AR  */  
   DocGrossAmt:number,
      /**  Gross Amount to update AP or AR  */  
   GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt1GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt2GrossAmt:number,
      /**  Gross Amount in reporting Currency  */  
   Rpt3GrossAmt:number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   DocDiscount:number,
      /**  Amount of Applied Cash Discount (AP or AR)  */  
   Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt1Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt2Discount:number,
      /**  Amount of Applied Cash Discount  in reporting Currency  */  
   Rpt3Discount:number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   DocWithholdAmt:number,
      /**  Amount of calculated withhold taxes (AR or AP)  */  
   WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt1WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt2WithholdAmt:number,
      /**  Amount of calculated withhold taxes  in reporting currency  */  
   Rpt3WithholdAmt:number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   DocBankAmt:number,
      /**  Bank Amount(Bank To Cash / Cash To Bank)  */  
   BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt1BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt2BankAmt:number,
      /**  Bank Amount in reporting currency  */  
   Rpt3BankAmt:number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   DocBankFeeAmt:number,
      /**  Bank Fee Amount(Bank To Cash / Cash To Bank)  */  
   BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt1BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt2BankFeeAmt:number,
      /**  Bank Fee Amount in reporting currency  */  
   Rpt3BankFeeAmt:number,
      /**  Rate Type  */  
   RateGrpType:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  OnAcctBankAcctID  */  
   OnAcctBankAcctID:string,
      /**  ReceiptAmt  */  
   ReceiptAmt:number,
      /**  Reference  */  
   Reference:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  PayMethodPMUID  */  
   PayMethodPMUID:number,
      /**  PayMethodName  */  
   PayMethodName:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CashDeskIDTransfer  */  
   CashDeskIDTransfer:string,
      /**  ExchangeRateDate  */  
   ExchangeRateDate:string,
      /**  ExchRateDateUserDefined  */  
   ExchRateDateUserDefined:boolean,
      /**  PrintPage  */  
   PrintPage:number,
      /**  PrintPageLegalNum  */  
   PrintPageLegalNum:string,
      /**  Reason  */  
   Reason:string,
      /**  Cash Head Reverse Date  */  
   ReverseDate:string,
      /**  Cash Head Reverse Amount  */  
   ReverseAmt:number,
   OprTypeDescription:string,
   OprTypeOpClassName:string,
   OprTypeReason:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskListRow{
      /**   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  */  
   AllowDraftCI:boolean,
      /**   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  */  
   AllowDraftCR:boolean,
      /**  Allow Negative Balance  */  
   AllowNegBal:boolean,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Cashier Name  */  
   Cashier:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  */  
   DayCloseMode:string,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   DocInitPayrollBal:number,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   DocInitTotalBal:number,
      /**  Entrusted Cashier  */  
   EntrustedCashier:string,
      /**   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  */  
   EntrustedFrom:string,
      /**   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  */  
   EntrustedTill:string,
      /**   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  */  
   Inactive:boolean,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   InitTotalBal:number,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   InitPayrollBal:number,
      /**  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  */  
   LimitExptPayroll:number,
      /**  Defines Limit (in Cash Desk Currency)  */  
   LimitTotal:number,
      /**  Cash Desk Location  */  
   Location:string,
      /**  Cash Desk Name  */  
   Name:string,
      /**  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   OpenedFrom:string,
      /**   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  */  
   PostingOpt:string,
      /**  Rate Type  */  
   RateGrpCode:string,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt1InitPayrollBal:number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt2InitPayrollBal:number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt3InitPayrollBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt1InitTotalBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt2InitTotalBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt3InitTotalBal:number,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   UseExtnNumForCI:boolean,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   UseExtnNumForCR:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  */  
   OperationExists:boolean,
      /**  Indicates if the user is authorized to make changes.  */  
   IsAuthorizedUser:boolean,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  Description  */  
   CurrRateGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskListTableset{
   PCashDeskList:Erp_Tablesets_PCashDeskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCashDeskOprRow{
      /**   Checked: Draft Documents can be used.
Unchecked: Draft Documents are not used.  */  
   AllowDraftDoc:boolean,
      /**   Checked: External document numbers can be used.
Unchecked: External document numbers are not used.  */  
   AllowUseExtnNum:boolean,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Company Identifier  */  
   Company:string,
      /**  Indicates that operation type is enabled for this petty cash desk.  */  
   OprTypeEnabled:boolean,
      /**  Defines Legal Number related to Transaction Document Type and therefore used for this Operation type.  */  
   LegalNumberID:string,
      /**  Unique identifier of Cash Operation Type.  */  
   OprTypeCode:string,
      /**  Used only in case of Supplier/Customer Recipient/Payer Type and defines contact used to retrieve personal data.  */  
   RoleCode:string,
      /**  Transaction Document Type for system transactions PCashRcpt and PCashIssue  */  
   TranDocTypeID:string,
      /**  Report ID to define Document Template used for printing  */  
   ReportID:string,
      /**  Report Style to define document template for printing  */  
   ReportStyleNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Description of the operation class  */  
   OprClassDesc:string,
      /**  Direction description  */  
   DirectionDesc:string,
      /**  Description of the RecPayerType  */  
   RecPayerTypeDesc:string,
      /**  The system transaction type - PCI or PCR.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
   BitFlag:number,
   LegalNumCnfgDescription:string,
   PCashOprTypeDirection:string,
   PCashOprTypePayrollBal:boolean,
   PCashOprTypeOprClass:string,
   PCashOprTypeDescription:string,
   PCashOprTypeRecPayerType:string,
   ReportRptDescription:string,
   RoleCdRoleDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskRow{
      /**   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  */  
   AllowDraftCI:boolean,
      /**   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  */  
   AllowDraftCR:boolean,
      /**  Allow Negative Balance  */  
   AllowNegBal:boolean,
      /**  Unique identifier of Cash Desk  */  
   CashDeskID:string,
      /**  Cashier Name  */  
   Cashier:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  */  
   DayCloseMode:string,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   DocInitPayrollBal:number,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   DocInitTotalBal:number,
      /**  Entrusted Cashier  */  
   EntrustedCashier:string,
      /**   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  */  
   EntrustedFrom:string,
      /**   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  */  
   EntrustedTill:string,
      /**   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  */  
   Inactive:boolean,
      /**  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   InitTotalBal:number,
      /**  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   InitPayrollBal:number,
      /**  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  */  
   LimitExptPayroll:number,
      /**  Defines Limit (in Cash Desk Currency)  */  
   LimitTotal:number,
      /**  Cash Desk Location  */  
   Location:string,
      /**  Cash Desk Name  */  
   Name:string,
      /**  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  */  
   OpenedFrom:string,
      /**   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  */  
   PostingOpt:string,
      /**  Rate Type  */  
   RateGrpCode:string,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt1InitPayrollBal:number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt2InitPayrollBal:number,
      /**  Value of InitPayrollBal in Reporting Currency  */  
   Rpt3InitPayrollBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt1InitTotalBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt2InitTotalBal:number,
      /**  Value of InitTotalBal in Reporting Currency  */  
   Rpt3InitTotalBal:number,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   UseExtnNumForCI:boolean,
      /**   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  */  
   UseExtnNumForCR:boolean,
      /**  FloatAmt  */  
   FloatAmt:number,
      /**  CashPayMethodPMUID  */  
   CashPayMethodPMUID:number,
      /**  CashPayMethodName  */  
   CashPayMethodName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrintLastPage  */  
   PrintLastPage:number,
      /**  PrintPerPage  */  
   PrintPerPage:number,
      /**  ReportTranDocType  */  
   ReportTranDocType:string,
      /**  Indicates if the user is authorized to make changes.  */  
   IsAuthorizedUser:boolean,
   LegalNumberDesc:string,
      /**  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  */  
   OperationExists:boolean,
   ReportTranDocTypeDesc:string,
      /**  BD ? Both Directions; CI ? Only Issues; CR ? Only Receipts;  */  
   Direction:string,
      /**  The user is authorized for Cash Receipt  */  
   IsAuthorizedCR:boolean,
      /**  The user is authorized for Cash Issue  */  
   IsAuthorizedCI:boolean,
      /**  User has access to read the Petty Cash Desk.  */  
   UserCanRead:boolean,
   BitFlag:number,
   BaseCurrCurrDesc:string,
   BaseCurrCurrSymbol:string,
   BaseCurrCurrName:string,
   BaseCurrCurrencyID:string,
   BaseCurrDocumentDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyDocumentDesc:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyCurrDesc:string,
   CurrRateGrpDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PCashDeskTableset{
   PCashDesk:Erp_Tablesets_PCashDeskRow[],
   PCashDeskAttch:Erp_Tablesets_PCashDeskAttchRow[],
   PCashDeskAuth:Erp_Tablesets_PCashDeskAuthRow[],
   PCashDeskOpr:Erp_Tablesets_PCashDeskOprRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PCashDeskTrackerTableset{
   PCashDeskBalance:Erp_Tablesets_PCashDeskBalanceRow[],
   PCashDeskBalHist:Erp_Tablesets_PCashDeskBalHistRow[],
   PCashDeskDocsHist:Erp_Tablesets_PCashDeskDocsHistRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPCashDeskTableset{
   PCashDesk:Erp_Tablesets_PCashDeskRow[],
   PCashDeskAttch:Erp_Tablesets_PCashDeskAttchRow[],
   PCashDeskAuth:Erp_Tablesets_PCashDeskAuthRow[],
   PCashDeskOpr:Erp_Tablesets_PCashDeskOprRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param cashDeskID
   */  
export interface GetByID_input{
   cashDeskID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PCashDeskTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PCashDeskTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PCashDeskTableset[],
}

   /** Required : 
      @param ipCashDeskID
      @param ipFromDate
      @param ipToDate
      @param ipIncludeDrafts
      @param ipPayrollOnly
      @param ds
   */  
export interface GetCashDeskBalHist_input{
      /**  Cash Desk ID  */  
   ipCashDeskID:string,
      /**  From Date  */  
   ipFromDate:string,
      /**  To Date  */  
   ipToDate:string,
      /**  Include Drafts  */  
   ipIncludeDrafts:boolean,
      /**  Payroll Only  */  
   ipPayrollOnly:boolean,
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}

export interface GetCashDeskBalHist_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}
}

   /** Required : 
      @param ipCashDeskID
      @param ds
   */  
export interface GetCashDeskBalance_input{
      /**  Cash Desk ID  */  
   ipCashDeskID:string,
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}

export interface GetCashDeskBalance_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}
}

   /** Required : 
      @param ipCashDeskID
      @param ipDate
      @param ipDirection
      @param ds
   */  
export interface GetCashDeskDocsHist_input{
      /**  Cash Desk ID  */  
   ipCashDeskID:string,
      /**  To Date  */  
   ipDate:string,
      /**  To Date  */  
   ipDirection:string,
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}

export interface GetCashDeskDocsHist_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTrackerTableset[],
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  The table name to get Code List  */  
   tableName:string,
      /**  The field name to get Code List  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_PCashDeskListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param ds
      @param cashDeskID
   */  
export interface GetNewPCashDeskAttch_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
   cashDeskID:string,
}

export interface GetNewPCashDeskAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param ds
      @param cashDeskID
   */  
export interface GetNewPCashDeskAuth_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
   cashDeskID:string,
}

export interface GetNewPCashDeskAuth_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param ds
      @param cashDeskID
   */  
export interface GetNewPCashDeskOpr_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
   cashDeskID:string,
}

export interface GetNewPCashDeskOpr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPCashDesk_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface GetNewPCashDesk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

   /** Required : 
      @param whereClausePCashDesk
      @param whereClausePCashDeskAttch
      @param whereClausePCashDeskAuth
      @param whereClausePCashDeskOpr
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePCashDesk:string,
   whereClausePCashDeskAttch:string,
   whereClausePCashDeskAuth:string,
   whereClausePCashDeskOpr:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PCashDeskTableset[],
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
   ds:Erp_Tablesets_UpdExtPCashDeskTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPCashDeskTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PCashDeskTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PCashDeskTableset[],
}
}

