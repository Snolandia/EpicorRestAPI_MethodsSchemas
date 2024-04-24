import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.MasterPackSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/$metadata", {
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
   Description: Get MasterPacks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPacks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackRow
   */  
export function get_MasterPacks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterPacks(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks", {
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
   Summary: Calls GetByID to retrieve the MasterPack item
   Description: Calls GetByID to retrieve the MasterPack item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPack
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   */  
export function get_MasterPacks_Company_PackNum(Company:string, PackNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MasterPack for the service
   Description: Calls UpdateExt to update MasterPack. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPack
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MasterPacks_Company_PackNum(Company:string, PackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")", {
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
   Summary: Call UpdateExt to delete MasterPack item
   Description: Call UpdateExt to delete MasterPack item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPack
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MasterPacks_Company_PackNum(Company:string, PackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")", {
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
   Description: Get MasterPackDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackDtlRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackDtls(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MasterPackDtl item
   Description: Calls GetByID to retrieve the MasterPackDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param MPackLine Desc: MPackLine   Required: True
      @param DtlPackNum Desc: DtlPackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackDtls_Company_MPackLine_DtlPackNum(Company:string, PackNum:string, MPackLine:string, DtlPackNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MasterPackUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackUPS1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackUPSRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackUPS(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MasterPackUP item
   Description: Calls GetByID to retrieve the MasterPackUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackUP1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MasterPackAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MasterPackAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackAttchRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackAttches(Company:string, PackNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MasterPackAttch item
   Description: Calls GetByID to retrieve the MasterPackAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   */  
export function get_MasterPacks_Company_PackNum_MasterPackAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPacks(" + Company + "," + PackNum + ")/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get MasterPackDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackDtls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackDtlRow
   */  
export function get_MasterPackDtls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterPackDtls(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls", {
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
   Summary: Calls GetByID to retrieve the MasterPackDtl item
   Description: Calls GetByID to retrieve the MasterPackDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MPackLine Desc: MPackLine   Required: True
      @param DtlPackNum Desc: DtlPackNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   */  
export function get_MasterPackDtls_Company_MPackLine_DtlPackNum(Company:string, MPackLine:string, DtlPackNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MasterPackDtl for the service
   Description: Calls UpdateExt to update MasterPackDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MPackLine Desc: MPackLine   Required: True
      @param DtlPackNum Desc: DtlPackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MasterPackDtls_Company_MPackLine_DtlPackNum(Company:string, MPackLine:string, DtlPackNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")", {
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
   Summary: Call UpdateExt to delete MasterPackDtl item
   Description: Call UpdateExt to delete MasterPackDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MPackLine Desc: MPackLine   Required: True
      @param DtlPackNum Desc: DtlPackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MasterPackDtls_Company_MPackLine_DtlPackNum(Company:string, MPackLine:string, DtlPackNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackDtls(" + Company + "," + MPackLine + "," + DtlPackNum + ")", {
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
   Description: Get MasterPackUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackUPS
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackUPSRow
   */  
export function get_MasterPackUPS(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterPackUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS", {
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
   Summary: Calls GetByID to retrieve the MasterPackUP item
   Description: Calls GetByID to retrieve the MasterPackUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   */  
export function get_MasterPackUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackUPSRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackUPSRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MasterPackUP for the service
   Description: Calls UpdateExt to update MasterPackUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MasterPackUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete MasterPackUP item
   Description: Call UpdateExt to delete MasterPackUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackUP
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MasterPackUPS_Company_PackNum_UPSQVSeq(Company:string, PackNum:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", {
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
   Description: Get MasterPackAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MasterPackAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterPackAttchRow
   */  
export function get_MasterPackAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MasterPackAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterPackAttches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches", {
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
   Summary: Calls GetByID to retrieve the MasterPackAttch item
   Description: Calls GetByID to retrieve the MasterPackAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MasterPackAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   */  
export function get_MasterPackAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MasterPackAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_MasterPackAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MasterPackAttch for the service
   Description: Calls UpdateExt to update MasterPackAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MasterPackAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MasterPackAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MasterPackAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete MasterPackAttch item
   Description: Call UpdateExt to delete MasterPackAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MasterPackAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PackNum Desc: PackNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MasterPackAttches_Company_PackNum_DrawingSeq(Company:string, PackNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/MasterPackAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", {
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
   Description: Get CartonDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonDetails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonDetailRow
   */  
export function get_CartonDetails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails", {
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
   Summary: Calls GetByID to retrieve the CartonDetail item
   Description: Calls GetByID to retrieve the CartonDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonDetail
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   */  
export function get_CartonDetails_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CartonDetailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CartonDetailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CartonDetail for the service
   Description: Calls UpdateExt to update CartonDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonDetail
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CartonDetails_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CartonDetail item
   Description: Call UpdateExt to delete CartonDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonDetail
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CartonDetails_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonDetails(" + SysRowID + ")", {
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
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts", {
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
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   */  
export function get_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LegalNumGenOptsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LegalNumGenOptsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LegalNumberID Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LegalNumGenOpts_Company_LegalNumberID(Company:string, LegalNumberID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MasterpackListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterpackListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterpackListRow)
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseMasterPack:string, whereClauseMasterPackAttch:string, whereClauseMasterPackDtl:string, whereClauseMasterPackUPS:string, whereClauseCartonDetail:string, whereClauseLegalNumGenOpts:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMasterPack!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMasterPack=" + whereClauseMasterPack
   }
   if(typeof whereClauseMasterPackAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMasterPackAttch=" + whereClauseMasterPackAttch
   }
   if(typeof whereClauseMasterPackDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMasterPackDtl=" + whereClauseMasterPackDtl
   }
   if(typeof whereClauseMasterPackUPS!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMasterPackUPS=" + whereClauseMasterPackUPS
   }
   if(typeof whereClauseCartonDetail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCartonDetail=" + whereClauseCartonDetail
   }
   if(typeof whereClauseLegalNumGenOpts!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(packNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof packNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "packNum=" + packNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetList" + params, {
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
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/AssignLegalNumber", {
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
   Summary: Invoke method CalculateWeight
   Description: Purpose:  calculate the weight of a carton based upon Part.Weight.
<param name="ds">MasterpackDataSet</param><param name="weight">Pack Weight</param>
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateWeight(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CalculateWeight", {
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
   Summary: Invoke method CancelVoidCarton
   Description: Checks to see if the carton void can be cancelled and re-opens it if it is allowed.
   OperationID: CancelVoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelVoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CancelVoidCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CancelVoidCarton", {
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
   Summary: Invoke method ClearConvertedManifest
   Description: Purpose: Clear TFShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearConvertedManifest(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/ClearConvertedManifest", {
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
   Summary: Invoke method CloseCarton
   Description: Checks to see if the carton can be closed and closes it if it is allowed.
   OperationID: CloseCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CloseCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CloseCarton", {
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
   Summary: Invoke method ConvertToManifestUOM
   Description: Purpose: Populate Masterpack Manifest fields.
<param name="ipPackNum">Pack Num to populate Manifest fields</param>
Notes:
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertToManifestUOM(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/ConvertToManifestUOM", {
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
   Summary: Invoke method GetCustPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetCustPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCustPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetCustPayBTFlagDefaults", {
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
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumGenOpts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetLegalNumGenOpts", {
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
   Summary: Invoke method GetMiscPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetMiscPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMiscPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMiscPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMiscPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetMiscPayBTFlagDefaults", {
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
   Summary: Invoke method GetPackaging
   Description: Purpose:
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Masterpack Shipment data set </param>
Notes:
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackaging(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetPackaging", {
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
   Summary: Invoke method GetPackClass
   Description: Purpose:
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Masterpack Shipment data set </param>
Notes:
   OperationID: GetPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPackClass(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetPackClass", {
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
   Summary: Invoke method GetPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param><param name="ds">The Masterpack shipment data set </param>
Notes:
   OperationID: GetPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetPayBTFlagDefaults", {
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
   Summary: Invoke method GetScale
   Description: Purpose: Retrieve workstation scale settings
Parameters:
<param name="workstationID">Workstation ID to retrieve scale settings </param><param name="ScaleID">Workstation default scale</param>
Notes:
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetScale(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetScale", {
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
   Summary: Invoke method GetShipDetails
   Description: This method displays the shipto address information when the ShipToNum field changes
Should only be called on new Shipments or if the Shipment has no lines and if
the MultipleShippers flag is yes
   OperationID: GetShipDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetShipDetails(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetShipDetails", {
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
   Summary: Invoke method GetSubPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetSubPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSubPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSubPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSubPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetSubPayBTFlagDefaults", {
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
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranDocTypeID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetTranDocTypeID", {
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
   Summary: Invoke method GetTransferPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ipPayFlag"> Pay Flag to retrieve defaults</param>
Notes:
   OperationID: GetTransferPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransferPayBTFlagDefaults(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetTransferPayBTFlagDefaults", {
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
   Summary: Invoke method OpenCarton
   Description: Checks to see if the carton can be opened and opens it if it is allowed.
   OperationID: OpenCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OpenCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/OpenCarton", {
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
   Summary: Invoke method ProcessFreightInfo
   Description: Purpose: Update the freighted shipment
<param name="iPackNum">The carton number of the carton to open </param><param name="ds">Freight Response data set</param><returns>The Masterpack data set </returns>
Notes:
   OperationID: ProcessFreightInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessFreightInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessFreightInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessFreightInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/ProcessFreightInfo", {
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
   Summary: Invoke method ProcessUnFreightInfo
   Description: Purpose: Update the freighted shipment
<param name="iPackNum">The carton number of the carton to open </param><param name="opWarnMsg">Warning message the UI is to present to the user</param><returns>The Masterpack data set </returns>
Notes:
   OperationID: ProcessUnFreightInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessUnFreightInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessUnFreightInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessUnFreightInfo(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/ProcessUnFreightInfo", {
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
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The Masterpack data set </param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVEnable(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/SetUPSQVEnable", {
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
   Summary: Invoke method SetUPSQVShipStatus
   Description: Purpose:
Parameters:
<param name="ipShipStatus">Shipment status</param><param name="ds">The Masterpack shipment data set </param>
Notes:
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVShipStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/SetUPSQVShipStatus", {
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
   Summary: Invoke method StageCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: StageCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StageCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_StageCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/StageCarton", {
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
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Purpose:  Calculate the CODAmount or DeclaredAmt
Parameters:
<param name="ipAmountType">COD or DeclaredAmt</param><param name="ipAction">Yes = recalculate No = reset to zero</param><param name="ds">Masterpack Shipment data set </param>
Notes:  Update the COD Amount and/or Declared Insurance amounts for manifesting purposes.
   OperationID: UpdateManifestChargeAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateManifestChargeAmts(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/UpdateManifestChargeAmts", {
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
   Summary: Invoke method VoidCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: VoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidCarton(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/VoidCarton", {
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
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VoidLegalNumber(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/VoidLegalNumber", {
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
   Summary: Invoke method CartonExists
   OperationID: CartonExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CartonExists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CartonExists", {
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
   Summary: Invoke method CheckCartonInShip
   OperationID: CheckCartonInShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCartonInShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCartonInShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCartonInShip(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CheckCartonInShip", {
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
   Summary: Invoke method CheckCartonStaged
   OperationID: CheckCartonStaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCartonStaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCartonStaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCartonStaged(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CheckCartonStaged", {
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
   Summary: Invoke method CheckShipStatus
   OperationID: CheckShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckShipStatus(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/CheckShipStatus", {
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
   Summary: Invoke method GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetCodeDescList", {
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
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetAvailTranDocTypes", {
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
   Summary: Invoke method GetListEnhanced
   Description: Purpose: Returns valid MasterPack Rows
Parameters:
<param name="ipType">type </param><param name="ipStatus">ipStatus</param><param name="ipSortBy">ipSortNy</param><param name="ipStartAtPackNum">ipStartAtPackNum</param><param name="ipStartAtShipDate">ipStartAtShipDate</param><param name="ipStartAtLegalNumber">ipStartAtLegalNumber</param><param name="ipShipViaCode">ipShipViaCode</param><param name="ipCustNum">ipCustNum</param><param name="ipShipToNum">ipShipToNum</param><param name="ipVendorNum">ipVendorNum</param><param name="pageSize">Page Size</param><param name="absolutePage">Absolute Page</param><param name="morePages">More Pages flag</param><returns>MasterpackListTableset dataset</returns>
Notes:
   OperationID: GetListEnhanced
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListEnhanced_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListEnhanced_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListEnhanced(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetListEnhanced", {
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
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateDigitalSignature(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GenerateDigitalSignature", {
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
   Summary: Invoke method GetNewMasterPack
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMasterPack(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetNewMasterPack", {
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
   Summary: Invoke method GetNewMasterPackAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMasterPackAttch(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetNewMasterPackAttch", {
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
   Summary: Invoke method GetNewMasterPackDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMasterPackDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetNewMasterPackDtl", {
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
   Summary: Invoke method GetNewMasterPackUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMasterPackUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMasterPackUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMasterPackUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMasterPackUPS(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetNewMasterPackUPS", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MasterPackSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonDetailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CartonDetailRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LegalNumGenOptsRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MasterPackAttchRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MasterPackDtlRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MasterPackRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterPackUPSRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MasterPackUPSRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MasterpackListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MasterpackListRow[],
}

export interface Erp_Tablesets_CartonDetailRow{
   "PackNum":number,
   "DtlPackNum":number,
   "OrderLine":number,
   "PartNumber":string,
   "Description":string,
   "PackQty":number,
   "QtyOrdered":number,
   "Company":string,
   "OrderNum":number,
      /**  Used by the freight web service  */  
   "partAESExp":string,
      /**  Used by the freight web service  */  
   "PartECNNumber":string,
      /**  Used by the freight web service  */  
   "PartExpLicNumber":string,
      /**  Used by the freight web service  */  
   "PartExpLicType":string,
      /**  Used by the freight web service  */  
   "PartHazClass":string,
      /**  Used by the freight web service  */  
   "PartHazGvrnmtID":string,
      /**  Used by the freight web service  */  
   "PartHazItem":boolean,
      /**  Used by the freight web service  */  
   "PartHazPackInstr":string,
      /**  Used by the freight web service  */  
   "PartHazSub":string,
      /**  Used by the freight web service  */  
   "PartHazTechName":string,
      /**  Used by the freight web service  */  
   "PartHTS":string,
      /**  Used by the freight web service  */  
   "PartNAFTAOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartNAFTAPref":string,
      /**  Used by the freight web service  */  
   "PartNAFTAProd":string,
      /**  Used by the freight web service  */  
   "PartOrigCountry":string,
      /**  Used by the freight web service  */  
   "PartSchedBCode":string,
      /**  Used by the freight web service  */  
   "PartUseHTSDesc":boolean,
   "PackQtyUom":string,
   "QtyOrderedUOM":string,
   "PackJobQty":number,
   "PackJobUom":string,
   "PackLine":number,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  AttributeSetID  */  
   "AttributeSetID":number,
      /**  ShortDescription  */  
   "AttributeSetShortDescription":string,
      /**  Optional field that contains the part  revision. Default from the RevisionNum field.  */  
   "RevisionNum":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   "Company":string,
   "LegalNumberID":string,
   "TransYear":number,
   "TransYearSuffix":string,
   "DspTransYear":string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   "ShowDspTransYear":boolean,
   "Prefix":string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   "PrefixList":string,
      /**  The suffix portion of the legal number.  */  
   "NumberSuffix":string,
      /**  Indicates if the prefix can be entered by the user.  */  
   "EnablePrefix":boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   "EnableSuffix":boolean,
   "NumberOption":string,
   "DocumentDate":string,
   "GenerationType":string,
   "Description":string,
   "TransPeriod":number,
      /**  Prefix for the period  */  
   "PeriodPrefix":string,
   "ShowTransPeriod":boolean,
      /**  Used when the full legal number is entered  */  
   "LegalNumber":string,
   "TranDocTypeID":string,
   "TranDocTypeID2":string,
   "GenerationOption":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MasterPackAttchRow{
   "Company":string,
   "PackNum":number,
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

export interface Erp_Tablesets_MasterPackDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Master pack packnum  */  
   "PackNum":number,
      /**  Carton number of the detail.  Links to a shipment header record ShipHead, etc.  */  
   "DtlPackNum":number,
      /**  An integer that uniquely identifies a detail record within a Master Pack. This is assigned by the system. Read last MasterPackDtl record for PackNum and add 1.  */  
   "MPackLine":number,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   "ShipmentType":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Used by the freight web service  */  
   "CertOfOrigin":boolean,
      /**  Used by the freight web service  */  
   "CommercialInvoice":boolean,
      /**  Used by the freight web service  */  
   "ConCity":string,
      /**  Used by the freight web service  */  
   "ConCompName":string,
      /**  Used by the freight web service  */  
   "ConContact":string,
      /**  Used by the freight web service  */  
   "ConCountry":string,
      /**  Used by the freight web service  */  
   "ConPhoneNum":string,
      /**  Used by the freight web service  */  
   "ConAddress1":string,
      /**  Used by the freight web service  */  
   "ConAddress2":string,
      /**  Used by the freight web service  */  
   "ConsigneeID":string,
      /**  Used by the freight web service  */  
   "ConState":string,
      /**  Used by the freight web service  */  
   "ConZip":string,
      /**  Used by the freight web service  */  
   "CustPONumber":string,
      /**  Used by the freight web service  */  
   "DropShip":boolean,
      /**  Used by the freight web service  */  
   "FFCity":string,
      /**  Used by the freight web service  */  
   "FFCompName":string,
      /**  Used by the freight web service  */  
   "FFContact":string,
      /**  Used by the freight web service  */  
   "FFCountry":string,
      /**  Used by the freight web service  */  
   "FFID":string,
      /**  Used by the freight web service  */  
   "FFPhoneNum":string,
      /**  Used by the freight web service  */  
   "FFAddress1":string,
      /**  Used by the freight web service  */  
   "FFAddress2":string,
      /**  Used by the freight web service  */  
   "FFState":string,
      /**  Used by the freight web service  */  
   "FFZip":string,
      /**  Used by the freight web service  */  
   "IntrntlShip":boolean,
      /**  Used by the freight web service  */  
   "JobNumber":string,
      /**  Used by the freight web service  */  
   "LetterOfInstr":boolean,
      /**  Used by the freight web service  */  
   "OrderNum":string,
      /**  Used by the freight web service  */  
   "PayAccount":string,
      /**  Used by the freight web service  */  
   "PayBTCity":string,
      /**  Used by the freight web service  */  
   "PayBTCountry":string,
      /**  Used by the freight web service  */  
   "PayBTAddress1":string,
      /**  Used by the freight web service  */  
   "PayBTAddress2":string,
      /**  Used by the freight web service  */  
   "PayBTState":string,
      /**  Used by the freight web service  */  
   "PayBTZip":string,
      /**  Used by the freight web service  */  
   "PayFlag":boolean,
      /**  Used by the freight web service  */  
   "ShipExprtDeclartn":boolean,
      /**  Used by the freight web service  */  
   "TotalOrderValue":number,
   "TotalOrderValueCurrencyUOM":string,
      /**  Readable translated description of ShipmentType  */  
   "ShipmentTypeDesc":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MasterPackRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   "ReadyToInvoice":boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   "Voided":boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External Identifier  */  
   "ExternalID":string,
      /**  Inter Company Received flag  */  
   "ICReceived":boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPackNum":string,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Packaging code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   "ShipmentType":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling Required flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Package flag.  */  
   "NonStdPkg":boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   "FFCountryNum":number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress3":string,
      /**  Shipping, The country number of the Payer main address.  */  
   "PayBTCountryNum":number,
      /**  Shipping, The phone number of the Payer main address.  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantity View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantity View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantity View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  This field is reserved for future development.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  */  
   "OurBank":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAuthorizationCode  */  
   "AGAuthorizationCode":string,
      /**  AGAuthorizationDate  */  
   "AGAuthorizationDate":string,
      /**  AGCarrierCUIT  */  
   "AGCarrierCUIT":string,
      /**  AGDocumentLetter  */  
   "AGDocumentLetter":string,
      /**  AGInvoicingPoint  */  
   "AGInvoicingPoint":string,
      /**  AGLegalNumber  */  
   "AGLegalNumber":string,
      /**  AGPrintingControlType  */  
   "AGPrintingControlType":string,
      /**  AGTrackLicense  */  
   "AGTrackLicense":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  DigitalSignature  */  
   "DigitalSignature":string,
      /**  SignedOn  */  
   "SignedOn":string,
      /**  SignedBy  */  
   "SignedBy":string,
      /**  FirstPrintDate  */  
   "FirstPrintDate":string,
      /**  DocCopyNum  */  
   "DocCopyNum":number,
   "BillToAddrList":string,
      /**  Indicates of TranDocTypeID is available for input  */  
   "EnableTranDocType":boolean,
      /**  Indicates if the option to void the legal number is available  */  
   "EnableVoidLegNum":boolean,
      /**  Logical indicating to the UI that the weight prompt is to be enabled.  */  
   "EnableWeight":boolean,
      /**  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  */  
   "HasCartonLines":boolean,
      /**  Indicates if a legal number configuration is setup for master pack  */  
   "HasLegNumCnfg":boolean,
   "LegalNumberMessage":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Zero indicates the height field is enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length field is enabled.  */  
   "PkgLenEnable":number,
      /**  Zero indicates the width field is enabled.  */  
   "PkgWidthEnable":number,
   "ShipStatusDescription":string,
   "SoldToAddrList":string,
   "AddrList":string,
      /**  Indicates if information on the master pack can be modified after the document has been printed.  */  
   "AllowChgAfterPrint":boolean,
      /**  The sumo of the value of the items in the carton  */  
   "CartonContentValue":number,
      /**  Carton height  */  
   "CartonHeight":number,
      /**  carton Length  */  
   "CartonLength":number,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
      /**  Carton width  */  
   "CartonWidth":number,
      /**  Indicates if the option to assign a legal number is available.  */  
   "EnableAssignLegNum":boolean,
   "DspDigitalSignature":string,
   "QSUseBOL":boolean,
   "QSUseIntl":boolean,
   "QSUseCO":boolean,
      /**  Formatted address column for ShipTo field  */  
   "ShipToAddrFormatted":string,
      /**  Formatted address column for Sold To  */  
   "SoldToAddrFormatted":string,
   "BitFlag":number,
   "AGInvoicingPointDescription":string,
   "CustomerCustID":string,
   "CustomerBTName":string,
   "CustomerName":string,
   "DeliveryTypeDescription":string,
   "FreightedShipViaCodeWebDesc":string,
   "FreightedShipViaCodeDescription":string,
   "OurBankDescription":string,
   "OurBankBankName":string,
   "ShipViaCodeWebDesc":string,
   "ShipViaCodeDescription":string,
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MasterPackUPSRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  UPS Quantity View Sequence  */  
   "UPSQVSeq":number,
      /**  Email adress to be used for notifications.  */  
   "EmailAddress":string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating if the UPS Quantum View is to be enabled.  */  
   "EnableQuantumView":boolean,
   "ShipStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MasterpackListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  */  
   "PackNum":number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   "ShipDate":string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   "ShipViaCode":string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   "ShipPerson":string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   "ShipLog":string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   "LabelComment":string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   "ShipComment":string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   "Invoiced":boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   "ShipToNum":string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   "ReadyToInvoice":boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   "CustNum":number,
      /**  The Site that shipment was made from.  */  
   "Plant":string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   "TrackingNumber":string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   "Voided":boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   "ExternalDeliveryNote":boolean,
      /**  External Identifier  */  
   "ExternalID":string,
      /**  Inter Company Received flag  */  
   "ICReceived":boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   "XRefPackNum":string,
      /**  Populated from OrderHed.BTCustNum.  */  
   "BTCustNum":number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   "BTConNum":number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   "ShipStatus":string,
      /**  Group the shipment belongs to for "Staging"  */  
   "ShipGroup":string,
      /**  Packaging code  */  
   "PkgCode":string,
      /**  NMFC Packaging Classification code.  */  
   "PkgClass":string,
      /**  Package Weight  */  
   "Weight":number,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Transaction Number returned by the Manifest Engine  */  
   "MFTransNum":string,
      /**  Manifest Call Tag Number  */  
   "MFCallTag":string,
      /**  Manifest Pickup Number  */  
   "MFPickupNum":string,
      /**  Manifest Discount Freight Amount  */  
   "MFDiscFreight":number,
      /**  Manifest Template Code  */  
   "MFTemplate":string,
      /**  Manifest flag to use 3 party billing  */  
   "MFUse3B":boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   "MF3BAccount":string,
      /**  Manifest Dimension Weight  */  
   "MFDimWeight":number,
      /**  Manifest Delivery Zone  */  
   "MFZone":string,
      /**  Manifest Published Freight Amount  */  
   "MFFreightAmt":number,
      /**  Manifest Other Amount  */  
   "MFOtherAmt":number,
      /**  Manifest Oversized flag  */  
   "MFOversized":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   "ShipmentType":string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   "BOLNum":number,
      /**  Bill of Lading line number linked to  */  
   "BOLLine":number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   "CommercialInvoice":boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   "ShipExprtDeclartn":boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   "CertOfOrigin":boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   "LetterOfInstr":boolean,
      /**  International Shipping - HazardousShipment  */  
   "HazardousShipment":boolean,
      /**  Is this an International shipment  */  
   "IntrntlShip":boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayFlag":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   "PayBTAddress1":string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress2":string,
      /**  Shipping, The city portion of the Payer main address.  */  
   "PayBTCity":string,
      /**  The state or province portion of the shipment payer main address.  */  
   "PayBTState":string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   "PayBTZip":string,
      /**  The country of the main shipping payers address.  */  
   "PayBTCountry":string,
      /**  International Shipping. Frieght Forwarder ID  */  
   "FFID":string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   "FFAddress1":string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   "FFAddress2":string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   "FFCity":string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   "FFState":string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   "FFZip":string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   "FFCountry":string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   "FFContact":string,
      /**  International Shipping. Frieght Forwarder company name  */  
   "FFCompName":string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   "FFPhoneNum":string,
      /**  Userid of user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date that the record was last changed  */  
   "ChangeDate":string,
      /**  The time that the record was last change (seconds since midnight)  */  
   "ChangeTime":number,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   "FFAddress3":string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Additional Handling Required flag  */  
   "AddlHdlgFlag":boolean,
      /**  Non Standard Package flag.  */  
   "NonStdPkg":boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   "FFCountryNum":number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   "PayBTAddress3":string,
      /**  Shipping, The country number of the Payer main address.  */  
   "PayBTCountryNum":number,
      /**  Shipping, The phone number of the Payer main address.  */  
   "PayBTPhone":string,
      /**  Way Bill Number  */  
   "WayBillNbr":string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   "FreightedShipViaCode":string,
      /**  UPS Quantity View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantity View Ship from Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantity View Memo  */  
   "UPSQVMemo":string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   "PkgLength":number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   "PkgWidth":number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   "PkgHeight":number,
      /**  Defines if this document is marked as EDI Ready  */  
   "EDIReady":boolean,
      /**  This field is reserved for future development.  */  
   "PhantomPack":boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   "PkgSizeUOM":string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   "WeightUOM":string,
      /**  Transaction document type id.  */  
   "TranDocTypeID":string,
      /**  Indicates if the document has been printed.  */  
   "DocumentPrinted":boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   "ShipToCustNum":number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   "DeviceUOM":string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   "ManifestSizeUOM":string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   "ManifestWtUOM":string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   "ManifestWeight":number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   "ManifestLength":number,
      /**  The pack width in the manifest unit of measure.  */  
   "ManifestWidth":number,
      /**  The pack height in the manifest unit of measure.  */  
   "ManifestHeight":number,
      /**  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  */  
   "OurBank":string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "AddrList":string,
   "ShipStatusDescription":string,
      /**  Carton height  */  
   "CartonHeight":number,
      /**  Carton width  */  
   "CartonWidth":number,
      /**  carton Length  */  
   "CartonLength":number,
      /**  The sumo of the value of the items in the carton  */  
   "CartonContentValue":number,
      /**  Carton Stage Number.  */  
   "CartonStageNbr":string,
      /**  Indicates if the manifest interface is enabled.  */  
   "ManifestFlag":boolean,
      /**  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  */  
   "HasCartonLines":boolean,
      /**  Zero indicates the height field is enabled.  */  
   "PkgHeightEnable":number,
      /**  Zero indicates the length field is enabled.  */  
   "PkgLenEnable":number,
      /**  Zero indicates the width field is enabled.  */  
   "PkgWidthEnable":number,
      /**  Logical indicating to the UI that the weight prompt is to be enabled.  */  
   "EnableWeight":boolean,
      /**  Indicates if the option to assign a legal number is available.  */  
   "EnableAssignLegNum":boolean,
      /**  Indicates if the option to void the legal number is available  */  
   "EnableVoidLegNum":boolean,
      /**  Indicates if a legal number configuration is setup for master pack  */  
   "HasLegNumCnfg":boolean,
      /**  Indicates if information on the master pack can be modified after the document has been printed.  */  
   "AllowChgAfterPrint":boolean,
      /**  Indicates of TranDocTypeID is available for input  */  
   "EnableTranDocType":boolean,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  Description of delivery type  */  
   "DeliveryTypeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "FreightedShipViaCodeWebDesc":string,
      /**  Full description for the shipping company (carrier).  */  
   "FreightedShipViaCodeDescription":string,
      /**  The Bank's full name.  */  
   "OurBankBankName":string,
      /**  Full description of the bank account.  */  
   "OurBankDescription":string,
      /**  Full description for the shipping company (carrier).  */  
   "ShipViaCodeDescription":string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   "ShipViaCodeWebDesc":string,
      /**  Description  */  
   "TranDocTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface AssignLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface AssignLegalNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
   opLegalNumMsg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CalculateWeight_input{
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface CalculateWeight_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
   weight:number,
}
}

   /** Required : 
      @param iPackNum
   */  
export interface CancelVoidCarton_input{
      /**  The carton number of the carton to open  */  
   iPackNum:number,
}

export interface CancelVoidCarton_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
}

   /** Required : 
      @param packNum
      @param shipmentType
   */  
export interface CartonExists_input{
   packNum:number,
   shipmentType:string,
}

export interface CartonExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param packNum
      @param shipViaCode
      @param shipToNum
      @param shipmentType
      @param custNum
      @param masterPackNum
   */  
export interface CheckCartonInShip_input{
   packNum:number,
   shipViaCode:string,
   shipToNum:string,
   shipmentType:string,
   custNum:number,
   masterPackNum:number,
}

export interface CheckCartonInShip_output{
   returnObj:boolean,
}

   /** Required : 
      @param packNum
      @param shipmentType
   */  
export interface CheckCartonStaged_input{
   packNum:number,
   shipmentType:string,
}

export interface CheckCartonStaged_output{
   returnObj:boolean,
}

   /** Required : 
      @param packNum
      @param shipmentType
   */  
export interface CheckShipStatus_input{
   packNum:number,
   shipmentType:string,
}

export interface CheckShipStatus_output{
   returnObj:string,
}

   /** Required : 
      @param ipPackNum
   */  
export interface ClearConvertedManifest_input{
   ipPackNum:number,
}

export interface ClearConvertedManifest_output{
}

   /** Required : 
      @param iPackNum
      @param ds
   */  
export interface CloseCarton_input{
      /**  The carton number of the carton to close  */  
   iPackNum:number,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface CloseCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPackNum
   */  
export interface ConvertToManifestUOM_input{
   ipPackNum:number,
}

export interface ConvertToManifestUOM_output{
}

   /** Required : 
      @param packNum
   */  
export interface DeleteByID_input{
   packNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CartonDetailRow{
   PackNum:number,
   DtlPackNum:number,
   OrderLine:number,
   PartNumber:string,
   Description:string,
   PackQty:number,
   QtyOrdered:number,
   Company:string,
   OrderNum:number,
      /**  Used by the freight web service  */  
   partAESExp:string,
      /**  Used by the freight web service  */  
   PartECNNumber:string,
      /**  Used by the freight web service  */  
   PartExpLicNumber:string,
      /**  Used by the freight web service  */  
   PartExpLicType:string,
      /**  Used by the freight web service  */  
   PartHazClass:string,
      /**  Used by the freight web service  */  
   PartHazGvrnmtID:string,
      /**  Used by the freight web service  */  
   PartHazItem:boolean,
      /**  Used by the freight web service  */  
   PartHazPackInstr:string,
      /**  Used by the freight web service  */  
   PartHazSub:string,
      /**  Used by the freight web service  */  
   PartHazTechName:string,
      /**  Used by the freight web service  */  
   PartHTS:string,
      /**  Used by the freight web service  */  
   PartNAFTAOrigCountry:string,
      /**  Used by the freight web service  */  
   PartNAFTAPref:string,
      /**  Used by the freight web service  */  
   PartNAFTAProd:string,
      /**  Used by the freight web service  */  
   PartOrigCountry:string,
      /**  Used by the freight web service  */  
   PartSchedBCode:string,
      /**  Used by the freight web service  */  
   PartUseHTSDesc:boolean,
   PackQtyUom:string,
   QtyOrderedUOM:string,
   PackJobQty:number,
   PackJobUom:string,
   PackLine:number,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  AttributeSetID  */  
   AttributeSetID:number,
      /**  ShortDescription  */  
   AttributeSetShortDescription:string,
      /**  Optional field that contains the part  revision. Default from the RevisionNum field.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightCartonResponseRow{
   CallTagNumber:string,
   DimWeight:number,
   DimWeightUOM:string,
   DiscountFreightAmount:number,
   DiscountFreightAmountUOM:string,
   ErrorFlag:boolean,
   ErrorMessage:string,
   EstimatedFreightAmount:number,
   EstimatedFreightAmountUOM:string,
   EstimatedFreightFlag:boolean,
   FreightZone:string,
   OtherAmount:number,
   OtherAmountUOM:string,
   OversizeFlag:boolean,
   PickupNumber:string,
   PublishedFreightAmount:number,
   PublishedFreightAmountUOM:string,
   ShipDate:string,
   TemplateCode:string,
   TransactionNumber:string,
   WayBillNbr:string,
   FreightedShipVia:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightCartonResponseTrackingRow{
   TrackingNumber:string,
   PackID:number,
      /**  Discounted freight amount calculated by the shipper  */  
   DiscountFreightAmt:number,
      /**  Published freight amount determined by the shipper.  */  
   PublishedFreightAmt:number,
      /**  Concatenation of the pack num and sequential case number.  */  
   CaseNum:string,
      /**  Shipment type  */  
   ShipmentType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FreightInfoResponseTableset{
   FreightCartonResponse:Erp_Tablesets_FreightCartonResponseRow[],
   FreightCartonResponseTracking:Erp_Tablesets_FreightCartonResponseTrackingRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterPackAttchRow{
   Company:string,
   PackNum:number,
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

export interface Erp_Tablesets_MasterPackDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Master pack packnum  */  
   PackNum:number,
      /**  Carton number of the detail.  Links to a shipment header record ShipHead, etc.  */  
   DtlPackNum:number,
      /**  An integer that uniquely identifies a detail record within a Master Pack. This is assigned by the system. Read last MasterPackDtl record for PackNum and add 1.  */  
   MPackLine:number,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   ShipmentType:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Used by the freight web service  */  
   CertOfOrigin:boolean,
      /**  Used by the freight web service  */  
   CommercialInvoice:boolean,
      /**  Used by the freight web service  */  
   ConCity:string,
      /**  Used by the freight web service  */  
   ConCompName:string,
      /**  Used by the freight web service  */  
   ConContact:string,
      /**  Used by the freight web service  */  
   ConCountry:string,
      /**  Used by the freight web service  */  
   ConPhoneNum:string,
      /**  Used by the freight web service  */  
   ConAddress1:string,
      /**  Used by the freight web service  */  
   ConAddress2:string,
      /**  Used by the freight web service  */  
   ConsigneeID:string,
      /**  Used by the freight web service  */  
   ConState:string,
      /**  Used by the freight web service  */  
   ConZip:string,
      /**  Used by the freight web service  */  
   CustPONumber:string,
      /**  Used by the freight web service  */  
   DropShip:boolean,
      /**  Used by the freight web service  */  
   FFCity:string,
      /**  Used by the freight web service  */  
   FFCompName:string,
      /**  Used by the freight web service  */  
   FFContact:string,
      /**  Used by the freight web service  */  
   FFCountry:string,
      /**  Used by the freight web service  */  
   FFID:string,
      /**  Used by the freight web service  */  
   FFPhoneNum:string,
      /**  Used by the freight web service  */  
   FFAddress1:string,
      /**  Used by the freight web service  */  
   FFAddress2:string,
      /**  Used by the freight web service  */  
   FFState:string,
      /**  Used by the freight web service  */  
   FFZip:string,
      /**  Used by the freight web service  */  
   IntrntlShip:boolean,
      /**  Used by the freight web service  */  
   JobNumber:string,
      /**  Used by the freight web service  */  
   LetterOfInstr:boolean,
      /**  Used by the freight web service  */  
   OrderNum:string,
      /**  Used by the freight web service  */  
   PayAccount:string,
      /**  Used by the freight web service  */  
   PayBTCity:string,
      /**  Used by the freight web service  */  
   PayBTCountry:string,
      /**  Used by the freight web service  */  
   PayBTAddress1:string,
      /**  Used by the freight web service  */  
   PayBTAddress2:string,
      /**  Used by the freight web service  */  
   PayBTState:string,
      /**  Used by the freight web service  */  
   PayBTZip:string,
      /**  Used by the freight web service  */  
   PayFlag:boolean,
      /**  Used by the freight web service  */  
   ShipExprtDeclartn:boolean,
      /**  Used by the freight web service  */  
   TotalOrderValue:number,
   TotalOrderValueCurrencyUOM:string,
      /**  Readable translated description of ShipmentType  */  
   ShipmentTypeDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterPackRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Inter Company Received flag  */  
   ICReceived:boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPackNum:string,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Packaging code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   ShipmentType:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   FFCountryNum:number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress3:string,
      /**  Shipping, The country number of the Payer main address.  */  
   PayBTCountryNum:number,
      /**  Shipping, The phone number of the Payer main address.  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantity View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  This field is reserved for future development.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  */  
   OurBank:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGCarrierCUIT  */  
   AGCarrierCUIT:string,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  AGTrackLicense  */  
   AGTrackLicense:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
   BillToAddrList:string,
      /**  Indicates of TranDocTypeID is available for input  */  
   EnableTranDocType:boolean,
      /**  Indicates if the option to void the legal number is available  */  
   EnableVoidLegNum:boolean,
      /**  Logical indicating to the UI that the weight prompt is to be enabled.  */  
   EnableWeight:boolean,
      /**  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  */  
   HasCartonLines:boolean,
      /**  Indicates if a legal number configuration is setup for master pack  */  
   HasLegNumCnfg:boolean,
   LegalNumberMessage:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Zero indicates the height field is enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length field is enabled.  */  
   PkgLenEnable:number,
      /**  Zero indicates the width field is enabled.  */  
   PkgWidthEnable:number,
   ShipStatusDescription:string,
   SoldToAddrList:string,
   AddrList:string,
      /**  Indicates if information on the master pack can be modified after the document has been printed.  */  
   AllowChgAfterPrint:boolean,
      /**  The sumo of the value of the items in the carton  */  
   CartonContentValue:number,
      /**  Carton height  */  
   CartonHeight:number,
      /**  carton Length  */  
   CartonLength:number,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
      /**  Carton width  */  
   CartonWidth:number,
      /**  Indicates if the option to assign a legal number is available.  */  
   EnableAssignLegNum:boolean,
   DspDigitalSignature:string,
   QSUseBOL:boolean,
   QSUseIntl:boolean,
   QSUseCO:boolean,
      /**  Formatted address column for ShipTo field  */  
   ShipToAddrFormatted:string,
      /**  Formatted address column for Sold To  */  
   SoldToAddrFormatted:string,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   DeliveryTypeDescription:string,
   FreightedShipViaCodeWebDesc:string,
   FreightedShipViaCodeDescription:string,
   OurBankDescription:string,
   OurBankBankName:string,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterPackTableset{
   MasterPack:Erp_Tablesets_MasterPackRow[],
   MasterPackAttch:Erp_Tablesets_MasterPackAttchRow[],
   MasterPackDtl:Erp_Tablesets_MasterPackDtlRow[],
   MasterPackUPS:Erp_Tablesets_MasterPackUPSRow[],
   CartonDetail:Erp_Tablesets_CartonDetailRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MasterPackUPSRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  UPS Quantity View Sequence  */  
   UPSQVSeq:number,
      /**  Email adress to be used for notifications.  */  
   EmailAddress:string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating if the UPS Quantum View is to be enabled.  */  
   EnableQuantumView:boolean,
   ShipStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterpackListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new Master pack, the user is prompted for a master pack number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last Masterpack on file and uses its PackNum + 1.  */  
   PackNum:number,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  */  
   ShipViaCode:string,
      /**  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  */  
   ShipPerson:string,
      /**  An optional field which can be used to enter a shipping log reference #.  */  
   ShipLog:string,
      /**  An optional field that will be printed on the shipping labels for this packing slip.  */  
   LabelComment:string,
      /**  Packing slip comments.  This will print on the Packing Slip.  */  
   ShipComment:string,
      /**  Used internally to indicate if the user has pulled this packing slip into invoice processing.  This does NOT ensure that the packing slip has been invoiced.  Only that it was functionally pulled into the invoice process.  This may also be set to "Yes" if the user does not want to use the shipments for generating invoices.  This is condition is indicated when ArSyst.SaveShipments = No.  Under this condition Shipping Entry would initialize "invoiced" to Yes, preventing invoice entry from pulling them in.  This feature would normally be used during the startup period when they do not yet have A/R fully implemented.  */  
   Invoiced:boolean,
      /**  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Indicates if the Packing Slip is complete and ready for invoicing. The invoice entry "Get Shipments" function will only select where ShipHead.ReadyToInvoice = Yes  */  
   ReadyToInvoice:boolean,
      /**  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  */  
   CustNum:number,
      /**  The Site that shipment was made from.  */  
   Plant:string,
      /**  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  */  
   TrackingNumber:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  A flag indicating if this is shipment voided.  This flag is updated via input from the user.  Once a shipment has been voided it can no longer be updated or invoiced.  */  
   Voided:boolean,
      /**  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  */  
   ExternalDeliveryNote:boolean,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Inter Company Received flag  */  
   ICReceived:boolean,
      /**  Cross reference Packing Slip number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefPackNum:string,
      /**  Populated from OrderHed.BTCustNum.  */  
   BTCustNum:number,
      /**  Bill To Customer Contact number.  This will populate from the OrderHed.BTConNum.  */  
   BTConNum:number,
      /**  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  */  
   ShipStatus:string,
      /**  Group the shipment belongs to for "Staging"  */  
   ShipGroup:string,
      /**  Packaging code  */  
   PkgCode:string,
      /**  NMFC Packaging Classification code.  */  
   PkgClass:string,
      /**  Package Weight  */  
   Weight:number,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Transaction Number returned by the Manifest Engine  */  
   MFTransNum:string,
      /**  Manifest Call Tag Number  */  
   MFCallTag:string,
      /**  Manifest Pickup Number  */  
   MFPickupNum:string,
      /**  Manifest Discount Freight Amount  */  
   MFDiscFreight:number,
      /**  Manifest Template Code  */  
   MFTemplate:string,
      /**  Manifest flag to use 3 party billing  */  
   MFUse3B:boolean,
      /**  Manifest's 3rd Party Billing Account  */  
   MF3BAccount:string,
      /**  Manifest Dimension Weight  */  
   MFDimWeight:number,
      /**  Manifest Delivery Zone  */  
   MFZone:string,
      /**  Manifest Published Freight Amount  */  
   MFFreightAmt:number,
      /**  Manifest Other Amount  */  
   MFOtherAmt:number,
      /**  Manifest Oversized flag  */  
   MFOversized:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  different types of cartonized shipments. Valid values are: "Sales" for sales order , "Transfer" for inter company transfer , "Sub" for subcontract, "Misc" for Miscellanous  */  
   ShipmentType:string,
      /**  Bill of Lading Number the packing slip is linked to  */  
   BOLNum:number,
      /**  Bill of Lading line number linked to  */  
   BOLLine:number,
      /**  Added for international shipping, Is a commercial invoice required  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration required  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin required.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping - HazardousShipment  */  
   HazardousShipment:boolean,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  International Shipping. The third line of the Freight Forwarder main address.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  International Shipping. The country number of the Freight Forwarder main address.  */  
   FFCountryNum:number,
      /**  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress3:string,
      /**  Shipping, The country number of the Payer main address.  */  
   PayBTCountryNum:number,
      /**  Shipping, The phone number of the Payer main address.  */  
   PayBTPhone:string,
      /**  Way Bill Number  */  
   WayBillNbr:string,
      /**  This is the ship via code the freighting system selected for shipping.  */  
   FreightedShipViaCode:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantity View Ship from Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  Length dimension for the packaging used to ship this shipment.  */  
   PkgLength:number,
      /**  Width dimension for the packaging used to ship this shipment.  */  
   PkgWidth:number,
      /**  Height dimension for the packaging used to ship this shipment.  */  
   PkgHeight:number,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  This field is reserved for future development.  */  
   PhantomPack:boolean,
      /**   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  */  
   PkgSizeUOM:string,
      /**   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  */  
   WeightUOM:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  */  
   DeviceUOM:string,
      /**  Unit of Measure the Manifest system expects the pack sizet to be measured in.  */  
   ManifestSizeUOM:string,
      /**  Unit of Measure of the Manifest system expects the pack to be weighed in.  */  
   ManifestWtUOM:string,
      /**  Package Weight in the Manifest System's unit of measure.  */  
   ManifestWeight:number,
      /**  The pack length in the Manifest Unit of Measure.  */  
   ManifestLength:number,
      /**  The pack width in the manifest unit of measure.  */  
   ManifestWidth:number,
      /**  The pack height in the manifest unit of measure.  */  
   ManifestHeight:number,
      /**  Bank for Cash Receipts. It is set only for ShipmentType 'Sales', default for this type is got from 1) Sales Order 2) Bill To Customer 3) System Default(Company).  */  
   OurBank:string,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   AddrList:string,
   ShipStatusDescription:string,
      /**  Carton height  */  
   CartonHeight:number,
      /**  Carton width  */  
   CartonWidth:number,
      /**  carton Length  */  
   CartonLength:number,
      /**  The sumo of the value of the items in the carton  */  
   CartonContentValue:number,
      /**  Carton Stage Number.  */  
   CartonStageNbr:string,
      /**  Indicates if the manifest interface is enabled.  */  
   ManifestFlag:boolean,
      /**  Logical indicating if lines already exist.  Used to determine if the freight fields need to be defaulted.  */  
   HasCartonLines:boolean,
      /**  Zero indicates the height field is enabled.  */  
   PkgHeightEnable:number,
      /**  Zero indicates the length field is enabled.  */  
   PkgLenEnable:number,
      /**  Zero indicates the width field is enabled.  */  
   PkgWidthEnable:number,
      /**  Logical indicating to the UI that the weight prompt is to be enabled.  */  
   EnableWeight:boolean,
      /**  Indicates if the option to assign a legal number is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if the option to void the legal number is available  */  
   EnableVoidLegNum:boolean,
      /**  Indicates if a legal number configuration is setup for master pack  */  
   HasLegNumCnfg:boolean,
      /**  Indicates if information on the master pack can be modified after the document has been printed.  */  
   AllowChgAfterPrint:boolean,
      /**  Indicates of TranDocTypeID is available for input  */  
   EnableTranDocType:boolean,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  Description of delivery type  */  
   DeliveryTypeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   FreightedShipViaCodeWebDesc:string,
      /**  Full description for the shipping company (carrier).  */  
   FreightedShipViaCodeDescription:string,
      /**  The Bank's full name.  */  
   OurBankBankName:string,
      /**  Full description of the bank account.  */  
   OurBankDescription:string,
      /**  Full description for the shipping company (carrier).  */  
   ShipViaCodeDescription:string,
      /**  "External" Ship Via description for Customer Connect (StoreFront) selection.  */  
   ShipViaCodeWebDesc:string,
      /**  Description  */  
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MasterpackListTableset{
   MasterpackList:Erp_Tablesets_MasterpackListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMasterPackTableset{
   MasterPack:Erp_Tablesets_MasterPackRow[],
   MasterPackAttch:Erp_Tablesets_MasterPackAttchRow[],
   MasterPackDtl:Erp_Tablesets_MasterPackDtlRow[],
   MasterPackUPS:Erp_Tablesets_MasterPackUPSRow[],
   CartonDetail:Erp_Tablesets_CartonDetailRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
   */  
export interface GenerateDigitalSignature_input{
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GenerateDigitalSignature_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param packNum
   */  
export interface GetByID_input{
   packNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
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
      @param ipPayFlag
   */  
export interface GetCustPayBTFlagDefaults_input{
   ipPayFlag:string,
}

export interface GetCustPayBTFlagDefaults_output{
}

   /** Required : 
      @param ipPackNum
      @param ds
   */  
export interface GetLegalNumGenOpts_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetLegalNumGenOpts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
   opPromptForNum:boolean,
}
}

   /** Required : 
      @param ipType
      @param ipStatus
      @param ipSortBy
      @param ipStartAtPackNum
      @param ipStartAtShipDate
      @param ipStartAtLegalNumber
      @param ipShipViaCode
      @param ipCustNum
      @param ipShipToNum
      @param ipVendorNum
      @param pageSize
      @param absolutePage
   */  
export interface GetListEnhanced_input{
   ipType:string,
   ipStatus:string,
   ipSortBy:string,
   ipStartAtPackNum:number,
   ipStartAtShipDate:string,
   ipStartAtLegalNumber:string,
   ipShipViaCode:string,
   ipCustNum:number,
   ipShipToNum:string,
   ipVendorNum:number,
   pageSize:number,
   absolutePage:number,
}

export interface GetListEnhanced_output{
   returnObj:Erp_Tablesets_MasterpackListTableset[],
parameters : {
      /**  output parameters  */  
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
   returnObj:Erp_Tablesets_MasterpackListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPayFlag
   */  
export interface GetMiscPayBTFlagDefaults_input{
   ipPayFlag:string,
}

export interface GetMiscPayBTFlagDefaults_output{
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewMasterPackAttch_input{
   ds:Erp_Tablesets_MasterPackTableset[],
   packNum:number,
}

export interface GetNewMasterPackAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ds
      @param mpackLine
   */  
export interface GetNewMasterPackDtl_input{
   ds:Erp_Tablesets_MasterPackTableset[],
   mpackLine:number,
}

export interface GetNewMasterPackDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ds
      @param packNum
   */  
export interface GetNewMasterPackUPS_input{
   ds:Erp_Tablesets_MasterPackTableset[],
   packNum:number,
}

export interface GetNewMasterPackUPS_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMasterPack_input{
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetNewMasterPack_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPkgClass
      @param ds
   */  
export interface GetPackClass_input{
   ipPkgClass:string,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetPackClass_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPkgCode
      @param ds
   */  
export interface GetPackaging_input{
   ipPkgCode:string,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetPackaging_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPayFlag
      @param ds
   */  
export interface GetPayBTFlagDefaults_input{
   ipPayFlag:string,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetPayBTFlagDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param whereClauseMasterPack
      @param whereClauseMasterPackAttch
      @param whereClauseMasterPackDtl
      @param whereClauseMasterPackUPS
      @param whereClauseCartonDetail
      @param whereClauseLegalNumGenOpts
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMasterPack:string,
   whereClauseMasterPackAttch:string,
   whereClauseMasterPackDtl:string,
   whereClauseMasterPackUPS:string,
   whereClauseCartonDetail:string,
   whereClauseLegalNumGenOpts:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param workstationID
   */  
export interface GetScale_input{
   workstationID:string,
}

export interface GetScale_output{
parameters : {
      /**  output parameters  */  
   ScaleID:string,
}
}

   /** Required : 
      @param ds
      @param PackNum
      @param DtlPackNum
      @param ShipmentType
   */  
export interface GetShipDetails_input{
   ds:Erp_Tablesets_MasterPackTableset[],
      /**  Master Pack ID  */  
   PackNum:number,
      /**  Detail Pack ID  */  
   DtlPackNum:number,
      /**  Shipment type:Sales,Misc,Sub or Transfer  */  
   ShipmentType:string,
}

export interface GetShipDetails_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPayFlag
   */  
export interface GetSubPayBTFlagDefaults_input{
   ipPayFlag:string,
}

export interface GetSubPayBTFlagDefaults_output{
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface GetTranDocTypeID_input{
      /**  TranDocTypeID supplied  */  
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface GetTranDocTypeID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipPayFlag
   */  
export interface GetTransferPayBTFlagDefaults_input{
   ipPayFlag:string,
}

export interface GetTransferPayBTFlagDefaults_output{
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
      @param iPackNum
      @param ipResetCODCharges
      @param ipResetInsCharges
   */  
export interface OpenCarton_input{
      /**  The carton number of the carton to open  */  
   iPackNum:number,
      /**  Indicates if the CODAmount is to be reset to zero  */  
   ipResetCODCharges:boolean,
      /**  Indicates if the DeclaredAmt is to be reset to zero  */  
   ipResetInsCharges:boolean,
}

export interface OpenCarton_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param iPackNum
      @param ds
   */  
export interface ProcessFreightInfo_input{
   iPackNum:number,
   ds:Erp_Tablesets_FreightInfoResponseTableset[],
}

export interface ProcessFreightInfo_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FreightInfoResponseTableset[],
}
}

   /** Required : 
      @param iPackNum
   */  
export interface ProcessUnFreightInfo_input{
   iPackNum:number,
}

export interface ProcessUnFreightInfo_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
}
}

   /** Required : 
      @param ipQVEnable
      @param ds
   */  
export interface SetUPSQVEnable_input{
   ipQVEnable:boolean,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ipShipStatus
      @param ds
   */  
export interface SetUPSQVShipStatus_input{
   ipShipStatus:string,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface SetUPSQVShipStatus_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param iPackNum
      @param ds
   */  
export interface StageCarton_input{
      /**  The carton number of the carton to Stage  */  
   iPackNum:number,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface StageCarton_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMasterPackTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMasterPackTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ipAmountType
      @param ipAction
      @param ds
   */  
export interface UpdateManifestChargeAmts_input{
   ipAmountType:string,
   ipAction:boolean,
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface UpdateManifestChargeAmts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MasterPackTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MasterPackTableset[],
}
}

   /** Required : 
      @param iPackNum
   */  
export interface VoidCarton_input{
      /**  The carton number of the carton to void  */  
   iPackNum:number,
}

export interface VoidCarton_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
}

   /** Required : 
      @param ipPackNum
      @param ipVoidedReason
   */  
export interface VoidLegalNumber_input{
      /**  Packing Slip number  */  
   ipPackNum:number,
      /**  Reason for the void  */  
   ipVoidedReason:string,
}

export interface VoidLegalNumber_output{
   returnObj:Erp_Tablesets_MasterPackTableset[],
}

