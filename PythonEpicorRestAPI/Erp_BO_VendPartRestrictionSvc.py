import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendPartRestrictionSvc
# Description: Vendor Part Price - Restriction Substances
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendPartRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartRestrictions
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_VendPartRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPartRestriction item
   Description: Calls GetByID to retrieve the VendPartRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPartRestriction for the service
   Description: Calls UpdateExt to update VendPartRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPartRestriction item
   Description: Call UpdateExt to delete VendPartRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_VendPartRestrictSubsts(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendPartRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPartRestrictSubsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")/VendPartRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictions_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPartRestrictSubst item
   Description: Calls GetByID to retrieve the VendPartRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestrictSubst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictions(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + ")/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictSubsts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendPartRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPartRestrictSubsts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def post_VendPartRestrictSubsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPartRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPartRestrictSubst item
   Description: Calls GetByID to retrieve the VendPartRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPartRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, SubstanceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPartRestrictSubst for the service
   Description: Calls UpdateExt to update VendPartRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPartRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPartRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendPartRestrictSubsts_Company_PartNum_OpCode_PUM_VendorNum_RestrictionTypeID_SubstanceID(Company, PartNum, OpCode, PUM, VendorNum, RestrictionTypeID, SubstanceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPartRestrictSubst item
   Description: Call UpdateExt to delete VendPartRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPartRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PUM: Desc: PUM   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/VendPartRestrictSubsts(" + Company + "," + PartNum + "," + OpCode + "," + PUM + "," + VendorNum + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPartRestrictionListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendPartRestriction, whereClauseVendPartRestrictSubst, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendPartRestriction=" + whereClauseVendPartRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendPartRestrictSubst=" + whereClauseVendPartRestrictSubst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, opCode, puM, vendorNum, restrictionTypeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "opCode=" + opCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "puM=" + puM
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "restrictionTypeID=" + restrictionTypeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeManual(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeManual
   Description: Used when Manual field of VendPartRestriction is being changed to a new value.
   OperationID: ChangeManual
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeManual_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeManual_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRestrictionSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRestrictionSubstance
   Description: This methods assigns associated fields when VendPartRestrictSubst.SubstanceID changes.
   OperationID: ChangeRestrictionSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRestrictionSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRestrictionSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRestrictionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRestrictionType
   Description: This methods assigns associated fields when VendPartRestriction.RestrictionTypeID changes.
   OperationID: ChangeRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRestrictionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRestrictionType
   Description: Used when RestrictionTypeID field of VendPartRestriction is being changging to a new value.
   OperationID: OnChangingRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPartRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPartRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPartRestrictSubst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPartRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPartRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPartRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPartRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendPartRestrictionSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictSubstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartRestrictSubstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartRestrictionListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPartRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPartRestrictionRow] = obj["value"]
      pass

class Erp_Tablesets_VendPartRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then weight is disregarded in compliance roll-up.  """  
      self.ExemptDate:str = obj["ExemptDate"]
      """  The date when exempt status for this substance expires.  """  
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      """  Optional. Exemption certificate.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Exempt:bool = obj["Exempt"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRestrictionListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.RollUp:bool = obj["RollUp"]
      """   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.LastRollUp:str = obj["LastRollUp"]
      """  Set after compliance roll-up  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      """  Restriction Type Description  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.RollUp:bool = obj["RollUp"]
      """   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.LastRollUp:str = obj["LastRollUp"]
      """  Set after compliance roll-up  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeManual_input:
   """ Required : 
   checkManual
   ds
   """  
   def __init__(self, obj):
      self.checkManual:bool = obj["checkManual"]
      """  Manual value  """  
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

class ChangeManual_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRestrictionSubstance_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

class ChangeRestrictionSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRestrictionType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

class ChangeRestrictionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   partNum
   opCode
   puM
   vendorNum
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtVendPartRestrictionTableset:
   def __init__(self, obj):
      self.VendPartRestriction:list[Erp_Tablesets_VendPartRestrictionRow] = obj["VendPartRestriction"]
      self.VendPartRestrictSubst:list[Erp_Tablesets_VendPartRestrictSubstRow] = obj["VendPartRestrictSubst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendPartRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then weight is disregarded in compliance roll-up.  """  
      self.ExemptDate:str = obj["ExemptDate"]
      """  The date when exempt status for this substance expires.  """  
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      """  Optional. Exemption certificate.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Exempt:bool = obj["Exempt"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRestrictionListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.RollUp:bool = obj["RollUp"]
      """   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.LastRollUp:str = obj["LastRollUp"]
      """  Set after compliance roll-up  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      """  Restriction Type Description  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRestrictionListTableset:
   def __init__(self, obj):
      self.VendPartRestrictionList:list[Erp_Tablesets_VendPartRestrictionListRow] = obj["VendPartRestrictionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendPartRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies our Part.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Code - this is a component of the index which uniquely identifies the record.  Used to identify specific subcontracting operations prices  for a Part/Vendor.
This field can be blank (raw materials) or must be valid in the OpMaster (subcontracts).  """  
      self.PUM:str = obj["PUM"]
      """   The Purchasing Unit of measure for the Part from the vendor.
Defaulted from Part.PUM.  This is used in Purchase Order entry as the default on line item details.  It Overrides Part.PUM  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.RollUp:bool = obj["RollUp"]
      """   Enabled when Manual flag is false. In the actions menu there is a roll-up function per supplier part or per supplier based on part master weight for part and weight per substance or exempt status in supplier part and thresholds in restriction maintenance.
When set to true then by all substances are copied from part master or operation master (subcontract) if no substances are listed.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.LastRollUp:str = obj["LastRollUp"]
      """  Set after compliance roll-up  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPartRestrictionTableset:
   def __init__(self, obj):
      self.VendPartRestriction:list[Erp_Tablesets_VendPartRestrictionRow] = obj["VendPartRestriction"]
      self.VendPartRestrictSubst:list[Erp_Tablesets_VendPartRestrictSubstRow] = obj["VendPartRestrictSubst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   opCode
   puM
   vendorNum
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartRestrictionListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewVendPartRestrictSubst_input:
   """ Required : 
   ds
   partNum
   opCode
   puM
   vendorNum
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetNewVendPartRestrictSubst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendPartRestriction_input:
   """ Required : 
   ds
   partNum
   opCode
   puM
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.opCode:str = obj["opCode"]
      self.puM:str = obj["puM"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendPartRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendPartRestriction
   whereClauseVendPartRestrictSubst
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendPartRestriction:str = obj["whereClauseVendPartRestriction"]
      self.whereClauseVendPartRestrictSubst:str = obj["whereClauseVendPartRestrictSubst"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangingRestrictionType_input:
   """ Required : 
   checkRestrictionTypeID
   ds
   """  
   def __init__(self, obj):
      self.checkRestrictionTypeID:str = obj["checkRestrictionTypeID"]
      """  RestrictionTypeID value  """  
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

class OnChangingRestrictionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendPartRestrictionTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendPartRestrictionTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendPartRestrictionTableset] = obj["ds"]
      pass

      """  output parameters  """  

