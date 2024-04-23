import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfigurationDesignSvc
# Description: Configuration Design Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfigurationDesigns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfigurationDesigns
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns",headers=creds) as resp:
           return await resp.json()

async def post_ConfigurationDesigns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfigurationDesigns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns_Company_ConfigID(Company, ConfigID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfigurationDesign item
   Description: Calls GetByID to retrieve the ConfigurationDesign item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfigurationDesign
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfigurationDesigns_Company_ConfigID(Company, ConfigID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfigurationDesign for the service
   Description: Calls UpdateExt to update ConfigurationDesign. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfigurationDesign
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfigurationDesigns_Company_ConfigID(Company, ConfigID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfigurationDesign item
   Description: Call UpdateExt to delete ConfigurationDesign item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfigurationDesign
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns_Company_ConfigID_PcPages(Company, ConfigID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcPages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcPages1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcPages",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns_Company_ConfigID_PcPages_Company_ConfigID_PageSeq(Company, ConfigID, PageSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcPage item
   Description: Calls GetByID to retrieve the PcPage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPage1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns_Company_ConfigID_PcStatusExprs(Company, ConfigID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcStatusExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcStatusExprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcStatusExprs",headers=creds) as resp:
           return await resp.json()

async def get_ConfigurationDesigns_Company_ConfigID_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company, ConfigID, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcStatusExpr item
   Description: Calls GetByID to retrieve the PcStatusExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusExpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/ConfigurationDesigns(" + Company + "," + ConfigID + ")/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcPages(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcPages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcPages
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages",headers=creds) as resp:
           return await resp.json()

async def post_PcPages(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcPages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcPageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcPageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcPages_Company_ConfigID_PageSeq(Company, ConfigID, PageSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcPage item
   Description: Calls GetByID to retrieve the PcPage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcPages_Company_ConfigID_PageSeq(Company, ConfigID, PageSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcPage for the service
   Description: Calls UpdateExt to update PcPage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcPage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcPageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcPages_Company_ConfigID_PageSeq(Company, ConfigID, PageSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcPage item
   Description: Call UpdateExt to delete PcPage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcPage
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcPages_Company_ConfigID_PageSeq_PcInputs(Company, ConfigID, PageSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcInputs",headers=creds) as resp:
           return await resp.json()

async def get_PcPages_Company_ConfigID_PageSeq_PcInputs_Company_ConfigID_InputName(Company, ConfigID, PageSeq, InputName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcPages_Company_ConfigID_PageSeq_PcPageExprs(Company, ConfigID, PageSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcPageExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcPageExprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcPageExprs",headers=creds) as resp:
           return await resp.json()

async def get_PcPages_Company_ConfigID_PageSeq_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company, ConfigID, PageSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcPageExpr item
   Description: Calls GetByID to retrieve the PcPageExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPageExpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPages(" + Company + "," + ConfigID + "," + PageSeq + ")/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs",headers=creds) as resp:
           return await resp.json()

async def post_PcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInput item
   Description: Calls GetByID to retrieve the PcInput item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInput for the service
   Description: Calls UpdateExt to update PcInput. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputs_Company_ConfigID_InputName(Company, ConfigID, InputName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInput item
   Description: Call UpdateExt to delete PcInput item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInput
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsLayerHeaders(Company, ConfigID, InputName, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputsLayerHeaders items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsLayerHeaders1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsLayerHeaders",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcDynLsts(Company, ConfigID, InputName, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcDynLsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcDynLsts",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company, ConfigID, InputName, ListSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLst item
   Description: Calls GetByID to retrieve the PcDynLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsExprs(Company, ConfigID, InputName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputsExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsExprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsExprs",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company, ConfigID, InputName, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsExpr item
   Description: Calls GetByID to retrieve the PcInputsExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsExpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsRules(Company, ConfigID, InputName, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputsRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsRules",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company, ConfigID, InputName, TargetInputName, RuleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsRule item
   Description: Calls GetByID to retrieve the PcInputsRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_QBuildObjs(Company, ConfigID, InputName, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QBuildObjs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QBuildObjs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/QBuildObjs",headers=creds) as resp:
           return await resp.json()

async def get_PcInputs_Company_ConfigID_InputName_QBuildObjs_Company_ConfigID_InputName_ObjName(Company, ConfigID, InputName, ObjName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QBuildObj item
   Description: Calls GetByID to retrieve the QBuildObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildObj1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputs(" + Company + "," + ConfigID + "," + InputName + ")/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerHeaders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerHeaders
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsLayerHeaders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerHeaders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerHeader item
   Description: Calls GetByID to retrieve the PcInputsLayerHeader item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsLayerHeader for the service
   Description: Calls UpdateExt to update PcInputsLayerHeader. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerHeaderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID(Company, ConfigID, InputName, ImageLayerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsLayerHeader item
   Description: Call UpdateExt to delete PcInputsLayerHeader item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerHeader
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID_PcInputsLayerDetails(Company, ConfigID, InputName, ImageLayerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputsLayerDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsLayerDetails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")/PcInputsLayerDetails",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerHeaders_Company_ConfigID_InputName_ImageLayerID_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerHeaders(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + ")/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsLayerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsLayerDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsLayerDetail item
   Description: Calls GetByID to retrieve the PcInputsLayerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsLayerDetail for the service
   Description: Calls UpdateExt to update PcInputsLayerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsLayerDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsLayerDetails_Company_ConfigID_InputName_ImageLayerID_LayerSeq(Company, ConfigID, InputName, ImageLayerID, LayerSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsLayerDetail item
   Description: Call UpdateExt to delete PcInputsLayerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsLayerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ImageLayerID: Desc: ImageLayerID   Required: True   Allow empty value : True
      :param LayerSeq: Desc: LayerSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsLayerDetails(" + Company + "," + ConfigID + "," + InputName + "," + ImageLayerID + "," + LayerSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDynLsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLsts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts",headers=creds) as resp:
           return await resp.json()

async def post_PcDynLsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company, ConfigID, InputName, ListSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLst item
   Description: Calls GetByID to retrieve the PcDynLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company, ConfigID, InputName, ListSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDynLst for the service
   Description: Calls UpdateExt to update PcDynLst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDynLsts_Company_ConfigID_InputName_ListSeq(Company, ConfigID, InputName, ListSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDynLst item
   Description: Call UpdateExt to delete PcDynLst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstCriterias(Company, ConfigID, InputName, ListSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcDynLstCriterias items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstCriterias1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstCriterias",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company, ConfigID, InputName, ListSeq, CriteriaSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstCriteria item
   Description: Calls GetByID to retrieve the PcDynLstCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstCriteria1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param CriteriaSeq: Desc: CriteriaSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstExprs(Company, ConfigID, InputName, ListSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcDynLstExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstExprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstExprs",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company, ConfigID, InputName, ListSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstExpr item
   Description: Calls GetByID to retrieve the PcDynLstExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstExpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstParams(Company, ConfigID, InputName, ListSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcDynLstParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcDynLstParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstParams",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLsts_Company_ConfigID_InputName_ListSeq_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company, ConfigID, InputName, ListSeq, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstParam item
   Description: Calls GetByID to retrieve the PcDynLstParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLsts(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + ")/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstCriterias(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDynLstCriterias items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstCriterias
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias",headers=creds) as resp:
           return await resp.json()

async def post_PcDynLstCriterias(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstCriterias
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company, ConfigID, InputName, ListSeq, CriteriaSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstCriteria item
   Description: Calls GetByID to retrieve the PcDynLstCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param CriteriaSeq: Desc: CriteriaSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company, ConfigID, InputName, ListSeq, CriteriaSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDynLstCriteria for the service
   Description: Calls UpdateExt to update PcDynLstCriteria. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param CriteriaSeq: Desc: CriteriaSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstCriteriaRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDynLstCriterias_Company_ConfigID_InputName_ListSeq_CriteriaSeq(Company, ConfigID, InputName, ListSeq, CriteriaSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDynLstCriteria item
   Description: Call UpdateExt to delete PcDynLstCriteria item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param CriteriaSeq: Desc: CriteriaSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstCriterias(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + CriteriaSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDynLstExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcDynLstExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company, ConfigID, InputName, ListSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstExpr item
   Description: Calls GetByID to retrieve the PcDynLstExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company, ConfigID, InputName, ListSeq, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDynLstExpr for the service
   Description: Calls UpdateExt to update PcDynLstExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDynLstExprs_Company_ConfigID_InputName_ListSeq_TypeCode_SeqNum(Company, ConfigID, InputName, ListSeq, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDynLstExpr item
   Description: Call UpdateExt to delete PcDynLstExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstExprs(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcDynLstParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcDynLstParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcDynLstParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams",headers=creds) as resp:
           return await resp.json()

async def post_PcDynLstParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcDynLstParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company, ConfigID, InputName, ListSeq, ParamName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcDynLstParam item
   Description: Calls GetByID to retrieve the PcDynLstParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcDynLstParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company, ConfigID, InputName, ListSeq, ParamName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcDynLstParam for the service
   Description: Calls UpdateExt to update PcDynLstParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcDynLstParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcDynLstParamsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcDynLstParams_Company_ConfigID_InputName_ListSeq_ParamName(Company, ConfigID, InputName, ListSeq, ParamName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcDynLstParam item
   Description: Call UpdateExt to delete PcDynLstParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcDynLstParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ListSeq: Desc: ListSeq   Required: True
      :param ParamName: Desc: ParamName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcDynLstParams(" + Company + "," + ConfigID + "," + InputName + "," + ListSeq + "," + ParamName + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company, ConfigID, InputName, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsExpr item
   Description: Calls GetByID to retrieve the PcInputsExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company, ConfigID, InputName, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsExpr for the service
   Description: Calls UpdateExt to update PcInputsExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsExprs_Company_ConfigID_InputName_TypeCode_SeqNum(Company, ConfigID, InputName, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsExpr item
   Description: Call UpdateExt to delete PcInputsExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsExprs(" + Company + "," + ConfigID + "," + InputName + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRules(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsRules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company, ConfigID, TargetInputName, RuleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsRule item
   Description: Calls GetByID to retrieve the PcInputsRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company, ConfigID, TargetInputName, RuleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsRule for the service
   Description: Calls UpdateExt to update PcInputsRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq(Company, ConfigID, TargetInputName, RuleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsRule item
   Description: Call UpdateExt to delete PcInputsRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq_PcInputsRuleDefs(Company, ConfigID, TargetInputName, RuleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcInputsRuleDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcInputsRuleDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")/PcInputsRuleDefs",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRules_Company_ConfigID_TargetInputName_RuleSeq_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company, ConfigID, TargetInputName, RuleSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsRuleDef item
   Description: Calls GetByID to retrieve the PcInputsRuleDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRuleDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRules(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + ")/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRuleDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcInputsRuleDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcInputsRuleDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcInputsRuleDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs",headers=creds) as resp:
           return await resp.json()

async def post_PcInputsRuleDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcInputsRuleDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company, ConfigID, TargetInputName, RuleSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcInputsRuleDef item
   Description: Calls GetByID to retrieve the PcInputsRuleDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcInputsRuleDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company, ConfigID, TargetInputName, RuleSeq, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcInputsRuleDef for the service
   Description: Calls UpdateExt to update PcInputsRuleDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcInputsRuleDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcInputsRuleDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcInputsRuleDefs_Company_ConfigID_TargetInputName_RuleSeq_SeqNum(Company, ConfigID, TargetInputName, RuleSeq, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcInputsRuleDef item
   Description: Call UpdateExt to delete PcInputsRuleDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcInputsRuleDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TargetInputName: Desc: TargetInputName   Required: True   Allow empty value : True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcInputsRuleDefs(" + Company + "," + ConfigID + "," + TargetInputName + "," + RuleSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_QBuildObjs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QBuildObjs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildObjs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs",headers=creds) as resp:
           return await resp.json()

async def post_QBuildObjs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildObjs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QBuildObjs_Company_ConfigID_InputName_ObjName(Company, ConfigID, InputName, ObjName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QBuildObj item
   Description: Calls GetByID to retrieve the QBuildObj item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QBuildObjs_Company_ConfigID_InputName_ObjName(Company, ConfigID, InputName, ObjName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QBuildObj for the service
   Description: Calls UpdateExt to update QBuildObj. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildObjRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QBuildObjs_Company_ConfigID_InputName_ObjName(Company, ConfigID, InputName, ObjName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QBuildObj item
   Description: Call UpdateExt to delete QBuildObj item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildObj
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")",headers=creds) as resp:
           return await resp.json()

async def get_QBuildObjs_Company_ConfigID_InputName_ObjName_QBuildMappings(Company, ConfigID, InputName, ObjName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QBuildMappings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QBuildMappings1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")/QBuildMappings",headers=creds) as resp:
           return await resp.json()

async def get_QBuildObjs_Company_ConfigID_InputName_ObjName_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildObjs(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + ")/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")",headers=creds) as resp:
           return await resp.json()

async def get_QBuildMappings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QBuildMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QBuildMappings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings",headers=creds) as resp:
           return await resp.json()

async def post_QBuildMappings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QBuildMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QBuildMapping item
   Description: Calls GetByID to retrieve the QBuildMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QBuildMapping for the service
   Description: Calls UpdateExt to update QBuildMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QBuildMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QBuildMappings_Company_ConfigID_InputName_ObjName_ObjParameter(Company, ConfigID, InputName, ObjName, ObjParameter, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QBuildMapping item
   Description: Call UpdateExt to delete QBuildMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QBuildMapping
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param InputName: Desc: InputName   Required: True   Allow empty value : True
      :param ObjName: Desc: ObjName   Required: True   Allow empty value : True
      :param ObjParameter: Desc: ObjParameter   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/QBuildMappings(" + Company + "," + ConfigID + "," + InputName + "," + ObjName + "," + ObjParameter + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcPageExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcPageExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcPageExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcPageExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcPageExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcPageExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company, ConfigID, PageSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcPageExpr item
   Description: Calls GetByID to retrieve the PcPageExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcPageExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company, ConfigID, PageSeq, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcPageExpr for the service
   Description: Calls UpdateExt to update PcPageExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcPageExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcPageExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcPageExprs_Company_ConfigID_PageSeq_TypeCode_SeqNum(Company, ConfigID, PageSeq, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcPageExpr item
   Description: Call UpdateExt to delete PcPageExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcPageExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PageSeq: Desc: PageSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcPageExprs(" + Company + "," + ConfigID + "," + PageSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcStatusExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcStatusExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcStatusExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcStatusExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcStatusExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company, ConfigID, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcStatusExpr item
   Description: Calls GetByID to retrieve the PcStatusExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcStatusExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company, ConfigID, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcStatusExpr for the service
   Description: Calls UpdateExt to update PcStatusExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcStatusExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcStatusExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcStatusExprs_Company_ConfigID_TypeCode_SeqNum(Company, ConfigID, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcStatusExpr item
   Description: Call UpdateExt to delete PcStatusExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcStatusExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/PcStatusExprs(" + Company + "," + ConfigID + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcStatusListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePcStatus, whereClausePcPage, whereClausePcInputs, whereClausePcInputsLayerHeader, whereClausePcInputsLayerDetail, whereClausePcDynLst, whereClausePcDynLstCriteria, whereClausePcDynLstExpr, whereClausePcDynLstParams, whereClausePcInputsExpr, whereClausePcInputsRule, whereClausePcInputsRuleDef, whereClauseQBuildObj, whereClauseQBuildMapping, whereClausePcPageExpr, whereClausePcStatusExpr, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcStatus=" + whereClausePcStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcPage=" + whereClausePcPage
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputs=" + whereClausePcInputs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsLayerHeader=" + whereClausePcInputsLayerHeader
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsLayerDetail=" + whereClausePcInputsLayerDetail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDynLst=" + whereClausePcDynLst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDynLstCriteria=" + whereClausePcDynLstCriteria
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDynLstExpr=" + whereClausePcDynLstExpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcDynLstParams=" + whereClausePcDynLstParams
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsExpr=" + whereClausePcInputsExpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsRule=" + whereClausePcInputsRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcInputsRuleDef=" + whereClausePcInputsRuleDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQBuildObj=" + whereClauseQBuildObj
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQBuildMapping=" + whereClauseQBuildMapping
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcPageExpr=" + whereClausePcPageExpr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcStatusExpr=" + whereClausePcStatusExpr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, epicorHeaders = None):
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
   params += "configID=" + configID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_NumberOfDecimalPlaces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NumberOfDecimalPlaces
   Description: Returns number of decimals in the specified format string
   OperationID: NumberOfDecimalPlaces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NumberOfDecimalPlaces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NumberOfDecimalPlaces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateAllowedToDeletePcInput(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateAllowedToDeletePcInput
   Description: Validate if the PcInputs is allowed to be deleted
   OperationID: ValidateAllowedToDeletePcInput
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateAllowedToDeletePcInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAllowedToDeletePcInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSourceInputNameList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSourceInputNameList
   Description: Gets available list of input names.
   OperationID: GetSourceInputNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourceInputNameList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourceInputNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateInputRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateInputRule
   Description: Duplicate Inputs Rule.
   OperationID: DuplicateInputRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateInputRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateInputRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInputType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInputType
   Description: Set defaults based on the control style.
   OperationID: OnChangeInputType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInputName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInputName
   Description: Set defaults when the control name is set.
   OperationID: OnChangeInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMinOrMaxForDecimal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMinOrMaxForDecimal
   Description: Set Increment default1 to 1 if 0 when a min or max is set.
   OperationID: OnChangeMinOrMaxForDecimal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMinOrMaxForDecimal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMinOrMaxForDecimal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInputTabOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInputTabOrder
   Description: Finds the Last Tab Order and add 10 to it.  Is used when pasing into a grid.
   OperationID: OnChangeInputTabOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputTabOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputTabOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewEmptyPcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewEmptyPcInputs
   Description: Create a new PcInput row based on the control style.  This method is used by the grid for list entry input.
   OperationID: CreateNewEmptyPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewEmptyPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewEmptyPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateNewPcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateNewPcInputs
   Description: Create a new PcInput record based on the control type. This method is used by the designer instead of the generic GetNewInput.
   OperationID: CreateNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeImageLayerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeImageLayerID
   Description: Validates the proposed image layer ID in the the ImageLayerHeader table
   OperationID: OnChangeImageLayerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeImageLayerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeImageLayerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImageLayerScriptCode(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImageLayerUpdateScriptCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImageLayerUpdateScriptCode
   Description: Method used to call the Image Layer Engine code generator and return updating Script code for execution.
   OperationID: ImageLayerUpdateScriptCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImageLayerUpdateScriptCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImageLayerUpdateScriptCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttributeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttributeID
   Description: Validates the attribute ID column of PcInputs in theConfiguration 'dirty' row. Also runs the foreign link to populate Attribute Description.
   OperationID: OnChangeAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDynAttributeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDynAttributeID
   Description: Call when changing the Attribute ID for a configurator tied to a PartAttrClass.
   OperationID: OnChangeDynAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributeDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributeDesc
   Description: Returns the description of a given attribute as it is set up in Insp Attribute Entry.
   OperationID: GetAttributeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDynAttributeDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDynAttributeDesc
   Description: Returns the description of a given dynamioc attribute
   OperationID: GetDynAttributeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynAttributeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynAttributeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePageDisplaySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePageDisplaySeq
   Description: Validate that the new PcPage.DisplaySeq value is not in use by another PcPage record.
   OperationID: OnChangePageDisplaySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePageDisplaySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePageDisplaySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInputPageNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInputPageNumber
   Description: Recalculates the PcInputs.PageSeq field from the new PcInputs.PageDisplaySeq.
   OperationID: OnChangeInputPageNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputPageNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputPageNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBAQColumnName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBAQColumnName
   Description: Validates if a QueryField row exists.
   OperationID: ValidateBAQColumnName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBAQColumnName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBAQColumnName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePcLookupTblHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePcLookupTblHed
   Description: Validates if a PcLookupTblHed with a matching ID exists
   OperationID: ValidatePcLookupTblHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcLookupTblHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcLookupTblHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePcLookupColSetDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePcLookupColSetDtl
   Description: Validates if a PcLookupColSetDtl with a matching ID exists
   OperationID: ValidatePcLookupColSetDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcLookupColSetDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcLookupColSetDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBAQDisplayColumnList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBAQDisplayColumnList
   Description: This method will provide a list of the selected Display Columns in a BAQ given its Query ID.
   OperationID: GetBAQDisplayColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBAQDisplayColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQDisplayColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInputList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInputList
   Description: Returns a dataset with a list of PcInputs rows
   OperationID: GetInputList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInputList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInputList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromptForPassword(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SyncRevision(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedGlobalInputVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedGlobalInputVar
   Description: Reset Values when Global Input Variable is false.
   OperationID: OnChangedGlobalInputVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedGlobalInputVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedGlobalInputVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingGlbInputVarName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingGlbInputVarName
   Description: Validate Name and update initial values
   OperationID: OnChangingGlbInputVarName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingGlbInputVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingGlbInputVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInputReadOnlyExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInputReadOnlyExpr
   Description: Reset Values when Read Only flag is false.
   OperationID: OnChangeInputReadOnlyExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInputReadOnlyExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInputReadOnlyExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePageReadOnlyExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePageReadOnlyExpr
   Description: Reset Values when Read Only flag is false.
   OperationID: OnChangePageReadOnlyExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePageReadOnlyExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePageReadOnlyExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingBAQName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingBAQName
   Description: Validate Name and update initial values
   OperationID: OnChangingBAQName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingBAQName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingBAQName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingUserDefinedMethodName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingUserDefinedMethodName
   Description: Validate Name and update initial values
   OperationID: OnChangingUserDefinedMethodName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingUserDefinedMethodName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingUserDefinedMethodName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingDataLookupFunction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingDataLookupFunction
   Description: Validate Name and update initial values
   OperationID: OnChangingDataLookupFunction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingDataLookupFunction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDataLookupFunction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingListDataSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingListDataSource
   Description: Delete dynamic list's previous values
   OperationID: OnChangingListDataSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingListDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingListDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourceInputName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourceInputName
   Description: Validations for change to Source Input name.
   OperationID: OnChangeSourceInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourceInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PageCountForCodeEditor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PageCountForCodeEditor
   Description: Returns the number of pages.  Used by the Code Editor
   OperationID: PageCountForCodeEditor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PageCountForCodeEditor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PageCountForCodeEditor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExistsProposedInputName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExistsProposedInputName
   Description: Return if an input name already exists
   OperationID: ExistsProposedInputName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExistsProposedInputName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsProposedInputName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInputName(requestBody, epicorHeaders = None):
   """  
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
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateImageLayerID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateImageLayerID
   Description: Validates the proposed image layer ID in the the ImageLayerHeader table
   OperationID: ValidateImageLayerID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateImageLayerID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateImageLayerID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultListItems(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultListItems
   Description: Return the list items by default when adding a Dynamic List.
   OperationID: GetDefaultListItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultListItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UpdateQBuildMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateQBuildMapping
   Description: Update the QBuild mapping and set PcInputs.ImageMapping to true or false
   OperationID: UpdateQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportImagesFileStore(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportImagesFileStore
   OperationID: ImportImagesFileStore
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportImagesFileStore_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportImagesFileStore_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteQBuildImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteQBuildImage
   Description: Call this method when the user has removed all objects from the drawing canvas
   OperationID: DeleteQBuildImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQBuildImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQBuildImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateMappedInput(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateMappedInput
   Description: Validates the entered MappedInputName
   OperationID: ValidateMappedInput
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateMappedInput_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMappedInput_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFormatString(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFormatString
   Description: checks QBuildMapping to see if this input is mapped to an integer object
   OperationID: OnChangeFormatString
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPcInputsWithLayerIDForConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPcInputsWithLayerIDForConfiguration
   Description: Retrieve the PcInputs with an ImageLayerID specified for a given configurator
   OperationID: GetPcInputsWithLayerIDForConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPcInputsWithLayerIDForConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPcInputsWithLayerIDForConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshImageLayerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshImageLayerDetails
   Description: Refresh the image layer details for an input
   OperationID: RefreshImageLayerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshImageLayerDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshImageLayerDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcStatus
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcPage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcPage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcPage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsLayerHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsLayerHeader
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsLayerDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsLayerDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsLayerDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsLayerDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsLayerDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDynLst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDynLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDynLstCriteria(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDynLstCriteria
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstCriteria
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstCriteria_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstCriteria_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDynLstExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDynLstExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcDynLstParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcDynLstParams
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcDynLstParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcDynLstParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcDynLstParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcInputsRuleDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcInputsRuleDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcInputsRuleDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcInputsRuleDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcInputsRuleDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQBuildObj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQBuildObj
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildObj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildObj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildObj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQBuildMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQBuildMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQBuildMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQBuildMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQBuildMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcPageExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcPageExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcPageExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcPageExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcPageExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcStatusExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcStatusExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcStatusExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcStatusExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcStatusExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfigurationDesignSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstCriteriaRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDynLstCriteriaRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDynLstExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstParamsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDynLstParamsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcDynLstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcDynLstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsRuleDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcInputsRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcInputsRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcPageExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcPageRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcPageRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcStatusRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QBuildMappingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QBuildObjRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QBuildObjRow] = obj["value"]
      pass

class Erp_Tablesets_PcDynLstCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.CriteriaSeq:int = obj["CriteriaSeq"]
      """  Criteria sequence number to make this record unique.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column name to use for BAQ query criteria  """  
      self.Condition:str = obj["Condition"]
      """  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  """  
      self.ValueFrom:str = obj["ValueFrom"]
      """  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  """  
      self.ColumnValue:str = obj["ColumnValue"]
      """  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  """  
      self.Operator:str = obj["Operator"]
      """  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.UseEmptyValue:bool = obj["UseEmptyValue"]
      """  UseEmptyValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ColumnType:str = obj["ColumnType"]
      """  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ValueFromDisplay:str = obj["ValueFromDisplay"]
      """  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  BAQ Program Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ListSeq:int = obj["ListSeq"]
      """  ListSeq  """  
      self.ParamName:str = obj["ParamName"]
      """  ParamName  """  
      self.ParamConst:bool = obj["ParamConst"]
      """  ParamConst  """  
      self.ParamValue:str = obj["ParamValue"]
      """  ParamValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ParamType:str = obj["ParamType"]
      """  This is the type of Parameter.  """  
      self.ParamInput:str = obj["ParamInput"]
      self.ParamModifier:str = obj["ParamModifier"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.Condition:str = obj["Condition"]
      """  Contains the logical expression as to when the list is used.  """  
      self.ListItems:str = obj["ListItems"]
      """  Contains the combo-box list items that are used when the condition is true.  """  
      self.InitVal:str = obj["InitVal"]
      """  The Initial value for the list.  """  
      self.BAQRunProgram:bool = obj["BAQRunProgram"]
      """  If TRUE then the dynamic list will be built by running a BAQ program  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  The BAQ program name used for building the dynamic list  """  
      self.BAQDispValue:str = obj["BAQDispValue"]
      """  Value that will be displayed from the BAQ  """  
      self.BAQInputVal:str = obj["BAQInputVal"]
      """  The input value for the BAQ  """  
      self.ListDataSource:str = obj["ListDataSource"]
      """  Defines the type of dynamic list from Static, BAQ, Program, etc.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RunTblLookup:bool = obj["RunTblLookup"]
      """  RunTblLookup  """  
      self.TblLookupID:str = obj["TblLookupID"]
      """  TblLookupID  """  
      self.TblLookupFunc:str = obj["TblLookupFunc"]
      """  TblLookupFunc  """  
      self.RunUserDefined:str = obj["RunUserDefined"]
      """  RunUserDefined  """  
      self.UserDefinedName:str = obj["UserDefinedName"]
      """  UserDefinedName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SortOrder:str = obj["SortOrder"]
      """  SortOrder  """  
      self.SubReturnColumn:str = obj["SubReturnColumn"]
      """  SubReturnColumn  """  
      self.ScriptCondition:str = obj["ScriptCondition"]
      """  ScriptCondition  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Reserved for Future Development  """  
      self.EnableScript:bool = obj["EnableScript"]
      """  Identifies if Script expressions are valid for Dynamic List Conditions  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      self.PageSeq:int = obj["PageSeq"]
      self.UserDefinedFunctionType:str = obj["UserDefinedFunctionType"]
      """  Either Client or Server where the UD Method is executed.  """  
      self.UserDefinedReturnType:str = obj["UserDefinedReturnType"]
      """  Storing the Return Type for the selected User Defined Method.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then details on this record can be updated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  LayerSeq  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  Order in which layers are placed on the base image.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png type is supported.  """  
      self.Category:str = obj["Category"]
      """  Free form text enabling users to categorize layers  """  
      self.Width:int = obj["Width"]
      """  Width of image  """  
      self.Height:int = obj["Height"]
      """  Height of image  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input name this header is assigned.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID.  """  
      self.ImageID:str = obj["ImageID"]
      """  File name of the image to be retrieved from the Image URL.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  The URL location of the image.  """  
      self.FileType:str = obj["FileType"]
      """  File types png and jpg are supported.  """  
      self.Width:int = obj["Width"]
      """  Image Width  """  
      self.Height:int = obj["Height"]
      """  Image height  """  
      self.Version:int = obj["Version"]
      """  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The order in which these definitions are interrogated.  """  
      self.SourceInputName:str = obj["SourceInputName"]
      """  Input whose value is used in determining if this rule is executed.  """  
      self.SourceInputProperty:str = obj["SourceInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.SourceCharacterValue:str = obj["SourceCharacterValue"]
      """  SourceCharacterValue  """  
      self.SourceIntegerValue:int = obj["SourceIntegerValue"]
      """  SourceIntegerValue  """  
      self.SourceDecimalValue:int = obj["SourceDecimalValue"]
      """  SourceDecimalValue  """  
      self.SourceDateValue:str = obj["SourceDateValue"]
      """  SourceDateValue  """  
      self.SourceLogicalValue:bool = obj["SourceLogicalValue"]
      """  SourceLogicalValue  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.LeftP:str = obj["LeftP"]
      """  Reserved for future development.  """  
      self.RightP:str = obj["RightP"]
      """  Reserved for future development.  """  
      self.AndOr:str = obj["AndOr"]
      """  Defaults to And and permits users to use more than one input in the rule.  """  
      self.CompOp:str = obj["CompOp"]
      """  Comparison operator used when evaluating the rule. Valid value at this time is equals.  """  
      self.Neg:bool = obj["Neg"]
      """  Reserved for future development.  Defaults to false.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ListValues:str = obj["ListValues"]
      self.SourceValue:str = obj["SourceValue"]
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, ComboBox  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourcePcInputsDesignControlType:str = obj["SourcePcInputsDesignControlType"]
      self.SourcePcInputsFormatString:str = obj["SourcePcInputsFormatString"]
      self.SourcePcInputsListItems:str = obj["SourcePcInputsListItems"]
      self.SourcePcInputsDataType:str = obj["SourcePcInputsDataType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.RuleDesc:str = obj["RuleDesc"]
      """  Enter text that describes what the rule does.  """  
      self.TargetInputProperty:str = obj["TargetInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.TargetInputValue:str = obj["TargetInputValue"]
      """  The new value of the input when this rule executes.  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DefinitionDesc:str = obj["DefinitionDesc"]
      """  Associated Rule Defintion descriptions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPageExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.PageTitle:str = obj["PageTitle"]
      """  The title of the configuration page.  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the page.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the page  """  
      self.SkipOnLeaveOPL:bool = obj["SkipOnLeaveOPL"]
      """  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add OnLeave expressions to the page  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.ProcessDynLstFirst:bool = obj["ProcessDynLstFirst"]
      """  Process dynamic lists before on leave expressions for this page  """  
      self.DynLstHigher:bool = obj["DynLstHigher"]
      """  Only process dynamic lists with higher tab sequences  """  
      self.SkipPageProcessOL:bool = obj["SkipPageProcessOL"]
      """  Skip processing page on leave on load  """  
      self.SkipPageNoInputs:bool = obj["SkipPageNoInputs"]
      """  Do not process on leave expressions when page loads  """  
      self.SkipOnLeaveOPE:bool = obj["SkipOnLeaveOPE"]
      """  Do not process on leave expressions when leaving pages  """  
      self.pWidth:int = obj["pWidth"]
      """  Width of panel  """  
      self.pHeight:int = obj["pHeight"]
      """  Height of panel  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.FirstPage:bool = obj["FirstPage"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  TypeCode  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.AllowReconPO:bool = obj["AllowReconPO"]
      """  AllowReconPO  """  
      self.CompPricingJobMethod:bool = obj["CompPricingJobMethod"]
      """  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  """  
      self.CreateRev:bool = obj["CreateRev"]
      """  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  """  
      self.DefaultECO:str = obj["DefaultECO"]
      """  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  """  
      self.GenerateMethod:bool = obj["GenerateMethod"]
      """  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      """  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  """  
      self.RemoveLink:bool = obj["RemoveLink"]
      """  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.UseSavedLayout:bool = obj["UseSavedLayout"]
      """  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.CreateNewConfigID:bool = obj["CreateNewConfigID"]
      """  CreateNewConfigID  """  
      self.UseTemplatePartDefaults:bool = obj["UseTemplatePartDefaults"]
      """  UseTemplatePartDefaults  """  
      self.DefaultPartNum:str = obj["DefaultPartNum"]
      """  DefaultPartNum  """  
      self.DefaultRevisionNum:str = obj["DefaultRevisionNum"]
      """  DefaultRevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  """  
      self.RecycleJobs:bool = obj["RecycleJobs"]
      """  RecycleJobs  """  
      self.ClientDeployedToEWCDate:str = obj["ClientDeployedToEWCDate"]
      """  ClientDeployedToEWCDate  """  
      self.EWCClientSyncRequired:bool = obj["EWCClientSyncRequired"]
      """  EWCClientSyncRequired  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.Kinetic:bool = obj["Kinetic"]
      """  Kinetic  """  
      self.KBConfigID:int = obj["KBConfigID"]
      """  KBConfigID  """  
      self.KBConfigDesc:str = obj["KBConfigDesc"]
      """  KBConfigDesc  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.HasInputs:bool = obj["HasInputs"]
      """  Indicates if the configurator has inputs in its design.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.ResetPCInputsAttributes:bool = obj["ResetPCInputsAttributes"]
      """  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.UpdateCreatePartTarget:bool = obj["UpdateCreatePartTarget"]
      """  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.EnableCPQPartCreation:bool = obj["EnableCPQPartCreation"]
      """  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the object name.  """  
      self.ObjParameter:str = obj["ObjParameter"]
      """  This is the name of the object parameter.  """  
      self.MappedInputName:str = obj["MappedInputName"]
      """  Name of the input mapped to this object parameter.  """  
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      """  This is the data type of the object parameter.  """  
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      """  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.PageSeq:int = obj["PageSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.QBuildObjObjType:str = obj["QBuildObjObjType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildObjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the name of the object.  """  
      self.ObjType:str = obj["ObjType"]
      """  This is the object type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateNewEmptyPcInputs_input:
   """ Required : 
   configId
   pageSeq
   ds
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  Configuration ID  """  
      self.pageSeq:int = obj["pageSeq"]
      """  Page Sequence where the input is being placed  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class CreateNewEmptyPcInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateNewPcInputs_input:
   """ Required : 
   configId
   pageSeq
   controlType
   designControlType
   ds
   """  
   def __init__(self, obj):
      self.configId:str = obj["configId"]
      """  Configuration ID  """  
      self.pageSeq:int = obj["pageSeq"]
      """  Page Sequence where the input is being placed.  """  
      self.controlType:str = obj["controlType"]
      """  Control type of the input, this is the control type used at runtime.  """  
      self.designControlType:str = obj["designControlType"]
      """  Control type used at design time, depending on this value the data type will be defaulted.  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class CreateNewPcInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteQBuildImage_input:
   """ Required : 
   ConfigID
   InputName
   ConfigurationDesignTS
   """  
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Name of control that is of type QBuild  """  
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

class DeleteQBuildImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

      """  output parameters  """  

class DuplicateInputRule_input:
   """ Required : 
   configID
   targetInputName
   ruleSeq
   newRuleDesc
   ds
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration used.  """  
      self.targetInputName:str = obj["targetInputName"]
      """  targetInputName used.  """  
      self.ruleSeq:int = obj["ruleSeq"]
      """  ruleSeq used.  """  
      self.newRuleDesc:str = obj["newRuleDesc"]
      """  new rule description to use.  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class DuplicateInputRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ConfigurationDesignListTableset:
   def __init__(self, obj):
      self.PcStatusList:list[Erp_Tablesets_PcStatusListRow] = obj["PcStatusList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfigurationDesignTableset:
   def __init__(self, obj):
      self.PcStatus:list[Erp_Tablesets_PcStatusRow] = obj["PcStatus"]
      self.PcPage:list[Erp_Tablesets_PcPageRow] = obj["PcPage"]
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.PcInputsLayerHeader:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["PcInputsLayerHeader"]
      self.PcInputsLayerDetail:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["PcInputsLayerDetail"]
      self.PcDynLst:list[Erp_Tablesets_PcDynLstRow] = obj["PcDynLst"]
      self.PcDynLstCriteria:list[Erp_Tablesets_PcDynLstCriteriaRow] = obj["PcDynLstCriteria"]
      self.PcDynLstExpr:list[Erp_Tablesets_PcDynLstExprRow] = obj["PcDynLstExpr"]
      self.PcDynLstParams:list[Erp_Tablesets_PcDynLstParamsRow] = obj["PcDynLstParams"]
      self.PcInputsExpr:list[Erp_Tablesets_PcInputsExprRow] = obj["PcInputsExpr"]
      self.PcInputsRule:list[Erp_Tablesets_PcInputsRuleRow] = obj["PcInputsRule"]
      self.PcInputsRuleDef:list[Erp_Tablesets_PcInputsRuleDefRow] = obj["PcInputsRuleDef"]
      self.QBuildObj:list[Erp_Tablesets_QBuildObjRow] = obj["QBuildObj"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.PcPageExpr:list[Erp_Tablesets_PcPageExprRow] = obj["PcPageExpr"]
      self.PcStatusExpr:list[Erp_Tablesets_PcStatusExprRow] = obj["PcStatusExpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcDynLstCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.CriteriaSeq:int = obj["CriteriaSeq"]
      """  Criteria sequence number to make this record unique.  """  
      self.ColumnName:str = obj["ColumnName"]
      """  Column name to use for BAQ query criteria  """  
      self.Condition:str = obj["Condition"]
      """  Condition to use for BAQ query criteria. Options include: =, < >, >, <, >=, <=, BEGINS, MATCHES  """  
      self.ValueFrom:str = obj["ValueFrom"]
      """  This field will indicate where the ColumnValue will be taken from. Current options are BAQ, CONST and INPUT.  """  
      self.ColumnValue:str = obj["ColumnValue"]
      """  This field holds either a constant, a baq column name or a input name from which it will take the value to be used in the BAQ criteria.  """  
      self.Operator:str = obj["Operator"]
      """  Operator to be applied between each criteria. Values are restricted to AND/OR and if none is defined then AND will be used as a default.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LeftP:str = obj["LeftP"]
      """  LeftP  """  
      self.RightP:str = obj["RightP"]
      """  RightP  """  
      self.UseEmptyValue:bool = obj["UseEmptyValue"]
      """  UseEmptyValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ColumnType:str = obj["ColumnType"]
      """  Column data type used to identify what type of value should it be compared to, this value should come from the QueryField table.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ValueFromDisplay:str = obj["ValueFromDisplay"]
      """  External field used to temporarily store a display value from which the real value is determined to then be stored in ValueFrom.  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  BAQ Program Name  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ListSeq:int = obj["ListSeq"]
      """  ListSeq  """  
      self.ParamName:str = obj["ParamName"]
      """  ParamName  """  
      self.ParamConst:bool = obj["ParamConst"]
      """  ParamConst  """  
      self.ParamValue:str = obj["ParamValue"]
      """  ParamValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      """  Page Sequence where the parent input exists  """  
      self.ParamType:str = obj["ParamType"]
      """  This is the type of Parameter.  """  
      self.ParamInput:str = obj["ParamInput"]
      self.ParamModifier:str = obj["ParamModifier"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcDynLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ListSeq:int = obj["ListSeq"]
      """  The unique sequence id for the dynamic list.  """  
      self.Condition:str = obj["Condition"]
      """  Contains the logical expression as to when the list is used.  """  
      self.ListItems:str = obj["ListItems"]
      """  Contains the combo-box list items that are used when the condition is true.  """  
      self.InitVal:str = obj["InitVal"]
      """  The Initial value for the list.  """  
      self.BAQRunProgram:bool = obj["BAQRunProgram"]
      """  If TRUE then the dynamic list will be built by running a BAQ program  """  
      self.BAQProgramName:str = obj["BAQProgramName"]
      """  The BAQ program name used for building the dynamic list  """  
      self.BAQDispValue:str = obj["BAQDispValue"]
      """  Value that will be displayed from the BAQ  """  
      self.BAQInputVal:str = obj["BAQInputVal"]
      """  The input value for the BAQ  """  
      self.ListDataSource:str = obj["ListDataSource"]
      """  Defines the type of dynamic list from Static, BAQ, Program, etc.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RunTblLookup:bool = obj["RunTblLookup"]
      """  RunTblLookup  """  
      self.TblLookupID:str = obj["TblLookupID"]
      """  TblLookupID  """  
      self.TblLookupFunc:str = obj["TblLookupFunc"]
      """  TblLookupFunc  """  
      self.RunUserDefined:str = obj["RunUserDefined"]
      """  RunUserDefined  """  
      self.UserDefinedName:str = obj["UserDefinedName"]
      """  UserDefinedName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SortOrder:str = obj["SortOrder"]
      """  SortOrder  """  
      self.SubReturnColumn:str = obj["SubReturnColumn"]
      """  SubReturnColumn  """  
      self.ScriptCondition:str = obj["ScriptCondition"]
      """  ScriptCondition  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Reserved for Future Development  """  
      self.EnableScript:bool = obj["EnableScript"]
      """  Identifies if Script expressions are valid for Dynamic List Conditions  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      self.PageSeq:int = obj["PageSeq"]
      self.UserDefinedFunctionType:str = obj["UserDefinedFunctionType"]
      """  Either Client or Server where the UD Method is executed.  """  
      self.UserDefinedReturnType:str = obj["UserDefinedReturnType"]
      """  Storing the Return Type for the selected User Defined Method.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then details on this record can be updated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerDetailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  InputName  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.LayerSeq:int = obj["LayerSeq"]
      """  LayerSeq  """  
      self.LayerName:str = obj["LayerName"]
      """  LayerName  """  
      self.LayerDesc:str = obj["LayerDesc"]
      """  LayerDesc  """  
      self.ZIndex:int = obj["ZIndex"]
      """  Order in which layers are placed on the base image.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.FileType:str = obj["FileType"]
      """  Png type is supported.  """  
      self.Category:str = obj["Category"]
      """  Free form text enabling users to categorize layers  """  
      self.Width:int = obj["Width"]
      """  Width of image  """  
      self.Height:int = obj["Height"]
      """  Height of image  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for Future Development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for Future Development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input name this header is assigned.  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  Image Layer ID.  """  
      self.ImageID:str = obj["ImageID"]
      """  File name of the image to be retrieved from the Image URL.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ImageURL:str = obj["ImageURL"]
      """  The URL location of the image.  """  
      self.FileType:str = obj["FileType"]
      """  File types png and jpg are supported.  """  
      self.Width:int = obj["Width"]
      """  Image Width  """  
      self.Height:int = obj["Height"]
      """  Image height  """  
      self.Version:int = obj["Version"]
      """  Internal next number indicating the current version. Thi is is used by Verfiy Configuration to identify when a warning message is to be written to the log.  """  
      self.xPos:int = obj["xPos"]
      """  Reserved for future development  """  
      self.yPos:int = obj["yPos"]
      """  Reserved for future development  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerIDWhereUsedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.ImageLayerID:str = obj["ImageLayerID"]
      self.InputName:str = obj["InputName"]
      self.RefreshLayerDetails:bool = obj["RefreshLayerDetails"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsLayerIDWhereUsedTableset:
   def __init__(self, obj):
      self.PcInputsLayerIDWhereUsed:list[Erp_Tablesets_PcInputsLayerIDWhereUsedRow] = obj["PcInputsLayerIDWhereUsed"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcInputsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.InputName:str = obj["InputName"]
      """  Actual name of the control.  Used to identify the control through out the system.  """  
      self.TabOrder:int = obj["TabOrder"]
      """  The order that the tab function will step through the inputs.  """  
      self.DataType:str = obj["DataType"]
      """  The type of data that can be stored in the control.  """  
      self.FormatString:str = obj["FormatString"]
      """  The format for which the data will be stored.  """  
      self.InitVal:str = obj["InitVal"]
      """  The initial value for the control.  """  
      self.StatusText:str = obj["StatusText"]
      """  The popup help message that appears when the cursor is over the control.  """  
      self.Required:bool = obj["Required"]
      """  Determines if the contol must have a value before leaving the widget or the page of controls.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  On what page does the control exist.  """  
      self.SideLabel:str = obj["SideLabel"]
      """  The control's label.  """  
      self.xPos:int = obj["xPos"]
      """  The pixel position for the x axis.  """  
      self.yPos:int = obj["yPos"]
      """  The pixel position for the Y axis.  """  
      self.pWidth:int = obj["pWidth"]
      """  The pixel width of the control.  """  
      self.pHeight:int = obj["pHeight"]
      """  The pixel height of the control.  """  
      self.ControlType:str = obj["ControlType"]
      """  The control type as defined by the client framework. For example: Ice.Lib.Framework.EpiLabel, Ice.Lib.EpiClientLib  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the widget.  """  
      self.ListItems:str = obj["ListItems"]
      """  If the widget is a combo-box or a radio-set, the list-items or the radio-buttons attribute.  """  
      self.StartDec:int = obj["StartDec"]
      """  The starting decimal for a validated numeric fill-in.  """  
      self.EndDec:int = obj["EndDec"]
      """  The ending decimal for a validated numeric fill-in.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The precision used to determine the list of numbers to validate against.  """  
      self.StartDate:str = obj["StartDate"]
      """  The starting date for a validated date fill-in.  """  
      self.EndDate:str = obj["EndDate"]
      """  The ending date for a validated date fill-in.  """  
      self.ValList:str = obj["ValList"]
      """  The list of valid responses for a validated string input.  """  
      self.Horizontal:bool = obj["Horizontal"]
      """  If the control is a radio-set, is it a horizontal or vertical radio-set.  """  
      self.IsGlobal:bool = obj["IsGlobal"]
      """  Indicates if this input's values should be made available to other configurations on different lines in the Order or Quote.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the control.  """  
      self.WebInputName:str = obj["WebInputName"]
      """  The web compatible version of the input name.  This name will be used for use on web pages only.  InputName should still be used for rules, etc.  """  
      self.SummaryLabel:str = obj["SummaryLabel"]
      """  The label that will be used for the input when displaying a configuration summary.  """  
      self.DLRunProgram:bool = obj["DLRunProgram"]
      """  If TRUE then the dynamic list will be built by running a program and using DLProgramInputs as inputs.  """  
      self.DLProgramName:str = obj["DLProgramName"]
      """  The Progress program used for building a dynamic list.  """  
      self.DLProgramInputs:str = obj["DLProgramInputs"]
      """  The inputs used for the Progress program used for building a dynamic list.  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.HideInSummary:bool = obj["HideInSummary"]
      """  If TRUE then this input will not be shown in the configuration summary  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add On Leave expressions to this control  """  
      self.Invisible:bool = obj["Invisible"]
      """  If true, the input will not be displayed on the input page  """  
      self.Comments:str = obj["Comments"]
      """  Comments describing the input  """  
      self.GlobalInputVar:bool = obj["GlobalInputVar"]
      """  Global Input Variable  """  
      self.GlbInputVarName:str = obj["GlbInputVarName"]
      """  Global Input Variable Name  """  
      self.NoDispSummary:bool = obj["NoDispSummary"]
      """  Do not display input in Summary  """  
      self.ExternalRef:bool = obj["ExternalRef"]
      """  If true, allows entry to link input to inspection attribute data  """  
      self.AttributeID:str = obj["AttributeID"]
      """  For an Inspection Plan this is the Inspection attribute ID.  The value must exist in the Inspection Attribute master table (InspAttr).  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table.  """  
      self.UseMinValue:bool = obj["UseMinValue"]
      """  Setting to true will use the Minimum Value value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseMaxValue:bool = obj["UseMaxValue"]
      """  Setting to true will use the Maximum Value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseIncrValue:bool = obj["UseIncrValue"]
      """  Setting to true will use the Incremental Value from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseInitVal:bool = obj["UseInitVal"]
      """  Setting to true will use the InitVal from the specification detail table for inspection plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseToolTip:bool = obj["UseToolTip"]
      """  Setting to true will use the Tool Tip value from the specification detail table.  """  
      self.UseScreenLabel:bool = obj["UseScreenLabel"]
      """  Setting to true will use the screen label value from the specification detail table or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.UseListValues:bool = obj["UseListValues"]
      """  Setting to true will use the List Values value from the specification detail table for inspeciton plans or the PartAttrClassDtl table for Product Configurators and Epicor Mobile Configurators.  """  
      self.SmartPartSeq:int = obj["SmartPartSeq"]
      """  Defines the sequence of this input value in a smart part string sent for automatic processing.  """  
      self.SmartStringStart:int = obj["SmartStringStart"]
      """  Defines a starting position for the value of this input in a smart string  """  
      self.SmartStringEnd:int = obj["SmartStringEnd"]
      """  Defines an ending position for the value of this input in a smart string  """  
      self.ShowDistinct:bool = obj["ShowDistinct"]
      """  When control type is a combo box and this flag is set to TRUE the option list will only show distinct combinations of value and description  """  
      self.DesignControlType:str = obj["DesignControlType"]
      """  ControlTypeDesign will keep the control type used in the configuratoin designer (i.e. Erp.Lib.Configurator.PcControls.EpiPcTextBox, Erp.Lib.Configurator) and ControlType will hold the control type used at runtime (i.e. Ice.Lib.Framework.EpiTextBox, Ice.Lib.EpiClientLib).
 NOTE: If they are the same then both fields will have the same reference.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoSizeList:bool = obj["AutoSizeList"]
      """  AutoSizeList  """  
      self.ListWidth:int = obj["ListWidth"]
      """  ListWidth  """  
      self.ImageSource:str = obj["ImageSource"]
      """  ImageSource  """  
      self.ImageLayerID:str = obj["ImageLayerID"]
      """  ImageLayerID  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then fields on the record may be updated  """  
      self.Content:str = obj["Content"]
      self.DispCharVal:str = obj["DispCharVal"]
      """  Char Value of InitVal, this used only for the Global Input Variables form in ConfigurationDesign  """  
      self.DspPageSeq:int = obj["DspPageSeq"]
      self.FullInputName:str = obj["FullInputName"]
      """  Used to display the full input name (InputName + DesignControlType) in the property grid of the configuration designer.  """  
      self.ImageMapping:bool = obj["ImageMapping"]
      self.InitDate:str = obj["InitDate"]
      """  The initial value of a date field  """  
      self.InitDecimal:int = obj["InitDecimal"]
      """  The initial value of a decimal input  """  
      self.InitLogical:bool = obj["InitLogical"]
      """  The initial value for a logical input  """  
      self.InputRules:bool = obj["InputRules"]
      """  Indicates whether or not Input Rules have been defined.  """  
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser.  """  
      self.IsGlobalInputVar:bool = obj["IsGlobalInputVar"]
      self.OnLaunch:str = obj["OnLaunch"]
      self.PageDisplaySeq:int = obj["PageDisplaySeq"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      """  Keeps a count of the dynamic lists defined for this input in case it is a Combobox. This field is used to provide feedback on the designer's property grid.  """  
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ImageURL:str = obj["ImageURL"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The order in which these definitions are interrogated.  """  
      self.SourceInputName:str = obj["SourceInputName"]
      """  Input whose value is used in determining if this rule is executed.  """  
      self.SourceInputProperty:str = obj["SourceInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.SourceCharacterValue:str = obj["SourceCharacterValue"]
      """  SourceCharacterValue  """  
      self.SourceIntegerValue:int = obj["SourceIntegerValue"]
      """  SourceIntegerValue  """  
      self.SourceDecimalValue:int = obj["SourceDecimalValue"]
      """  SourceDecimalValue  """  
      self.SourceDateValue:str = obj["SourceDateValue"]
      """  SourceDateValue  """  
      self.SourceLogicalValue:bool = obj["SourceLogicalValue"]
      """  SourceLogicalValue  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.LeftP:str = obj["LeftP"]
      """  Reserved for future development.  """  
      self.RightP:str = obj["RightP"]
      """  Reserved for future development.  """  
      self.AndOr:str = obj["AndOr"]
      """  Defaults to And and permits users to use more than one input in the rule.  """  
      self.CompOp:str = obj["CompOp"]
      """  Comparison operator used when evaluating the rule. Valid value at this time is equals.  """  
      self.Neg:bool = obj["Neg"]
      """  Reserved for future development.  Defaults to false.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ListValues:str = obj["ListValues"]
      self.SourceValue:str = obj["SourceValue"]
      self.InputType:str = obj["InputType"]
      """  Input type valid values Label, Character, Numeric, Date, ComboBox  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourcePcInputsDesignControlType:str = obj["SourcePcInputsDesignControlType"]
      self.SourcePcInputsFormatString:str = obj["SourcePcInputsFormatString"]
      self.SourcePcInputsListItems:str = obj["SourcePcInputsListItems"]
      self.SourcePcInputsDataType:str = obj["SourcePcInputsDataType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.TargetInputName:str = obj["TargetInputName"]
      """  The Input that is updated based upon the rule definition.  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  Internal column used to keep the rows unique and permit the rule to be resequenced.  """  
      self.RuleDesc:str = obj["RuleDesc"]
      """  Enter text that describes what the rule does.  """  
      self.TargetInputProperty:str = obj["TargetInputProperty"]
      """  Reserved for future development.  Defaults to Value.  """  
      self.TargetInputValue:str = obj["TargetInputValue"]
      """  The new value of the input when this rule executes.  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Order in which this rule executes.  For example, if the value is 2 it is the second rule to execute providing the first rule did not result in executing.  This is assigned programmatically.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DefinitionDesc:str = obj["DefinitionDesc"]
      """  Associated Rule Defintion descriptions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcInputsTableset:
   def __init__(self, obj):
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PcPageExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.Expression:str = obj["Expression"]
      """  The On Leave expression for the control.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcPageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PageSeq:int = obj["PageSeq"]
      """  The configuration page sequence.  """  
      self.PageTitle:str = obj["PageTitle"]
      """  The title of the configuration page.  """  
      self.PromptWhen:str = obj["PromptWhen"]
      """  The prompt when expression for the page.  """  
      self.OnLeave:str = obj["OnLeave"]
      """  The On Leave expression for the page  """  
      self.SkipOnLeaveOPL:bool = obj["SkipOnLeaveOPL"]
      """  If this is set to true then 'On Leave' expressions will not be processed when the input page loads during the configuration process.  Also, if this is set to true then it won't process the 'On Leave' expression for the current input unless the value changes.  If the value changes and the  OnLeave expression for the current input changes the value of another input then it will process the 'On Leave' expression for the other input.  """  
      self.OnLeave2:str = obj["OnLeave2"]
      """  Additional field to add OnLeave expressions to the page  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.ProcessDynLstFirst:bool = obj["ProcessDynLstFirst"]
      """  Process dynamic lists before on leave expressions for this page  """  
      self.DynLstHigher:bool = obj["DynLstHigher"]
      """  Only process dynamic lists with higher tab sequences  """  
      self.SkipPageProcessOL:bool = obj["SkipPageProcessOL"]
      """  Skip processing page on leave on load  """  
      self.SkipPageNoInputs:bool = obj["SkipPageNoInputs"]
      """  Do not process on leave expressions when page loads  """  
      self.SkipOnLeaveOPE:bool = obj["SkipOnLeaveOPE"]
      """  Do not process on leave expressions when leaving pages  """  
      self.pWidth:int = obj["pWidth"]
      """  Width of panel  """  
      self.pHeight:int = obj["pHeight"]
      """  Height of panel  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  Order sequence in which the page will be displayed to the user. This value has been separated from PageSeq.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ReadOnly:bool = obj["ReadOnly"]
      """  ReadOnly  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.FirstPage:bool = obj["FirstPage"]
      self.TestPlan:bool = obj["TestPlan"]
      self.ReadOnlyExpression:str = obj["ReadOnlyExpression"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.TypeCode:str = obj["TypeCode"]
      """  TypeCode  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.Approved:bool = obj["Approved"]
      """  Configurator Approval Status  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date the configuration was approved.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.StringStyle:str = obj["StringStyle"]
      """  Smart String Style  """  
      self.Separator:str = obj["Separator"]
      """  Smart String Seperator character  """  
      self.NumberFormat:str = obj["NumberFormat"]
      """  Smart String Digit Structure  """  
      self.StartNumber:int = obj["StartNumber"]
      """  Smart String Starting Sequence  """  
      self.CrtCustPart:bool = obj["CrtCustPart"]
      """  Part Creation Method  """  
      self.PrefacePart:bool = obj["PrefacePart"]
      """  Smart String preface with part numbner  """  
      self.ConfigVersion:int = obj["ConfigVersion"]
      """  Configurator Version  """  
      self.QuotePCode:str = obj["QuotePCode"]
      """  Quote Price Code  """  
      self.OrderPCode:str = obj["OrderPCode"]
      """  Order Price Code  """  
      self.OrdQuoCom:bool = obj["OrdQuoCom"]
      """  OrdQuoCom  """  
      self.JobPickCom:bool = obj["JobPickCom"]
      """  JobPickCom  """  
      self.ShipCom:bool = obj["ShipCom"]
      """  ShipCom  """  
      self.InvCom:bool = obj["InvCom"]
      """  InvCom  """  
      self.CreatePart:bool = obj["CreatePart"]
      """  Create Part Flag  """  
      self.CrtPartUsing:str = obj["CrtPartUsing"]
      """  Create part method  """  
      self.InQuoting:bool = obj["InQuoting"]
      """  Create New Part In Quote Entry  """  
      self.AutoCrtPart:bool = obj["AutoCrtPart"]
      """  Automatically create a new part number  """  
      self.NotUnique:bool = obj["NotUnique"]
      """  Do not prompt user if part exists  """  
      self.InOrderEntry:bool = obj["InOrderEntry"]
      """  Create New Part In Sales Order Entry  """  
      self.InJobEntry:bool = obj["InJobEntry"]
      """  Create New Part In Job Entry  """  
      self.CreateBOM:bool = obj["CreateBOM"]
      """  Create Bill of Material  """  
      self.ZeroCost:bool = obj["ZeroCost"]
      """  Create Part at zero cost  """  
      self.CrtPartDesc:bool = obj["CrtPartDesc"]
      """  Create Smart String in part description  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.SingleLevelConf:bool = obj["SingleLevelConf"]
      """  Added to provide backward compatibility to previous releases.  """  
      self.SaveInputValues:bool = obj["SaveInputValues"]
      """  Indicates if the input values should be saved.  """  
      self.SetPartNumOnly:bool = obj["SetPartNumOnly"]
      """  If this is set to true then the part number field will be updated on the quote, order, or job with the generated part number but no part record will be created.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.AprvRev:bool = obj["AprvRev"]
      """  If true, revision will also be approved when configuration is approved.  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  This flag indicates that the configurator is an enterprise configurator and enables the external company setup options within the product configurator designer.  """  
      self.Synchronize:bool = obj["Synchronize"]
      """  This option is available for enterprise configurators.  If true, configuration will be synchronized with external companies.  """  
      self.DispConfSummary:bool = obj["DispConfSummary"]
      """  If true, the configuration summary grid will be displayed when reconfiguring a part  """  
      self.PartComments:str = obj["PartComments"]
      """  Part creation comments  """  
      self.CompPricing:bool = obj["CompPricing"]
      """  If checked, the order price will be calculated using the resulting bill of material based on the pricelists of each remaining component after the method rules have been applied.  The resulting order price will be the total component price plus any additional order input pricing that may have been defined.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External configurator  """  
      self.ExtMfgCompID:str = obj["ExtMfgCompID"]
      """  External company ID  """  
      self.TestPlan:bool = obj["TestPlan"]
      """  Set to true if the configuration is being created for an Inspection type part (Part.TypeCode = I).  """  
      self.MarkMtlGlb:bool = obj["MarkMtlGlb"]
      """  If true, material components of the enterprise configurator will be marked as global to be exported to external companies  """  
      self.SIValuesUseQt:bool = obj["SIValuesUseQt"]
      """  If true, when saving input values, the generated method will be created using the resulting quote method instead of the resulting job method.  """  
      self.AllowSmartString:bool = obj["AllowSmartString"]
      """  This field will enable smart string processing for this configuration  """  
      self.InDemandEntry:bool = obj["InDemandEntry"]
      self.DemandPCode:str = obj["DemandPCode"]
      """  Demand Price Code  """  
      self.AllAltMethods:bool = obj["AllAltMethods"]
      """  If checked, all alternate methods of the part revision will be created  """  
      self.AllowReconPO:bool = obj["AllowReconPO"]
      """  AllowReconPO  """  
      self.CompPricingJobMethod:bool = obj["CompPricingJobMethod"]
      """  If you select the Use Component Pricing check box and the Epicor application uses the resulting job method to determine component pricing during an actual configuration session. When a user completes the session and saves the configuration, the Epicor application applies the appropriate Keep When and Set Field method rules against the job entity defined for this Configurator ID. After applying these rules, the Epicor application uses the resulting part number and per quantities to create a virtual method of manufacture for the job, which it uses to roll up the prices for each resulting material and its quantity.  """  
      self.CreateRev:bool = obj["CreateRev"]
      """  Select this check box if the Epicor application should also create a new part revision record for the newly created part when you save a configuration after completing a Configuration session  """  
      self.DefaultECO:str = obj["DefaultECO"]
      """  If you select the Prompt For Checkout check box, you can use this field to specify the default value that displays in the ECO Group field in the Part Revision Checkout window (invoked when you use the Check Out Revision selection, located under the Revision submenu in the Part Maintenance Actions menu).  """  
      self.GenerateMethod:bool = obj["GenerateMethod"]
      """  If you select this check box, the Epicor application generates a method of manufacture by processing associated method rules.  """  
      self.PromptForConfig:bool = obj["PromptForConfig"]
      """  PromptForConfig  """  
      self.PromptForCheckout:bool = obj["PromptForCheckout"]
      """  Specifies if Part Revision Checkout should automatically display when a configuration is saved after completing a Configuration session.  """  
      self.RemoveLink:bool = obj["RemoveLink"]
      """  If you select the Create Non-Configurable Part check box, the application removes the link back to the base configured part. The newly created part is treated as a standard part and is no longer considered a reconfigurable part  """  
      self.SIValuesUseGenMethod:bool = obj["SIValuesUseGenMethod"]
      """  SIValuesUseGenMethod  """  
      self.UseSavedLayout:bool = obj["UseSavedLayout"]
      """  Select this check box to designate that the Epicor application should load the layout that was created when the part was originally configured  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ConfigType:str = obj["ConfigType"]
      """  ConfigType  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.CreateNewConfigID:bool = obj["CreateNewConfigID"]
      """  CreateNewConfigID  """  
      self.UseTemplatePartDefaults:bool = obj["UseTemplatePartDefaults"]
      """  UseTemplatePartDefaults  """  
      self.DefaultPartNum:str = obj["DefaultPartNum"]
      """  DefaultPartNum  """  
      self.DefaultRevisionNum:str = obj["DefaultRevisionNum"]
      """  DefaultRevisionNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  For a Product Configurator or Epicor Mobile this is the PartAttrClassDtl Attribute ID and must exist in that table  """  
      self.RecycleJobs:bool = obj["RecycleJobs"]
      """  RecycleJobs  """  
      self.ClientDeployedToEWCDate:str = obj["ClientDeployedToEWCDate"]
      """  ClientDeployedToEWCDate  """  
      self.EWCClientSyncRequired:bool = obj["EWCClientSyncRequired"]
      """  EWCClientSyncRequired  """  
      self.ShrinkFieldProperties:bool = obj["ShrinkFieldProperties"]
      """  ShrinkFieldProperties  """  
      self.Kinetic:bool = obj["Kinetic"]
      """  Kinetic  """  
      self.KBConfigID:int = obj["KBConfigID"]
      """  KBConfigID  """  
      self.KBConfigDesc:str = obj["KBConfigDesc"]
      """  KBConfigDesc  """  
      self.AvailSmartStringInputs:str = obj["AvailSmartStringInputs"]
      """  The available inputs available for use in the smart string  """  
      self.ECOGroup:str = obj["ECOGroup"]
      """  If not null, indicates the revision is checked out to an ECO group.  """  
      self.HasInputs:bool = obj["HasInputs"]
      """  Indicates if the configurator has inputs in its design.  """  
      self.IsValidPwd:bool = obj["IsValidPwd"]
      self.ResetPCInputsAttributes:bool = obj["ResetPCInputsAttributes"]
      """  Yes indicates the Attributes assigned to the PCInputs for this ConfigID will be set to the initial values.  """  
      self.RevApproved:bool = obj["RevApproved"]
      """  True if the PartRev record is approved  """  
      self.SampleSmartString:str = obj["SampleSmartString"]
      """  A sample smart string constructed from the smart string options  """  
      self.SelectedSmartStringInputs:str = obj["SelectedSmartStringInputs"]
      """  The inputs that have been selected for use in the smart string  """  
      self.UpdateCreatePartTarget:bool = obj["UpdateCreatePartTarget"]
      """  Yes indicates the Target Entities Create Part column is to be set to the value of PCStatus.CreatePart  """  
      self.AuditDesc:str = obj["AuditDesc"]
      """  The change description to use for the PcAudit when approving a configuration  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      """  If true then detail fields other than Approved can be updated  """  
      self.EnableCPQPartCreation:bool = obj["EnableCPQPartCreation"]
      """  Enable/disable Part Creation for CPQ type configurators.  This is controlled by the Feature Flag CPQPartCreation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTypeCode:str = obj["PartNumTypeCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildDrawingObjectsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ConfigID:str = obj["ConfigID"]
      self.InputName:str = obj["InputName"]
      self.ObjName:str = obj["ObjName"]
      self.ObjParameter:str = obj["ObjParameter"]
      self.ObjType:str = obj["ObjType"]
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildDrawingObjectsTableset:
   def __init__(self, obj):
      self.QBuildDrawingObjects:list[Erp_Tablesets_QBuildDrawingObjectsRow] = obj["QBuildDrawingObjects"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QBuildMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the object name.  """  
      self.ObjParameter:str = obj["ObjParameter"]
      """  This is the name of the object parameter.  """  
      self.MappedInputName:str = obj["MappedInputName"]
      """  Name of the input mapped to this object parameter.  """  
      self.ObjParameterDataType:str = obj["ObjParameterDataType"]
      """  This is the data type of the object parameter.  """  
      self.ObjParameterInitValue:str = obj["ObjParameterInitValue"]
      """  This is the initial value of the object parameter as it was defined in the designer.  This is reserved for future development.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DataType:str = obj["DataType"]
      self.PageSeq:int = obj["PageSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.QBuildObjObjType:str = obj["QBuildObjObjType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QBuildObjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.InputName:str = obj["InputName"]
      """  Input Name  """  
      self.ObjName:str = obj["ObjName"]
      """  This is the name of the object.  """  
      self.ObjType:str = obj["ObjType"]
      """  This is the object type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PageSeq:int = obj["PageSeq"]
      self.DataType:str = obj["DataType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QueryFieldListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SubQueryID:str = obj["SubQueryID"]
      """  SubQueryID  """  
      self.TableID:str = obj["TableID"]
      """  TableID  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.DBSchemaName:str = obj["DBSchemaName"]
      """  DBSchemaName  """  
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  Data Type  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.External:bool = obj["External"]
      """  External  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  IsCalculated  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldSeq:int = obj["LikeDataFieldSeq"]
      """  Like Data Field Sequence  """  
      self.Aggregation:str = obj["Aggregation"]
      """  Aggregation  """  
      self.IsGroupBy:bool = obj["IsGroupBy"]
      """  IsGroupBy  """  
      self.UseLike:bool = obj["UseLike"]
      """  Use Like  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Field Name  """  
      self.Updatable:bool = obj["Updatable"]
      """  Wheither field can be updated  """  
      self.RaiseEvent:bool = obj["RaiseEvent"]
      """  Raise event on update  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  ID of Quick Search assigned to this query field  """  
      self.DropDown:bool = obj["DropDown"]
      """  This flag tells whether this display field is used as source of distinct values for drop down list in IW  """  
      self.UpdInitExpression:str = obj["UpdInitExpression"]
      """  Initial expression for updatable field, filled on UBAQ.GetNew  """  
      self.Alias:str = obj["Alias"]
      """  Alias  """  
      self.IsRequired:bool = obj["IsRequired"]
      """  IsRequired  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  IsReadOnly  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisplayName:str = obj["DisplayName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QueryFieldListTableset:
   def __init__(self, obj):
      self.QueryFieldList:list[Erp_Tablesets_QueryFieldListRow] = obj["QueryFieldList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtConfigurationDesignTableset:
   def __init__(self, obj):
      self.PcStatus:list[Erp_Tablesets_PcStatusRow] = obj["PcStatus"]
      self.PcPage:list[Erp_Tablesets_PcPageRow] = obj["PcPage"]
      self.PcInputs:list[Erp_Tablesets_PcInputsRow] = obj["PcInputs"]
      self.PcInputsLayerHeader:list[Erp_Tablesets_PcInputsLayerHeaderRow] = obj["PcInputsLayerHeader"]
      self.PcInputsLayerDetail:list[Erp_Tablesets_PcInputsLayerDetailRow] = obj["PcInputsLayerDetail"]
      self.PcDynLst:list[Erp_Tablesets_PcDynLstRow] = obj["PcDynLst"]
      self.PcDynLstCriteria:list[Erp_Tablesets_PcDynLstCriteriaRow] = obj["PcDynLstCriteria"]
      self.PcDynLstExpr:list[Erp_Tablesets_PcDynLstExprRow] = obj["PcDynLstExpr"]
      self.PcDynLstParams:list[Erp_Tablesets_PcDynLstParamsRow] = obj["PcDynLstParams"]
      self.PcInputsExpr:list[Erp_Tablesets_PcInputsExprRow] = obj["PcInputsExpr"]
      self.PcInputsRule:list[Erp_Tablesets_PcInputsRuleRow] = obj["PcInputsRule"]
      self.PcInputsRuleDef:list[Erp_Tablesets_PcInputsRuleDefRow] = obj["PcInputsRuleDef"]
      self.QBuildObj:list[Erp_Tablesets_QBuildObjRow] = obj["QBuildObj"]
      self.QBuildMapping:list[Erp_Tablesets_QBuildMappingRow] = obj["QBuildMapping"]
      self.PcPageExpr:list[Erp_Tablesets_PcPageExprRow] = obj["PcPageExpr"]
      self.PcStatusExpr:list[Erp_Tablesets_PcStatusExprRow] = obj["PcStatusExpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExistsProposedInputName_input:
   """ Required : 
   configID
   proposedValue
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.proposedValue:str = obj["proposedValue"]
      """  Proposed Value  """  
      pass

class ExistsProposedInputName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetAttributeDesc_input:
   """ Required : 
   attributeID
   """  
   def __init__(self, obj):
      self.attributeID:str = obj["attributeID"]
      """  Target Attribute ID  """  
      pass

class GetAttributeDesc_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Inspection Attribute Description  """  
      pass

class GetBAQDisplayColumnList_input:
   """ Required : 
   searchExpression
   """  
   def __init__(self, obj):
      self.searchExpression:str = obj["searchExpression"]
      """  Search filter expression  """  
      pass

class GetBAQDisplayColumnList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QueryFieldListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["returnObj"]
      pass

class GetDefaultListItems_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDynAttributeDesc_input:
   """ Required : 
   schemaName
   tableName
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Related to table Name  """  
      self.attrClassID:str = obj["attrClassID"]
      """  Part Attribute Class ID to use to validate the Attribute ID  """  
      self.attributeID:str = obj["attributeID"]
      """  Target Attribute ID  """  
      pass

class GetDynAttributeDesc_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Part Attribute Description  """  
      pass

class GetInputList_input:
   """ Required : 
   searchExpression
   """  
   def __init__(self, obj):
      self.searchExpression:str = obj["searchExpression"]
      """  Seatch expression  """  
      pass

class GetInputList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcInputsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfigurationDesignListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPcDynLstCriteria_input:
   """ Required : 
   ds
   configID
   inputName
   listSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.listSeq:int = obj["listSeq"]
      pass

class GetNewPcDynLstCriteria_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDynLstExpr_input:
   """ Required : 
   ds
   configID
   inputName
   listSeq
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.listSeq:int = obj["listSeq"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcDynLstExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDynLstParams_input:
   """ Required : 
   ds
   configID
   inputName
   listSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.listSeq:int = obj["listSeq"]
      pass

class GetNewPcDynLstParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcDynLst_input:
   """ Required : 
   ds
   configID
   inputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetNewPcDynLst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsExpr_input:
   """ Required : 
   ds
   configID
   inputName
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcInputsExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsLayerDetail_input:
   """ Required : 
   ds
   configID
   inputName
   imageLayerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class GetNewPcInputsLayerDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsLayerHeader_input:
   """ Required : 
   ds
   configID
   inputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetNewPcInputsLayerHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsRuleDef_input:
   """ Required : 
   ds
   configID
   targetInputName
   ruleSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.targetInputName:str = obj["targetInputName"]
      self.ruleSeq:int = obj["ruleSeq"]
      pass

class GetNewPcInputsRuleDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputsRule_input:
   """ Required : 
   ds
   configID
   targetInputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.targetInputName:str = obj["targetInputName"]
      pass

class GetNewPcInputsRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcInputs_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcInputs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcPageExpr_input:
   """ Required : 
   ds
   configID
   pageSeq
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.pageSeq:int = obj["pageSeq"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcPageExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcPage_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewPcPage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcStatusExpr_input:
   """ Required : 
   ds
   configID
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcStatusExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcStatus_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class GetNewPcStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQBuildMapping_input:
   """ Required : 
   ds
   configID
   inputName
   objName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      self.objName:str = obj["objName"]
      pass

class GetNewQBuildMapping_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQBuildObj_input:
   """ Required : 
   ds
   configID
   inputName
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.inputName:str = obj["inputName"]
      pass

class GetNewQBuildObj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPcInputsWithLayerIDForConfiguration_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration to retrieve the Inputs with an ImageLayerID specified.  """  
      pass

class GetPcInputsWithLayerIDForConfiguration_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PcInputsLayerIDWhereUsedTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePcStatus
   whereClausePcPage
   whereClausePcInputs
   whereClausePcInputsLayerHeader
   whereClausePcInputsLayerDetail
   whereClausePcDynLst
   whereClausePcDynLstCriteria
   whereClausePcDynLstExpr
   whereClausePcDynLstParams
   whereClausePcInputsExpr
   whereClausePcInputsRule
   whereClausePcInputsRuleDef
   whereClauseQBuildObj
   whereClauseQBuildMapping
   whereClausePcPageExpr
   whereClausePcStatusExpr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePcStatus:str = obj["whereClausePcStatus"]
      self.whereClausePcPage:str = obj["whereClausePcPage"]
      self.whereClausePcInputs:str = obj["whereClausePcInputs"]
      self.whereClausePcInputsLayerHeader:str = obj["whereClausePcInputsLayerHeader"]
      self.whereClausePcInputsLayerDetail:str = obj["whereClausePcInputsLayerDetail"]
      self.whereClausePcDynLst:str = obj["whereClausePcDynLst"]
      self.whereClausePcDynLstCriteria:str = obj["whereClausePcDynLstCriteria"]
      self.whereClausePcDynLstExpr:str = obj["whereClausePcDynLstExpr"]
      self.whereClausePcDynLstParams:str = obj["whereClausePcDynLstParams"]
      self.whereClausePcInputsExpr:str = obj["whereClausePcInputsExpr"]
      self.whereClausePcInputsRule:str = obj["whereClausePcInputsRule"]
      self.whereClausePcInputsRuleDef:str = obj["whereClausePcInputsRuleDef"]
      self.whereClauseQBuildObj:str = obj["whereClauseQBuildObj"]
      self.whereClauseQBuildMapping:str = obj["whereClauseQBuildMapping"]
      self.whereClausePcPageExpr:str = obj["whereClausePcPageExpr"]
      self.whereClausePcStatusExpr:str = obj["whereClausePcStatusExpr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSourceInputNameList_input:
   """ Required : 
   configID
   targetInputName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration used.  """  
      self.targetInputName:str = obj["targetInputName"]
      """  targetInputName used.  """  
      pass

class GetSourceInputNameList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class ImageLayerScriptCode_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class ImageLayerScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImageLayerUpdateScriptCode_input:
   """ Required : 
   imageLayerID
   """  
   def __init__(self, obj):
      self.imageLayerID:str = obj["imageLayerID"]
      pass

class ImageLayerUpdateScriptCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportImagesFileStore_input:
   """ Required : 
   FileName
   Image
   RenameDuplicates
   UpdateDuplicates
   ConfigID
   InputName
   ConfigurationDesignTS
   ttQBuildDrawingObjectsTablesetTS
   """  
   def __init__(self, obj):
      self.FileName:str = obj["FileName"]
      """  Name of Image file  """  
      self.Image:str = obj["Image"]
      """  byte array of the content  """  
      self.RenameDuplicates:bool = obj["RenameDuplicates"]
      """  boolean indicating whether or not to rename duplicates.  """  
      self.UpdateDuplicates:bool = obj["UpdateDuplicates"]
      """  boolean indicating whether or not to update duplicates.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  Configuration ID  """  
      self.InputName:str = obj["InputName"]
      """  Input that is being updated  """  
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      self.ttQBuildDrawingObjectsTablesetTS:list[Erp_Tablesets_QBuildDrawingObjectsTableset] = obj["ttQBuildDrawingObjectsTablesetTS"]
      pass

class ImportImagesFileStore_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

      """  output parameters  """  

class NumberOfDecimalPlaces_input:
   """ Required : 
   inParam
   """  
   def __init__(self, obj):
      self.inParam:str = obj["inParam"]
      """  Format string  """  
      pass

class NumberOfDecimalPlaces_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class OnChangeAttributeID_input:
   """ Required : 
   schemaName
   tableName
   attributeID
   ds
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Related to table Name  """  
      self.attributeID:str = obj["attributeID"]
      """  proposed attribute ID to validate  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeAttributeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeDynAttributeID_input:
   """ Required : 
   schemaName
   tableName
   attributeID
   ds
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Related to table Name  """  
      self.attributeID:str = obj["attributeID"]
      """  proposed attribute ID to validate  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeDynAttributeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.warningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFormatString_input:
   """ Required : 
   ConfigID
   InputName
   NewFormatString
   """  
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      self.InputName:str = obj["InputName"]
      self.NewFormatString:str = obj["NewFormatString"]
      pass

class OnChangeFormatString_output:
   def __init__(self, obj):
      pass

class OnChangeImageLayerID_input:
   """ Required : 
   proposedImageLayerID
   ds
   """  
   def __init__(self, obj):
      self.proposedImageLayerID:str = obj["proposedImageLayerID"]
      """  Image layer id to validate  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeImageLayerID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      self.imageURL:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeInputName_input:
   """ Required : 
   inputName
   ds
   """  
   def __init__(self, obj):
      self.inputName:str = obj["inputName"]
      """  The control name.  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeInputName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInputPageNumber_input:
   """ Required : 
   newPageDispSeq
   ds
   """  
   def __init__(self, obj):
      self.newPageDispSeq:int = obj["newPageDispSeq"]
      """  Target Display Sequence  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeInputPageNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInputReadOnlyExpr_input:
   """ Required : 
   readOnlyExpr
   ds
   """  
   def __init__(self, obj):
      self.readOnlyExpr:bool = obj["readOnlyExpr"]
      """  Is ReadOnlyExpr Variable  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeInputReadOnlyExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInputTabOrder_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeInputTabOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInputType_input:
   """ Required : 
   inputType
   ds
   """  
   def __init__(self, obj):
      self.inputType:str = obj["inputType"]
      """  The control style.  Options are Label, Character, Date, Decimal, CheckBox, Button, Editor, ComboBox, Rectangle, RadioSet, Browser  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeInputType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMinOrMaxForDecimal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeMinOrMaxForDecimal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePageDisplaySeq_input:
   """ Required : 
   newPageDispSeq
   ds
   """  
   def __init__(self, obj):
      self.newPageDispSeq:int = obj["newPageDispSeq"]
      """  Target Display Sequence  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangePageDisplaySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePageReadOnlyExpr_input:
   """ Required : 
   readOnlyExpr
   ds
   """  
   def __init__(self, obj):
      self.readOnlyExpr:bool = obj["readOnlyExpr"]
      """  Is ReadOnlyExpr Variable  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangePageReadOnlyExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSourceInputName_input:
   """ Required : 
   sourceInputName
   ds
   """  
   def __init__(self, obj):
      self.sourceInputName:str = obj["sourceInputName"]
      """  Source Input Name  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangeSourceInputName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedGlobalInputVar_input:
   """ Required : 
   globalInputVar
   ds
   """  
   def __init__(self, obj):
      self.globalInputVar:bool = obj["globalInputVar"]
      """  Is Global Input Variable  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangedGlobalInputVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingBAQName_input:
   """ Required : 
   inputName
   listSeq
   ds
   """  
   def __init__(self, obj):
      self.inputName:str = obj["inputName"]
      """  Input Name  """  
      self.listSeq:str = obj["listSeq"]
      """  List Seq  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangingBAQName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingDataLookupFunction_input:
   """ Required : 
   functionName
   ds
   """  
   def __init__(self, obj):
      self.functionName:str = obj["functionName"]
      """  Function Method Name  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangingDataLookupFunction_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingGlbInputVarName_input:
   """ Required : 
   glbInputVarName
   ds
   """  
   def __init__(self, obj):
      self.glbInputVarName:str = obj["glbInputVarName"]
      """  Global Input Variable Name  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangingGlbInputVarName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingListDataSource_input:
   """ Required : 
   listDataSource
   ds
   """  
   def __init__(self, obj):
      self.listDataSource:str = obj["listDataSource"]
      """  Data Source Type  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangingListDataSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingUserDefinedMethodName_input:
   """ Required : 
   userDefinedMethodName
   configId
   company
   ds
   """  
   def __init__(self, obj):
      self.userDefinedMethodName:str = obj["userDefinedMethodName"]
      """  User Defined Method Name  """  
      self.configId:str = obj["configId"]
      """  Current ConfigID  """  
      self.company:str = obj["company"]
      """  Current Company  """  
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class OnChangingUserDefinedMethodName_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PageCountForCodeEditor_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      pass

class PageCountForCodeEditor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pageCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class PromptForPassword_input:
   """ Required : 
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID  """  
      pass

class PromptForPassword_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPromptForPassword:bool = obj["opPromptForPassword"]
      self.opRevisionStatus:bool = obj["opRevisionStatus"]
      self.opRevisionFound:bool = obj["opRevisionFound"]
      pass

      """  output parameters  """  

class RefreshImageLayerDetails_input:
   """ Required : 
   ds
   dsConfigDesign
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsLayerIDWhereUsedTableset] = obj["ds"]
      self.dsConfigDesign:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["dsConfigDesign"]
      pass

class RefreshImageLayerDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PcInputsLayerIDWhereUsedTableset] = obj["ds"]
      self.dsConfigDesign:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["dsConfigDesign"]
      pass

      """  output parameters  """  

class SyncRevision_input:
   """ Required : 
   ipApproved
   ipValidPassword
   ipConfigID
   ipAuditDesc
   """  
   def __init__(self, obj):
      self.ipApproved:bool = obj["ipApproved"]
      """  The proposed approval flag  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID  """  
      self.ipAuditDesc:str = obj["ipAuditDesc"]
      """  The audit description entered for the configuration approval  """  
      pass

class SyncRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.revSynched:bool = obj["revSynched"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfigurationDesignTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfigurationDesignTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateQBuildMapping_input:
   """ Required : 
   ConfigurationDesignTS
   """  
   def __init__(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

class UpdateQBuildMapping_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateAllowedToDeletePcInput_input:
   """ Required : 
   configID
   inputName
   skipQBuildMappingChecks
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configurator ID  """  
      self.inputName:str = obj["inputName"]
      """  PcInput name  """  
      self.skipQBuildMappingChecks:bool = obj["skipQBuildMappingChecks"]
      """  Skip Validate QBuild Mapping  """  
      pass

class ValidateAllowedToDeletePcInput_output:
   def __init__(self, obj):
      pass

class ValidateBAQColumnName_input:
   """ Required : 
   queryID
   fieldName
   """  
   def __init__(self, obj):
      self.queryID:str = obj["queryID"]
      """  Query ID  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class ValidateBAQColumnName_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if a QueryField record exists with the given parameters  """  
      pass

   def parameters(self, obj):
      self.dataType:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateImageLayerID_input:
   """ Required : 
   proposedImageLayerID
   """  
   def __init__(self, obj):
      self.proposedImageLayerID:str = obj["proposedImageLayerID"]
      """  Image layer id to validate  """  
      pass

class ValidateImageLayerID_output:
   def __init__(self, obj):
      pass

class ValidateInputName_input:
   """ Required : 
   ConfigID
   ProposedInputName
   """  
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      """  the configuration ID of the Input  """  
      self.ProposedInputName:str = obj["ProposedInputName"]
      """  The name the user wants to use as a name  """  
      pass

class ValidateInputName_output:
   def __init__(self, obj):
      pass

class ValidateMappedInput_input:
   """ Required : 
   ConfigurationDesignTS
   MappedInputName
   """  
   def __init__(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      self.MappedInputName:str = obj["MappedInputName"]
      """  Proposed Mapped Input Name to validate  """  
      pass

class ValidateMappedInput_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ConfigurationDesignTS:list[Erp_Tablesets_ConfigurationDesignTableset] = obj["ConfigurationDesignTS"]
      pass

      """  output parameters  """  

class ValidatePcLookupColSetDtl_input:
   """ Required : 
   inLookupTblID
   colName
   """  
   def __init__(self, obj):
      self.inLookupTblID:str = obj["inLookupTblID"]
      """  LookupTblID  """  
      self.colName:str = obj["colName"]
      """  ColName  """  
      pass

class ValidatePcLookupColSetDtl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if a PcLookupColSetDtl record exists with the given parameter  """  
      pass

class ValidatePcLookupTblHed_input:
   """ Required : 
   inLookupTblID
   """  
   def __init__(self, obj):
      self.inLookupTblID:str = obj["inLookupTblID"]
      """  LookupTblID  """  
      pass

class ValidatePcLookupTblHed_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if a PcLookupTblHed record exists with the given parameter  """  
      pass

