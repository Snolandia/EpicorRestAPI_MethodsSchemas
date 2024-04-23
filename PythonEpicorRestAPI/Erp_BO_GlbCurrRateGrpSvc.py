import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbCurrRateGrpSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrRateGrps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrRateGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrRateGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company, GlbCompany, GlbRateGrpCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrRateGrp item
   Description: Calls GetByID to retrieve the GlbCurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company, GlbCompany, GlbRateGrpCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCurrRateGrp for the service
   Description: Calls UpdateExt to update GlbCurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode(Company, GlbCompany, GlbRateGrpCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCurrRateGrp item
   Description: Call UpdateExt to delete GlbCurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrRateGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrConvRules(Company, GlbCompany, GlbRateGrpCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GlbCurrConvRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrConvRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrConvRules",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrConvRule item
   Description: Calls GetByID to retrieve the GlbCurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrConvRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrRateDisps(Company, GlbCompany, GlbRateGrpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GlbCurrRateDisps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrRateDisps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrRateDisps",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateGrps_Company_GlbCompany_GlbRateGrpCode_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company, GlbCompany, GlbRateGrpCode, GlbSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrRateDisp item
   Description: Calls GetByID to retrieve the GlbCurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateDisp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSeq: Desc: GlbSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateGrps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + ")/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrConvRules(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrConvRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrConvRules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrConvRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrConvRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrConvRule item
   Description: Calls GetByID to retrieve the GlbCurrConvRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCurrConvRule for the service
   Description: Calls UpdateExt to update GlbCurrConvRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrConvRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCurrConvRule item
   Description: Call UpdateExt to delete GlbCurrConvRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrConvRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbCurrExRates(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GlbCurrExRates items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCurrExRates1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")/GlbCurrExRates",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrConvRules_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, GlbEffectiveDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrExRate item
   Description: Calls GetByID to retrieve the GlbCurrExRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrExRate1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param GlbEffectiveDate: Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrConvRules(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + ")/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrExRates(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrExRates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrExRates
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrExRates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrExRates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, GlbEffectiveDate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrExRate item
   Description: Calls GetByID to retrieve the GlbCurrExRate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param GlbEffectiveDate: Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, GlbEffectiveDate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCurrExRate for the service
   Description: Calls UpdateExt to update GlbCurrExRate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param GlbEffectiveDate: Desc: GlbEffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrExRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCurrExRates_Company_GlbCompany_GlbRateGrpCode_GlbSourceCurrCode_GlbTargetCurrCode_GlbEffectiveDate(Company, GlbCompany, GlbRateGrpCode, GlbSourceCurrCode, GlbTargetCurrCode, GlbEffectiveDate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCurrExRate item
   Description: Call UpdateExt to delete GlbCurrExRate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrExRate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSourceCurrCode: Desc: GlbSourceCurrCode   Required: True   Allow empty value : True
      :param GlbTargetCurrCode: Desc: GlbTargetCurrCode   Required: True   Allow empty value : True
      :param GlbEffectiveDate: Desc: GlbEffectiveDate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrExRates(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSourceCurrCode + "," + GlbTargetCurrCode + "," + GlbEffectiveDate + ")",headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateDisps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCurrRateDisps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCurrRateDisps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps",headers=creds) as resp:
           return await resp.json()

async def post_GlbCurrRateDisps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCurrRateDisps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company, GlbCompany, GlbRateGrpCode, GlbSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCurrRateDisp item
   Description: Calls GetByID to retrieve the GlbCurrRateDisp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSeq: Desc: GlbSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company, GlbCompany, GlbRateGrpCode, GlbSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCurrRateDisp for the service
   Description: Calls UpdateExt to update GlbCurrRateDisp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSeq: Desc: GlbSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCurrRateDispRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCurrRateDisps_Company_GlbCompany_GlbRateGrpCode_GlbSeq(Company, GlbCompany, GlbRateGrpCode, GlbSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCurrRateDisp item
   Description: Call UpdateExt to delete GlbCurrRateDisp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCurrRateDisp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbRateGrpCode: Desc: GlbRateGrpCode   Required: True   Allow empty value : True
      :param GlbSeq: Desc: GlbSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/GlbCurrRateDisps(" + Company + "," + GlbCompany + "," + GlbRateGrpCode + "," + GlbSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCurrRateGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbCurrRateGrp, whereClauseGlbCurrConvRule, whereClauseGlbCurrExRate, whereClauseGlbCurrRateDisp, pageSize, absolutePage, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlbCurrRateGrp=" + whereClauseGlbCurrRateGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlbCurrConvRule=" + whereClauseGlbCurrConvRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlbCurrExRate=" + whereClauseGlbCurrExRate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGlbCurrRateDisp=" + whereClauseGlbCurrRateDisp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbRateGrpCode, epicorHeaders = None):
   """  
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
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbRateGrpCode=" + glbRateGrpCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCurrRateGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrRateGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCurrConvRule(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCurrConvRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrConvRule
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrConvRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrConvRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCurrExRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCurrExRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCurrRateDisp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCurrRateDisp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCurrRateDisp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCurrRateDisp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCurrRateDisp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCurrRateGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrConvRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrConvRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrExRateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrExRateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateDispRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrRateDispRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrRateGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCurrRateGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCurrRateGrpRow] = obj["value"]
      pass

class Erp_Tablesets_GlbCurrConvRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.UseBaseRate:bool = obj["UseBaseRate"]
      """  Determine if the user should use the base rate group defined in CurrRateGrp  """  
      self.RuleCode:int = obj["RuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.DisplayMode:int = obj["DisplayMode"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrExRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbEffectiveDate:str = obj["GlbEffectiveDate"]
      """  Effective Date from Source Company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Seq:int = obj["Seq"]
      """  Order in which the currencies should be displayed in the matrix grids  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code to be displayed  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbSeq:int = obj["GlbSeq"]
      """  Sequence from Source Company  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RateNumDec:int = obj["RateNumDec"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkRateGrpCode:str = obj["LinkRateGrpCode"]
      """  CurrRateGrp.RateGrpCode to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RateNumDec:int = obj["RateNumDec"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkRateGrpCode:str = obj["LinkRateGrpCode"]
      """  CurrRateGrp.RateGrpCode to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  holds description of currency rate group from local rate group linked.  """  
      self.Select:bool = obj["Select"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbCurrConvRuleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.UseBaseRate:bool = obj["UseBaseRate"]
      """  Determine if the user should use the base rate group defined in CurrRateGrp  """  
      self.RuleCode:int = obj["RuleCode"]
      """  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  """  
      self.FixedRate:bool = obj["FixedRate"]
      """  Indiates if the exchange rate is fixed and cannot be updated  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.DisplayMode:int = obj["DisplayMode"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrExRateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceCurrCode:str = obj["SourceCurrCode"]
      """  A unique code that identifies the source currency.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  This rate is effective as of this date.  """  
      self.CurrentRate:int = obj["CurrentRate"]
      """   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was modified.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was modified.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.Reference:str = obj["Reference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.TargetCurrCode:str = obj["TargetCurrCode"]
      """  A unique code that identifies the target currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from Source Company  """  
      self.GlbSourceCurrCode:str = obj["GlbSourceCurrCode"]
      """  Source Currency from Source Company  """  
      self.GlbTargetCurrCode:str = obj["GlbTargetCurrCode"]
      """  Target Currency from Source Company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbEffectiveDate:str = obj["GlbEffectiveDate"]
      """  Effective Date from Source Company  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateDispRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Seq:int = obj["Seq"]
      """  Order in which the currencies should be displayed in the matrix grids  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code to be displayed  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.GlbSeq:int = obj["GlbSeq"]
      """  Sequence from Source Company  """  
      self.ScaleFactor:int = obj["ScaleFactor"]
      """  Display factor for exchange rates  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Currency Rate Group is Global (master or linked)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RateNumDec:int = obj["RateNumDec"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkRateGrpCode:str = obj["LinkRateGrpCode"]
      """  CurrRateGrp.RateGrpCode to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpListTableset:
   def __init__(self, obj):
      self.GlbCurrRateGrpList:list[Erp_Tablesets_GlbCurrRateGrpListRow] = obj["GlbCurrRateGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCurrRateGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbRateGrpCode:str = obj["GlbRateGrpCode"]
      """  Currency Rate Group Code from source company  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Source Company  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates that the user has reviewed the record but its not going to be linked currently  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines if the record is inactive  """  
      self.BaseRateGrpCode:str = obj["BaseRateGrpCode"]
      """  Determins if there is a base rate group to use if no rules or rates are defined for a currency  """  
      self.CrossCurrCode:str = obj["CrossCurrCode"]
      """  Currency to use during single or double currency conversions  """  
      self.CrossRound:bool = obj["CrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.CrossRoundDec:int = obj["CrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.AltCrossCurrCode:str = obj["AltCrossCurrCode"]
      """  Currency used for double currency conversions  """  
      self.AltCrossRound:bool = obj["AltCrossRound"]
      """  Determine if rounding should be done after conversion  """  
      self.AltCrossRoundDec:int = obj["AltCrossRoundDec"]
      """  Number of decimals to use during rounding  """  
      self.GlobalGrp:bool = obj["GlobalGrp"]
      """  Determines whether or not this rate group is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this record will receive global updates.  """  
      self.DisplayMode:int = obj["DisplayMode"]
      """  Indicates which exchange rate to display/update on the transaction  """  
      self.RateNumDec:int = obj["RateNumDec"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkRateGrpCode:str = obj["LinkRateGrpCode"]
      """  CurrRateGrp.RateGrpCode to link to (new or existing)  """  
      self.LocalDesc:str = obj["LocalDesc"]
      """  holds description of currency rate group from local rate group linked.  """  
      self.Select:bool = obj["Select"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCurrRateGrpTableset:
   def __init__(self, obj):
      self.GlbCurrRateGrp:list[Erp_Tablesets_GlbCurrRateGrpRow] = obj["GlbCurrRateGrp"]
      self.GlbCurrConvRule:list[Erp_Tablesets_GlbCurrConvRuleRow] = obj["GlbCurrConvRule"]
      self.GlbCurrExRate:list[Erp_Tablesets_GlbCurrExRateRow] = obj["GlbCurrExRate"]
      self.GlbCurrRateDisp:list[Erp_Tablesets_GlbCurrRateDispRow] = obj["GlbCurrRateDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbCurrRateGrpTableset:
   def __init__(self, obj):
      self.GlbCurrRateGrp:list[Erp_Tablesets_GlbCurrRateGrpRow] = obj["GlbCurrRateGrp"]
      self.GlbCurrConvRule:list[Erp_Tablesets_GlbCurrConvRuleRow] = obj["GlbCurrConvRule"]
      self.GlbCurrExRate:list[Erp_Tablesets_GlbCurrExRateRow] = obj["GlbCurrExRate"]
      self.GlbCurrRateDisp:list[Erp_Tablesets_GlbCurrRateDispRow] = obj["GlbCurrRateDisp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbRateGrpCode
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbCurrConvRule_input:
   """ Required : 
   ds
   glbCompany
   glbRateGrpCode
   glbSourceCurrCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      self.glbSourceCurrCode:str = obj["glbSourceCurrCode"]
      pass

class GetNewGlbCurrConvRule_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlbCurrExRate_input:
   """ Required : 
   ds
   glbCompany
   glbRateGrpCode
   glbSourceCurrCode
   glbTargetCurrCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      self.glbSourceCurrCode:str = obj["glbSourceCurrCode"]
      self.glbTargetCurrCode:str = obj["glbTargetCurrCode"]
      pass

class GetNewGlbCurrExRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlbCurrRateDisp_input:
   """ Required : 
   ds
   glbCompany
   glbRateGrpCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.glbRateGrpCode:str = obj["glbRateGrpCode"]
      pass

class GetNewGlbCurrRateDisp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGlbCurrRateGrp_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbCurrRateGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbCurrRateGrp
   whereClauseGlbCurrConvRule
   whereClauseGlbCurrExRate
   whereClauseGlbCurrRateDisp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbCurrRateGrp:str = obj["whereClauseGlbCurrRateGrp"]
      self.whereClauseGlbCurrConvRule:str = obj["whereClauseGlbCurrConvRule"]
      self.whereClauseGlbCurrExRate:str = obj["whereClauseGlbCurrExRate"]
      self.whereClauseGlbCurrRateDisp:str = obj["whereClauseGlbCurrRateDisp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbCurrRateGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbCurrRateGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCurrRateGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

