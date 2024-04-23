import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COMagneticMediaSetupSvc
# Description: CO Magnetic Media Setup BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaSetups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COMagneticMediaSetups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COMagneticMediaSetups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups",headers=creds) as resp:
           return await resp.json()

async def post_COMagneticMediaSetups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COMagneticMediaSetups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaSetups_Company_DefinitionID(Company, DefinitionID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COMagneticMediaSetup item
   Description: Calls GetByID to retrieve the COMagneticMediaSetup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COMagneticMediaSetup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COMagneticMediaDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups(" + Company + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COMagneticMediaSetups_Company_DefinitionID(Company, DefinitionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COMagneticMediaSetup for the service
   Description: Calls UpdateExt to update COMagneticMediaSetup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COMagneticMediaSetup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups(" + Company + "," + DefinitionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COMagneticMediaSetups_Company_DefinitionID(Company, DefinitionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COMagneticMediaSetup item
   Description: Call UpdateExt to delete COMagneticMediaSetup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COMagneticMediaSetup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups(" + Company + "," + DefinitionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaSetups_Company_DefinitionID_COMagneticMediaFormatHeads(Company, DefinitionID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COMagneticMediaFormatHeads items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COMagneticMediaFormatHeads1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaFormatHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups(" + Company + "," + DefinitionID + ")/COMagneticMediaFormatHeads",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaSetups_Company_DefinitionID_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID(Company, DefinitionID, FormatID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COMagneticMediaFormatHead item
   Description: Calls GetByID to retrieve the COMagneticMediaFormatHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COMagneticMediaFormatHead1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaSetups(" + Company + "," + DefinitionID + ")/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatHeads(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COMagneticMediaFormatHeads items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COMagneticMediaFormatHeads
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaFormatHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads",headers=creds) as resp:
           return await resp.json()

async def post_COMagneticMediaFormatHeads(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COMagneticMediaFormatHeads
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID(Company, DefinitionID, FormatID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COMagneticMediaFormatHead item
   Description: Calls GetByID to retrieve the COMagneticMediaFormatHead item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COMagneticMediaFormatHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID(Company, DefinitionID, FormatID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COMagneticMediaFormatHead for the service
   Description: Calls UpdateExt to update COMagneticMediaFormatHead. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COMagneticMediaFormatHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID(Company, DefinitionID, FormatID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COMagneticMediaFormatHead item
   Description: Call UpdateExt to delete COMagneticMediaFormatHead item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COMagneticMediaFormatHead
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID_COMagneticMediaFormatDtls(Company, DefinitionID, FormatID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get COMagneticMediaFormatDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_COMagneticMediaFormatDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaFormatDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")/COMagneticMediaFormatDtls",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatHeads_Company_DefinitionID_FormatID_COMagneticMediaFormatDtls_Company_DefinitionID_FormatID_FormatLine(Company, DefinitionID, FormatID, FormatLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COMagneticMediaFormatDtl item
   Description: Calls GetByID to retrieve the COMagneticMediaFormatDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COMagneticMediaFormatDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param FormatLine: Desc: FormatLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatHeads(" + Company + "," + DefinitionID + "," + FormatID + ")/COMagneticMediaFormatDtls(" + Company + "," + DefinitionID + "," + FormatID + "," + FormatLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COMagneticMediaFormatDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COMagneticMediaFormatDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaFormatDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatDtls",headers=creds) as resp:
           return await resp.json()

async def post_COMagneticMediaFormatDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COMagneticMediaFormatDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COMagneticMediaFormatDtls_Company_DefinitionID_FormatID_FormatLine(Company, DefinitionID, FormatID, FormatLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COMagneticMediaFormatDtl item
   Description: Calls GetByID to retrieve the COMagneticMediaFormatDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COMagneticMediaFormatDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param FormatLine: Desc: FormatLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatDtls(" + Company + "," + DefinitionID + "," + FormatID + "," + FormatLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COMagneticMediaFormatDtls_Company_DefinitionID_FormatID_FormatLine(Company, DefinitionID, FormatID, FormatLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COMagneticMediaFormatDtl for the service
   Description: Calls UpdateExt to update COMagneticMediaFormatDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COMagneticMediaFormatDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param FormatLine: Desc: FormatLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COMagneticMediaFormatDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatDtls(" + Company + "," + DefinitionID + "," + FormatID + "," + FormatLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COMagneticMediaFormatDtls_Company_DefinitionID_FormatID_FormatLine(Company, DefinitionID, FormatID, FormatLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COMagneticMediaFormatDtl item
   Description: Call UpdateExt to delete COMagneticMediaFormatDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COMagneticMediaFormatDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DefinitionID: Desc: DefinitionID   Required: True   Allow empty value : True
      :param FormatID: Desc: FormatID   Required: True   Allow empty value : True
      :param FormatLine: Desc: FormatLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/COMagneticMediaFormatDtls(" + Company + "," + DefinitionID + "," + FormatID + "," + FormatLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COMagneticMediaDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOMagneticMediaDef, whereClauseCOMagneticMediaFormatHead, whereClauseCOMagneticMediaFormatDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOMagneticMediaDef=" + whereClauseCOMagneticMediaDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOMagneticMediaFormatHead=" + whereClauseCOMagneticMediaFormatHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCOMagneticMediaFormatDtl=" + whereClauseCOMagneticMediaFormatDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(definitionID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "definitionID=" + definitionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CopyDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyDefinition
   Description: Create a new Definition from another one
   OperationID: CopyDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportDefinition
   Description: Export Definition to XML
   OperationID: ExportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportDefinitionFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportDefinitionFile
   Description: Export definition as xml file
   OperationID: ExportDefinitionFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportDefinitionFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportDefinitionFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateImportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateImportFile
   Description: Validates definition XML file and returns its DefinitionID
   OperationID: ValidateImportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateImportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateImportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportDefinitionFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportDefinitionFile
   Description: Import Definition from XML file
   OperationID: ImportDefinitionFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDefinitionFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDefinitionFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportDefinition
   Description: Import Definition from XML
   OperationID: ImportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOMagneticMediaDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOMagneticMediaDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOMagneticMediaDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOMagneticMediaDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOMagneticMediaDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOMagneticMediaFormatHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOMagneticMediaFormatHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOMagneticMediaFormatHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOMagneticMediaFormatHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOMagneticMediaFormatHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOMagneticMediaFormatDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOMagneticMediaFormatDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOMagneticMediaFormatDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOMagneticMediaFormatDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOMagneticMediaFormatDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COMagneticMediaSetupSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COMagneticMediaDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COMagneticMediaDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COMagneticMediaDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COMagneticMediaDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COMagneticMediaFormatDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COMagneticMediaFormatDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COMagneticMediaFormatHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COMagneticMediaFormatHeadRow] = obj["value"]
      pass

class Erp_Tablesets_COMagneticMediaDefListRow:
   def __init__(self, obj):
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaID:str = obj["SchemaID"]
      """  SchemaID  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.GenericOneTimeID:str = obj["GenericOneTimeID"]
      """  GenericOneTimeID  """  
      self.ForeignOneTimeIDPattern:str = obj["ForeignOneTimeIDPattern"]
      """  ForeignOneTimeIDPattern  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaID:str = obj["SchemaID"]
      """  SchemaID  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.GenericOneTimeID:str = obj["GenericOneTimeID"]
      """  GenericOneTimeID  """  
      self.ForeignOneTimeIDPattern:str = obj["ForeignOneTimeIDPattern"]
      """  ForeignOneTimeIDPattern  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaFormatDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.FormatID:str = obj["FormatID"]
      """  FormatID  """  
      self.FormatLine:int = obj["FormatLine"]
      """  FormatLine  """  
      self.ConceptID:str = obj["ConceptID"]
      """  ConceptID  """  
      self.AccountIncluded:str = obj["AccountIncluded"]
      """  AccountIncluded  """  
      self.AccountExcluded:str = obj["AccountExcluded"]
      """  AccountExcluded  """  
      self.ReportColumn:str = obj["ReportColumn"]
      """  ReportColumn  """  
      self.SmallAmountLimit:bool = obj["SmallAmountLimit"]
      """  SmallAmountLimit  """  
      self.TypeOfMovement:int = obj["TypeOfMovement"]
      """  TypeOfMovement  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaFormatHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.FormatID:str = obj["FormatID"]
      """  FormatID  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ReportLimit:int = obj["ReportLimit"]
      """  ReportLimit  """  
      self.SmallAmountLimit:int = obj["SmallAmountLimit"]
      """  SmallAmountLimit  """  
      self.SummaryColumn:str = obj["SummaryColumn"]
      """  SummaryColumn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CopyDefinition_input:
   """ Required : 
   scrDefinitionID
   newDefinitionID
   newDescription
   """  
   def __init__(self, obj):
      self.scrDefinitionID:str = obj["scrDefinitionID"]
      """  Source Definition ID  """  
      self.newDefinitionID:str = obj["newDefinitionID"]
      """  New Definition ID  """  
      self.newDescription:str = obj["newDescription"]
      """  Description  """  
      pass

class CopyDefinition_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_COMagneticMediaDefListRow:
   def __init__(self, obj):
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaID:str = obj["SchemaID"]
      """  SchemaID  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.GenericOneTimeID:str = obj["GenericOneTimeID"]
      """  GenericOneTimeID  """  
      self.ForeignOneTimeIDPattern:str = obj["ForeignOneTimeIDPattern"]
      """  ForeignOneTimeIDPattern  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaDefListTableset:
   def __init__(self, obj):
      self.COMagneticMediaDefList:list[Erp_Tablesets_COMagneticMediaDefListRow] = obj["COMagneticMediaDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COMagneticMediaDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SchemaID:str = obj["SchemaID"]
      """  SchemaID  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.GenericOneTimeID:str = obj["GenericOneTimeID"]
      """  GenericOneTimeID  """  
      self.ForeignOneTimeIDPattern:str = obj["ForeignOneTimeIDPattern"]
      """  ForeignOneTimeIDPattern  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaFormatDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.FormatID:str = obj["FormatID"]
      """  FormatID  """  
      self.FormatLine:int = obj["FormatLine"]
      """  FormatLine  """  
      self.ConceptID:str = obj["ConceptID"]
      """  ConceptID  """  
      self.AccountIncluded:str = obj["AccountIncluded"]
      """  AccountIncluded  """  
      self.AccountExcluded:str = obj["AccountExcluded"]
      """  AccountExcluded  """  
      self.ReportColumn:str = obj["ReportColumn"]
      """  ReportColumn  """  
      self.SmallAmountLimit:bool = obj["SmallAmountLimit"]
      """  SmallAmountLimit  """  
      self.TypeOfMovement:int = obj["TypeOfMovement"]
      """  TypeOfMovement  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaFormatHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DefinitionID:str = obj["DefinitionID"]
      """  DefinitionID  """  
      self.FormatID:str = obj["FormatID"]
      """  FormatID  """  
      self.Version:int = obj["Version"]
      """  Version  """  
      self.ReportLimit:int = obj["ReportLimit"]
      """  ReportLimit  """  
      self.SmallAmountLimit:int = obj["SmallAmountLimit"]
      """  SmallAmountLimit  """  
      self.SummaryColumn:str = obj["SummaryColumn"]
      """  SummaryColumn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COMagneticMediaSetupTableset:
   def __init__(self, obj):
      self.COMagneticMediaDef:list[Erp_Tablesets_COMagneticMediaDefRow] = obj["COMagneticMediaDef"]
      self.COMagneticMediaFormatHead:list[Erp_Tablesets_COMagneticMediaFormatHeadRow] = obj["COMagneticMediaFormatHead"]
      self.COMagneticMediaFormatDtl:list[Erp_Tablesets_COMagneticMediaFormatDtlRow] = obj["COMagneticMediaFormatDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCOMagneticMediaSetupTableset:
   def __init__(self, obj):
      self.COMagneticMediaDef:list[Erp_Tablesets_COMagneticMediaDefRow] = obj["COMagneticMediaDef"]
      self.COMagneticMediaFormatHead:list[Erp_Tablesets_COMagneticMediaFormatHeadRow] = obj["COMagneticMediaFormatHead"]
      self.COMagneticMediaFormatDtl:list[Erp_Tablesets_COMagneticMediaFormatDtlRow] = obj["COMagneticMediaFormatDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportDefinitionFile_input:
   """ Required : 
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      pass

class ExportDefinitionFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ExportDefinition_input:
   """ Required : 
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      """  Definition to export  """  
      pass

class ExportDefinition_output:
   def __init__(self, obj):
      self.returnObj:object
      """  XML with Definition Data  """  
      pass

class GetByID_input:
   """ Required : 
   definitionID
   """  
   def __init__(self, obj):
      self.definitionID:str = obj["definitionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COMagneticMediaDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCOMagneticMediaDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

class GetNewCOMagneticMediaDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOMagneticMediaFormatDtl_input:
   """ Required : 
   ds
   definitionID
   formatID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      self.formatID:str = obj["formatID"]
      pass

class GetNewCOMagneticMediaFormatDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCOMagneticMediaFormatHead_input:
   """ Required : 
   ds
   definitionID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      self.definitionID:str = obj["definitionID"]
      pass

class GetNewCOMagneticMediaFormatHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOMagneticMediaDef
   whereClauseCOMagneticMediaFormatHead
   whereClauseCOMagneticMediaFormatDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOMagneticMediaDef:str = obj["whereClauseCOMagneticMediaDef"]
      self.whereClauseCOMagneticMediaFormatHead:str = obj["whereClauseCOMagneticMediaFormatHead"]
      self.whereClauseCOMagneticMediaFormatDtl:str = obj["whereClauseCOMagneticMediaFormatDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["returnObj"]
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

class ImportDefinitionFile_input:
   """ Required : 
   filename
   newDefinitionID
   """  
   def __init__(self, obj):
      self.filename:str = obj["filename"]
      """  Name of definition xml file  """  
      self.newDefinitionID:str = obj["newDefinitionID"]
      """  New Definition ID  """  
      pass

class ImportDefinitionFile_output:
   def __init__(self, obj):
      pass

class ImportDefinition_input:
   """ Required : 
   definitionImport
   newDefinitionID
   """  
   def __init__(self, obj):
      self.definitionImport:object
      """  XML with Definition data  """  
      self.newDefinitionID:str = obj["newDefinitionID"]
      """  New Definition ID  """  
      pass

class ImportDefinition_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOMagneticMediaSetupTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOMagneticMediaSetupTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COMagneticMediaSetupTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateImportFile_input:
   """ Required : 
   filename
   """  
   def __init__(self, obj):
      self.filename:str = obj["filename"]
      pass

class ValidateImportFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  DefinitionID  """  
      pass

